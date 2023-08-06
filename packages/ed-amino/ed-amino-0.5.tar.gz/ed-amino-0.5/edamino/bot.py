from time import time
from os import environ

from ujson import loads
from .client import Client
from .logger import logger as log
from .context import Context
from .objects import Message
from .api import MessageType, MediaType, InvalidRequest, WebSocketConnectError

from dotenv import load_dotenv
from asyncio import get_event_loop, AbstractEventLoop
from json import JSONDecodeError
from collections import namedtuple
from typing import Optional, List, Union, Tuple, Dict, Callable

load_dotenv('.env')

Handler = namedtuple('Handler', ['media_types', 'message_types', 'callback', 'description'])
HANDLERS_COMMANDS: Dict[str, Handler] = {}
HANDLERS_EVENTS: List[Handler] = []
ON_READY: Optional[Callable] = None


def exception_handler(loop, context):
    exception = context.get("exception", None)
    if isinstance(exception, InvalidRequest):

        try:
            data = loads(exception.args[0])
            log.error(f"{data['api:message']} {data['api:statuscode']}")
        except JSONDecodeError:
            log.error(exception)
    else:
        raise exception


async def help(ctx: Context):
    string: str = ""
    for key, value in HANDLERS_COMMANDS.items():
        if 'help' not in key:
            string += f'{key} - {value.description}\n'

    await ctx.reply(message=string)


class Bot:
    __slots__ = ('email', 'password', 'prefix', 'loop', 'sid', 'uid', 'timestamp')

    def __init__(self, email: str, password: str, prefix: str = ""):
        self.uid = None
        self.sid = None
        self.loop = None
        self.email = email
        self.password = password
        self.prefix = prefix
        self.timestamp = None

    def check_cfg(self):
        email = environ.get('email')
        password = environ.get('password')

        if email != self.email:
            self.sid = None
            return

        if password == self.password:
            self.sid = environ.get('sid')
            self.uid = environ.get('uid')
        else:
            self.sid = None

        try:
            self.timestamp = int(environ.get('timestamp'))
            if time() - self.timestamp > 60 * 60 * 12:
                self.sid = None
        except TypeError:
            self.timestamp = int(time())
            self.sid = None

    def update_cfg(self):
        string = f"sid={self.sid}\n" \
                 f"uid={self.uid}\n" \
                 f"email={self.email}\n" \
                 f"password={self.password}\n" \
                 f"timestamp={int(time())}"

        with open('.env', 'w') as file:
            file.write(string)

    @staticmethod
    def event(
            message_types: Optional[Union[List[int], Tuple[int, ...]]] = None,
            media_types: Optional[Union[List[int], Tuple[int, ...]]] = None):

        if not message_types:
            message_types = [MessageType.TEXT]
        if not media_types:
            media_types = [MediaType.TEXT]

        def register_handler(callback):
            handler = Handler(
                description=None,
                media_types=tuple(media_types),
                message_types=tuple(message_types),
                callback=callback
            )
            HANDLERS_EVENTS.append(handler)
            return callback

        return register_handler

    def command(self,
                command: str,
                description: Optional[str] = None,
                message_types: Optional[Union[List[int], Tuple[int, ...]]] = None,
                media_types: Optional[Union[List[int], Tuple[int, ...]]] = None):

        command = command.lower()

        if not message_types:
            message_types = [MessageType.TEXT]
        if not media_types:
            media_types = [MediaType.TEXT]

        def register_handler(callback):
            handler = Handler(
                description=description,
                media_types=tuple(media_types),
                message_types=tuple(message_types),
                callback=callback
            )
            HANDLERS_COMMANDS[f"{self.prefix}{command}"] = handler

            return callback

        return register_handler

    async def __call(self, client: Client) -> None:
        ws = await client.ws_connect()
        if ON_READY:
            await ON_READY()

        while True:
            try:
                if ws.closed:
                    if time() - self.timestamp > 60 * 60 * 12:
                        await client.login(self.email, self.password)
                        log.info('login')
                        self.update_cfg()

                    ws = await client.ws_connect()
                    log.info('Reconnected.')

                data = await ws.receive_json(loads=loads)
                if data['t'] == 1000:
                    msg = Message(**data['o']['chatMessage'], ndcId=data['o']['ndcId'])

                    client_context = Client(session=client.session, device_id=client.device_id, com_id=msg.ndcId)
                    client_context.login_sid(self.sid, self.uid)
                    context = Context(msg=msg, client=client_context)

                    if msg.author.uid != self.uid:

                        for handler in HANDLERS_EVENTS:
                            if msg.type in handler.message_types and msg.mediaType in handler.media_types:
                                self.loop.create_task(handler.callback(context))

                        if msg.content is not None:
                            command = msg.content.split(" ")[0]
                            command = command.lower()
                            handler = HANDLERS_COMMANDS[command]

                            if msg.type in handler.media_types and msg.mediaType in handler.media_types:
                                self.loop.create_task(handler.callback(context))

            except (TypeError, KeyError, AttributeError, WebSocketConnectError) as e:
                continue

    def start(self, loop: Optional[AbstractEventLoop] = None, device_id: Optional[str] = None) -> None:
        self.check_cfg()
        self.loop = loop if loop is not None else get_event_loop()
        self.loop.set_exception_handler(exception_handler)

        client = Client(device_id=device_id)
        try:
            if self.sid is None:
                login = self.loop.run_until_complete(client.login(self.email, self.password))
                self.sid = login.sid
                self.uid = login.auid
                log.info("update cfg")
                self.update_cfg()

            client.sid = self.sid
            client.uid = self.uid
            # future = run_coroutine_threadsafe(self.__call(loop), loop)
            # Thread(target=loop.run_forever).start()
            #
            # future.result()

            handler = Handler(
                callback=help,
                message_types=[MessageType.TEXT],
                media_types=[MediaType.TEXT],
                description=None
            )

            HANDLERS_COMMANDS[f'{self.prefix}help'] = handler

            self.loop.run_until_complete(self.__call(client))
        except KeyboardInterrupt:
            log.info("Goodbye. ^^")
        finally:
            self.loop.run_until_complete(client.session.close())

    @staticmethod
    def on_ready(t):
        # :)
        global ON_READY
        ON_READY = t
