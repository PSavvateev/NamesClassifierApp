# Names Classifier App: predicting gender by name

## Overview
Machine learning-based web-application predicting gender of a person by the first (given) name.<br>
Despite the more or less accurate classification of the existent names, the app defines the gender and probability 
of being "more male" / "more female" for any newly invented name.

## ML-Model
### Data used
ML Model is trained on approximately 60k popular international names. I used several official datasets of most 
popular given names from EU bureaus of statistic (Netherlands, France, Sweden); 
plus a large corporate dataset of an internationally operated company, having a good representation of the employees names.
(all original datasets are as *.csv* in *`classifier_modeling/data`*). 
Names origins representation:
- The dataset has good coverage of European, American (based on roman languages) names;
- potentially good representation of Eastern-European and slavic names (written in latin transliteration);
- some coverage of Middle-Eastern, Middle-Asian most common names (written in latin transliteration);
- almost no coverage of Far-Eastern and South-Asian names.

### Model principles
The key component is an approach of transforming a name into features vector.
The program takes prefix and suffix of a name and hashing it into d-dimensional vector.
Number of symbols in the suffix and prefix  as well as number of dimensions substantially impact the performance of the model.



Empirically, the best performing classifier was chosen with next parameters:
- number of symbols for suffix / prefix: *3*;
- dimensions: *320*;
- algorithm: *random forest classifier* with 300 trees and unlimited leaves.

Details of the model are in the jupyter notebook: *`classifier_modelling/NamesClassifier_modeling.ipynb`*

## Credits
The name classification method was suggested by Cornell University in their ML Certification Course with the reference to an original idea of <a href="http://nickm.com">Nick Montfort</a>)

## Architecture
1. **`app.py`** - flask application and enter point
2. **`forms.py`** - module defining web-form (wtform) class
3. **`templates/index.html`** - the single html-page of the app
4. **`classifier.py`** - module defining *`NameClassifier`* class with name hashing and prediction functionality
5. **`classifier_modeling/trained_model_rf.joblib`** - packed train model

## Requirements
`python 3`
<br><br>
Packages:
- `Flask~=2.2.2`
- `joblib~=1.2.0`
- `python-dotenv~=0.21.0`
- `WTForms~=3.0.1`
- `numpy~=1.23.4`
- `Unidecode~=1.3.6`

