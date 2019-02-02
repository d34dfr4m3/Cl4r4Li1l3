#! /usr/bin/python3
from telethon import TelegramClient, sync, utils

from telethon.tl.types import PeerUser
from classbot import Bot
from time import sleep

api_id = INTEGER
api_hash = 'STRING'
acervo = "STRING"
# Extensões aceitas para serem encaminhadas.
exts_perm = [".pdf",".zip",".epub",'.doc','.txt']
group='SOME_STRING_ORWHATEVER_ENTITY_STUFF'

client = TelegramClient('clara_memory', api_id, api_hash)
client.start()
target_handler = client.get_entity(group)
client = Bot(client)
print("[*] Running...")
oldID = None
client.sendMsg(target_handler,"Hi, Clara Lille here!")
try:
    while 1:
        sleep(0.6) # o sleep evita sobrecarga. Evitando Travamentos demorados n lembro porque isso ta aq 
        messagesblock,oldID = client.getMsg(target_handler,oldID)
        if messagesblock:
            for msg in messagesblock:
                if msg.media:
                    if utils.get_extension(msg.media) in exts_perm:
                        filename = msg.media.document.attributes[0].file_name
                        if client.searchmedia(acervo,filename):
                            client.forwardfile(msg, acervo)
                            client.msg_reply(msg,"[*] Upload Sucessfull to "+ acervo +", by Clara Lille",target_handler)
                        else:
                            client.msg_reply(msg,"[*] File Exist, by Clara Lille", target_handler)
                else:
                        client.check_command(msg,target_handler,acervo)
except KeyboardInterrupt:
    client.sendMsg(target_handler, "i'll AFK, bye")
    client.dead()
