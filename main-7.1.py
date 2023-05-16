stocks = {
  "AAPL": "165.33",
  "MSFT": "281.77",
  "IBM": "125.40",
  "AAPL": "165.33",
  "GME": "19.93",
  "BBY": "73.55",
  "WMT": "152.76",
  "TGT": "163.94",
  "HD": "301.64",  
  "NVDA": "207.42"
}

def main():
  ticker = str(input("Please enter the stock ticker symbol:"))
  print()
  
  if(ticker in stocks):
    print('Ticker symbol:', ticker)
    print('Stock price:', stocks[ticker])
    print()
  else:
    print('Ticker not found. Please try again')
    print()
    main()

main()