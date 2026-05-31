from pydantic import BaseModel

class BlogRequest(BaseModel):
    prompt:str
