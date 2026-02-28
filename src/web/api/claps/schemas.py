from pydantic import BaseModel


class Clap(BaseModel):
    identifier: str
    count: int


class ClapsCreateRequest(BaseModel):
    identifier: str


class ClapsCreateResponse(BaseModel):
    clap: Clap


class ClapsGetCountRequest(BaseModel):
    identifier: str


class ClapsGetCountResponse(BaseModel):
    clap: Clap
