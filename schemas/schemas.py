from pydantic import BaseModel


class Result(BaseModel):
    result: int


class Input(BaseModel):
    input : int