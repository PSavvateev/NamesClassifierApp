from flask import Flask, redirect, render_template, url_for
from flask_wtf.csrf import CSRFProtect
from forms import NameSubmit
from classifier import NameClassifier
import joblib
import os
from dotenv import load_dotenv

load_dotenv()
SECRET_KEY = os.environ["SECRET_KEY"]
WTF_CSRF_SECRET_KEY = os.environ["WTF_CSRF_SECRET_KEY"]

app = Flask(__name__)
ccsrf = CSRFProtect(app)
model = joblib.load('classifier_modeling/trained_model_rf.joblib')

app.config.update(dict(
   SECRET_KEY=SECRET_KEY,
   WTF_CSRF_SECRET_KEY=WTF_CSRF_SECRET_KEY
))


@app.route("/", methods=['GET', 'POST'])
def index():
    form = NameSubmit()
    input_name = str()
    gender = str()
    proba = str()
    script = str()

    if form.validate_on_submit():
        input_name = form.input_name.data
        name_classifier = NameClassifier(name=input_name, model=model)
        gender, proba, script = name_classifier.prediction()

    return render_template('index.html', form=form, name=input_name, outcome=(gender, proba, script))


if __name__ == "__main__":
    app.run(debug=True)
