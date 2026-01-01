# Secure Login System (Password Hashing)

## Description
This project demonstrates a basic user authentication system that securely stores and verifies passwords using hashing.

## Cybersecurity Relevance
Storing plaintext passwords is one of the most serious security flaws in software systems. This project shows how password hashing protects users even if a database is compromised.

## Features
- Password hashing using bcrypt
- Secure password verification
- No plaintext password storage
- Simulated user database using JSON

## Technologies Used
- Python
- bcrypt

## How It Works
1. User password are hashed with a unique salt.
2. Only the hash is stored.
3. During login, entered passwords are compared against the stored hash

## Ethical Considerations
This project is for education purposes only and does not implement real world authentication infrastructure.

## What I Learned
 - Why hashing is essential for password security
 - How salting prevents rainbow table attacks
 - How authentication systems verify credentials securely

 ## Possible Improvements
 - Account lockout after multiple failed attempts
 - Database integration
 - Secure session handling
