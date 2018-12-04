#socks module have proxy options. it is from PySocks package.
#because some slow connection of some networks, like tor. I used sleep for avoid problems with delay
from time import sleep
import socks
class Ircbot(object):
    def __init__(self, Host, Port, ssl=False, proxy=None):
        socket = socks.socksocket()     
        if proxy:
            if type(proxy) != tuple:
                raise TypeError("Proxy need be a tuple. Example (addr_str, port_int)")
            print("PROXY ativo {0}/{1} ".format(proxy[0], proxy[1]))
            socket.set_proxy(socks.SOCKS5, proxy[0], proxy[1])
        
         
        print("Conectando a "+Host+" "+str(Port))
        socket.connect((Host,Port))
        print("Conectado!")        
        if ssl:
            print("SSL Ativo")
            import ssl
            socket = ssl.wrap_socket(socket) 
     
        self.socket = socket
        self.Host = Host
        self.Port = Port

    def set_cred(self, nick="IRCBOT", username="IRCBOT", realname="IRCBOT"):
        socket = self.socket
        cmd_0 = "USER {0} {0} {0} :{1}\n".format(username, realname).encode()
        cmd_1 = "NICK {0}\n".format(nick).encode()
        socket.send(cmd_0)
        sleep(2)
        socket.send(cmd_1)
        sleep(2)

    def ping_answ(self, text):
        socket = self.socket
        pong = text.split()[1]
        pong = "PONG "+pong+"\n"
        socket.send(pong.encode())
        sleep(1)
    def recv_msg(self):
        socket = self.socket
        data = socket.recv(1024)
        data = data.decode()
        if data.find("PRIVMSG") != -1:
            try:
                data = data.split("!",1)
                nick = data[0].split(":",1)[1]
                msg = data[1].split(":", 1)[1]
                return((nick, msg))
            except:
                return None
        elif data.find("PING ") != -1:
            self.ping_answ(data)
            return "ping_response"
        else:
            return None
    def recv(self):
        return socket.recv(1024)
    def sendmsg(self, text, channel):
        socket = self.socket
        cmd = "PRIVMSG {0} {1}\n".format(channel, text)
        socket.send(cmd.encode())
    def join(self, channel):
        socket = self.socket
        cmd = "JOIN "+channel+"\n"
        cmd = cmd.encode()
        socket.send(cmd)


