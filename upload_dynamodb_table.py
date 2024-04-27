import boto3
import json
from decimal import Decimal, InvalidOperation


def is_number(s):
    """Check if the string is a number."""
    try:
        Decimal(s)
        return True
    except (ValueError, InvalidOperation):
        return False
    
def json_decimal_converter(obj):
    """Convert numeric values to Decimal, leave other types unchanged."""
    if isinstance(obj, list):
        return [json_decimal_converter(sub_obj) for sub_obj in obj]
    elif isinstance(obj, dict):
        return {k: json_decimal_converter(v) for k, v in obj.items()}
    elif isinstance(obj, (float, int)):
        try:
            return Decimal(str(obj))
        except InvalidOperation:
            return obj
    else:
        return obj

# Set your development environment table name
table_name = 'CardsPack-7dxrcivpwjfzxbf67vf6vs3heq-dev'

# Path to your CSV file
file_path = r'C:\Users\neema\mentor-cards\tables\CardsPack-ffx5lo4aivekbbvot2z2rsyojy-prod.json'

# Initialize a DynamoDB resource for your development environment
# Make sure to configure it to point to your development environment
dynamodb_dev = boto3.resource('dynamodb')
new_table = dynamodb_dev.Table(table_name)


# Read data from JSON file
with open(file_path, 'r', encoding='utf-8') as file:
    items = json.load(file, parse_float=Decimal)

    # Convert numeric values to Decimal
    items = json_decimal_converter(items)

# Upload data to the new DynamoDB table
for item in items:
    new_table.put_item(Item=item)
