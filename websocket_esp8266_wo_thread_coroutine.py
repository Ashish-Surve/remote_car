from websockets.uri import parse_uri
import time
import websockets

import sys
import tty
import termios

def get_char():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        char = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return char

# Define the WebSocket server URI
websocket_uri = "ws://192.168.1.14:81"

import websockets
import asyncio

class WebSocketClient:
    def __init__(self):
        self.websocket = None
        self.connected = False

    async def connect(self, uri):
        self.websocket = await websockets.connect(uri)
        self.connected = True

    async def send_message(self, message):
        if self.websocket and self.connected:
            await self.websocket.send(message)
            print(f"Sent: {message}")
            # response = await self.websocket.recv()
            # print(f"Received: {response}")
        else:
            print("WebSocket is not connected.")

    def close(self):
        if self.websocket and self.connected:
            self.websocket.close()
            self.connected = False
            print("WebSocket connection closed.")
        else:
            print("WebSocket is not connected.")



# Example usage
async def main():
    client = WebSocketClient()
    await client.connect(websocket_uri)
    await client.send_message("w")
    print("Ashish")
    await client.send_message("y")

   




# Run the main coroutine
asyncio.run(main())
