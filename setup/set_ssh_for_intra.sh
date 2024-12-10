#!/bin/bash

# Function to print colored output
print_message() {
    echo -e "\033[1;32m$1\033[0m"
}

print_error() {
    echo -e "\033[1;31m$1\033[0m"
}

print_message "Starting SSH key setup for Intra..."

# 1. Generate SSH Key
EMAIL="your_email@example.com"  # Replace with your Intra email
SSH_KEY_PATH="$HOME/.ssh/id_rsa"
if [ -f "$SSH_KEY_PATH" ]; then
    print_message "An SSH key already exists at $SSH_KEY_PATH. Overwrite it? (y/n)"
    read -r OVERWRITE
    if [ "$OVERWRITE" != "y" ]; then
        print_message "Exiting without making changes."
        exit 0
    fi
fi

ssh-keygen -t rsa -b 4096 -C "$EMAIL" -f "$SSH_KEY_PATH" -N "" <<<y >/dev/null 2>&1
print_message "SSH key generated at $SSH_KEY_PATH."

# 2. Start SSH Agent and Add Key
eval "$(ssh-agent -s)" >/dev/null 2>&1
ssh-add "$SSH_KEY_PATH" >/dev/null 2>&1
print_message "SSH key added to the SSH agent."

# 3. Display the Public Key
print_message "Your public SSH key is:"
cat "$SSH_KEY_PATH.pub"
echo
print_message "Copy the above key and add it to Intra (https://intra.42.fr/):"
print_message "Profile -> SSH Keys -> Add SSH Key."
print_message "Waiting for you to add the key..."

# 4. Test Connection in a Loop
while true; do
    ssh -T git@vogsphere-v2.1337.ma >/dev/null 2>&1
    if [ $? -eq 0 ]; then
        print_message "SSH setup is complete. Connection to Vogsphere is successful."
        break
    else
        print_error "Connection failed. Ensure you have added the SSH key to Intra."
        print_message "Retrying in 5 seconds..."
        sleep 5
    fi
done
