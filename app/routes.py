from fastapi import APIRouter, HTTPException
from .schemas import StockIn, StockOut
from .model import predict

router = APIRouter()


@router.post("/predict", response_model=StockOut, status_code=200)
async def prediction(payload: StockIn):
    ticker = payload.ticker
    prediction_list = predict(ticker)
    
    if not prediction_list:
        raise HTTPException(status_code=400, detail="Model not found.")
    
    response = {"ticker": ticker, "forecast": prediction_list}
    return response