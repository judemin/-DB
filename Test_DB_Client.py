'''
python Test_DB_Client.py
'''
import socket

print("Test Messenger Client")
HOST = input("Input IP : ")
PORT = 50007
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
print("Connected to " + HOST)
userName = "Tmp"

while True :
	print("")
	tmp = input("1:Login 2:Register - ")
	if tmp is '1':
		s.sendall(tmp.encode())
		tmp_id = input("Input ID : ")
		s.sendall(tmp_id.encode())
		tmp_pw = input("Input PW : ")
		s.sendall(tmp_pw.encode())
		status = (s.recv(1024)).decode('utf-8')
		if status is '1' :
			print("Welcome " + tmp_id)
			userName = tmp_id
			break
		else :
			print("ID or PW is Incorrect!")

	elif tmp is '2':
		s.sendall(tmp.encode())
		tmp_id = input("Input ID : ")
		s.sendall(tmp_id.encode())
		tmp_pw = input("Input PW : ")
		s.sendall(tmp_pw.encode())
		status = (s.recv(1024)).decode('utf-8')
		if status is '1' :
			print("Registration Complete!")
		else :
			print("Registration Error!")
	else:
		print("Incorrect Command")

while True :
	print("")
	tmp = input("1:Logout  2:Send Message  3:Show Messages - ")
	if tmp is '1':
		s.sendall(tmp.encode())
		print("Good Bye " + userName)
		break
	elif tmp is '2':
		s.sendall(tmp.encode())
		tmp_rcv = input("To whom? : ")
		tmp_title = input(">> Title : ")
		tmp_msg = input("Message : ")
		s.sendall(tmp_rcv.encode())
		s.sendall(tmp_title.encode())
		s.sendall(tmp_msg.encode())
	elif tmp is '3':
		s.sendall(tmp.encode())
		messageNum = 0
		while True :
			data = (s.recv(1024)).decode('utf-8')
			if data.endswith('0'):
				break
			print(data)
			messageNum += 1
		print("There were " + str(messageNum) + " messages")
	else:
		print("Incorrect Command")
s.close()
