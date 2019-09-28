import handlers


def register(d):
    object = d.get("object_id")
    content = d.get("content")
    start_date = d.get("start_date")
    return handlers._register_new_appeal(object, content, start_date)
