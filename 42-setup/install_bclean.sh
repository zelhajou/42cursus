#!/bin/bash

# Define the repository URL
REPO_URL="https://github.com/Ra-Wo/bleach_42"

# Clone the repository
echo "Cloning the repository..."
git clone "$REPO_URL"

# Navigate into the cloned directory
REPO_NAME=$(basename "$REPO_URL" .git)
cd "$REPO_NAME" || { echo "Failed to enter directory $REPO_NAME"; exit 1; }

# Make sure the installation script is executable
echo "Making the installation script executable..."
chmod +x install.bash

# Run the installation script
echo "Running the installation script..."
./install.bash

echo "Setup complete! Repository cloned and installation script executed."

