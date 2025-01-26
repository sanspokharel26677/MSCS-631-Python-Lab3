# MSCS-631-Python-Lab3

# SMTP Client Implementation in Python

## Overview
This project demonstrates a low-level implementation of the **SMTP (Simple Mail Transfer Protocol)** using Python sockets. The client establishes a connection with Gmail's SMTP server, authenticates via STARTTLS, and sends an email. The implementation avoids using Python's `smtplib` library to provide hands-on exposure to SMTP protocol details and raw socket programming.

## Features
- Connects to Gmail's SMTP server (`smtp.gmail.com`) on port `587`.
- Upgrades to a secure connection using **STARTTLS**.
- Authenticates using Gmail's **App Passwords** for secure login.
- Sends an email from the sender to the specified recipient with a custom message body.

## Prerequisites
- Python 3 installed on your system.
- A valid Gmail account with **App Passwords** enabled.
- Internet access to connect to Gmail's SMTP server.

## Usage
1. Clone or download this project to your local system.
2. Replace the placeholders in the script (`smtp2.py`) with your email credentials:
   - `sender_email`: Your Gmail address.
   - `recipient_email`: The email address you want to send the message to.
   - `password`: Your Gmail App Password (generated from your Google account).
3. Run the script:
   ```bash
   python3 smtp2.py
