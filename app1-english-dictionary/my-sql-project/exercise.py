import mysql.connector  # installed library to connect to mysql db
from difflib import get_close_matches

con = mysql.connector.connect(
    # pass credentials of mysql db
    user="ardit700_student",
    password="ardit700_student",
    host="108.167.140.122",
    database="ardit700_pm1database"
)  # if no error appears that means connection is successfull

cursor = con.cursor()

word = input("Enter a word: ")

# inside execute is mysql commands or query
query = cursor.execute(
    "SELECT * FROM Dictionary WHERE Expression = '%s' " % word)
results = cursor.fetchall()

if results:
    for result in results:
        print(result[1])
else:
    print("No word found")
