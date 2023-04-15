from kubernetes_resources.namespace import create_namespace
from kubernetes_resources.deployment import create_deployment
from kubernetes_resources.service import create_service

NAMESPACE = 'temp'

# Create the namespace
create_namespace()

# # Create the deployment
create_deployment(NAMESPACE)

# # Create the service
create_service(NAMESPACE)