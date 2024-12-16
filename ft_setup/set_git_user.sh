#!/bin/bash

# Prompt user for their Git username and email
read -p "Enter your Git username: " git_username
read -p "Enter your Git email: " git_email

# Configure Git with user details (global configuration)
git config --global user.name "$git_username"
git config --global user.email "$git_email"

# Show the current Git configuration to verify
echo -e "\nGit username and email configured:"
git config --list
