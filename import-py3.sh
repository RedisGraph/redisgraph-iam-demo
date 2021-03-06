#!/bin/bash

# Large Graph
mkdir largegraph
python3 importscripts/createcsv_large.py
python3 redisgraph-bulk-loader/bulk_insert.py IAM_LARGE -n largegraph/Team.csv -n largegraph/User.csv -n largegraph/Resource.csv -r largegraph/RESOURCE_ACCESS.csv -r largegraph/PART_OF_TEAM.csv "$@"
python3 importscripts/createindex.py IAM_LARGE -i ':User(userId)' -i ':Team(teamId)' -i ':Resource(resourceId)' "$@"

# Small Graph
mkdir smallgraph
python3 importscripts/createcsv_small.py
python3 redisgraph-bulk-loader/bulk_insert.py IAM_SMALL -n smallgraph/Team.csv -n smallgraph/User.csv -n smallgraph/Resource.csv -r smallgraph/RESOURCE_ACCESS.csv -r smallgraph/PART_OF_TEAM.csv "$@"
python3 importscripts/createindex.py IAM_SMALL -i ':User(userId)' -i ':Team(teamId)' -i ':Resource(resourceId)' "$@"
