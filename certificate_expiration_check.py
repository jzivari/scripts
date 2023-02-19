from prometheus_client import Gauge,CollectorRegistry,pushadd_to_gateway
from urllib.request import ssl, socket
import  datetime, smtplib, requests

websites = [
    'site1.com',
    'site2.info'
]
port = '443'
def visit_website(hostname):
    context = ssl.create_default_context()
    with socket.create_connection((hostname, port)) as sock:
        with context.wrap_socket(sock, server_hostname = hostname ) as ssock:
            certificate = ssock.getpeercert()

    certExpires = datetime.datetime.strptime(certificate['notAfter'], '%b %d %H:%M:%S %Y %Z')
    daysToExpiration = (certExpires - datetime.datetime.now()).days

    registry = CollectorRegistry()
    g = Gauge('certificate_check_expiration', 'mycompany', registry=registry)
    g.set(daysToExpiration)
    pushadd_to_gateway('pushgateway-server:9091', job=hostname, registry=registry)

for website in websites:
    visit_website(website)
