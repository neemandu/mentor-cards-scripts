import os
import boto3
from boto3.dynamodb.conditions import Key


table_name = 'CardsPack-7dxrcivpwjfzxbf67vf6vs3heq-dev'

# Initialize a DynamoDB resource
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(table_name)
scan_kwargs = {}
data = []

while True:
    response = table.scan(**scan_kwargs)
    data.extend(response['Items'])

    # Check if the scan is complete
    if 'LastEvaluatedKey' not in response:
        break

    # Set the ExclusiveStartKey for the next scan
    scan_kwargs['ExclusiveStartKey'] = response['LastEvaluatedKey']

def update_cards_pack_table():
    try:
        for item in data:
            print('start item:', item['id'])
            if 'cards' in item:
                updated_cards = [
                    {
                        'categoryName': '-1',
                        'categoryStepNumber': -1,
                        'cardsImages': item['cards'],
                    }
                ]

                update_params = {                    
                    'TableName': table_name,
                    'Key': {'id': item['id']},
                    'UpdateExpression': 'SET cards = :updatedCards, isHardCopyAvailable = :isHardCopyAvailable, ownerName = :ownerName, numberOfCards = :numberOfCards, videoUrl = :videoUrl',
                    'ExpressionAttributeValues': {
                        ':updatedCards': updated_cards,
                        ':isHardCopyAvailable': False,
                        ':ownerName': "",
                        ':numberOfCards': -1,
                        ':videoUrl': None,
                    }
                }

                table.update_item(**update_params)
                print('finish item:', item['id'])

        print('Update completed successfully.')
    except Exception as error:
        print('Error updating the CardsPack table:', error)


print('start')
update_cards_pack_table()
print('finish')
