# trading/data_downloader.py

import argparse
import yfinance as yf
import os

def download_data(ticker: str, start_date: str, end_date: str, output_path: str) -> None:
    """
    Download historical data from Yahoo Finance for a given ticker and date range,
    then save it as a CSV file.
    """
    # If the CSV already exists, skip download to save time (optional behavior).
    if os.path.exists(output_path):
        print(f"File {output_path} already exists. Skipping download.")
        return

    print(f"Downloading data for {ticker} from {start_date} to {end_date}...")
    df = yf.download(ticker, start=start_date, end=end_date)
    df.to_csv(output_path)
    print(f"Data saved to {output_path}.")

def main():
    """
    Command-line entry point. Parses arguments and calls download_data().
    """
    parser = argparse.ArgumentParser(
        description="Download historical data from Yahoo Finance and save to CSV."
    )
    parser.add_argument("--ticker", required=True, help="Ticker symbol (e.g. AAPL)")
    parser.add_argument("--start", required=True, help="Start date (YYYY-MM-DD)")
    parser.add_argument("--end", required=True, help="End date (YYYY-MM-DD)")
    parser.add_argument("--output", required=True, help="Output CSV file path")

    args = parser.parse_args()
    download_data(args.ticker, args.start, args.end, args.output)

if __name__ == "__main__":
    main()
