from redis import Redis
from rq import Queue
from tasks import classify_appeal
import db


r = Redis()
q = Queue(connection=r)


class TaskManager:
    def __init__(self):
        self.r = Redis()
        self.q = Queue(connection=self.r)

    def get_q(self):
        return self.q

    def start_initial_analyze(self, appeal_id):
        self.q.enqueue(classify_appeal, appeal_id)

    def __del__(self):
        self.r.close()