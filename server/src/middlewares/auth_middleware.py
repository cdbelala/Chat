from fastapi import Request, HTTPException
from starlette.middleware.base import BaseHTTPMiddleware
from firebase_admin import auth
from firebase_admin.auth import ExpiredIdTokenError, InvalidIdTokenError
from typing import Callable


class AuthMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next: Callable):
        # Extract the Firebase token from the Authorization header
        auth_header = request.headers.get('Authorization')

        # Ensure the request has an Authorization header with 'Bearer' prefix
        if not auth_header or not auth_header.startswith('Bearer '):
            raise HTTPException(status_code=401, detail="Authorization header missing or malformed")

        # Extract the token part after 'Bearer'
        token = auth_header.split(' ')[1]
        try:
            # Verify the Firebase ID token
            decoded_token = auth.verify_id_token(token)
            request.state.user = decoded_token  # Attach user info to request for later use
        except ExpiredIdTokenError:
            raise HTTPException(status_code=401, detail="Authentication token expired")
        except InvalidIdTokenError:
            raise HTTPException(status_code=401, detail="Invalid authentication token")
        except Exception as e:
            raise HTTPException(status_code=401, detail="Authentication failed")

        # Proceed to the next middleware or route
        response = await call_next(request)
        return response