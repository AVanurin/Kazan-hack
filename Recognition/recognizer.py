from Recognition.aidoc import get_aidoc_recognition
from Recognition.xmlparser import Classifier


def get_classification(text):
    print(text)
    try:
        api_response = get_aidoc_recognition(text)
        classification = Classifier.classifiers_from_xml(api_response)
        return classification.get_class_type()
    except:
        if "газ" in text:
            return "проблема с газовой абонентской сетью"
        if 'отопл' in text:
            return "проблемы с отоплением"
        if 'вод' in text:
            return "проблема с горячим водоснабжением"
        if 'горяч' in text:
            return 'проблема с горячим водоснабжением'
    return "Неопределенная"
