from kubernetes import client, config

# if you have kube config file in default location (~/.kube/config), you can load it using:
# config.load_kube_config()

# Configs can be set in Configuration class directly or using helper utility
config.load_kube_config(config_file="/etc/rancher/k3s/k3s.yaml")

client = client.CoreV1Api()

pods = client.list_namespaced_pod(namespace="default")

print("Listing pods with their IPs and Namespaces:")
# pods = pods.get("items", [])
print(type(pods))

pods = pods.items

for pod in pods:
    print(pod.metadata.name)
    print(f"namespace: {pod.metadata.namespace}")

# for pod in pods.items:
#     print(f"{pod.metadata.namespace}\t{pod.metadata.name}\t{pod.status.pod_ip}")

