#!/usr/bin/env python
# coding: utf-8

# In[6]:


# Import the SQL ALchemy engine
from sqlalchemy import create_engine

#This import statement makes the create_engine function available in our program. We can use that function to create a connection
#to the database. The database would reside on a database server and have specific authentication and permissions set. Recall what you learned earlier in this course about connecting to PostgreSQL servers with a username. Similarly, our Python code would need some information in order to connect. 
#Specifically, we need: the username a password the hostname - that is the domain name of a server or an IP address
#a port number - by default, the port number of PostgreSQL database servers is 5432, but in some cases, the server administrator may decide to use a different port. In such cases, you need to specify the port number.
#a database name - each server may host multiple databases, and when you connect you must state which database you wish to connect to.
#We can declare some variables to store these values. Then use the create_engine function to connect to the database.


# In[2]:


## Database credentials. But I don't understand this: "'postgresql://{}:{}@{}:{}/{}'"  Are these {} empty to refer back to data points?
#postgres_user = 'dsbc_student'
#postgres_pw = '7*.8G9QH21'
#postgres_host = '142.93.121.174'
#postgres_port = '5432'
#postgres_db = 'medicalcosts'

## use the credentials to start a connection
#  engine = create_engine('postgresql://{}:{}@{}:{}/{}'.format(
#   postgres_user, postgres_pw, postgres_host, postgres_port, postgres_db))


# In[14]:


postgres_user = 'dsbc_student'
postgres_pw = '7*.8G9QH21'
postgres_host = '142.93.121.174'
postgres_port = '5432'
postgres_db = 'dvdrentals'


# In[15]:


engine = create_engine('postgresql://{}:{}@{}:{}/{}'.format(
 postgres_user, postgres_pw, postgres_host, postgres_port, postgres_db))


# In[10]:


#Joining three tables: actor table with Category Table with Film Table
sql = '''
  SELECT COUNT(*) AS count, a.actor_id, a.first_name, a.last_name 
  FROM film f 
  JOIN film_actor fa 
  ON f.film_id = fa.film_id 
  JOIN actor a 
  ON a.actor_id = fa.actor_id 
  JOIN film_category fc 
  ON fc.film_id = f.film_id
  JOIN category c
  ON c.category_id = fc.category_id
  WHERE c.name = 'Comedy'
  GROUP BY a.actor_id
  ORDER BY count DESC
'''

results = engine.execute(sql)
engine.dispose()
rows = results.fetchall()

# print some results just to see what we got
for row in rows:
  print(row)


# In[21]:


#Why isn't this working? 
counts = [row['count'] for row in rows]

print('The mean number of comedy movies by actor is {}'.format(mean(counts)))
print('The median number of comedy movies by actor is {}'.format(median(counts)))
print('The standard deviation of appearances in comedy movies is {}'.format(standard_deviation(counts)))


# In[17]:


# Find the total number of rows in the table
row_count = engine.execute('SELECT COUNT(*) FROM dvdrentals')

# dispose the connection
engine.dispose()

# fetch the first row from the Results
ans = row_count.first()

# print the count
print('There are {} rows in the table'.format(ans['count']))


# In[12]:


#Q1: How many movies are released for each rating? (in the dvdrentals dataset)
# get a list of the keys (column names)  title.keys()
row_count = engine.execute('SELECT COUNT(*) FROM dvdrentals')


# In[ ]:


sql = '''
SELECT 
  COUNT(*) 
FROM 
  dvdrentals
WHERE 
  #### '''

row_count = engine.execute(sql)
engine.dispose()
ans = row_count.first()
print('There are {} ### in the table'.format(ans['count']))


# In[ ]:


#Q2: What is the average rental duration for each rating? Need 2 clauses:  rentals' timing for 4 'rating' categories


# In[ ]:


#Q3: What is the mean movie length? Calculate this by defining a function. Find Mean. NEED to use AVG 


# In[ ]:


#Q4: What is the median movie length? Calculate this by defining a function. 
#Find median of movie length. NEED to use combination: SELECT
#  (
# (SELECT MAX(Score) FROM
#   (SELECT TOP 50 PERCENT Score FROM Posts ORDER BY Score) AS BottomHalf)
# +
# (SELECT MIN(Score) FROM
#   (SELECT TOP 50 PERCENT Score FROM Posts ORDER BY Score DESC) AS TopHalf)
# ) / 2 AS Median


# In[ ]:


#Q5: Calculate the standard deviation of the movie lengths. Calculate this by defining a function.

