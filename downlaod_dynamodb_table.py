import boto3
import json
import os
from decimal import Decimal


class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            if obj % 1 == 0:
                return int(obj)
            else:
                return float(obj)
        return super(DecimalEncoder, self).default(obj)

# Set the table name and output path
table_name = 'CardsPack-ffx5lo4aivekbbvot2z2rsyojy-prod'
output_path = r'C:\Users\neema\mentor-cards\tables'

# Ensure the output directory exists
os.makedirs(output_path, exist_ok=True)
output_file = os.path.join(output_path, f'{table_name}.json')

# Initialize a DynamoDB resource
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(table_name)

# Initialize the scan parameters
scan_kwargs = {}
data = []

# Scan the table
while True:
    response = table.scan(**scan_kwargs)
    data.extend(response['Items'])

    # Check if the scan is complete
    if 'LastEvaluatedKey' not in response:
        break

    # Set the ExclusiveStartKey for the next scan
    scan_kwargs['ExclusiveStartKey'] = response['LastEvaluatedKey']

# Write data to JSON file
with open(output_file, 'w', encoding='utf-8') as file:
    json.dump(data, file, cls=DecimalEncoder, indent=4, ensure_ascii=False)