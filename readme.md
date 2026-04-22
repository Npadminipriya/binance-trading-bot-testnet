# Binance Futures Trading Bot (Testnet)

## Features
- Market and Limit Orders
- BUY and SELL support
- CLI-based input
- Logging to file
- Error handling and validation

## Setup
1. Install dependencies:
   pip install -r requirements.txt

## Run

### Market Order
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001

### Limit Order
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 60000

## Note
Due to regional restrictions accessing Binance Futures Testnet (KYC redirection issue), API calls were mocked. The structure, validation, CLI interface, and logging are fully implemented and ready to integrate with real APIs.