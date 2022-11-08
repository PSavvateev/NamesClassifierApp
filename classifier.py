"""
Module contains functionality to convert a string input into a d-features vector
and make a prediction based on the pre-trained model
"""

import numpy as np
import hashlib
from unidecode import unidecode


# Global parameters for the hashing of the names.
# Should not be changed, as the model was trained using the same parameters

FIX = 3  # max number of symbols for suffix and prefix to be hashed
DIM = 320  # number of dimensions (features)


def str_hashing(string: str) -> int:
    """
    Function replace any string to a digit.
    analogue of inbuilt hash(), but without random seed
    """
    return int(hashlib.sha512(string.encode('utf-8')).hexdigest(), 16)


class NameClassifier:
    def __init__(self, name: str, model):
        self.name = name
        self.model = model
        self.fix = FIX
        self.d = DIM

    def hashfeatures(self) -> np.array:
        """
        Converts a string into d-array
        where: d - number of dimensions / features;
              fix - max number of symbols for suffix and prefix to be hashed
        """

        # lowering the letters and replacing special latin characters
        name = unidecode(self.name).lower()

        v = np.zeros(self.d)
        for m in range(1, self.fix + 1):
            prefix = name[:m] + ">"
            P = str_hashing(prefix) % self.d
            v[P] = 1

            suffix = "<" + name[-m:]
            S = str_hashing(suffix) % self.d
            v[S] = 1

        return v

    def prediction(self) -> (str, str):
        """
        Make a prediction based on the preloaded trained model
        returns: gender - label class (male / female)
                 proba - probability of the predicted class
                 script  - description of the probability
        """

        name_vector = self.hashfeatures().reshape(1, -1)
        gender_class = self.model.predict(name_vector)
        gender_probs = self.model.predict_proba(name_vector)
        male_prob = gender_probs[0][1]
        female_prob = gender_probs[0][0]

        if gender_class == np.array([1.]):
            gender = 'male'
            likelihood = male_prob*100

        else:
            gender = 'female'
            likelihood = female_prob*100

        if likelihood <= 60:
            script = f"{self.name} is closer to be a {gender}, however this name is quite gender-neutral."
        elif 60 < likelihood <= 75:
            script = f"{self.name} is likely to be a {gender}. Also may imply both genders."
        elif 75 < likelihood <= 90:
            script = f"{self.name} is very likely to be a {gender}. Of course, exceptions are possible."
        else:
            script = f"{self.name} should be definitely a {gender}."

        proba = "%.2f" % likelihood + '%'

        return gender, proba, script
