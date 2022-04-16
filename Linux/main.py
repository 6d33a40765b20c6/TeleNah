# -*- coding: utf-8 -*-
__author__ = 'except'
import asyncio
from getpass import getpass
from json import loads
from os import mkdir, path, system
from secrets import choice
from time import sleep

import requests
from rich import pretty, print
from rich.prompt import Prompt
from telethon import TelegramClient, events, utils
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.messages import ImportChatInviteRequest

FORMAT = "%(message)s"
pretty.install()
bb = '\x5b\x6d\x61\x67\x65\x6e\x74\x61\x5d\x0a\x6f\x6f\x6f\x6f\x6f\x6f\x6f\x6f\x6f\x6f\x6f\x6f\x6f\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x6f\x6f\x6f\x6f\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x6f\x6f\x6f\x6f\x6f\x20\x20\x20\x20\x20\x20\x6f\x6f\x6f\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x6f\x6f\x6f\x6f\x0a\x38\x27\x20\x20\x20\x38\x38\x38\x20\x20\x20\x60\x38\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x60\x38\x38\x38\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x60\x38\x38\x38\x62\x2e\x20\x20\x20\x20\x20\x60\x38\x27\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x60\x38\x38\x38\x0a\x20\x20\x20\x20\x20\x38\x38\x38\x20\x20\x20\x20\x20\x20\x20\x2e\x6f\x6f\x6f\x6f\x6f\x2e\x20\x20\x20\x38\x38\x38\x20\x20\x20\x2e\x6f\x6f\x6f\x6f\x6f\x2e\x20\x20\x20\x38\x20\x60\x38\x38\x62\x2e\x20\x20\x20\x20\x38\x20\x20\x20\x2e\x6f\x6f\x6f\x6f\x2e\x20\x20\x20\x20\x38\x38\x38\x20\x2e\x6f\x6f\x2e\x0a\x20\x20\x20\x20\x20\x38\x38\x38\x20\x20\x20\x20\x20\x20\x64\x38\x38\x27\x20\x60\x38\x38\x62\x20\x20\x38\x38\x38\x20\x20\x64\x38\x38\x27\x20\x60\x38\x38\x62\x20\x20\x38\x20\x20\x20\x60\x38\x38\x62\x2e\x20\x20\x38\x20\x20\x60\x50\x20\x20\x29\x38\x38\x62\x20\x20\x20\x38\x38\x38\x50\x22\x59\x38\x38\x62\x0a\x20\x20\x20\x20\x20\x38\x38\x38\x20\x20\x20\x20\x20\x20\x38\x38\x38\x6f\x6f\x6f\x38\x38\x38\x20\x20\x38\x38\x38\x20\x20\x38\x38\x38\x6f\x6f\x6f\x38\x38\x38\x20\x20\x38\x20\x20\x20\x20\x20\x60\x38\x38\x62\x2e\x38\x20\x20\x20\x2e\x6f\x50\x22\x38\x38\x38\x20\x20\x20\x38\x38\x38\x20\x20\x20\x38\x38\x38\x0a\x20\x20\x20\x20\x20\x38\x38\x38\x20\x20\x20\x20\x20\x20\x38\x38\x38\x20\x20\x20\x20\x2e\x6f\x20\x20\x38\x38\x38\x20\x20\x38\x38\x38\x20\x20\x20\x20\x2e\x6f\x20\x20\x38\x20\x20\x20\x20\x20\x20\x20\x60\x38\x38\x38\x20\x20\x64\x38\x28\x20\x20\x38\x38\x38\x20\x20\x20\x38\x38\x38\x20\x20\x20\x38\x38\x38\x0a\x20\x20\x20\x20\x6f\x38\x38\x38\x6f\x20\x20\x20\x20\x20\x60\x59\x38\x62\x6f\x64\x38\x50\x27\x20\x6f\x38\x38\x38\x6f\x20\x60\x59\x38\x62\x6f\x64\x38\x50\x27\x20\x6f\x38\x6f\x20\x20\x20\x20\x20\x20\x20\x20\x60\x38\x20\x20\x60\x59\x38\x38\x38\x22\x22\x38\x6f\x20\x6f\x38\x38\x38\x6f\x20\x6f\x38\x38\x38\x6f\x0a\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x5b\x2f\x6d\x61\x67\x65\x6e\x74\x61\x5d\x5b\x79\x65\x6c\x6c\x6f\x77\x5d\x62\x79\x20\x65\x78\x63\x65\x70\x74\x5b\x2f\x79\x65\x6c\x6c\x6f\x77\x5d'


def askCode(phone):
    while True:
        code = Prompt.ask(f'[magenta]Code sent to you "[green]{phone}[/green]"[/magenta]')
        try:
            int(code)
            return code
        except:
            print('[red]Is not code[/red]')
def askPassword(phone):
    return Prompt.ask(f'[magenta]Password (2fa) "[green]{phone}[/green]"[/magenta]')
def  banner():
        system('clear')
        print(bb)




class TeleNah():
    def __init__(self):
        self.accounts = []
        self.text = []
        self.channels = []
        self.clients = []
        banner()
        if not self.config_read():
            return
        if not path.exists('sessions'):
            mkdir('sessions')
        banner()
        asyncio.get_event_loop().run_until_complete(self.LoginAccounts())
        if self.channels:
            asyncio.get_event_loop().run_until_complete(self.JoinChannels())
        asyncio.get_event_loop().run_until_complete(self.LaunchNah())


    def sendTG(self,message):
        if self.token_bot and self.user_id:
            requests.post(
            url='https://api.telegram.org/bot{0}/{1}'.format(self.token_bot, 'sendMessage'),
            data={'chat_id': int(self.user_id), 'text': '[<a href="https://lolz.guru/members/2977610/">TeleNah by except</a>]\n'+message,'parse_mode':'HTML'}
            )


    def config_read(self):
        print('[yellow]Read config.json...[/yellow]')
        try:
            with open('config.json','r') as file:
                    cfg = loads(file.read())
            self.API_ID = cfg['API_ID']
            self.API_HASH = cfg['API_HASH']
            self.link_preview = cfg['link_preview']
            if cfg['token_bot'] and cfg['user_id']:
                self.token_bot = cfg['token_bot']
                self.user_id = cfg['user_id']
            else:
                self.token_bot = False
                self.user_id = False
            try:
                with open(cfg['PatchFileText'],'r') as file:
                    for text in file.readlines():
                        self.text.append(text)
            except:
                raise Exception('File with "PatchFileText" not found.')
            try:
                with open(cfg['PatchFileAccounts'],'r') as file:
                    for _ in file.readlines():
                        phone = utils.parse_phone(_)
                        if phone:
                            self.accounts.append(phone)
                        else:
                            print(f'[cyan]"{_}" is not phone number[/cyan]')
            except:
                raise Exception('File with "PatchFileAccounts" not found.')
            try:
                if cfg['PatchFileChannels']:
                    with open(cfg['PatchFileChannels'],'r') as file:
                        for channel in file.readlines():
                            self.channels.append(channel.replace('\n',''))
            except:
                raise Exception('File with "PatchFileChannels" not found.')
            print('[green]Successful reading of config.json[/green]')
            sleep(0.5)
            return True
        except Exception as error:
            print(
                f'''[red]Error:[/red] [blue]"{error}"[/blue]''',
                '''\n[magenta]Read please:[/magenta] [green]https://github.com/6d33a40765b20c6/TeleNah/blob/main/README.md[/green]'''
            )


    async def LoginAccounts(self):
        for account in self.accounts:
            try:
                client =  TelegramClient(
                    f"sessions/{account}_telenah.session",
                    self.API_ID,
                    self.API_HASH,
                    device_model='TeleNah by except'
                )

                await client.start(
                    account,
                    lambda: askPassword(account),
                    code_callback= lambda: askCode(account)
                )
                me = await client.get_me()
                print(f'[magenta]"[green]{account}[/green]": Login [/magenta]')
                self.clients.append(client)
            except:
                print(f'[magenta]"[red]{account}[/red]": Not login [/magenta]')
        self.sendTG('<b>All accounts loaded!</b>')


    async def JoinChannels(self):
        for channel in self.channels:
            for client in self.clients:
                me = await client.get_me()
                phone = me.phone
                if '@' in channel:
                    try:
                        await client(JoinChannelRequest(channel.replace('@','')))
                        print(f'[magenta]"[green]{phone}[/green]": Joined "[green]{channel}[/green]"[/magenta]')
                    except:
                        print(f'[magenta]"[red]{phone}[/red]": Did not join "[red]{channel}[/red]"[/magenta]')
                elif 't.me/+' in channel:
                    try:
                        await client(ImportChatInviteRequest(channel.replace('t.me/+','').replace('https://','')))
                        print(f'[magenta]"[green]{phone}[/green]": Joined "[green]{channel}[/green]"[/magenta]')
                    except:
                        print(f'[magenta]"[red]{phone}[/red]": Did not join "[red]{channel}[/red]"[/magenta]')
        self.sendTG('<b>All accounts Joined!</b>')


    async def LaunchNah(self):
        for client in self.clients:
            async def __(client):
                @client.on(events.NewMessage())
                async def _(event):
                    try:
                        if event.message.post and event.message.replies:
                            event.message.peer_id.channel_id
                            await client.send_message(
                                event.chat,
                                choice(self.text).replace('[n]','\n'),
                                comment_to=event.message.id,
                                link_preview=self.link_preview,
                                parse_mode='markdown'
                            )
                            me = await client.get_me()
                            channel  = await client.get_entity(event.chat)
                            if channel.username:
                                channel = channel.username
                            else:
                                channel = channel.title
                            print(f'[magenta]"[green]{me.phone}[/green]": Send message to "[green]{channel}[/green]"[/magenta]')
                            self.sendTG(f'<code>{me.phone}</code><i>: Send message to "{channel}"</i>')
                    except Exception as error:
                        me = await client.get_me()
                        self.sendTG(f'<code>{me.phone}</code><i>: Error send "{error}"</i>')
            await __(client)
try:
    s = TeleNah()
    for client in s.clients:
        client.run_until_disconnected()
except Exception as e:
    print(e)

getpass('Press enter...')