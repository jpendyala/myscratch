  import boto3
  
    role_arn = "arn:aws:iam::12345678911:role/my-machine-or-human-role"
    sts_client = boto3.client('sts')
    session  = sts_client.assume_role(RoleArn=role_arn, RoleSessionName='dynamodb-to-s3')
    ddb = boto3.client('dynamodb', region_name="us-east-1", aws_access_key_id=session['Credentials']['AccessKeyId'], 
    aws_secret_access_key=session['Credentials']['SecretAccessKey'], aws_session_token=session['Credentials']['SessionToken'])
    
    ss = ddb.export_table_to_point_in_time(
        TableArn='arn:aws:dynamodb:us-east-1:12345678911:table/table-name-in-other-aws-account',
        # ExportTime in timestamp format
        ExportTime=1627528502,
        S3Bucket='target-s3-bucket-name',
        S3BucketOwner='12345678911',
        S3Prefix='folder-name',
        ExportFormat='DYNAMODB_JSON'
        )
        
    print(ss)
