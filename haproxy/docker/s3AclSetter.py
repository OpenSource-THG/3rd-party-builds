#!/usr/bin/env python
import boto3
import argparse

def process_s3_objects(bucket, prefix):
    client = boto3.client('s3')
    kwargs = {'Bucket': bucket, 'Prefix': prefix}
    bucket_access_ids = get_bucket_access_ids(client, bucket)
    bucket_owner_id = client.get_bucket_acl(Bucket=bucket).get("Owner", {}).get("ID", "")
    process_objects = True
    print "Allowing access to IDs: {}".format(", ".join(bucket_access_ids))
    while process_objects:
        resp = client.list_objects_v2(**kwargs)
        for obj in resp['Contents']:
            print "Setting ACL for {}".format(obj['Key'])
            kwargs['ContinuationToken'] = resp.get('NextContinuationToken', None)
            set_acl(client, bucket_access_ids, bucket_owner_id, bucket, obj['Key'])
        process_objects = (kwargs['ContinuationToken'] != None)

def set_acl(client, access_ids, bucket_owner_id, bucket, key):
    id_string = ",".join(map(lambda x: "id={}".format(x), access_ids))
    client.put_object_acl(
        GrantRead=id_string,
        GrantReadACP=id_string,
        GrantFullControl="id={}".format(bucket_owner_id),
        Bucket=bucket,
        Key=key
    )

def get_bucket_access_ids(client, bucket):
    bucket_acls = client.get_bucket_acl(Bucket=bucket)
    ids = map(lambda x: x.get('Grantee', {}).get('ID', ""), bucket_acls.get('Grants', [])) + [bucket_acls.get("Owner", {}).get("ID", "")]
    return list(list(filter(None, set(ids))))

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--bucket', required=True, action="store")
    parser.add_argument('--prefix', required=True, action="store")
    args = parser.parse_args()
    process_s3_objects(args.bucket, args.prefix)

main()
