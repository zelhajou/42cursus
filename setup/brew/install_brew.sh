#!/bin/bash

# Check if Homebrew is installed
brew -v &>/dev/null

if [ $? == 0 ]; then
    printf "Brew already installed ✅\n\n"
    printf "Did you want to check for an update? yes/no : "
    read arg
    echo -e
    if [ "$arg" == "yes" ]; then
        check=$(brew update) &>/dev/null
        if [[ $check == "Already up-to-date." ]]; then
            echo "Already up-to-date ✅"
            echo -e
        else
            echo "Brew updated ✅"
            echo -e
        fi
    fi
else
    # Install Homebrew in `goinfre`
    cd ~/goinfre
    git clone https://github.com/Homebrew/brew homebrew &>/dev/null
    eval "$(homebrew/bin/brew shellenv)"
    brew update --force --quiet &>/dev/null
    chmod -R go-w "$(brew --prefix)/share/zsh" &>/dev/null
    echo 'export PATH=$HOME/goinfre/homebrew/bin:$PATH' >> ~/.zshrc
    echo 'export HOMEBREW_CACHE=$HOME/goinfre/homebrew-cache' >> ~/.zshrc
    mkdir -p $HOME/goinfre/homebrew-cache
    source ~/.zshrc
    cd - &>/dev/null
    echo "Homebrew installed in ~/goinfre ✅"
fi

# Set cache directory explicitly
export HOMEBREW_CACHE=$HOME/goinfre/homebrew-cache
mkdir -p $HOMEBREW_CACHE

# Clean up previous cache issues
brew cleanup -s &>/dev/null

echo -e "\nHomebrew setup completed successfully 🎉"
