## Synopsis

BoardProject is a web application build in django 2.2. It is a simple project to learn basic aspects of python and Django framework.


## Installation

Creation of python 3 virtual environment is recomended

	git clone https://github.com/Aniruddh9/BoardProject.git
	
	cd BoardProject
	
	pip install requirements.txt
	
	python manage.py migrate
	
	python manage.py runserver 0.0.0.0:8000
	
This will start webserver in localhost:8000
	

## Tests

To run test cases :
	
	cd BoardProject
	
	python manage.py test
	
Nosetest is integrated, all the nosetest arguments can be passed to the above command.

Example : 
	python manage.py -h
	
	python manage.py test -vv
	
	python manage.py -with-xunit
