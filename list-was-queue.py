# This script created a queue
#
# Author - Paul Doyle Aug 2013
#
#
import boto.sqs
import boto.sqs.queue
from boto.sqs.message import Message
from boto.sqs.connection import SQSConnection
from boto.exception import SQSError

conn = boto.sqs.connect_to_region("us-east-1", aws_access_key_id='BKIAIR7EH3TNSTDUCWKB', aws_secret_access_key='s2FZT5mrLYy8gX7kS1q0p4ObQYXTwGnaiUm+rxHA')

rs = conn.get_all_queues()
for q in rs:
	print q.id
