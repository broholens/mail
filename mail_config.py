import zmail

netease_server = zmail.server('', '')
outlook_server = zmail.server('', '')
qq_server = zmail.server('', '')


server_mapping_table = {
    '126.com': netease_server,
    '163.com': netease_server,
    'qq.com': qq_server,
    'outlook.com': outlook_server
}