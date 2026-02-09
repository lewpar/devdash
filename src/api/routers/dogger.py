from fastapi import APIRouter

import docker

router = APIRouter(prefix="/docker", tags=["Docker"])

@router.get("/containers")
def get_docker_containers():
    client = docker.from_env()
    containers = client.containers
    return containers.list()