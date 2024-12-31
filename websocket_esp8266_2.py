from pynput import keyboard
import websockets

# Define a function to handle key press events
async def on_press(key):
    try:
        print(f"Key {key.char} pressed")
        await send_payloads(key.char)
    except AttributeError:
        print(f"Special key {key} pressed")

# Define a function to handle key release events
async def on_release(key):
    try:
        print(f"Key {key.char} released")
        send_payloads("y")
    except AttributeError:
        print(f"Special key {key} released")
    
    # Stop listener if 'esc' key is pressed
    if key == keyboard.Key.esc:
        return False


async def send_payloads(payload):
    websocket_uri = "ws://192.168.1.14:81"
    
    async with websockets.connect(websocket_uri) as websocket:
        print(f"Connected to WebSocket server at {websocket_uri}")
        
        await websocket.send(payload)
        print(f"Sent payload: {payload}")
        # await asyncio.sleep(0.5)  # Wait for 1 second before sending the next payload

# Create keyboard listener objects
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    print("Listening for key events...")
    listener.join()