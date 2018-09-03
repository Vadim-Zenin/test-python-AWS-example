# test-python-AWS-example

## Python function that communicates with AWS RDS and checks if any backups disrespect a retention period of 7 days.

## Environment

```cp python-virtual-environment.sh.example python-virtual-environment.sh```

Edit path and execute.

## Dependencies:

```pip install -r requirements.txt```

## Usage:

```cp rds-old-snapshot-check.json.example rds-old-snapshot-check.json```

Replace CHANGE_TO_YOURS_AWS_ strings.

Execute command
```rds-old-snapshot-check.py -c rds-old-snapshot-check.json```

## Output example

Instance: myrdsinstance01; Snapshot: myrdsinstance01-201809022253; SnapshotCreateTime: 2018-09-02 21:54:03.124000+00:00

Instance: myrdsinstance01; Snapshot: rds:myrdsinstance01-2018-09-02-21-40; SnapshotCreateTime: 2018-09-02 21:41:33.902000+00:00

Process finished with exit code 0

## Config file example:
```json
{
    "aws_access_key": "CHANGE_TO_YOURS_AWS_ACCESS_KEY",
    "aws_secret_key": "CHANGE_TO_YOURS_AWS_SECRET_KEY",
    "region": "eu-west-1",
    "time_delta_hours": 168
}
```
