from application import app
from flask import render_template
from application.forms import NameSubmit
from application.classifier import NameClassifier
import joblib


model = joblib.load('application/static/trained_model_rf.joblib')


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
