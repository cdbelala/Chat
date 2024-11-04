from fastapi import APIRouter, WebSocket, WebSocketDisconnect, Depends
from typing import List
import logging
from services.logging_service import LoggingService

# Initialize router and logging service
router = APIRouter()
logger = LoggingService()

# Define a manager to handle WebSocket connections
class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)
        logger.info("New connection established.")

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)
        logger.info("Connection closed.")

    async def broadcast(self, message: str):
        for connection in self.active_connections:
            await connection.send_text(message)
            logger.info(f"Broadcasted message: {message}")

manager = ConnectionManager()

@router.websocket("/ws/chat")
async def chat_endpoint(websocket: WebSocket):
    # Connect the client
    await manager.connect(websocket)
    try:
        while True:
            # Receive message from the client
            data = await websocket.receive_text()
            logger.info(f"Received message: {data}")
            
            # Broadcast the message to all connected clients
            await manager.broadcast(data)
    except WebSocketDisconnect:
        # Remove the connection when client disconnects
        manager.disconnect(websocket)
        logger.info("Client disconnected.")
