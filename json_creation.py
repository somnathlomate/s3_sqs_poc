try:
    import boto3
    import os
    import sys
    import json
except Exception as e:
    print(e)

AWS_ACCESS_KEY="AKIAQR2VIYAI67E4OV7Z"
AWS_SECRET_KEY="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"
AWS_SQS_QUEUE_NAME = "my-new-queue"


class SQSQueue(object):

    def __init__(self, queueName=None):
        self.resource = boto3.resource('sqs', region_name='ap-south-1',
                                       aws_access_key_id=AWS_ACCESS_KEY,
                                       aws_secret_access_key=AWS_SECRET_KEY)
        self.queue = self.resource.get_queue_by_name(QueueName=AWS_SQS_QUEUE_NAME)
        self.QueueName = queueName

    def send(self, Message={}):
        data = json.dumps(Message)
        response = self.queue.send_message(MessageBody=data)
        return response

    def receive(self):
        try:
            queue = self.resource.get_queue_by_name(QueueName=self.QueueName)
            for message in queue.receive_messages():
                data = message.body
                data = json.loads(data)
                message.delete()
        except Exception:
            print(e)
            return []
        return data


if __name__ == "__main__":
    q = SQSQueue(queueName=AWS_SQS_QUEUE_NAME)
    Message = {"name":" Somnath Lomate ", "age":32}
    response = q.send(Message=Message)
    print(response)
    # data = q.receive()
    # print(data)