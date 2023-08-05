import inspect
import logging
from typing import Dict, List, Union, Optional

import timeout_decorator

import core.basic_models.classifiers.classifiers_constants as cls_const
import core.logging.logger_constants as log_const
import scenarios.logging.logger_constants as scenarios_log_const
from core.basic_models.classifiers.basic_classifiers import Classifier
from core.logging.masker import LogMasker
from core.utils.stats_timer import StatsTimer

MESSAGE_ID_STR = "message_id"
UID_STR = "uid"
LOGGING_UUID = "logging_uuid"
CLASS_NAME = "class_name"
LOG_STORE_FOR = "log_store_for"


class LoggerMessageCreator:
    ART_NAMES = [
        "channel", "type", "device_channel", "device_channel_version", "device_platform", "group",
        "device_platform_version", "device_platform_client_type", "csa_profile_id", "test_deploy"
    ]

    @classmethod
    def update_user_params(cls, user, params):
        message = user.message
        for name in cls.ART_NAMES:
            param = getattr(message, name, None)
            if param:
                params[name] = param

    @classmethod
    def update_other_params(cls, user, params, cls_name='', log_store_for=0):
        message_id, uuid, logging_uuid = None, None, None
        if user:
            message = user.message
            message_id = message.incremental_id
            uuid = user.id
            logging_uuid = message.logging_uuid
        params[UID_STR] = uuid
        params[MESSAGE_ID_STR] = message_id
        params[LOGGING_UUID] = logging_uuid
        params[CLASS_NAME] = cls_name
        params[LOG_STORE_FOR] = log_store_for

    @classmethod
    def make_message(cls, user=None, params=None, cls_name='', log_store_for=0):
        params = params or {}
        if user:
            cls.update_user_params(user, params)
        params = LogMasker.mask_structure(params, LogMasker.percent_fix)
        cls.update_other_params(user, params, cls_name, log_store_for)
        return params


default_logger = logging.getLogger()


def log(message, user=None, params=None, level="INFO", exc_info=None, log_store_for=0):
    try:
        level_name = logging.getLevelName(level)
        current_frame = inspect.currentframe()
        previous_frame = current_frame.f_back
        module_name = previous_frame.f_globals["__name__"]
        logger = logging.getLogger(module_name)
        instance = previous_frame.f_locals.get('self', None)

        from smart_kit.configs import get_app_config
        app_config = get_app_config()
        message_maker = app_config.LOGGER_MESSAGE_CREATOR

        if instance is not None:
            params = message_maker.make_message(user, params, instance.__class__.__name__, log_store_for)
        else:
            params = message_maker.make_message(user, params, log_store_for=log_store_for)

        logger.log(level_name, message, params, exc_info=exc_info)
    except timeout_decorator.TimeoutError:
        raise
    except:
        default_logger.log(logging.getLevelName("ERROR"), "Failed to write a log. Exception occurred",
                           params, exc_info=True)


def log_classifier_result(classification_res: List[Dict[str, Union[str, float, bool]]], user,
                          classifier: Classifier, timer: Optional[StatsTimer] = None) -> None:
    classifier_name = classifier.settings.get("classifier", "intent_recognizer")
    score_key = cls_const.INTENT_RECOGNIZER_ANSWER_DISTANCE_KEY if classifier_name == "intent_recognizer" \
        else cls_const.SCORE_KEY
    params = {
        log_const.KEY_NAME: scenarios_log_const.CLASSIFIER_VALUE,
        "classifier_name": classifier_name,
        "result": [el[cls_const.ANSWER_KEY] for el in classification_res],
        "score": [el[score_key] for el in classification_res]
    }
    if timer:
        params["time"] = timer.msecs

    log(scenarios_log_const.CLASSIFIER_MESSAGE, user, params)


# backward naming_compatibility
behaviour_log = log
