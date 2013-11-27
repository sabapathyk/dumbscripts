#!/usr/bin/python

import boto.ec2

#ACCESS_KEY='AKIAIBIGKVNIDIV5T3HQ'
#SECRET_KEY='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'
region_list={"Virginia":"us-east-1",
             "California":"us-west-1",
             "Oregon":"us-west-2",
             "Ireland":"eu-west-1",
             "Singapore":"ap-southeast-1",
             "Sydney":"ap-southeast-2",
             "Tokyo":"ap-northeast-1",
             "Sao Paulo":"sa-east-1"}

vol_id=[]
ACCESS_KEY=raw_input("Access Key: ")
SECRET_KEY=raw_input("Secret Key: ")

print "The following regions are available: \nVirginia, \nCalifornia, \nOregon, \nIreland, \nSingapore, \nSydney, \nTokyo, \nSao Paulo: "
region=raw_input("Region? :")
REGION=region_list[region]

if (ACCESS_KEY and SECRET_KEY):
    conn = boto.ec2.connect_to_region(REGION,aws_access_key_id=ACCESS_KEY,aws_secret_access_key=SECRET_KEY)
else:
    conn = boto.ec2.connect_to_region(REGION)

print "Connection to AWS established"

print "Getting Volumes..."

print "ID | Creation Time | Attached Status | Volume State"

vol_id = conn.get_all_volumes()

for i in vol_id:
    print "%s | %s | %s" % (i.id, i.create_time, i.attachment_state(), i.volume_state())

if raw_input("Create Snapshots for all volumes? [y/n] ") == 'y':
    print "Snapshotting all volumes..."
    for i in vol_id:
        snapshot_name = "snapshot of " + str(i)
        i.create_snapshot(description=snapshot_name)
        #snapshot = conn.create_snapshot(vol_id, snapshot_name)
else:
    vols_tbsnapped= raw_input("Enter the volume IDs to be snap shotted seperated by space: ")
    snapthese = map(str, vols_tbsnapped.split())
    print "Snapshotting..."
    for j in snapthese:
        snapshot_name = "snapshot of " + str(j)
        conn.create_snapshot(j, snapshot_name)
        print "Snapshot created for " + str(j)

