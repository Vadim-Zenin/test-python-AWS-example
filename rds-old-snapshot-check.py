#!/usr/bin/python
################################################################################
# Author: Vadim Zenin https://github.com/Vadim-Zenin
# Date:   2018-09-03 18:42
#
#   Python function that communicates with AWS RDS and checks if any backups
#   disrespect a retention period of 7 days.
#
# Usage: rds-old-snapshot-check.py -c rds-old-snapshot-check.json
#
# Tested platform:
# Ubuntu 16.04.5 LTS
# Python 3.5.2
# boto3 1.8.6
# python-dateutil 2.7.3
#
# This code is made available as is, without warranty of any kind. The entire
# risk of the use or the results from the use of this code remains with the user.
################################################################################

import boto3
import datetime
import sys
import json


def usage():
    print("Usage: %s -c config_file.json" % sys.argv[0])


def get_config_from_file(config_path):
    try:
        with open(config_path, "r") as f:
            return json.loads(f.read())
    except Exception as e:
        print("ERROR: Unable to read the config file: {0}".format(e))
        sys.exit(1)


def get_rds_client(config):
    rds = boto3.client(
        'rds',
        aws_access_key_id=config['aws_access_key'],
        aws_secret_access_key=config['aws_secret_key'],
        region_name=config['region']
    )
    return rds


def rds_snapshots_list(rds, config):
    now = datetime.datetime.now()
    for snapshot in rds.describe_db_snapshots()['DBSnapshots']:
        if snapshot['SnapshotCreateTime'].replace(tzinfo=None) <= now - datetime.timedelta(hours=config['time_delta_hours']):
            print('Instance: %(DBInstanceIdentifier)s; Snapshot: %(DBSnapshotIdentifier)s; SnapshotCreateTime: %(SnapshotCreateTime)s' % snapshot)


def start():
    if len(sys.argv) < 2:
        usage()
        sys.exit(1)
    config = get_config_from_file(sys.argv[2])
    rds = get_rds_client(config)
    rds_snapshots_list(rds, config)


if __name__ == "__main__":
    start()
