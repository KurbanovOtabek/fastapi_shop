from pydantic import BaseModel, Field


class CategoryBase(BaseModel):
    name: str
