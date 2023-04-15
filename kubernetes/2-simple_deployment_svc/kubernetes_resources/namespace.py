import yaml
from kubernetes import client,config

# Load the Kubernetes configuration from default location
config.load_kube_config()

# Create a Kubernetes API client
api = client.CoreV1Api()

def create_namespace():
    # Load the namespace YAML file
    with open('kube_config/namespace.yaml', 'r') as f:
        namespace = yaml.safe_load(f)

    # Extract the namespace name from the YAML file
    NAMESPACE = namespace['metadata']['name']

    # Create the namespace
    api.create_namespace(body=namespace)
    print(f'Namespace {NAMESPACE} created')