from lxml import etree


def _xml_string_to_tree(xml_string):
    root = etree.XML(xml_string)
    return root[0]


def _parse_from_etree(classifiers_tree):
    result = []
    for classifier in classifiers_tree:
        if classifier.tag == "Classifier":
            c = Classifier(class_id=classifier.get('class_id'),
                           element_id=classifier.get('elementID'),
                           probability=classifier.get('probability'))
            result.append(c)
    return result


class Classifier:
    def __init__(self, class_id, element_id, probability):
        self.class_id = class_id
        self.element_id = element_id
        self.probability = probability

    @staticmethod
    def classifiers_from_xml(xml):
        list_of_classifiers = _parse_from_etree(_xml_string_to_tree(xml))
        return Classification(list_of_classifiers)


class Classification:
    def __init__(self, classifiers_list):
        print(classifiers_list)
        self.classifiers = classifiers_list

    def __str__(self):
        r = ''
        self.classifiers.sort(key=lambda val: val.probability, reverse=True)
        for classifier in self.classifiers:
            r += f'\n<{classifier.class_id}> {classifier.element_id} with {classifier.probability}'
        return r
