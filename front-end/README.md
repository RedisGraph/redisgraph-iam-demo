# RedisGraph Demo Front End

## Install it

```
npm install
```

Requires Node 10.

## Run it

```
$ node index.js -p [port] -P [password] -h [host]
```

## Use it

1. Point your browser at localhost:4000
2. Open the devtools console (option-command-I on a mac/chrome)
3. Type in your query:
```
redisgraph('MATCH (n:Team {teamId:2})<-[r]-(m:User) RETURN ID(n), n.name, n.type, ID(m), m.name, m.type',3);
```
First argument is the query, second is "the chunk" - in this case it's 3 because n has three different properties returned.

`redisgraph()` defaults to the key `IAM_SMALL`. This can be changed by setting the variable `key` from the in-browser REPL. 
```
key = 'IAM_LARGE';
```

You can also set `showTable = true` to show a table of the results as well as the visualization.

You can also zoom in/out with the trackpad and pan with a drag.
