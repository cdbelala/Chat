from fastapi import FastAPI, Request
from routes.auth_routes import router as auth_router
from fastapi.responses import JSONResponse
from services.logging_service import LoggingService
from controllers.chat_controller import router as chat_router  # Import the chat router
from middlewares.auth_middleware import AuthMiddleware
# Initialize FastAPI and LoggingService
app = FastAPI() 
logger = LoggingService()

app.include_router(auth_router)
app.add_middleware(AuthMiddleware)

# Middleware for logging requests and responses
@app.middleware("http")
async def log_requests(request: Request, call_next):
    # Log the incoming request
    logger.info(f"Request: {request.method} {request.url}")
    
    # Process the request and capture the response
    response = await call_next(request)
    
    # Log the response status code
    logger.info(f"Response status: {response.status_code}")
    return response

# Custom exception handler for logging errors
@app.exception_handler(Exception)
async def handle_exception(request: Request, exc: Exception):
    logger.error(f"Unhandled error: {exc}")
    return JSONResponse(
        status_code=500,
        content={"message": "An unexpected error occurred."},
    )

# Include the chat router to handle WebSocket connections
app.include_router(chat_router)

# Include routers
app.include_router(auth_router, prefix="/auth")
app.include_router(chat_router, prefix="/chat")