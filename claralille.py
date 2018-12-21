#! /usr/bin/python3
from telethon import TelegramClient, sync, utils
from telethon.tl.types import PeerUser
from classbot import Bot
from time import sleep
api_id = #
api_hash = #
acervo = #
target_handler = #

exts_perm = [".pdf",".zip",".epub",'.doc','.txt'] #extensoes que serao redirecionadas


client = TelegramClient('clara_memory', api_id, api_hash)
client.start()
target_handler = client.get_entity('https://t.me/joinchat/IA-by07Fa_k4J7Y1JB0JIQ')
client = Bot(client)
print("[*] Running...")
oldID=None
client.sendMsg(target_handler,"Hi, Clara Lille here!")
try:
    while 1:
        sleep(0.6) # o sleep evita sobrecarga. Evitando Travamentos demorados
        messagesblock,oldID = client.getMsg(target_handler,oldID)
        if messagesblock:
            for i in messagesblock:
                if i.media: #verifica se a msg eh um arquivo.
                    file = i.media
                    ext = utils.get_extension(file)
                    if ext in exts_perm:
                        filename = i.media.document.attributes[0].file_name
                        if client.searchmedia(acervo,filename):
                            client.forwardfile(i, acervo)
                            client.msg_reply(i,"[*] Upload Sucessfull to @Ac3rv0b4t4t4, by Clara Lille",target_handler)
                        else:
                            client.msg_reply(i,"[*] File Exist, by Clara Lille", target_handler)
                    # Se não for uma media, verifica se é um comando: 
                else:
                        client.check_command(i,target_handler,acervo)
except KeyboardInterrupt:
    client.sendMsg(target_handler, "i'll AFK, bye")
    client.dead()
