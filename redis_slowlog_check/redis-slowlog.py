import redis
from collections import namedtuple
from datetime import datetime
import socket
from prometheus_client import Gauge,CollectorRegistry,pushadd_to_gateway


def prometheus_pushgateway(duration):
        registry = CollectorRegistry()
        g = Gauge('redis_slow_log_count', 'mycompany', registry=registry)
        g.set(duration)
        pushadd_to_gateway('pushgateway-server:9091', job=hostname, registry=registry)

def parse_slowlog(slowlog):
    Entry = namedtuple('Entry', ('id', 'start_time', 'duration', 'command'))
    for entry in slowlog:
        yield Entry(
            id = entry['id'],
            start_time = datetime.fromtimestamp(entry['start_time']),
            duration = round(entry['duration'] / 1000 / 1000, 2),
            command = entry['command'].decode())

hostname = socket.gethostname()
r = redis.Redis(
    host="localhost",
    port=6379,
    db=0,
    socket_timeout=1)

slowlog_len = r.slowlog_len()
slowlog = parse_slowlog(r.slowlog_get(slowlog_len))
sorted_slowlog = sorted(slowlog, key=lambda x: x.duration, reverse=True)

if slowlog_len == 0:
    prometheus_pushgateway(0)

for entry in sorted_slowlog[:1]:
    if entry.duration >= 1:
        prometheus_pushgateway(entry.duration)
    else:
        prometheus_pushgateway(0)