import aiohttp
from typing import *
from . import logger


class ServerOffline(Exception):
    pass

class NodeInstance:
    def __init__(self, url: str):
        self.session = aiohttp.ClientSession(headers={'Accepts': 'application/json'})
        self.url: str = url
    
    def __repr__(self) -> str:
        return f'<WsInstance {self.url}>'
    
    async def check_alive(self) -> bool:
        # send a ping to the server
        try:
            async with self.session.post(self.url, json={'jsonrpc': '2.0', 'method': 'eth_syncing', 'params': [], 'id': 1}) as resp:
                if resp.status == 200:
                    if (await resp.json())['result']:   # "alive" is also syncedl
                        return False
                    else:
                        return True
                else:
                    return False
        except:
            return False
    
    async def handle_request(self, json: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        # send the request to the server
        try:
            async with self.session.post(self.url, json=json) as resp:
                if resp.status == 200:
                    return await resp.json()
                else:
                    return {'error': f'Server returned error code {resp.status}'}
        except:
            raise ServerOffline('Server is offline')
    
    async def stop_session(self):
        await self.session.close()

class NodeResponse:
    def __init__(self, json: Dict[str, Any], status_code: int):
        self.json: Dict[str, Any] = json
        self.status_code: int = status_code

class InstanceList:
    def __init__(self, nodeinstance: NodeInstance, status: bool):
        self.instance = nodeinstance
        self.url = nodeinstance.url
        self.status = status

    def __repr__(self) -> str:
        return f'<InstanceList {self.url} Status {self.status}>'
    

class NodeRouter:
    def __init__(self, urls: list):
        if not urls:
            raise ValueError('No nodes provided')
        self.urls: List[str] = urls
        self.instances: List[InstanceList] = []
        self.dispatch = logger.dispatch
        self.listener = logger.listener

    async def set_offline(self, instance: NodeInstance) -> None:
        index = self.instances.index(instance)
        self.instances[index].status = False
        await self.dispatch('node_offline', instance.url)
    
    async def set_online(self, instance: NodeInstance) -> None:
        index = self.instances.index(instance)
        self.instances[index].status = True
        await self.dispatch('node_online', instance.url)

    async def setup(self) -> None:
        for url in self.urls:
            instance = NodeInstance(url)
            if (await instance.check_alive()):
                self.instances.append(InstanceList(instance, True))
            else:
                self.instances.append(InstanceList(instance, False))
        print('Ready.')
    
    async def recheck(self) -> None:
        for instance in self.instances: # check servers for if they're dead or alive
            if await instance.instance.check_alive():
                await self.set_online(instance.instance)
            else:
                await self.set_offline(instance.instance)

    async def get_alive_server(self) -> Optional[InstanceList]:
        for instance in self.instances:
            if not instance.status:
                continue
            if (await instance.instance.check_alive()):
                return instance
            else:
                await self.set_offline(instance.instance)

    async def do_request(self, request: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        instance = await self.get_alive_server()
        try:
            data = await instance.instance.handle_request(request)
            return data
        except ServerOffline:
            await self.set_offline(instance.instance)
            return None
        except AttributeError:
            return None # you're probably out of alive nodes!!

    async def route(self, request: Dict[str, Any]) -> NodeResponse:
        data = await self.do_request(request)
        counter = 0
        while not data:
            data = await self.do_request(request)
            counter += 1
            if counter > 10:
                await self.dispatch('all_offline')
                return NodeResponse({'error': 'Could not connect to any nodes'}, 503)
        #await self.dispatch('request_done', request, data) lmk if this should be added, I think it's not needed
        return NodeResponse(data, 200)

    async def stop(self) -> None:
        for instance in self.instances:
            await instance.instance.stop_session()
    