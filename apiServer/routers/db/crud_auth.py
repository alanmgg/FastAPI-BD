from jwt import encode, decode, exceptions
from datetime import datetime, timedelta
from fastapi.responses import JSONResponse

import env

def expire_date(days: int):
    date = datetime.now()
    new_date = date + timedelta(days)
    return new_date

def write_token(data: dict):
    token = encode(payload={**data, "exp": expire_date(2)}, key=env.SECRET_KEY, algorithm="HS256")
    return token

def validate_token(token, output=False):
    try:
        if output:
            return decode(token, key=env.SECRET_KEY, algorithms=["HS256"])
        decode(token, key=env.SECRET_KEY, algorithms=["HS256"])
    except exceptions.DecodeError:
        return JSONResponse(content={"message": "Invalid token"}, status_code=401)
    except exceptions.ExpiredSignatureError:
        return JSONResponse(content={"message": "Token expired"}, status_code=401)
