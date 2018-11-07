#!/bin/bash

python createcsv.py
python redisgraph-bulk-loader/bulk_insert.py IAM -n Team.csv -n User.csv -n Resource.csv -r RESOURCE_ACCESS.csv -r PART_OF_TEAM.csv
python createindex.py IAM -i ':User(userId)' -i ':Team(teamId)' -i ':Resource(resourceId)'
