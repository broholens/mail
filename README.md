# mail

## send email with **[zmail flask celery restful]**


## support: **[outlook, 126, 163, qq]**


## POST: 
`data = {
    'recipient': 'yourfriend@example.com',  # email address      
    'subject': 'Success!',  # Anything you want.                 
    'content': 'This message from zmail!',  # Anything you want. 
    'attachments': '/Users/zyh/Documents/example.zip',  # Absolute path will be better.
}
requests.post('http://localhost:5000/', data=data)`


## questions:
celery: windows celery4.x eventlet 
        > celery -A mail.celery worker -l info -P eventlet
        <https://blog.csdn.net/qq_30242609/article/details/79047660>
        
celery: Celery(app.import_name) Celery('mail')
