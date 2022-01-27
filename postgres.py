#!/usr/bin/python3

from datetime import datetime
import psycopg2

current_time = datetime.now()
# Connecting to Postgres
conn = psycopg2.connect(
    host="db.my-finaltask.local",
    database="app_db",
    user="prod_user",
    password="12345")
if conn:
    print ("Connected Successfully")
else:
    print ("Connection Not Established")
    breakpoint

cur = conn.cursor()
print('Postgres database version:')
cur.execute('SELECT version()')
db_version = cur.fetchone()
print(db_version)

# Fetching data from SQL
cur.execute(
    'select magazines.name, article_types.type, author.author from magazines, article_types, author, "Articles" where "Articles".magazines_id = magazines.id and "Articles".article_type_id = article_types.id and "Articles".author_id = author.id')
print(f"There are {cur.rowcount} rows in table")
row = cur.fetchone()
articles = []

while row is not None:
    articles.append(row)
    row = cur.fetchone()

# Composing HTML template
head_html = '''
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta content="text/html; charset=UTF-8" http-equiv="content-type">
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
<title>Final-Task EPAM School by DIR</title></head>
<style>table, th, td {border:1px index black;}</style>
<body>
<center>
<br><h3>Final-Task EPAM School</h3><br>
<table class="table table-dark table-hover">
<tr><td><center><b>Magazine</b></center></td>
<td><center><b>Type</b></center></td>
<td><center><b>Author</b></center></td></b><br>'''

foot_html = str(f"</table></center><p><p><p align=left> Valid for: {current_time}</p></body></html>")

# Composing HTML table with SQL data
with open('/usr/share/nginx/html/articles.html', 'w') as file:
    file.write(head_html)
    for line in articles:
        file.write("<tr>")
        file.write("\n")
        for x in line:
            text = "<th><center>"+str(x)+"</center></th>"+"\n"
            file.write(text)
        file.write("</tr>")
        file.write("\n")
    file.write(foot_html)

# Closing SQL connection
if conn:
        conn.close()
        print("Postgres connection is closed.")
