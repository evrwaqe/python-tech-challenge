import socket
import json
from dotenv import load_dotenv
import os

load_dotenv()

HOST = "127.0.0.1"
PORT = int(os.getenv("MCP_PORT", 5000))


def send_filters(filters: dict) -> list:
    payload = json.dumps({"filters": filters})
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(payload.encode())
        data = s.recv(4096).decode()
        return json.loads(data)
