import json
import boto3


print('Loading function')


def lambda_handler(event, context):
    env_value = event['tagname']
    env_name = event['tagvalue'] 
    ec2_resource = boto3.resource('ec2')
    instance_ids = []
    for instance in ec2_resource.instances.all():
        for name_pair in instance.tags:
            if env_name in name_pair.values() and env_value in name_pair.values():
                instance_ids.append(instance.id)
                instance.stop()
    return instance_ids
    #raise Exception('Something went wrong')