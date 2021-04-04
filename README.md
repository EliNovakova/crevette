# Crevette (shrimp)

## Installation

Install the virtual environment and all the required packages:

* `pip3 install pipenv`
* `pipenv install`

## Run the server

Enter in the virtual environment:

* `pipenv shell`

In `src`:

* update or create the database:
  * `python manage.py makemigrations`
  * `python manage.py migrate`
* run the server:
  * `python manage.py runserver`
* open you browser and enter the url:
  * <http://localhost:8000/>
