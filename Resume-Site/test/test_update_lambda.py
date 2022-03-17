import boto3
import json

#table name = "table"
#partition key or pk = "visitors"
#columns = "visitors", "vc"

def lambda_handler(event, context):
    client = boto3.resource('dynamodb')
    table = client.Table('table')
    
    response = table.get_item(
        Key={
            'visitors':1
        }
        )
    count = response['Item']['vc'] + 1
    
    print(count)
    
    response = table.update_item(
            Key={
                'visitors': 1
            },
            UpdateExpression="set vc=:vc",
            ExpressionAttributeValues={
                ':vc': count
            },
            ReturnValues="UPDATED_NEW"
        )
    

    return {
        'statusCode': 200,
        'body': json.dumps(str(count)),
        'headers': {
            'Access-Control-Allow-Origin': '*',
            'Content-Type': 'application/json',
            'Access-Control-Allow-Headers':'Content-Type'
        },
    }
