# Cl4r4Li1l3
##### Description: Telegram Bot to check files and send to a Channel to store these files.
So, ClaraLille will stay checking a channel, when a user send a file, I mean, something which loooks like a good paper, Then Clara will forward this file to a Channel with a descrition Header of that file. 

## Require
- telethon
- idk what else, i dont care too

## Obtaining API_ID/API_HASH
    Sign up for Telegram using any application.
    Log in to your Telegram core: https://my.telegram.org.
    Go to ‘API development tools’ and fill out the form.
    You will get basic addresses as well as the api_id and api_hash parameters required for user authorization.
    For the moment each number can only have one api_id connected to it.

## Using Telethon framework to Telegram API 
Repare que 'session_name' vai ser utilizado para salvar a sua sessão(informações persistentes como a key e outras), assim como 'session_name.session' no seu disco. Isso por default um arquivo de banco de dados usado pelo Python sqlite3

It’s important that the library always accesses the same session file so that you don’t need to re-send the code over and over again. By default it creates the file in your working directory, but absolute paths work too.


Please note that if you fail to login around 5 times (or change the first parameter of the TelegramClient, which is the session name) you will receive a FloodWaitError of around 22 hours, so be careful not to mess this up! This shouldn’t happen if you’re doing things as explained, though.

É necessário registrar o bot com um token, vocẽ pode fazer manualmente com a linha abaixo, porém lembre-se de que caso você retorne o token por dentro do bot, ele irá expirar imediatamente. 
```
client.is_user_authorized()  # Returns True if you can send requests
```
##### Caso você não tenha acesso, será solicitado os dados: 
```
$ ./claralillie.py 
Please enter your phone (or bot token): 218292901
Please enter the code you received: 28149
Signed in successfully as dead
[+] - Clara Lille has access
```

If you send the code that Telegram sent you over the app through the app itself, it will expire immediately. You can still send the code through the app by “obfuscating” it (maybe add a magic constant, like 12345, and then subtract it to get the real code back) or any other technique.

- https://telethon.readthedocs.io/en/stable/extra/basic/creating-a-client.html#creating-a-client



#### Tratando medias:
##### PDF 
```
MessageMediaDocument(document=Document(id=50915231312313, access_hash=489213131903561696, date=datetime.datetime(2018, 10, 27, 17, 53, 39, tzinfo=datetime.timezone.utc), mime_type='application/pdf', size=1383566, thumb=PhotoSizeEmpty(type=''), dc_id=1, version=0, attributes=[DocumentAttributeFilename(file_name='42280-how-to-exploit-eternalblue-on-windows-server-2012-r2.pdf')]), ttl_seconds=None)
```
##### Web Links 
```
MessageMediaWebPage(webpage=WebPage(id=150343213123123, url='https://www.youtube.com/watch?v=lVIbSbueJM0', display_url='youtube.com/watch?v=lVIbSbueJM0', hash=0, type='video', site_name='YouTube', title='Dubvirus - Razorgirl', description='Support Internet Freedom: https://GravitasRecordings.lnk.to/defcon24Yo DEF CON (defcon.org), one of the worlds largest and oldest annual hacking conferences,...', photo=Photo(id=5324541220, access_hash=-414343243242654654803, date=datetime.datetime(2017, 9, 28, 21, 22, 31, tzinfo=datetime.timezone.utc), sizes=[PhotoSize(type='s', location=FileLocation(dc_id=4, volume_id=463231, local_id=41431, secret=-79fdsfa759), w=90, h=51, size=1124), PhotoSize(type='m', location=FileLocation(dc_id=4, volume_id=435504831, local_id=41432, secret=-4324186137690385873), w=320, h=180, size=14838), PhotoSize(type='x', location=FileLocation(dc_id=4, volume_id=435504831, local_id=41433, secret=-48463643611112371337), w=800, h=450, size=67018), PhotoSize(type='y', location=FileLocation(dc_id=4, volume_id=435504831, local_id=41434, secret=-36436364377), w=1280, h=720, size=128095)], has_stickers=False), embed_url='https://www.youtube.com/embed/lVIbSbueJM0', embed_type='iframe', embed_width=1280, embed_height=720, duration=None, author=None, document=None, cached_page=None))
```
##### Imagens(JPEG/JPG):
```
MessageMediaPhoto(photo=Photo(id=50915fds48, access_hash=-3997fds019, date=datetime.datetime(2018, 10, 27, 17, 44, 4, tzinfo=datetime.timezone.utc), sizes=[PhotoCachedSize(type='s', location=FileLocation(dc_id=1, volume_id=806025988, local_id=99325, secret=-1079118621146640111), w=90, h=51, bytes=b'\xff\xd8\xff\xe0\x00\x10JFIF\x00\x01\x01\x01\x00H\x00H\x00\x00\xff\xdb\x00C\x00\x0e\n\x0b\r\x0b\t\x0e\r\x0c\r\x10\x0f\x0e\x11\x16$\x17\x16\x14\x14\x16, !\x1a$4.763.22:ASF:=N>22HbINVX]^]8EfmeZlS[]Y\xff\xdb\x00C\x01\x0f\x10\x10\x16\x13\x16*\x17\x17*Y;2;YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY\xff\xc0\x00\x11\x08\x003\x00Z\x03\x01"\x00\x02\x11\x01\x03\x11\x01\xff\xc4\x00\x1b\x00\x00\x02\x03\x01\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x05\x00\x02\x04\x06\x01\x07\xff\xc4\x008\x10\x00\x02\x01\x03\x02\x03\x03\x07\x0c\x03\x01\x00\x00\x00\x00\x00\x01\x02\x03\x00\x04\x11\x12!\x051Q\x13"A\x14\x15Ta\x93\xb1\xd1\x0623BDSbq\x81\x91\x92\xe1#r\xa1\xc1\xff\xc4\x00\x18\x01\x00\x03\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x03\x04\x00\x02\xff\xc4\x00\x1f\x11\x00\x02\x02\x01\x05\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x02\x11\x03\x12!12Aa\x13\xff\xda\x00\x0c\x03\x01\x00\x02\x11\x03\x11\x00?\x00\xe8&\xb1\xb6\xb8`\xd3\xc1\x1c\xac\x06\x01u\x0c@\xfdh~j\xb0\xf4+\x7ff*\x9c7\x8e[\xdd\x92\x97\x01m\xe4\xce\xd9m\x9b\xf5\xa7\x06!\xd2\x9bh\xe3qO\x9a\xec=\n\xdf\xd9\x8a\x9ek\xb0\xf4;\x7ff)\xa1\x88ULTv\x06\xe2\xbf5\xd8z\x1d\xbf\xb3\x15\xe1\xe1V\'\xec\x90{1L\x8cUC\x1d\x1d\x81\xb8\x96H8DNU\xbc\x89\x1clA*\x08\xa1\x96\xe1\nN&\xb2\x07\xfd\xd6\xb9n.\xc1x\xc5\xe0+\x93\xda\xb7N\xb5\x90\xc8\xa0\xfc\xc1\xfa\xe3\xe1\\k\xf8u\xa7\xe9\xd8\x16\xe1#\x94\xb6_\xcdhe\xb8P\xe5-\x98\xfc\x99k\x91.\xacwOw\xc2\xa8Jg\xe6\x9f\xdc|+~\x9f\x01\xf9\xfd;(\xe1\xb1\x9b=\x87\x93\xc9\xa7\x9e\x8c\x1c~\xd5<\x82\x0c\xfd\x04\x7f\xc4V\x0f\x91\xc8\x1ek\xbc\xf8*\xfb\xcdu~M\xea\xa6\xc6I\xab\xa1n->N-A\xd5\x9c\x1eT\xe6\xd3\x8f\xdc\xd9[\xf6EV`\x08\xd2\\\x93\xa4x\x8a\xe4\xda\xe6F\xc1f$\x8f\x13E[\x82b$\x97:F\xfb\xedSjeT\x9f\xa7}e\xf2\x8e\xdeH\x9b\xcb\x07c \xe5\xa4\x12\x1a\x99\xdb\xde\xda]F\x8f\x14\xc8C\x9c\x00N\x0ezc\xad|\xc4\xf1\x00\x08\xc1\'H\xe7\xa4w\x8d\x1a\x0b\x91pX$D\xb8\x1a\xb4\xafJ\xda\xeb\x93h\xbe\x19\xf4\x99n\xada\x90G%\xc4j\xe7\x92\x96\xde\xab\x15\xdd\xb4\xf7\r\x0cR\x06u\x19\xdb\x91\xfc\x8d|\xf7\xb5\x06R\xa5H }m\xce@;\x7f\xc1L-nE\xbd\xcc=\x85\xc1\x8d\xc9\xce@\xce\xc7\x96\xc6\x83\xcd\x14e\x89\xb1/\x1b%x\xfd\xf6>\xf5\xbd\xf5\x9eC*\x82XcoW\xc2\xbd\xe22\xf6\xdcN\xe2\\\xea\xd7#6z\xe4\xd1\x1bO\xd5\xecN\xd9\xfa:\x17{\x82\xabc\x01\xc6v\xa9F\x95r2\n\x91\xf8S\x18\xa1\x15#\x98"\xba\x00\xc7\x84\xdd\xcbi\r\xdbE\x8e\xf2\xa89\xf09\xc85\xd2\xad\xcbi\x1a\xe6}x\xefw\x8f:\xe78*#\xb4\xab ,\xbd\xd3\xa4x\xe3&\xaa\xd7\x93k=\xf3\xcf\xa5K\x91Jr\xd2\x9f\x05X\xdcc\x1bk\x90n\xb0\xe9*\xa8q\xa39<\xf3\x8c\x9a\x02\xaa\x95#\x7f\x03\xcb\xfb\xa6\x97\t\x1cV\xe9\x82\xa1\xde7s\x8f\xc46\x14\xad!\'\x9a\x91\xc8\xe7\x04\xd3a+Bf\xa8\xf1V6a\xb1#>\x03\x07\xdf[\xf8F\x98\xaf\xbb\xb9%\x91\x97q\x8e\x9e\xba\xc4CH\xc31\x003\xe0\x98\xad\xdc\x1d\x04W\xda\x9f+\xa5\x1c\xe4\x8e{V\xcb\xd1\x83\x1fdU\xe4\x0c\xef&4`\x9c\x8e\x87\x15\xa9\x99_\x85!\x8fm\xd7$\xf5\x14\x1e!*vk\xa4.w;~~5Y&Aki\x14x\x00)f9\xf1<\xe9Ui\x0e\xe1\xb4,e,\xc4\xa88\xad\x8c\x8c\xa3\x0c\xdb\x91\x9d\xa8~Iq+\xebH\x89V\xdc\x11D~\x1f>6\xb7<\xba\x7fuA8<\xb0\xc0\xee\xe3\x9eumA\x90\x06?W=uQM\x85\xd9\xfb;\n\xf3\xcd\xf7\x7fp\xf4v0~\x0f9\x82\xf5W\x00\x89\x0e\x93\xbf*u%\x84FG&V\x04\x93\x90\r!\x82\xda\xe6;\x84B\x85\x18\xf7\xc6GJn\xbc5\xd9A{\xb2\x18\x8c\x91\x8eF\xa5\xcdJWtU\x87x\xd5X\x96\xe1\x98\xb62p6\x02\x8fr\x8aQ\x9bH\xce\x85<\xbdu*S\x9f\x82\xd7\xa6\x01\xb3mG\x84\xe9\x91\x88\xdbj\x95)\x8f\x81Q))\'\x99\'sV\x8c\x96U\x04\x92\x07!\xd3z\x95(x\x1fJ\x95\x1a\x1bn\x9f\xf9Z\xb8th\xc9!dV!\x80\x19\x19\xf0?\n\x95+\x99\xf5\x0c;##\x01\xaf\x90\xe7SH\xc0\xda\xa5J\xe8\x08a\xc1\xfb\xabpG=#\xdf[Zyu\xb7\xf9\x1b\x9dJ\x954\xd5\xcd\x95b\xe8\x8f\xff\xd9'), PhotoSize(type='m', location=FileLocation(dc_id=1, volume_id=806025988, local_id=99326, secret=-8122635699413968908), w=320, h=180, size=18690), PhotoSize(type='x', location=FileLocation(dc_id=1, volume_id=806025988, local_id=99327, secret=-3747029989447944857), w=800, h=450, size=95674), PhotoSize(type='y', location=FileLocation(dc_id=1, volume_id=806025988, local_id=99324, secret=1023167122911426534), w=1280, h=720, size=185739)], has_stickers=False), ttl_seconds=None)
```

##### MP4 
```
MessageMediaDocument(document=Document(id=532576172337318944, access_hash=-432432432432155325, date=datetime.datetime(2017, 11, 15, 22, 50, 52, tzinfo=datetime.timezone.utc), mime_type='video/mp4', size=118515, thumb=PhotoSize(type='s', location=FileLocation(dc_id=4, volume_id=45312137, local_id=8533, secret=325452421452), w=90, h=33, size=1503), dc_id=4, version=0, attributes=[DocumentAttributeVideo(duration=2, w=480, h=178, round_message=False, supports_streaming=True), DocumentAttributeFilename(file_name='giphy.mp4'), DocumentAttributeAnimated()]), ttl_seconds=None)
```

#### Papers: 
##### Telegram API
- https://core.telegram.org

###### Library, a wrapper for heavy work.
- https://github.com/LonamiWebs/Telethon
- https://en.wikipedia.org/wiki/Wrapper_function
- https://telethon.readthedocs.io/en/stable/
- https://towardsdatascience.com/introduction-to-the-telegram-api-b0cd220dbed2
- https://telethon.readthedocs.io/en/stable/telethon.client.html#telethon.client.users.UserMethods.get_me
- https://telethon.readthedocs.io/en/stable/telethon.client.html#telethon-client
###### Users, Chats and Channels:
- https://telethon.readthedocs.io/en/stable/extra/basic/entities.html
###### Working with chats and channels;
- https://telethon.readthedocs.io/en/stable/extra/examples/chats-and-channels.html
