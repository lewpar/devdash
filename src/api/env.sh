ENV_PATH=".venv"
ACTIVATE_PATH="$ENV_PATH/bin/activate"

echo "Checking for environment.."

if [ ! -d "$ENV_PATH" ]; then
    echo "Environment missing, creating.."
    python -m venv .venv
else
    echo "Environment found: $ENV_PATH"
fi

echo "Activating environment.."
source $ACTIVATE_PATH