import yaml
from kubernetes import client,config

# Load the Kubernetes configuration from default location
config.load_kube_config()

# Create a Kubernetes API client
api = client.CoreV1Api()

def create_service(namespace):
    # Load the service YAML file
    with open('kube_config/service.yaml', 'r') as f:
        svc = yaml.safe_load(f)

    # Set the namespace for the service
    svc['metadata']['namespace'] = namespace

    # Create the service
    api.create_namespaced_service(body=svc, namespace=namespace)
    print(f'Service created in namespace {namespace}')