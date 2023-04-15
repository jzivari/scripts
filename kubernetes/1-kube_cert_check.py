from prometheus_client import Gauge,CollectorRegistry,pushadd_to_gateway
import subprocess

subprocess = subprocess.Popen("sudo kubeadm alpha certs check-expiration --config /etc/kubernetes/kubeadm-config.yaml | grep admin.conf | awk '{ print $7 }' ", shell=True, stdout=subprocess.PIPE)

kube_output = str(subprocess.stdout.read(), 'UTF-8')
last_output = int(kube_output[:-2])

registry = CollectorRegistry()
g = Gauge('kubeMaster_certExpiration', 'mydigipay', registry=registry)
g.set(last_output)
pushadd_to_gateway('pushgateway-server-url:9091', job='kubernetes_certiticate', registry=registry)
