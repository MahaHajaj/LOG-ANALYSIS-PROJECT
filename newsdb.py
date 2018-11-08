#!/usr/bin/env python3

import psycopg2

DBNAME = "news"
db = psycopg2.connect(database=DBNAME)


def top_articles():
    c = db.cursor()
    Q1 = c.execute("""SELECT title, COUNT(*) as counter
      FROM articles
      JOIN log on articles.slug = substring(log.path, length('/articles/'))
      GROUP BY title
      ORDER BY counter DESC LIMIT 3;""")
    result = c.fetchall()
    print("\n The most popular three articles of all time are : ")
    for row in result:
        print(" \"" + row[0] + "\" " + " -- " + str(row[1]) + " Views")


def top_authors():
    c = db.cursor()
    Q2 = c.execute("""SELECT q2.name , counter
      FROM (SELECT author, COUNT(*) as counter
      FROM articles
      JOIN log on articles.slug = substring(log.path, length('/articles/'))
      JOIN authors ON authors.id = articles.author
      GROUP BY author
      ORDER BY counter DESC) q1
      JOIN (SELECT id ,name FROM authors) q2 ON q1.author = q2.id ;""")
    result = c.fetchall()
    print("\n The most popular article authors of all time : ")
    for row in result:
        print(" \"" + row[0] + "\" " + " -- " + str(row[1]) + " Views")


def error_perc():
    c = db.cursor()
    Q3 = c.execute("""SELECT CAST(time AS DATE),
      AVG( (status <> '200 OK')::int )*100 as rate
      FROM log GROUP BY CAST(time AS DATE)
      ORDER BY rate DESC LIMIT 1;""")
    result = c.fetchall()
    db.close()
    print("\n The days that have more than 1% of requests lead to errors :")
    for row in result:
        print(" \"" + str(row[0]) + "\" " +
              " -- " + str(round(row[1], 2)) + " % errors")


top_articles()
top_authors()
error_perc()
