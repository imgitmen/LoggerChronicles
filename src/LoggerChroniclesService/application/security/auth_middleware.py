from fastapi import Security, HTTPException, status
from fastapi.security import APIKeyHeader

api_key_header = APIKeyHeader(name="X-API-Key")

class AuthService():
    def __init__(self, api_key: str):
        self._api_key = api_key
        
    def check_api_key(self, api_key: str):
        result = False
        
        if api_key is not None:
            result = True
        
        if result:
            result = False
            if api_key == self._api_key:
                result = True
                
        return result

def authMiddleware(auth_service: AuthService):
    def check_api_key(api_key: str = Security(api_key_header)):
        result = auth_service.check_api_key(api_key)

        if not result:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Missing or invalid API key"
            )
        else:
            return result
        
    return check_api_key

