import json
import boto3

client = boto3.client('s3', region_name='ap-south-1',
                        aws_access_key_id="AKIAQR2VIYAI67E4OV7Z",
                        aws_secret_access_key="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")

'''Read data from S3'''
response = client.get_object(Bucket="somnathbucket",Key="fruit_list.json")
data = response['Body'].read()
print(data)
import sys
sys.exit(0)
'''Write into Json file'''
data = {"Category":"fruit", "fruit": "Apple","size": "Large","color": "Red"}
data = json.dumps(data).encode('UTF-8')
response = client.put_object(Body=data, Bucket="somnathbucket",Key="fruit_list.json")
print(response)
import sys
sys.exit(0)
'''Download File from S3'''
response = client.download_file('somnathbucket','fruit.json',r'E:\download_files\fruit12.json')
import sys
sys.exit(0)
'''Upload a file'''
response = client.upload_file(r'E:\fruit.json','somnathbucket','data/fruit.json')

import sys
sys.exit(0)
'''Delete Object'''
response = client.delete_object(Bucket="somnathbucket",Key="vpn_connection.jpg")

import sys
sys.exit(0)
'''Copy files from one bucket to another'''
s3 = boto3.resource('s3', region_name='ap-south-1',
                        aws_access_key_id="AKIAQR2VIYAI67E4OV7Z",
                        aws_secret_access_key="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"
                        )
copy_source = {
    'Bucket': 'somnathbucket',
    'Key': 'fruit_list.json'
}
bucket = s3.Bucket('somnath-bucket-destination')
bucket.copy(copy_source, 'copied-data/fruit_list.json')