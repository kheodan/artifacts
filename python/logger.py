import logging

# class Configuration usually have to be stored somewere else with lot of other values
class Configuration:
    DEBUG = True

def logger(app):
    logger_engine = logging.getLogger(app)
    # handler = logging.FileHandler(filename='app.log', encoding='utf-8', mode='w')
    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
    logger_engine.addHandler(handler)
    if Configuration.DEBUG:
        logger_engine.setLevel(logging.DEBUG)
    else:
        logger_engine.setLevel(logging.INFO)
    return logger_engine

logger = logger('app')

subject1 = 'Foo'
subject2 = 'Bar'

logger.info("{} have passed with {}".format(subject1, subject2))
