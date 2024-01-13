import yfinance as yf
from loguru import logger

from nord_and_lysa_etfs import (
    lysa_bond_etfs,
    lysa_stock_etfs,
    nord_etfs,
)


def download_data(start_date, end_date):
    """
    Function to download all needed ETF data for NORD and Lysa portfolios
    """

    all_tickers = []
    # Get list of all tickers
    for dictionary in [lysa_stock_etfs, lysa_bond_etfs, nord_etfs]:
        all_tickers.extend(dictionary.values())

    # Download price data from Yahoo! finance based on list of ETF tickers and start/end dates
    try:
        daily_prices = yf.download(all_tickers, start=start_date, end=end_date)[
            "Adj Close"
        ]
    except Exception as e:
        logger.warning(f"Problem when downloading our data with an error: {e}")
        daily_prices = None

    return daily_prices


if __name__ == "__main__":
    daily_prices_df = download_data(start_date="2020-11-20", end_date="2022-01-20")
