# mail
send email with zmail flask celery

port: 5000
POST: 
data = {
    'to': 'yourfriend@example.com',  # email address
    'subject': 'Success!',  # Anything you want.
    'content': 'This message from zmail!',  # Anything you want.
    'attachments': '/Users/zyh/Documents/example.zip',  # Absolute path will be better.
}

requests.post('http://localhost:5000', data=data)