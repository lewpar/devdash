from pydantic import BaseModel

class DeleteDockerContainerModel(BaseModel):
    id: str