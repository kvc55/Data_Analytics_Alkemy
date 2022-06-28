# Introduction
### Data analytics project with Python. The aim is to collect data from three different sources to populate a PostgreSQL database with information about argentinian museums, cinemas and libraries. 

# Installation instructions
### Create a virtualenv
    python -m venv path\to\myenv

### Clone the project repository
    git clone https://github.com/kvc55/Data_Analytics_Alkemy


### Install the requirements
    pip install -r requirements.txt

### Configure the connection to the database
Create a .ini or .env file configuring the data connection:

    DB_USERNAME = my_user_name
    DB_PASSWORD = my_password
    DB_HOST = host
    DB_PORT = port
    DB_NAME = my_database
    
### You can execute the project by running
    python main.py



