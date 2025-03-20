import sqlite3
import bcrypt
import pandas as pd
from datetime import datetime

# Database setup
conn = sqlite3.connect('users.db')
cursor = conn.cursor()

# Create users table
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    password TEXT NOT NULL,
    role TEXT NOT NULL
)
''')
conn.commit()

# Password hashing
def hash_password(password):
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())

def verify_password(hashed_password, password):
    return bcrypt.checkpw(password.encode(), hashed_password)

# Add user function with password hashing
def add_user(username, password, role):
    hashed_pw = hash_password(password)
    cursor.execute("INSERT INTO users (username, password, role) VALUES (?, ?, ?)", (username, hashed_pw, role))
    conn.commit()
    print(f"User '{username}' added with role '{role}'.")

# Access logging
def log_access(username, access_level, success):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    data = {'Username': [username], 'Access Level': [access_level], 'Success': [success], 'Timestamp': [timestamp]}
    df = pd.DataFrame(data)
    df.to_csv('access_log.csv', mode='a', header=False, index=False)

# Authentication and access control
def authenticate(username, password):
    cursor.execute("SELECT password, role FROM users WHERE username = ?", (username,))
    result = cursor.fetchone()

    if result and verify_password(result[0], password):
        print(f"User '{username}' authenticated as '{result[1]}'.")
        access_control(username, result[1])
    else:
        print("Authentication failed! Invalid credentials.")
        log_access(username, 'Unauthorized', 'Fail')

# Role-based access control (RBAC)
def access_control(username, role):
    log_access(username, role, 'Success')

    if role == 'Admin':
        print(f"🔒 {username} has Admin access: Full access granted!")
    elif role == 'Manager':
        print(f"🔒 {username} has Manager access: Moderate access granted!")
    elif role == 'User':
        print(f"🔒 {username} has User access: Basic access granted!")
    else:
        print("❌ Undefined role. Access denied!")

# Example setup
add_user("alice", "Admin123", "Admin")
add_user("bob", "Manager123", "Manager")
add_user("charlie", "User123", "User")

# Access test
username = input("Enter username: ")
password = input("Enter password: ")
authenticate(username, password)

conn.close()
