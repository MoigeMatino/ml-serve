from pydantic import BaseModel

class StockIn(BaseModel):
    ticker: str
    
    class Config:
        orm_mode = True


class StockOut(StockIn):
    forecast: list[dict]