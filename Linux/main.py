import asyncio
from json import loads
from threading import Thread
 
import names
import requests
from colorama import Fore, init
from telethon import TelegramClient, events, functions
from os import system
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
system('clear')
init()
C = Fore
#не удаляй
bb = f'''{C.LIGHTBLUE_EX}
ooooooooooooo           oooo            ooooo      ooo           oooo        
8'   888   `8           `888            `888b.     `8'           `888        
     888       .ooooo.   888   .ooooo.   8 `88b.    8   .oooo.    888 .oo.   
     888      d88' `88b  888  d88' `88b  8   `88b.  8  `P  )88b   888P"Y88b  
     888      888ooo888  888  888ooo888  8     `88b.8   .oP"888   888   888  
     888      888    .o  888  888    .o  8       `888  d8(  888   888   888  
    o888o     `Y8bod8P' o888o `Y8bod8P' o8o        `8  `Y888""8o o888o o888o 
                                       {C.WHITE}by https://lolz.guru/members/2977610/
'''#не удаляй

#не удаляй
print(bb)#не удаляй
#не удаляй


class spamer():
    def __init__(self):
        with open('config.json','r') as file:
            cfg = dict(loads(file.read()))
        self.text = cfg['text']
        self.report = cfg['report']
        self.edit_data = cfg['edit_data']
        self.channels = []
        self.accounts = []
        self.Gaccounts = []
        with open(cfg['PatchFileAccounts'],'r') as file:
            for account in file.readlines():
                self.accounts.append(account.replace('\n','').split(':'))
        if cfg['join_channels']:
            with open(cfg['join_channels'],'r') as file:
                for channel in file.readlines():
                    self.channels.append(channel.replace('\n','').replace('https://t.me/+',''))
    def _loginAll(self):
        e = 0
        g = 0
        for account in self.accounts:
            try:
                client =  TelegramClient('spam_'+account[0],int(account[0]),account[1])
                client.start()
                print(C.GREEN+account[0],'- login')
                self.Gaccounts.append(client)
                for channel in self.channels:
                    try:
                        if '@' in channel:
                            loop = client.loop
                            tasks = [asyncio.ensure_future(client(JoinChannelRequest(channel.replace('@',''))))]
                            loop.run_until_complete(asyncio.wait(tasks))  
                        else:
                            loop = client.loop
                            tasks = [asyncio.ensure_future(client(ImportChatInviteRequest(channel)))]
                            loop.run_until_complete(asyncio.wait(tasks))        
                    except:pass                  
                g+=1
            except:
                e+=1
                print(C.RED+account[0],' - not login')
        if self.report:
                g,e = str(g),str(e)
                token,id = self.report.split('|')
                requests.post(
                        url='https://api.telegram.org/bot{0}/{1}'.format(token, 'sendMessage'),
                                        data={'chat_id': int(id), 'text': f'<b>Запуск!</b>\n<b>Успешно:</b> <code>{g}</code>\n<b>Ошибок:</b> <code>{e}</code>','parse_mode':'HTML'}
                    )            

    

    def _get_sub(self):
                        def read(self,client):
                            async def _edit_data(client):
                                    await client(functions.account.UpdateProfileRequest(names.get_first_name(),names.get_last_name()))
                                    await client(functions.account.UpdateUsernameRequest(names.get_last_name()))
                            @client.on(events.NewMessage())
                            async def normal_handler(event):
                                
                                try:
                                    if event.is_channel and event.post:
                                        text = requests.get(self.text).text
                                        await client.send_message(event.original_update.message.peer_id, text, comment_to=event.original_update.message.id)
                                        if self.report:
                                                token,id = self.report.split('|')
                                                channel_info = await client.get_entity(event.original_update.message.peer_id)
                                                channel = channel_info.title
                                                if channel_info.username != None:' @'+ str(channel_info.username)
                                                user_info = await client.get_me()
                                                user =str(user_info.first_name) + ' ' + str(user_info.last_name)
                                                if user_info.username != None:user +=' <b>Ник:</b> @'+str(user_info.username)
                                                report = f'<b>Новый успешный первонах!</b>\n<b>Канал:</b> <i>{str(channel)}</i>\n<b>Аккаунт:</b> <i>{str(user)}</i>'
                                                requests.post(
                                                        url='https://api.telegram.org/bot{0}/{1}'.format(token, 'sendMessage'),
                                                        data={'chat_id': int(id), 'text': report,'parse_mode':'HTML'}
                                                    )
                                        if self.edit_data:
                                            await _edit_data(client)
                                except:
                                    pass     
   
                        for client in self.Gaccounts:
                                t = Thread(target=read,args=(self,client,),daemon=True)
                                t.start()
        




if __name__ == '__main__':
    sp = spamer()

    sp._loginAll()
    sp._get_sub()
    for с in sp.Gaccounts:
        с.run_until_disconnected()
