import asyncio
import websockets
import time

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


async def send_payloads():
    websocket_uri = "ws://192.168.1.14:81"
    
    async with websockets.connect(websocket_uri) as websocket:
        print(f"Connected to WebSocket server at {websocket_uri}")
        
        while True:
            start_time = time.time()
            payload = get_char()  # Prompt user for input
            if payload=="q":
                exit()
            await websocket.send(payload)
            print(f"Sent payload: {payload}")
            # await asyncio.sleep(0.5)  # Wait for 1 second before sending the next payload


# Create and run an event loop for the coroutine
async def main():
    await send_payloads()

if __name__ == "__main__":
    asyncio.run(main())

