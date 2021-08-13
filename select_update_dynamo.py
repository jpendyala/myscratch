import boto3
import pprint as pp
from boto3.dynamodb.conditions import Key, Attr
import datetime
import os




count = 0

sts_client=boto3.client('sts')

session=sts_client.assume_role(RoleArn='arn:aws:iam::000000000000:role/MYROLE',RoleSessionName="test")

client=boto3.resource('dynamodb',region_name="us-east-1",aws_access_key_id=session["Credentials"]['AccessKeyId'],aws_secret_access_key=session["Credentials"]['SecretAccessKey'],aws_session_token=session["Credentials"]['SessionToken'])

dynamodb=boto3.client('dynamodb',region_name="us-east-1",aws_access_key_id=session["Credentials"]['AccessKeyId'],aws_secret_access_key=session["Credentials"]['SecretAccessKey'],aws_session_token=session["Credentials"]['SessionToken'])

table = client.Table("my-dynamo-db-table")
myFilterExpression = Attr('File_Name').contains("FOLDERNAME/SUBFOLDER/FileName.extension")
myKeyConditionExpression = Key('COLUMN_NAME').eq("VALUE1")

query_response = table.query(IndexName="INDEX_NAME", FilterExpression=myFilterExpression,KeyConditionExpression=myKeyConditionExpression)

pp.pprint(query_response)

################################################################RUN BELOW TO DO UPDATE ###################################################################################

table_name = 'my-dynamo-db-table'

ts = datetime.datetime.now()
cur_time = ts.strftime('%Y-%m-%d %H:%M:%S.%f')

val1 = 'FOLDERNAME/SUBFOLDER/FileName.extension'
UpdateExpression_val = 'SET COLUMN_NAME1 = :val1, COLUMN_NAME2 = :val2'
ExpressionAttributeValues_val = {
    ':val1': {'S': 'VALUE1'},
    ':val2': {'S': str(cur_time)}
}
Key = {'COLUMN_NAME1': {'S': val1}, 'File_Timestamp': {'S': '2021-07-21 02:14:55.778'}}
update_response = dynamodb.update_item(TableName=table_name, Key=Key, UpdateExpression=UpdateExpression_val,
                                       ExpressionAttributeValues=ExpressionAttributeValues_val)

print(update_response)
