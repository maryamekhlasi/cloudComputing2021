import boto3 

# client = boto3.client('ec2-instance-connect')

# s3 = boto3.resource(
#     service_name='s3',
#     region_name='us-east-1',
#     aws_access_key_id='ASIAVPXDYLQ2VOI47DSR',
#     aws_secret_access_key='x+0dF6FLVobrILAWRUbAWrdEExveuzVj6CccmSbr'
# )

# for bucket in s3.buckets.all():
#     print(bucket.name)


s3 = boto3.resource('s3')
for bucket in s3.buckets.all():
    print(bucket.name)