import asyncio
import websockets
import threading
from pynput import keyboard

# mac 98:f4:ab...
websocket_uri = "ws://192.168.1.10:81"

class WebSocketClient:
    def __init__(self):
        self.webso
        self.connected = False

    async def connect(self, uri):
        self.websocket = await websockets.connect(uri)
        self.connected = True

    def send_message(self, message):
        if self.websocket and self.connected:
            asyncio.run_coroutine_threadsafe(self.websocket.send(message), self.websocket.loop)
            print(f"Sent: {message}")
        else:
            print("WebSocket is not connected.")

    def close(self):
        if self.websocket and self.connected:
            self.websocket.close()
            self.connected = False
            print("WebSocket connection closed.")
        else:
            print("WebSocket is not connected.")

exit_program = False

def on_press(key):
    global exit_program
    try:
        if key.char == 'q':
            print("Exiting...")
            exit_program = True
            return False  # Stop the listener
        elif key.char =='a':  # quick fix fix arduino code.
            client.send_message("d")
            print(f"Key {key.char} pressed")
        elif key.char =='d': # quick fix fix qrduino code.
            client.send_message("a")
            print(f"Key {key.char} pressed")
        else:
            client.send_message(key.char)
            print(f"Key {key.char} pressed")
    except AttributeError:
        print(f"Special key {key} pressed")

def on_release(key):
    global client
    try:
        print(f"Key {key.char} released")
        client.send_message("y") # anything other than wasd is stop motors
    except AttributeError:
        print(f"Special key {key} released")

def keyboard_listener():
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        print("Listening for key events...")
        listener.join()

async def main():
    global client, exit_program
    client = WebSocketClient()
    await client.connect(websocket_uri)
    keyboard_thread = threading.Thread(target=keyboard_listener)
    keyboard_thread.start()

    while not exit_program:
        await asyncio.sleep(1)

    client.close()  # Close the WebSocket connection
    keyboard_thread.join()  # Wait for the keyboard thread to finish

asyncio.run(main())
