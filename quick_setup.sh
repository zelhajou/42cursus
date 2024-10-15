#!/bin/bash

#install brew

brew -v &>/dev/null

if [ $? == 0 ]
then
	printf "Brew already installed ✅\n\n"
	printf "Did you want to check for an update? yes/no : "
	read arg
	echo -e
	if [ "$arg" == "yes" ]
	then
		check=$(brew update) &>/dev/null
		if [[ $check == "Already up-to-date." ]]
		then
			echo "Already up-to-date ✅"
			echo -e
		else
			echo "Brew updated ✅"
			echo -e
		fi
	fi
else
	cd ~/goinfre
	git clone https://github.com/Homebrew/brew homebrew &>/dev/null
	eval "$(homebrew/bin/brew shellenv)"
	brew update --force --quiet &>/dev/null
	chmod -R go-w "$(brew --prefix)/share/zsh" &>/dev/null
	echo 'export PATH=$HOME/goinfre/homebrew/bin:$PATH' >> ~/.zshrc
	cd - &>/dev/null
fi

./install.sh
