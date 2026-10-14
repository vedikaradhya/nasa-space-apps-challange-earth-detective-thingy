from sqlmodel import SQLModel, Field
from typing import Optional

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    github_id: Optional[int] = Field(index=True)
    login: Optional[str]
    email: Optional[str]
    is_active: bool = True

class DataRecord(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    source: str
    remote_id: Optional[str]
    payload: Optional[str]
