# RBAC-Implementation
Role-Based Access Control (RBAC) Implementation in Python using SQLite

# 🔐 Advanced Role-Based Access Control (RBAC) System for Cybersecurity

## 📚 Project Overview
This project demonstrates a secure **Role-Based Access Control (RBAC)** system using Python and SQLite to simulate a real-world cybersecurity scenario. The system is designed to authenticate users, assign roles, control access, and log all access attempts for monitoring.

---

## 💡 Features:
- **Secure Authentication:** Passwords are hashed using **bcrypt** to protect against unauthorized access.
- **Role-Based Access Levels:** Supports roles like **Admin**, **Manager**, and **User** with specific access privileges.
- **Access Logging:** Records all access attempts to **access_log.csv** for monitoring and analysis.
- **Attack Simulation:** Test for brute-force attacks and SQL injection attempts to understand vulnerabilities.

---

## 📁 File Structure:
```
/Advanced-RBAC-Security/
│── rbac_security.py         # Main Python script for the RBAC system
│── users.db                 # SQLite database (auto-created)
│── access_log.csv           # Access log file for monitoring (auto-created)
│── requirements.txt         # Python dependencies
│── README.md                # Project documentation
```

---

## 🔧 Installation & Setup:
### Step 1: Clone the Repository
```bash
git clone https://github.com/YourUsername/Advanced-RBAC-Security.git
cd Advanced-RBAC-Security
```

### Step 2: Install Dependencies
Install the required packages listed in **requirements.txt**:
```bash
pip install -r requirements.txt
```

### Step 3: Run the Project
Run the **rbac_security.py** script:
```bash
python rbac_security.py
```

---

## 👩‍💻 How It Works:
1. The script initializes an SQLite database (`users.db`) with a **users** table.  
2. User credentials are hashed using **bcrypt** for security.  
3. Access attempts are logged in **access_log.csv** with:
   - Username
   - Access Level
   - Success/Failure
   - Timestamp  
4. Role-based access is granted based on user roles (`Admin`, `Manager`, `User`).

---

## 🔎 Example Users:
The following users are added for testing:
- **Admin:** Username: `alice`, Password: `Admin123`
- **Manager:** Username: `bob`, Password: `Manager123`
- **User:** Username: `charlie`, Password: `User123`

**Example Output:**
```
Enter username: alice
Enter password: Admin123
🔒 User 'alice' authenticated as 'Admin'.
🔓 alice has Admin access: Full access granted!
```

---

## 🔥 Security Testing:
Test the security aspects to understand the robustness of the system:
- **Brute Force Attacks:** Attempt multiple wrong passwords.
- **SQL Injection:** Try entering `' OR 1=1--` as the username.
- **Weak Password Testing:** Check the effectiveness of bcrypt hashing.

---

## 📊 Access Log Monitoring:
The **access_log.csv** file stores all access attempts for auditing and monitoring:

```
Username, Access Level, Success, Timestamp
alice, Admin, Success, 2025-03-19 14:35:22
bob, Manager, Success, 2025-03-19 14:36:10
charlie, User, Success, 2025-03-19 14:36:58
dave, Unauthorized, Fail, 2025-03-19 14:37:30
```
You can analyze it using **pandas** for better insights.

---

## 🛡️ Future Enhancements:
- Implement **Multi-Factor Authentication (MFA)** for added security.
- Develop a **web-based dashboard** using Flask or Django.
- Integrate with **SIEM tools** for advanced monitoring.
- Add advanced logging features for compliance (e.g., GDPR).

---

## 💼 Applications:
- Secure access management in small to medium organizations.
- Educational demonstrations for cybersecurity training.
- Integration with other security systems for access control.

---

## 📩 Contact Information:
For any queries or collaboration, reach out to:
- **Your Name:** Godina Mohitheswar  
- **Email:** mohitheswargodina@gmail.com  
- **GitHub:** [Your GitHub Username](https://github.com/YourUsername)

---

## ⭐ Contribute:
Feel free to submit issues or contribute to this project. Pull requests are welcome!

---

### ⚠️ Disclaimer:
This project is for educational purposes only. Do not use it for unauthorized access or malicious activities.

```

---

### 🔥 **Your GitHub Project Is Now Ready!**
- Upload all files to your GitHub repository: **`Advanced-RBAC-Security`**
- Make sure to update the **GitHub link** and **contact information** in the README.  
- Share your project link on your resume or with peers!  

---

If you need help with any step or adjustments, just let me know! 😊🚀
