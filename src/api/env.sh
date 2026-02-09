#!/bin/bash

ENV_PATH=".venv"
ACTIVATE_PATH="$ENV_PATH/bin/activate"

if [ -z "$VIRTUAL_ENV" ]; then
    echo "Already inside a virtual environment, deactivating.."
    deactivate
fi

echo "Checking for virtual environment.."

if [ ! -d "$ENV_PATH" ]; then
    echo "Virtual environment missing, creating.."
    python -m venv .venv
    echo "> Created virtual environment at path '$ENV_PATH'."
else
    echo "> Virtual environment found at path: '$ENV_PATH'."
fi

echo "Activating virtual environment.."
source $ACTIVATE_PATH
echo "> Virtual enviroment activated."

echo "Checking for installed dependencies.."

# FastAPI

pip show --quiet "fastapi"
exit_status=$?

if [ $exit_status -ne 0 ]; then
    echo "FastAPI dependency missing, installing.."
    pip install --quiet "fastapi[standard]"
fi

# PSUtil

pip show --quiet "psutil"
exit_status=$?

if [ $exit_status -ne 0 ]; then
    echo "psutil dependency missing, installing.."
    pip install --quiet "psutil"
fi

# Docker

pip show --quiet "docker"
exit_status=$?

if [ $exit_status -ne 0 ]; then
    echo "docker dependency missing, installing.."
    pip install --quiet "docker"
fi

echo "> Done checking dependencies."

echo "> Completed setting up virtual environment."