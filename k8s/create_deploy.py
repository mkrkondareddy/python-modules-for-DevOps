from kubernetes import client, config

config.load_kube_config(config_file="/etc/rancher/k3s/k3s.yaml")

DEPLOYMENT_NAME = "nginx-deployment"

apps_v1 = client.AppsV1Api()

container = client.V1Container(
        name="nginx",
        image="nginx:1.15.4",
        ports=[client.V1ContainerPort(container_port=80)],
        resources=client.V1ResourceRequirements(
            requests={"cpu": "100m", "memory": "200Mi"},
            limits={"cpu": "500m", "memory": "500Mi"},
        ),
    )

    # Create and configure a spec section
template = client.V1PodTemplateSpec(
        metadata=client.V1ObjectMeta(labels={"app": "nginx"}),
        spec=client.V1PodSpec(containers=[container]),
    )

    # Create the specification of deployment
spec = client.V1DeploymentSpec(
        replicas=3, template=template, selector={
            "matchLabels":
            {"app": "nginx"}})

    # Instantiate the deployment object
deployment = client.V1Deployment(
        api_version="apps/v1",
        kind="Deployment",
        metadata=client.V1ObjectMeta(name=DEPLOYMENT_NAME),
        spec=spec,
    )  

resp = apps_v1.create_namespaced_deployment(
        body=deployment, namespace="default"
    )
print("\n[INFO] deployment `nginx-deployment` created.\n")
print("%s\t%s\t\t\t%s\t%s" % ("NAMESPACE", "NAME", "REVISION", "IMAGE"))
print(
        "%s\t\t%s\t%s\t\t%s\n"
        % (
            resp.metadata.namespace,
            resp.metadata.name,
            resp.metadata.generation,
            resp.spec.template.spec.containers[0].image,
        )
    )