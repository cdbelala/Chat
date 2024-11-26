from fastapi import APIRouter, WebSocket, WebSocketDisconnect, Query
from typing import List, Optional
import logging
from services.logging_service import LoggingService
from ..models import user, database

# Initialize router and logging service
router = APIRouter()
logger = LoggingService()

# Define a manager to handle WebSocket connections
class ConnectionManager:
    def __init__(self):
        # List of active WebSocket connections
        self.active_connections: List[WebSocket] = []
        # Mapping of usernames to WebSocket connections
        self.users: dict[str, WebSocket] = {}

    async def connect(self, websocket: WebSocket, username: str):
        await websocket.accept()
        self.active_connections.append(websocket)
        self.users[username] = websocket
        logger.info(f"User '{username}' connected.")

    def disconnect(self, websocket: WebSocket, username: str):
        if websocket in self.active_connections:
            self.active_connections.remove(websocket)
            del self.users[username]
            logger.info(f"User '{username}' disconnected.")

    async def broadcast(self, message: str, sender: str):
        for username, connection in self.users.items():
            if username != sender:  # Avoid echoing back to the sender
                await connection.send_text(f"{sender}: {message}")
        logger.info(f"Message broadcasted: {message}")

manager = ConnectionManager()

@router.websocket("/ws/chat")
async def chat_endpoint(
    websocket: WebSocket,
    username: Optional[str] = Query(None),  # Username to identify users
    data = ""
):
    if not username:
        await websocket.close()
        logger.error("Connection attempt without a username.")
        return

    # Connect the client
    await manager.connect(websocket, username)
    try:
        while True:
            # Receive message from the client
            data = await websocket.receive_text()
            logger.info(f"Message received from '{username}': {data}")
            
            # Broadcast the message to all connected clients
            await manager.broadcast(data, username)
    except WebSocketDisconnect:
        # Handle disconnection
        manager.disconnect(websocket, username)
        logger.info(f"User '{username}' disconnected.")
