# coding=utf-8

import sys
import socket
import time
# import pymysql

reload(sys)
sys.setdefaultencoding("utf-8")

sock = socket.socket()
sock.bind(('127.0.0.1', 8001))
sock.listen(5)


def index(request):
    """
    处理用户请求，并返回响应内容
    :param request: 
    :return: 
    """
    f = open('index.html', 'rb')
    data = f.read()
    f.close()
    return data


def article(request):
    f = open('article.html', 'rb')
    data = f.read()
    f.close()
    ctime = time.time()
    data = data.replace('@@sw@@', str(ctime))
    data = bytes(data)
    return data

# def users(request):
#     conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='db02', charset='utf8')
#     cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
#     cursor.execute('select id,name,email from users')
#     user_list = cursor.fetchall()
#     cursor.close()
#     conn.close()
#     print(user_list)
#     content_list = []
#     for row in user_list:
#         tp = '''<tr>
#             <td>%s</td>
#             <td>%s</td>
#             <td>%s</td>
#         </tr>'''%(row['id'], row['name'], row['email'])

#         content_list.append(tp)
#     content=''.join(content_list)
#     f = open('users.html', 'r', encoding='utf8')
#     template = f.read()
#     f.close()
#     template = template.replace('@content@', content)
#     template = bytes(template,encoding='utf8')
#     return template



routes = [
    ('/index', index),
    ('/article', article),
    # ('/users', users)
]


def run():
    while True:
        conn, addr = sock.accept()
        data = conn.recv(8096)
        data = str(data)
        headers,bodys = data.split('\r\n\r\n')
        temp_list = headers.split('\r\n')
        method,url,protocal = temp_list[0].split(' ')

        func_name = None
        for item in routes:
            if item[0] == url:
                func_name = item[1]
                break
        if func_name:
            response = func_name(data)
        else:
            response = b'404'

        if response == b'404':
            conn.send(b'HTTP/1.1 404 NOT FOUND\r\n\r\n')
        else:
            conn.send(b'HTTP/1.1 200 OK\r\n\r\n')
        conn.send(response)
        conn.close()

if __name__ == "__main__":
    run()