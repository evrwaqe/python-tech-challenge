import socket
import json
from server.db_handler import DBHandler
from dotenv import load_dotenv
import os

load_dotenv()

HOST = "127.0.0.1"
PORT = int(os.getenv("MCP_PORT", 5000))


def handle_request(data: str) -> str:
    try:
        request = json.loads(data)
        filters = request.get("filters", {})
        db = DBHandler()
        vehicles = db.get_filtered_vehicles(filters)
        db.close()

        response = [
            {
                "brand": v.brand,
                "model": v.model,
                "year": v.year,
                "color": v.color,
                "mileage": v.mileage,
                "price": v.price
            }
            for v in vehicles
        ]
        return json.dumps(response)
    except Exception as e:
        return json.dumps({"error": str(e)})


def run_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print(f"[SERVER] Listening on {HOST}:{PORT}")

        while True:
            conn, addr = s.accept()
            with conn:
                print(f"[SERVER] Connected by {addr}")
                data = conn.recv(4096).decode()
                if not data:
                    break
                response = handle_request(data)
                conn.sendall(response.encode())


if __name__ == "__main__":
    run_server()
