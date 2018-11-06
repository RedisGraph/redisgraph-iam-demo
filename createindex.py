import redis
import click

@click.command()
@click.argument('graph')
@click.option('--host', '-h', default='127.0.0.1', help='Redis server host')
@click.option('--port', '-p', default=6379, help='Redis server port')
@click.option('--index', '-i', multiple=True, help="colon Label (property) e.g. ':Person(id)'")
def create_index(graph,host,port,index):
    redis_client = redis.StrictRedis(host=host, port=port)
    for i in index:
        redis_client.execute_command("GRAPH.QUERY",
              graph,
              "CREATE INDEX ON " + i
              )

if __name__ == '__main__':
  create_index()
