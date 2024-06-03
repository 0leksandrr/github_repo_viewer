from datetime import datetime

from pydantic import BaseModel


class RepositorySchema(BaseModel):
    name: str
    created_at: datetime
    stargazers_count: int
    colaborators_count: int

    class Config:
        orm_mode = True
