import requests
import uuid
import json
import config

def send_event(event_name):
    payload = {
        "client_id": config.TRACKING_ID,
        "non_personalized_ads": False,
        "events":[
            {
                "name": event_name
            }
        ]
    }

    headers = {
        "Content-Type": "application/json"
    }

    url = f'https://www.google-analytics.com/mp/collect?api_secret={config.API_SECRET}&measurement_id={config.MEASUREMENT_ID}'

    try:
        response = requests.post(url, data=json.dumps(payload), headers=headers)
        if response.status_code == 200:
            print('Event sent successfully.')
        else:
            print(f'Event failed with status code: {response.status_code}')
    except Exception as e:
        print(f'Error sending event: {str(e)}')
    return

if __name__=='__main__':
    send_event('OK')