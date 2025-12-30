from kubernetes import client, config

config.load_kube_config(config_file="/etc/rancher/k3s/k3s.yaml")

v1 = client.CoreV1Api()
# print(dir(client))

pod = client.V1Pod(
    metadata=client.V1ObjectMeta(name="nginx-python"),
    spec=client.V1PodSpec(
        containers=[
            client.V1Container(
                name="nginx",
                image="nginx"
            )
        ]
    )
)

v1.create_namespaced_pod(namespace="default", body=pod)
