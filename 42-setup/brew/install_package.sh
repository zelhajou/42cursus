#!/bin/bash

# Ensure a package name is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <package-name>"
    exit 1
fi

PACKAGE_NAME=$1
PACKAGE_LIST="brew-packages.txt"

# Check if the package is already in the list
if grep -q "^$PACKAGE_NAME\$" "$PACKAGE_LIST"; then
    echo "$PACKAGE_NAME is already recorded in $PACKAGE_LIST ✅"
else
    # Install the package and add it to the list
    echo "Installing $PACKAGE_NAME..."
    brew install "$PACKAGE_NAME" || brew install --cask "$PACKAGE_NAME"
    echo "$PACKAGE_NAME" >> "$PACKAGE_LIST"
    echo "$PACKAGE_NAME added to $PACKAGE_LIST ✅"
fi

# Commit the updated package list to GitHub
echo "Syncing $PACKAGE_LIST with GitHub..."
git add "$PACKAGE_LIST"
git commit -m "Add $PACKAGE_NAME to package list"
git push
echo "Sync complete 🎉"
