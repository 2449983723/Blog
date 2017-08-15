import socket

HOST = ''
PORT = 8000

text_content = '''HTTP/1.x 200 OK
Content-Type: text/html

<head>
<title>Hello World</title>
</head>
<html>
<p>Python Server</p>
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
f.close()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))

while True:
	s.listen(3)
	conn,addr = s.accept()
	request = conn.recv(1024)
	print 'Request is:', request
	method = request.split(' ')[0]
	src = request.split(' ')[1]
	
	if method == 'GET':
		if src == '/test.png':
			content = pic_content
		else: content= text_content
		
		print 'Connected by', addr
		conn.sendall(content)
	if method == 'POST':
		form = request.split('\r\n')
		idx = form.index('')
		print 'idx' + str(idx)
		entry = form[idx:]
		print 'entry:' + str(entry)
		value = entry[-1].split('=')[-1]
		conn.sendall(text_content + '\n <p>' + value + '</p>')
		print text_content + '\n <p>' + value + '</p>'
	conn.close()

































