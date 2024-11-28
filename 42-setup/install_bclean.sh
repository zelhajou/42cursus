#!/bin/bash

# Define the repository URL
REPO_URL="https://github.com/Ra-Wo/bleach_42"

# Clone the repository
echo "Cloning the repository..."
git clone "$REPO_URL"

mv bleach_42 ~/.bleach_42

# Navigate into the cloned directory
cd ~/.bleach_42

# Make sure the installation script is executable
echo "Making the installation script executable..."
chmod +x install.bash

# Run the installation script
echo "Running the installation script..."
./install.bash

echo "Setup complete! Repository cloned and installation script executed."

