import logging


def log_event(user, event, code=None):
    if code is not None:
        print('event is:')
        print(event)
        print('user is: ')
        print(user)
        log_info = "USERNAME:"+user+"/EVENT: " + event + " CODE"
        logging.basicConfig(filename='myapp.log', level=logging.INFO)
        logging.info(log_info)
        event_info = 'USER CODE: ' + code
        logging.info(event_info)
    else:
        print('event is:')
        print(event)
        print('user is: ')
        print(user)
        log_info = "USERNAME:" + user + "/EVENT: " + event + " CODE"
        logging.basicConfig(filename='myapp.log', level=logging.INFO)
        logging.info(log_info)
