import yaml
from kubernetes import client,config

# Load the Kubernetes configuration from default location
config.load_kube_config()

# Create a Kubernetes API client
api = client.AppsV1Api()

def create_deployment(namespace):
    # Load the deployment YAML file
    with open('kube_config/nginx-deployment.yaml', 'r') as f:
        dep = yaml.safe_load(f)

    # Set the namespace for the deployment
    dep['metadata']['namespace'] = namespace

    # Create the deployment
    api.create_namespaced_deployment(body=dep, namespace=namespace)
    print(f'Deployment created in namespace {namespace}')