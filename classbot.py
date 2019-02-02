from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
from telethon.tl.types import InputMessagesFilterDocument
from telethon.tl.functions.messages import SearchRequest
from telethon.tl.types import InputMessagesFilterEmpty
from telethon import utils
import requests
import io
import re

class Bot(object):
    def __init__(self, bot):
        self.bot = bot
        self.maxmsg = 1000
        #self.MSG_oldID = ""
    def owner(self):
        bot = self.bot
        return bot.get_me()
    def dead(self):
        bot = self.bot
        bot.disconnect()
        print("[!] - Clara Lille is dead")
    def sendMsg(self, target, msg):
        bot = self.bot
        if type(msg) == str:
            msg = "**[Clara]:**\t"+msg
        bot.send_message(target, msg)
    def sendFile(self, target, msgfile):
        bot = self.bot
        bot.send_file(target, msgfile)
        print("Sending Message to %s : FILE: %s" %(target, msgfile))
    def getEntity(self,target):
        bot = self.bot
        return bot.client.get_entity(target)
    def getMsg(self,target,oldID=None):
        bot = self.bot
        MSG = bot.get_messages(target)
        newID=MSG[0].id
        msgBlock = []
        if oldID == None:
            oldID=newID
        if isinstance(oldID, int) and isinstance(newID, int) and oldID != newID:
            print("NEW ID %s OLD ID %s" % (newID, oldID))
            for message in bot.iter_messages(target, limit=newID-oldID):
                msgBlock.append(message)
        if len(msgBlock) == 0:
            msgblock = False
        return [msgBlock, newID]

    def msg_reply(self,msg,payload,target):
        bot = self.bot
        bot.send_message(target,payload,reply_to=msg, link_preview=False)
    def forwardfile(self, file, target):
        bot = self.bot
        sendMsg = self.sendMsg # funcoes internas que serao usadas
        filename = file.media.document.attributes[0].file_name
        filename = filename.replace(".", " ", ( filename.count(".")-1 ) ).split(".")[0]
        if filename.find("_") != -1: #replace _ with space
            filename = filename.replace("_", " ")
        if filename.find("-") != -1:
            filename = filename.replace("-", " ")
        sendMsg(target, filename)
        sendMsg(target, file)
    def downloadProfilePhotos(self, target):
        bot = self.bot
        bot.download_profile_photo(target)
    def check_command(self,msg,target,acervo):
        bot = self.bot
        sendMsg = self.sendMsg
        searchMessage = self.searchMessage
        interaction = { '/clara@isonline':"Yes I'm here, bitch. by Clara Lille"
                        ,'/clara@source':"https://github.com/d34dfr4m3/Cl4r4Li1l3"
                        ,'/clara@acervo':'https://t.me/Ac3rv0b4t4t4'
                        ,'/clara@help': "Hello, My name is Clara Lille\nHere is the good stuff\n\t/clara@search -> Search files inside the Acervo\n\t/clara@isonline -> Check if i'm alive\n\t/clara@source -> My Source Code\n\t/clara@acervo -> Link to Acervo\n\t/clara@shellcode -> [Shellcode API](http://shell-storm.org/shellcode/), try this: `/clara@shellcode linux /bin/bash`\n\t/clara@help -> This message"
                        }
        try:
            searchObj = re.search(r'/clara@\w+', msg.message)
            if msg.message.startswith('/clara@search'):
                print("[+] Search Call")
                query = msg.message.split()[1]
                if query.find("pdf") != -1 or len(query) == 1:
                    self.msg_reply(msg, "Put in your ass", target)
                    return 0
                searchMessage(msg, acervo, target, query)


            elif msg.message.startswith('/clara@shellcode'):
                print("[+] Shellcode Call")

                query = 'http://shell-storm.org/api/?s='
                data = msg.message.split()
                data.pop(0)
                if len(data) == 1:
                    query += data[0]
                else:
                    query += data[0]
                    data.pop(0)
                    for q in range(len(data)):
                        query += '*' + data[q]

                try:
                    page = requests.get(query)
                    buf = io.StringIO(page.text)
                    if len(buf.readline()) == 0:
                        self.msg_reply(msg, "F*ck, no luck with that bro!", target)
                        return True
                    aux = 0
                    foobar="Have Fun!\n"
                    while (len(buf.readline())) > aux:
                        aux += 1
                        line = buf.readline()
                        linha = line.split('::::')
                        foobar+=linha[0] + ' ' + linha[1] + ' [{}]({})\n'.format(linha[2], linha[4].replace('\n',''))
                    self.msg_reply(msg, foobar, target)
                except Exception as error:
                    print("[!!] Feature: Shellcode : Error - ", error)

            elif searchObj:
                if searchObj.group() in interaction:
                    self.msg_reply(msg, interaction[searchObj.group()], target)
            elif 'clara is dead' in msg.message:
                self.msg_reply(msg,"huh go fuck yourself Ubisoft",target)
            elif 'drugs' in msg.message:
                self.msg_reply(msg,'Alright, lets get high and hack some stuff',target)

        except Exception as error:
            pass

    def searchMessage(self,msg, acervo,target, string):
        bot = self.bot
        sendReply = self.msg_reply
        link = "https://t.me/"+acervo[1:]+"/"
        filter = InputMessagesFilterEmpty()
        result = bot(SearchRequest(peer=acervo,q=string,filter=filter,min_date=None,max_date=None,offset_id=0,add_offset=0,limit=100,max_id=0,min_id=0,from_id=None,hash=0))
        payload = ''

        for i in range(len(result.messages)):
            try:
                pdf_file = result.messages[i]
                file_name = pdf_file.media.document.attributes[0].file_name
                file_link = link+str(pdf_file.id) 
                # example: [ [file_name](file_link) (file_data) ]
                payload+="[{0}]({1})\n".format(file_name, file_link)
            except Exception as error:
                pass
        if payload:
            banner = "RESULTADOS PARA \"{0}\"".format(string)
            banner = "**{0}**\n{1}\n".format(banner, (len(banner)*"="))
            payload = banner+payload
            sendReply(msg,payload,target)
        else:
            sendReply(msg,"Nenhum resultado foi encontrado.",target)

    def searchmedia(self, target, filename):
        bot = self.bot
        for message in bot.iter_messages(target, filter=InputMessagesFilterDocument):
            if filename == message.media.document.attributes[0].file_name:
                return False
        return True
    def get_username(self, id):
        bot = self.bot
        infos = bot.get_entity(id)
        if infos.username:
            return infos.username
        else:
            return infos.first_name
