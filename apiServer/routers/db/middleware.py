from fastapi import Request
from fastapi.routing import APIRoute
from . import crud_auth

class VerifyToken(APIRoute):
    def get_route_handler(self):
        original_route = super().get_route_handler()

        async def verify_token_middleware(request: Request):
            token = request.headers["Authorization"].split(" ")[1]
            validation_response = crud_auth.validate_token(token, output=False)

            if validation_response == None:
                return await original_route(request)
            else:
                return crud_auth.validate_token(token, output=True)
        
        return verify_token_middleware