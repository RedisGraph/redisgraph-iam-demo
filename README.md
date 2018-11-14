# redisgraph-iam-demo
A Python utility to create an IAM data set and import it into RedisGraph

## Installation
```
git submodule update --init --recursive
```
```
pip install --user -r requirements.txt
```

## Execution
Run RedisGraph
```
docker run --name redis-graph -d -p 6379:6379 redislabs/redisgraph:1.0.0
```
```
import.sh
```
or
```
import-py3.sh
```
## Queries
[Example queries](https://github.com/K-Jo/redisgraph-iam-demo/blob/master/queries)

## Frontend
[Front-end](https://github.com/K-Jo/redisgraph-iam-demo/blob/master/front-end/)

## Schema
![Schema](images/schema.png?raw=true "Schema IAM")

## TODO

allow for passing of host, port and password in import script
