import json

def lambda_handler(event, context):
    data = json.loads(event['body'])

    if 'name' not in data or 'message' not in data:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': 'Name and message are required'})
        }

    guestbook_entry = {'name': data['name'], 'message': data['message']}

    return {
        'statusCode': 200,
        'body': json.dumps({'message': 'Entry submitted successfully'})
    }
