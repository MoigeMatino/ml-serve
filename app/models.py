from sqlmodel import SQLModel, Field, Relationship
from typing import List
from .utils import short_uuid
from datetime import datetime, timezone
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy import Column

class Stock(SQLModel, table=True):
    id: str | None = Field(default_factory=short_uuid, primary_key=True)
    name: str = Field(nullable=False)
    ticker: str = Field(unique=True, nullable=False, index=True) 
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    predictions: List["Prediction"] = Relationship(back_populates="stock")

class Prediction(SQLModel, table=True):
    id: str | None = Field(default_factory=short_uuid, primary_key=True)
    stock_id: str = Field(foreign_key="stock.id", nullable=False)
    results: dict = Field(sa_column=Column(JSONB, nullable=False))  
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc), index=True)

    stock: Stock = Relationship(back_populates="predictions")
