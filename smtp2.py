"""
This SMTP client connects to Gmail's SMTP server, authenticates using STARTTLS, 
and sends an email from sanspokharel@gmail.com to sanspokharel94@gmail.com.
Ensure the App Password is valid, and check spam/junk folders for the email.
"""

from socket import *
import ssl
import base64  # For encoding login credentials

# Email details
sender_email = "sanspokharel@gmail.com"  # Sender email address
recipient_email = "sanspokharel94@gmail.com"  # Recipient email address
password = "xwrf krqm kuhm fgig"  # Gmail App Password

msg = "\r\nI love computer networks!"
endmsg = "\r\n.\r\n"

# Gmail SMTP server details
mailserver = ("smtp.gmail.com", 587)

# Create socket and establish a TCP connection with the mail server
clientSocket = socket(AF_INET, SOCK_STREAM)  # Create a TCP socket
clientSocket.connect(mailserver)  # Connect to Gmail's SMTP server

# Receive the initial server response
recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '220':
    print("220 reply not received from server.")

# Send HELO command and print the response
heloCommand = 'HELO Alice\r\n'
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '250':
    print("250 reply not received from server.")

# Request STARTTLS to upgrade to a secure connection
starttlsCommand = "STARTTLS\r\n"
clientSocket.send(starttlsCommand.encode())
recv2 = clientSocket.recv(1024).decode()
print(recv2)
if recv2[:3] != '220':
    print("220 reply not received for STARTTLS.")

# Secure the connection with SSL/TLS
context = ssl.create_default_context()
clientSocket = context.wrap_socket(clientSocket, server_hostname="smtp.gmail.com")

# Authenticate with the server
# Send AUTH LOGIN command
authCommand = "AUTH LOGIN\r\n"
clientSocket.send(authCommand.encode())
recv3 = clientSocket.recv(1024).decode()
print(recv3)

# Send Base64 encoded username
clientSocket.send(base64.b64encode(sender_email.encode()) + b"\r\n")
recv4 = clientSocket.recv(1024).decode()
print(recv4)

# Send Base64 encoded password
clientSocket.send(base64.b64encode(password.encode()) + b"\r\n")
recv5 = clientSocket.recv(1024).decode()
print(recv5)

# Send MAIL FROM command and print server response
mailFrom = f"MAIL FROM:<{sender_email}>\r\n"
clientSocket.send(mailFrom.encode())
recv6 = clientSocket.recv(1024).decode()
print(recv6)
if recv6[:3] != '250':
    print("250 reply not received for MAIL FROM.")

# Send RCPT TO command and print server response
rcptTo = f"RCPT TO:<{recipient_email}>\r\n"
clientSocket.send(rcptTo.encode())
recv7 = clientSocket.recv(1024).decode()
print(recv7)
if recv7[:3] != '250':
    print("250 reply not received for RCPT TO.")

# Send DATA command and print server response
dataCommand = "DATA\r\n"
clientSocket.send(dataCommand.encode())
recv8 = clientSocket.recv(1024).decode()
print(recv8)
if recv8[:3] != '354':
    print("354 reply not received for DATA.")

# Send the email message body
clientSocket.send(msg.encode())
clientSocket.send(endmsg.encode())
recv9 = clientSocket.recv(1024).decode()
print(recv9)
if recv9[:3] != '250':
    print("250 reply not received for message data.")

# Send QUIT command to end the session
quitCommand = "QUIT\r\n"
clientSocket.send(quitCommand.encode())
recv10 = clientSocket.recv(1024).decode()
print(recv10)
if recv10[:3] != '221':
    print("221 reply not received for QUIT.")

# Close the socket
clientSocket.close()