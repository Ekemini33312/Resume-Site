# boto3 libary for interacting with AWS 
import boto3 

# client for dynamoDB 
dynamodb_client = boto3.client('dynamodb')

# set table 
visitors_table = 'table'

'''
get item from visitors_table
'''
# need to set a key to elete 
key ={
    'visitors':{'N':'1'}
}

response = dynamodb_client.update_item(
                            TableName = visitors_table,
                            Key= key,
                            ExpressionAttributeNames = {
                            'incr': 'increase'
                            },
                            UpdateExpression="SET incr = incr + :visitors",
                            ExpressionAttributeValues={
                                ':visitors': {
                                    'N':'1'
                                }
                            }
                        )


# return-values ALL_NEW
# print response 
print(response)
