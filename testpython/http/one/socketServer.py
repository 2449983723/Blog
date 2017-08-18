# coding=utf-8
import SocketServer

HOST = ''
PORT = 8000

text_content = '''
HTTP/1.x 200 OK
Content-Type: text/html

<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
<title>python</title>
</head>
<html>
<p>Wow, Python Server，凯哥吊毛</p>
<IMG src="test.png"/>
<form name="input" action="/" method="post">
First name:<input type="text" name="firstname"><br>
<input type="submit" value="Submit">
</form> 
</html>
'''

f = open('test.png', 'rb')
pic_content = '''
HTTP/1.x 200 OK
Content-Type: image/png

'''
pic_content = pic_content + f.read()

class MyTCPHandler(SocketServer.BaseRequestHandler):
	def handle(self):
		request = self.request.recv(1024)
		
		print 'Connected by', self.client_address[0]
		print 'Request is', request

		method = request.split(' ')[0]
		src = request.split(' ')[1]

		if method == 'GET':
			if src == '/test.png':
				content = pic_content
			else:
				content = text_content
			self.request.sendall(content)

		if method == 'POST':
			form = request.split('\r\n')
			idx = form.index('')
			entry = form[idx:]
			value = entry[-1].split('=')[-1]
			self.request.sendall(text_content + '\n <p>' + value + '</p>')

server = SocketServer.TCPServer((HOST, PORT), MyTCPHandler)
server.serve_forever()
















