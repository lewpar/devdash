# DevDash API
This is the FastAPI backend for the DevDash project.

## Setup (Linux)
1. Setup environment and dependencies:
```py
source ./env.sh
```
2. Start API:
```py
fastapi run
```
> To start in dev mode, run `fastapi dev main.py

> Ensure your user is part of the `docker` user group, otherwise you will get permission errors.