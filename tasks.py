from Recognition.recognizer import get_classification


def classify_appeal(text, task_id):
    classification = get_classification(text=text)
    with open("test_log.txt", 'w') as f:
        f.write(str(classification))