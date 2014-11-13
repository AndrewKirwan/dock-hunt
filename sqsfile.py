import boto.sqs
import boto.sqs.queue
from boto.sqs.message import Message
from boto.sqs.connection import SQSConnection
from boto.exception import SQSError

conn = boto.sqs.connect_to_region('us-east-1',aws_access_key_id='AKIAIR7EH3TNSTDUCWKA',aws_secret_access_key='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')

q=conn.create_queue('C12339291')

m=Message()
m.set_body('First message.')
q.write(m)

rs=q.get_messages()
len(rs)

m=rs[0]
messageVar=m.get_body()
print(messageVar)
q.delete_message(m)
