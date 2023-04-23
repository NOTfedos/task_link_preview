from typing import Optional
from pydantic import BaseModel


class LinkUrl(BaseModel):
    url: str


class PreviewResponse(BaseModel):
    title: str
    description: Optional[str]
    imageUrl: Optional[str]


class PreviewErrorMsg(BaseModel):
    message: str


class PreviewErrorResp(BaseModel):
    error: PreviewErrorMsg
