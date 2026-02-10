from fastapi import APIRouter
from pydantic import BaseModel

import docker

router = APIRouter(prefix="/docker", tags=["Docker"])

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
    container = client.containers.create("hello-world")
    client.containers.run("hello-world")
    return {
        "id": container.id
    }

class DeleteDockerContainerModel(BaseModel):
    id: str

@router.post("/delete")
def delete_docker_container(model: DeleteDockerContainerModel):
    client = docker.from_env()
    container = client.containers.get(model.id)
    container.remove()
    return "removed"