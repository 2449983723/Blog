# coding=utf-8

import sys
import socket
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
    return data

def testImg(request):
    f = open('test.png', 'rb')
    data = f.read()
    f.close()
    return data

routes = [
    ('/index', index),
    ('/article', article),
    ('/test.png', testImg)
]


def run():
    while True:
        conn, addr = sock.accept()
        data = conn.recv(8096)
        data = str(data)
        print data
        headers,bodys = data.split('\r\n\r\n')
        print headers
        print '\n\n'
        print bodys
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