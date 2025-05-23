from pydantic import BaseModel
from typing import List

class MarkExportedPayload(BaseModel):
    document_ids: List[str]

class ArchiveCardsPayload(BaseModel):
    document_ids: List[str]
    status: str
    review_status: str

class DeleteCardsPayload(BaseModel):
    document_ids: List[str]

class MoveCardsPayload(BaseModel):
    document_ids: List[str]
    status: str = "reviewed" 