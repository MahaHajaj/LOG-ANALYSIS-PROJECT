LOG ANALYSIS PROJECT
The first project in Udacity's full stack web development nanodegree program , The aim of the project is building an internal reporting tool by sql database queries.

Reporting tool should answer three questions :
1.What are the most popular three articles of all time?
2.Who are the most popular article authors of all time?
3.On which days did more than 1% of requests lead to errors?

Prerequisites :
Python
Vagrant
VirtualBox

Installing :
1.Install Vagrant and VirtualBox.
2.Download or fork and clone from github fullstack-nandegree-vm repository.
3.Download the newsdata.sql and put this file into the vagrant directory.

Running :
1.start VM using vagrant up.
2.log in to VM using vagrant ssh.
3.change directory to /vagrant.
4.load the data using psql -d news -f newsdata.sql.
5.connect to your database using psql -d news.
6.explore the tables using the \dt and \d table commands and select statements.
7.import psycopg2 library in your python code.
8.Use a style standard to test your python code quality like “pycodestyle”.
8.run the python file using python newsdb.py.
