# mail

#### send email with **zmail** + **flask** + **celery** + **restful**


### Installation

- 在mail_config.py中配置邮箱服务(需要打开对应邮箱的SMTP服务)
- `python mail.py`


### Quickstart: 

```python
import requests

data = {

    'recipient': 'yourfriend@example.com',  # email address      
    
    'subject': 'Success!',  # Anything you want.                 
    
    'content': 'This message from zmail!',  # Anything you want. 
    
    'attachments': '/Users/zyh/Documents/example.zip',  # Absolute path will be better.
    
}
requests.post('http://localhost:5000/', json=data)
```


### questions:
- **celery: windows celery4.x eventlet**

  `>celery -A mail.celery worker -l info -P eventlet` [参考链接](https://blog.csdn.net/qq_30242609/article/details/79047660)

- **celery: Celery(app.import_name)**

  `>Celery('mail')`
