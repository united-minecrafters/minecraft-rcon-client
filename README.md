# minecraft-rcon-client

A simple class to allow you to interact with a minecraft server. The server must have rcon enabled in `server.properties`:
```ini
enable-rcon=true
rcon.port=2000
rcon.password=secret
```

## Usage
```python
import asyncio

from minecraft import Server

async def main():
    ip = "1.1.1.1"
    port = 2000 # rcon port
    password = "password"
    
    # can be used in a context manager
    async with Server(ip, port, password) as server:
        print(await server.send("list"))
    
    # can also be used procedurally
    server = Server(ip, port, password, connect_on_send=True)
    # connect_on_send make it so the Server tried to reconnect if
    # it's disconnected, otherwise it raises a NotConnectedError
    print(await server.send("list"))
    
    for i in await server.online():
        print(f"{i} is online")
    
    await server.close()

asyncio.run(main())
```

## Requirements
Python >= 3.6
