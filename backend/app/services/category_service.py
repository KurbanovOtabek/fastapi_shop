from sqlalchemy.orm import Session
from typing import List
from ..repositories.category_repository import CategoryRepository
from ..schemas.category import CategoryResponse, CategoryCreate
from fastapi import HTTPException, status


class CategoryService:
    def __init__(self, db: Session):
        self.repository = CategoryRepository(db)

    def get_all_categories(self) -> List[CategoryResponse]:
        categories = self.repository.get_all()
