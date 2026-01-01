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
1. User passwords are hashed with a unique salt.
2. Only the hash is stored.
3. During login, entered passwords are compared against the stored hash

## Security Design Decisions
- Passwords are never stored in plaintext to prevent credential exposure.
- bcrypt is used because it is intentionally slow, reducing the effectiveness of brute-force attacks.
- Salting ensures that identical passwords produce different hashes, protecting against rainbow table attacks.

## Ethical Considerations
This project is for educational purposes only and does not implement real-world authentication infrastructure.

## What I Learned
 - Why hashing is essential for password security
 - How salting prevents rainbow table attacks
 - How authentication systems verify credentials securely

 ## Possible Improvements
 - Account lockout after multiple failed attempts
 - Database integration
 - Secure session handling
