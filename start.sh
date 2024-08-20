#!/bin/bash

# Set environment variables
export ENV=production
export VIRTUAL_ENV=venv
export LLM_MODEL="gpt-4o"
export OPENAI_API_KEY=

# Create virtual environment
python3 -m venv $VIRTUAL_ENV

# Activate virtual environment
PATH="$VIRTUAL_ENV/bin:$PATH"

# Install dependencies if the condition is true
if [ "$1" == "build" ]; then

    # Install dependencies
    pip3 install -r requirements.txt

fi

# Run the application
panel serve chatbot.py --show
