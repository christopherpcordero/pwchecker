# NIST Compliant Password Toolbox

## Overview

This Python-based **password security** toolbox provides three essential functionalities for secure authentication and **data breach prevention**, all compliant with **NIST SP 800-63B guidelines**. It includes a robust password generator, a strength checker, and a compromise detection tool integrated with the Have I Been Pwned API. This project demonstrates practical application of **identity and access management (IAM)** principles and proactive security measures.

## Features

* **Password Generator:** Creates strong, randomized passwords based on user-defined length, adhering to NIST recommendations for complexity (lowercase, uppercase, digits, special characters).

* **Password Strength Check:** Assesses the compliance of an entered password against NIST SP 800-63B guidelines, providing specific suggestions for improvement if non-compliant.

* **Password Leak Check:** Utilizes the Have I Been Pwned API to securely check if an inputted password has been compromised in known data breaches, without sending the full password.

## How It Works

### Password Generator

Prompts the user for a desired length and generates a random password consisting of a mix of letters (upper and lower case), digits, and special characters, ensuring it meets a minimum length requirement.

### Password Strength Check

Takes user input (masked for security) and evaluates it against NIST SP 800-63B's common criteria, such as minimum length (8 characters) and inclusion of various character types (lowercase, uppercase, digits, special characters). It provides immediate feedback on compliance and lists areas for improvement.

### Password Leak Check

1. The user enters a password (masked).

2. The program computes the **SHA-1 hash** of the password.

3. Only the first 5 characters (the prefix) of this hash are sent to the **Have I Been Pwned API**'s `pwnedpasswords` service.

4. The API responds with a list of suffixes of all SHA-1 hashes that match the given prefix.

5. The application then checks if the full SHA-1 hash of the user's password exists within the returned list, indicating if the password has been compromised in any known data breaches.

## Tools Used

* **Python 3:** The core programming language.

* `hashlib`: Python's built-in module for secure hashing (SHA-1).

* `requests`: Python library for making HTTP requests to external APIs.

* `maskpass`: Library used for securely masking password input in the console.

* **Have I Been Pwned API:** External service used for checking password compromise.

## Skills Showcased

This project highlights practical experience and proficiency in:

* **Identity & Access Management (IAM):** Implementing secure password practices and authentication mechanisms.

* **Security Frameworks & Compliance:** Adhering to **NIST SP 800-63B guidelines** for digital identity.

* **Cybersecurity Automation:** Developing tools to automate security tasks.

* **API Integration:** Securely interacting with third-party APIs (Have I Been Pwned).

* **Data Breach Prevention:** Proactive measures for identifying compromised credentials.

* **Python Programming:** Developing interactive command-line applications.

* **Cryptography Fundamentals:** Understanding and applying hashing algorithms (SHA-1).

* **User Experience (UX):** Designing a clear and secure command-line interface.
