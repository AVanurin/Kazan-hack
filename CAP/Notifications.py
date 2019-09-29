import requests
import datetime
import pytz

base_url = "https://cosoc.car.cos.ru/CAPMessages/services/rest/insert/json"

status = "Actual"
message_type = "Alert"
source = ""
scope = "Public"
category = "Safety"


def _make_headers():
    headers = {"Content-Type":"application/json",
               "charset": "UTF-8"}
    return headers


def _make_time():
  n = datetime.datetime.now()
  time_string = str(n.replace(tzinfo=pytz.utc))
  time_list = time_string.split(" ")
  time_list[1] = time_list[1][:8]
  r = "T".join([time_list[0], time_list[1]])
  return r + "+00:00"


def _make_body(object_id, text, job ,assignee_name ,address ,lattitude, longitude, appeal_id):
    """
    "2017-12-26T09:17:08+00:00"
    """
    sent_date = _make_time()

    b = {
  "alert": {
    "identifier": "146121",
    "sender": job,
    "sent": sent_date,
    "status": "Actual",
    "msgType": "Alert",
    "source": "Kazan-app",
    "scope": "Public",
    "code": "Publish",
    "info": {
      "parameter": [
        {
          "valueName": "RecourseID",
          "value": "123"
        },
        {
          "valueName": "Type",
          "value": "Проблема"
        },
        {
          "valueName": "Priority",
          "value": "Средний"
        },
        {
          "valueName": "Status",
          "value": "Актуален"
        },
        {
          "valueName": "Phone",
          "value": "+79031234567"
        },
        {
          "valueName": "E-mail",
          "value": "mail@example.com"
        },
        {
        "valueName": "Assignee",
        "value": assignee_name
        },
      ],
      "language": "ru_RU",
      "category": "Env",
      "responseType": "None",
      "urgency": "Immediate",
      "severity": "Moderate",
      "certainty": "Observed",
      "audience": "all",
      "effective": sent_date,
      "senderName": assignee_name,
      "headline": f"Обращение в УК #13-{appeal_id}",
      "description": text,
      "area": {
        "areaDesc": address,
        "circle": str(lattitude) +','+ str(longitude) + " 0.0"
      }
    }
  }
}

    return str(b)


class CAPManager:
    def __init__(self):
        pass


    def _send_message(self, object_id, text, job ,assignee_name ,address ,lattitude, longitude, appeal_id):
        body = _make_body(object_id, text, job ,assignee_name ,address ,lattitude, longitude, appeal_id)
        headers = _make_headers()

        r = requests.post(base_url, data=body.encode("utf-8"), headers=headers)
        print(r.content)

