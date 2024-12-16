#!/bin/bash

PACKAGE_LIST="brew-packages.txt"

if [ ! -f "$PACKAGE_LIST" ]; then
    echo "Package list file ($PACKAGE_LIST) not found!"
    exit 1
fi

echo "Syncing packages from $PACKAGE_LIST..."
while IFS= read -r package; do
    if ! brew list --formula | grep -q "^$package\$" && ! brew list --cask | grep -q "^$package\$"; then
        echo "Installing $package..."
        brew install "$package" || brew install --cask "$package"
    else
        echo "$package is already installed ✅"
    fi
done < "$PACKAGE_LIST"
