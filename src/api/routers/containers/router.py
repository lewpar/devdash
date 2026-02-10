from fastapi import APIRouter

import docker
import models

router = APIRouter(prefix="/containers", tags=["Containers"])

@router.get("/containers")
def get_docker_containers():
    client = docker.from_env()
    containers = client.containers.list(all=True)
    serializable_containers = []
    for container in containers:
        serializable_containers.append({
            "id": container.id
        })
    return serializable_containers

@router.get("/create")
def create_docker_container():
    client = docker.from_env()
    container = client.containers.create("hello-world", name="Hello World")
    return {
        "id": container.id,
        "name": container.name
    }

@router.post("/delete")
def delete_docker_container(model: models.DeleteDockerContainerModel):
    client = docker.from_env()
    container = client.containers.get(model.id)
    container.remove()
    return "removed"