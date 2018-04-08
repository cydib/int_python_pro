#!/bin/bash

Init(){
	if [[ ! `pip3` ]]
	then
		sudo apt-get install python3-pip
	fi
	if [[ ! `pip3 show parameterized` ]]
	then
		sudo pip3 install parameterized
	fi

	if [[ ! `pip3 show requests` ]]
	then
		sudo pip3 install requests
	fi

	if [[ ! `pip3 show mysqlclient` ]]
	then
		sudo pip3 install mysqlclient
	fi
}

run(){
	if [ ! -d report ]
	then
		mkdir report
	fi
	python3 run_tests.py
}


Init
run