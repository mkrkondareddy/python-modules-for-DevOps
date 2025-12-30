from kubernetes import client, config

config.load_kube_config(config_file="/etc/rancher/k3s/k3s.yaml")

pod_name = "konda"

v1 = client.CoreV1Api()
resp = v1.delete_namespaced_pod(
        name=pod_name,
        namespace="default"
    )