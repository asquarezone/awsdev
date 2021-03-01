import boto3

my_s3 = boto3.resource('s3')
print

# print all the bucket names
for bucket in my_s3.buckets.all():
    print("name = {0} created = {1}".format(bucket.name,bucket.creation_date))