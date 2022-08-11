'''code for sqs queue'''
import boto3

client = boto3.resource('sqs', region_name='ap-south-1',
                        aws_access_key_id="AKIAQR2VIYAI67E4OV7Z",
                        aws_secret_access_key="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")
print(client)
queue = client.get_queue_by_name(QueueName='my-new-queue')
client = boto3.client('sqs', region_name='ap-south-1',
                      aws_access_key_id="AKIAQR2VIYAI67E4OV7Z",
                      aws_secret_access_key="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")
QUEUEURL = 'https://sqs.ap-south-1.amazonaws.com/038296666129/my-new-queue'
# Send message to SQS queue
response = client.send_message(
    QueueUrl=QUEUEURL,
    DelaySeconds=10,
    MessageAttributes={
        'Title': {
            'DataType': 'String',
            'StringValue': 'The Whistler'
        },
        'Author': {
            'DataType': 'String',
            'StringValue': 'John Grisham'
        },
        'WeeksOn': {
            'DataType': 'Number',
            'StringValue': '6'
        }
    },
    MessageBody=(
        'Information about current NY Times fiction bestseller for '
        'week of 12/11/2016.'
    )
)

print(response['MessageId'])
'''Receice message from SQS Queue'''

response = client.receive_message(
    QueueUrl=QUEUEURL,
    AttributeNames=[
        'SentTimestamp'
    ],
    MaxNumberOfMessages=1,
    MessageAttributeNames=[
        'All'
    ],
    VisibilityTimeout=0,
    WaitTimeSeconds=0
)
# print(response)
message = response['Messages'][0]
receipt_handle = message['ReceiptHandle']
# print(message)
# print(receipt_handle)
'''Delete message from SQS Queue'''
client.delete_message(
    QueueUrl=QUEUEURL,
    ReceiptHandle=receipt_handle
)
print(f'Received and deleted {message}')


def create_queue():
    sqs_client = boto3.client('sqs', region_name='ap-south-1',
                              aws_access_key_id="AKIAQR2VIYAI67E4OV7Z",
                              aws_secret_access_key="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")
    response = sqs_client.create_queue(
        QueueName="my-new-queue2",
        Attributes={
            "DelaySeconds": "0",
            "VisibilityTimeout": "60",  # 60 seconds
        }
    )
    print('Queue created successfully',response)


create_queue()
