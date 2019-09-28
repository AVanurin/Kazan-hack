import db
from core.handlers import get_appeal_info_full


def get_info(appeal_id):
    return _get_appeal_actual_appeal_info(appeal_id)


def _get_appeal_actual_appeal_info(appeal_id):
    return get_appeal_info_full(appeal_id)