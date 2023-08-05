almastorage
========

Simple web-application used for accessing project with SwiftStack storage

Quick Install
-------------

1) Install almastorage:

    pip install django-almastorage

2) Add 'almastorage' into your INSTALLED_APPS in project settings 

3) Add fields into project settings infortation from your swiftstack:

	SW_USERNAME = 'user'//account name

	SW_KEY = 'key' //account key
	
	SW_AUTH_URL = 'http://your_url' //auth_url 

4) Make migration

	./manage.py schemamigration almastorage --initial
	
	./manage.py migrate almastorage

