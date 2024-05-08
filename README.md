# SeniorCapstone
This repository holds the files for my senior project. I am creating a python based GUI that pairs to a SQLite
database for managing reserving dates at a property. The unique aspects of this project are multilayer design for 
easier switching between database dialects, and it will feature a visible calendar showing the taken
dates.

## Getting Started

The program is straight forward. Download the files you want to utilize, gui.py and core.py are the two files that are implicitly needed. The gui.py file contains the code to make the GUI appear, core.py contains the code that allows the GUI to send information to and from dbconnect, and dbconnect.py is specific to running this program using SQLAlchemy and a SQLite database. The file calendar.db contains some sample families, and reservations to allow for testing of the
GUI functions.

## Prerequisites
You will need to have Python3 and SQAlchemy installed for this project to work on your system.
Before you begin, ensure you have installed Python 3 on your machine. You can download it from the 
[official Python website](https://www.python.org/downloads/).

Next, you will need to verify that it is installed, run `python --version` in a terminal to check that the latest 
version is installed. 

Next check that pip is properly installed by entering `pip --version` into the terminal.

To install SQLAlchemy enter `pip install SQLAlchemy` into a terminal. To verify that it is installed correctly,
open a python terminal and enter `import sqlalchemy` hit enter, and then enter `sqlalchemy.__version__`. This will show
the version you have installed.
