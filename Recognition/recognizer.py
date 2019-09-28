from Recognition.aidoc import get_aidoc_recognition
from Recognition.xmlparser import Classifier


def get_classification(text):
    api_response = get_aidoc_recognition(text)
    classification = Classifier.classifiers_from_xml(api_response)
    return classification
