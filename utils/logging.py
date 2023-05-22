import google.cloud.logging
import logging
import config

client = google.cloud.logging.Client()
client.setup_logging()
logger = client.logger('python')


def start_log():
    logger.log_struct({
        'Log': 'service started',
        'severity': 'INFO',
    })
    print('start logging')
    return

def get_request_log(path):
    print('success')
    logger.log_struct({
        'Log': 'GET Request',
        'path': f'GET {path}',
        'severity': 'INFO',
    })
    print(f'Write GET request logs to {logger.name}.')
    return

def post_request_log(api):
    logger.log_struct({
        'LOG': 'POST Request',
        'api': api,
        'severity': 'INFO',
    })
    print(f'Write POST request logs to {logger.name}')
    return


    