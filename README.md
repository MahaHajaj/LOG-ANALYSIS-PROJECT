# LOG ANALYSIS PROJECT
The first project in Udacity's full stack web development nanodegree program
The aim of the project is building an internal reporting tool by sql database queries.

**Reporting tool should answer three questions :**
1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?

**Prerequisites :**
- Python3
- Vagrant
- VirtualBox

**Installing :**
1. Install [Vagrant](https://www.vagrantup.com/downloads.html) and [VirtualBox](https://www.virtualbox.org/wiki/Downloads).
2. Download or fork and clone from github [fullstack-nandegree-vm](https://github.com/udacity/fullstack-nanodegree-vm) repository.
3. Download the [newsdata.sql](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) and put this file into the vagrant directory.

**Running :**
1. Start VM using ```vagrant up```.
2. Log in to VM using ```vagrant ssh```.
3. Change directory to ```/vagrant```.
4. Load the data using ```psql -d news -f newsdata.sql```.
5. Connect to your database using ```psql -d news```.
6. Explore the tables using the ```\dt``` and ```\d table``` commands and select statements.
7. Import psycopg2 library in your python code.
8. Use a style standard to test your python code quality like “pycodestyle”.
8. Run the python file using ```python3 newsdb.py```.
