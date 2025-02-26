import datetime
from pathlib import Path

import joblib
import pandas as pd
import yfinance as yf
from prophet import Prophet

ASSETS_DIR = Path(__file__).resolve(strict=True).parent
ASSETS_DIR = ASSETS_DIR / "assets"
ASSETS_DIR.mkdir(parents=True, exist_ok=True)
TODAY = datetime.date.today()


def train(ticker):
    """
    Downloads historical stock data with yfinance, creates 
    a new Prophet model, fits the model to the stock data, 
    and then serializes and saves the model as a Joblib file.
    """
    data = yf.download(ticker, "2020-01-01", TODAY.strftime("%Y-%m-%d"))
    data.head()    

    if 'Close' not in data.columns:
        raise ValueError("The 'Close' column is missing. Check the ticker symbol or date range.")
    
    data["Close"].plot(title=f"{ticker} Stock Adjusted Closing Price")

    df_forecast = data.copy()
    df_forecast.reset_index(inplace=True)
    df_forecast["ds"] = df_forecast["Date"]
    df_forecast["y"] = df_forecast["Close"]
    df_forecast = df_forecast[["ds", "y"]]
    df_forecast

    model = Prophet()
    model.fit(df_forecast)

    joblib.dump(model, Path(ASSETS_DIR).joinpath(f"{ticker}.joblib"))


def predict(ticker, days=7):
    """
    Loads and deserializes the saved model, generates a new forecast, 
    creates images of the forecast plot and forecast components, 
    and returns the days included in the forecast as a list of dicts.
    """
    model_file = Path(ASSETS_DIR).joinpath(f"{ticker}.joblib")
    if not model_file.exists():
        return False

    model = joblib.load(model_file)

    future_date = TODAY + datetime.timedelta(days=days)

    dates = pd.date_range(start="2020-01-01", end=future_date.strftime("%m/%d/%Y"),)
    df = pd.DataFrame({"ds": dates})

    forecast = model.predict(df)
    
    # Save plots in assets folder
    # plot_path = ASSETS_DIR / f"{ticker}_plot.png"
    # components_plot_path = ASSETS_DIR / f"{ticker}_plot_components.png"

    # model.plot(forecast).savefig(plot_path)
    # model.plot_components(forecast).savefig(components_plot_path)

    return forecast.tail(days).to_dict("records")


def convert(prediction_list):
    """
    Takes the list of dicts from predict and outputs a dict of dates 
    and forecasted values (e.g., {"07/02/2020": 200}
    """
    output = {}
    for data in prediction_list:
        date = data["ds"].strftime("%m/%d/%Y")
        output[date] = data["trend"]
    return output
