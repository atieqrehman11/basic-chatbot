#!/bin/bash

# Set environment variables
export ENV=production
export VIRTUAL_ENV=venv
export LLM_MODEL="gpt-4o"
export OPENAI_API_KEY="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"


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
