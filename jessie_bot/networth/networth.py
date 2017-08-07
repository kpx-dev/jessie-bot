import json
import logging
import os
import boto3
from jessie_bot.helpers.lex_helper import success

logger = logging.getLogger(__name__)

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ.get('TABLE_NAME') or 'TEST')
# slack_token = boto3.client('kms').decrypt(CiphertextBlob=b64decode(os.environ['SLACK_OAUTH_TOKEN']))['Plaintext'].decode('utf-8')

def get_networth(event):
    return success(message='100k!')


def _parse_mint_email(text):
    try:
        net_worth = text.split('*NET WORTH*')[1].split('[image: See your accounts]')[0].strip()

        return net_worth
    except Exception as e:
        print('problem parsing mint email', e)

def process_networth(event):
    net_worth = 0
    #     # if request.form.get('from') == 'team@mint.com':
    #     net_worth = _parse_mint_email(text=request.form.get('text'))

    return success(message='processing networth...')


def handler(event, context):
    print('event is ', json.dumps(event, indent=3))

    # lambda cron
    if 'source' in event and event['source'] == 'aws.events':
        return process_networth(event)

    # api gateway POST request
    if 'path' in event and event['httpMethod'] == 'POST':
        return process_networth(event)

    intent_name = event['currentIntent']['name']

    if intent_name == 'GetNetworth':
        return get_networth(event)
    elif intent_name == 'ProcessNetworth':
        return process_networth(event)

    return error(message='Invalid intent')

if __name__ == '__main__':
    event = {
        'currentIntent': {
            'name': 'GetNetworth'
        }
    }
    res = handler(event=event, context={})

    print(json.dumps(res, indent=3))
