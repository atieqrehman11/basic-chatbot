#!/bin/bash

# Set environment variables
export ENV=production
export VIRTUAL_ENV=venv
export LLM_MODEL="gpt-4o"
export OPENAI_API_KEY=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

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
