import pyodbc 
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from pandas import DataFrame
import pandas as pd



conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=.;DATABASE=StackOverflow;Trusted_Connection=yes;')
#query = "select top 1 * FROM  order by NEWID();"


# query = "SELECT * FROM [StackOverflow].[dbo].[Posts] TABLESAMPLE(50000 rows);"

# query = "SELECT * FROM [StackOverflow].[dbo].[Comments] TABLESAMPLE(50000 rows);"

# cursor = conn.cursor()
# # results = cursor.execute(cmd).fetchall()
# df = pd.read_sql(query, conn)

# dfRandomQuestions = df[df['PostTypeId'] == 1]

# dfRandomAnswers = df[df['PostTypeId'] == 2]

# df.to_csv('PostsRandomDec8.csv', encoding='utf-8', index=False)

# dfRandomQuestions.to_csv('PostsRandomQuestionsDec8.csv', encoding='utf-8', index=False)


# dfRandomAnswers.to_csv('CommentsRandomAnswersDec8.csv', encoding='utf-8', index=False)



query = "SELECT * FROM [StackOverflow].[dbo].[Comments] TABLESAMPLE(50000 rows);"

cursor = conn.cursor()
# results = cursor.execute(cmd).fetchall()
df = pd.read_sql(query, conn)


# dfRandomQuestions = df[df['PostTypeId'] == 1]

# dfRandomAnswers = df[df['PostTypeId'] == 2]

df.to_csv('CommentsRandomDec8.csv', encoding='utf-8', index=False)

# dfRandomQuestions.to_csv('CommentsRandomQuestionsDec8.csv', encoding='utf-8', index=False)


# dfRandomAnswers.to_csv('CommentsRandomAnswersDec8.csv', encoding='utf-8', index=False)

