import mysql.connector

mydb = mysql.connector.connect(
  host="0.0.0.0",
  user="root",
  password="",
  database="app"
)

mycursor = mydb.cursor()

# Create one user in the db
mycursor.execute("INSERT INTO users VALUES('nathan', 'password')")

username = input("This is a field that is not vulnerable! ")
mycursor.execute("SELECT * FROM users WHERE username = %s", (username,))
myresult = mycursor.fetchone()
if myresult:
    print("Successfully logged in!")
else:
    print("Failed to log in!")

username = input("This is a vulnerable field! ")
mycursor.execute("SELECT * FROM users WHERE username = '" + username + "'")
myresult = mycursor.fetchone()
if myresult:
    print("Successfully logged in!")
else:
    print("Failed to log in!")