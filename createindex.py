import redis
import click

@click.command()
@click.argument('graph')
# Redis server connection settings
@click.option('--host', '-h', default='127.0.0.1', help='Redis server host')
@click.option('--port', '-p', default=6379, help='Redis server port')
@click.option('--password', '-P', default=None, help='Redis server password')
@click.option('--ssl', '-s', default=False, help='Server is SSL-enabled')
# Indexes
@click.option('--index', '-i', multiple=True, help="colon Label (property) e.g. ':Person(id)'")
def create_index(graph, host, port, password, ssl,index):
    redis_client = redis.StrictRedis(host=host, port=port, password=password, ssl=ssl)
    for i in index:
        redis_client.execute_command("GRAPH.QUERY",
              graph,
              "CREATE INDEX ON " + i
              )

if __name__ == '__main__':
  create_index()
