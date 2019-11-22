import socket
import json

class SocketClient:
    def __init__(self, port = 80, host = 'localhost'):
        self.__socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__port = port
        self.__host = host
    
    def host(self, host = None):
        if host is None: return self.__host
        self.__host = host
        return self

    def port(self, port = None):
        if port is None: return self.__port
        self.__port = port
        return self

    def connect(self):
        self.__socket.connect((self.__host, self.__port))
        return self

    def disconnect(self):
        self.__socket.close()
        return self

    def send(self, message, jsonType = True):
        toSend = json.dumps(message) if jsonType else message
        length = len(toSend)
        self.__socket.sendall(length.to_bytes(4, byteorder='big'))
        self.__socket.sendall(toSend.encode())
        return self
    
    def read(self, jsonType = True):
        raw_msglen = self.receive(4)
        if not raw_msglen: return None
        msglen = int.from_bytes(raw_msglen, byteorder='big')
        raw_msg = self.receive(msglen)
        message = raw_msg.decode()
        return json.loads(message) if jsonType else message

    def json(self):
        return json.loads(self.read())

    def receive(self, n):
        data = bytearray()
        while len(data) < n:
            packet = self.__socket.recv(n - len(data))
            if not packet:
                return None
            data.extend(packet)
        return data

