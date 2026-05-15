import websocket
import json
import threading

#gesture recognition
#import yolo
#publish results(labels ect) to a new topic

ROS_IP = "192.168.30.100"  
fps = 0

def on_message(ws, message):
    global fps
    data = json.loads(message)
    if data.get("topic") == "/metrics/fps":
        fps = data["msg"]["data"]
        
def on_open(ws):
    # subscribe to topic
    subscribe_msg = {
        "op": "subscribe",
        "topic": "/metrics/fps"
    }
    ws.send(json.dumps(subscribe_msg))

ws = websocket.WebSocketApp(
    f"ws://{ROS_IP}:9090",
    on_message=on_message,
    on_open=on_open
)

wst=threading.Thread(target=ws.run_forever)
wst.daemon = True
wst.start()


def getfps():
    global fps
    return fps


