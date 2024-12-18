#!/bin/bash

# Function to check current shell
check_shell() {
    if [ -n "$ZSH_VERSION" ]; then
        echo "zsh"
    elif [ -n "$BASH_VERSION" ]; then
        echo "bash"
    else
        echo "unknown"
    fi
}

# Function to ensure running in correct shell
ensure_correct_shell() {
    current_shell=$(check_shell)
    if [ "$current_shell" != "zsh" ]; then
        echo "Error: This script must be run in zsh shell. Current shell: $current_shell"
        echo "Please run: zsh ./install_brew.sh"
        exit 1
    fi
}

# Function to setup Homebrew
setup_homebrew() {
    cd ~/goinfre || exit 1
    echo "Cloning Homebrew..."
    git clone https://github.com/Homebrew/brew homebrew &>/dev/null || {
        echo "Error: Failed to clone Homebrew repository"
        exit 1
    }
    
    eval "$(homebrew/bin/brew shellenv)"
    brew update --force --quiet &>/dev/null
    chmod -R go-w "$(brew --prefix)/share/zsh" &>/dev/null
    
    # Update shell configuration
    {
        echo 'export PATH=$HOME/goinfre/homebrew/bin:$PATH'
        echo 'export HOMEBREW_CACHE=$HOME/goinfre/homebrew-cache'
    } >> ~/.zshrc
    
    mkdir -p "$HOME/goinfre/homebrew-cache"
    source ~/.zshrc
    cd - &>/dev/null || exit 1
    echo "Homebrew installed in ~/goinfre ✅"
}

# Function to check and update Homebrew
check_and_update_brew() {
    if brew -v &>/dev/null; then
        printf "Brew already installed ✅\n\n"
        printf "Did you want to check for an update? (yes/no): "
        read -r arg
        echo
        
        if [ "$arg" = "yes" ]; then
            echo "Checking for updates..."
            if brew update 2>&1 | grep -q "Already up-to-date"; then
                echo "Already up-to-date ✅"
            else
                echo "Brew updated ✅"
            fi
            echo
        fi
        return 0
    fi
    return 1
}

# Main script
main() {
    # First ensure we're running in zsh
    ensure_correct_shell
    
    # Check if Homebrew exists and handle updates
    if ! check_and_update_brew; then
        setup_homebrew
    fi
    
    # Set cache directory explicitly
    export HOMEBREW_CACHE=$HOME/goinfre/homebrew-cache
    mkdir -p "$HOMEBREW_CACHE"
    
    # Clean up
    echo "Cleaning up cache..."
    brew cleanup -s &>/dev/null
    
    echo -e "\nHomebrew setup completed successfully 🎉"
}

main