
import pandas as pd
import yfinance as yf
import numpy as np
import os

def get_nasdaq100_data_with_metrics(period="1y"):
    """
    Fetches P/E ratios, Market Cap, and calculates annualized historical volatility
    for NASDAQ 100 tickers.

    Args:
        period (str): The period for which to fetch historical data for volatility calculation.
                      e.g., "1y", "6mo", "3mo".

    Returns:
        dict: A dictionary where keys are ticker symbols and values are
              dictionaries containing 'PE_Ratio', 'Market_Cap', and 'Volatility'.
    """

    nasdaq100_tickers = [
        "AAPL", "ABNB", "ADBE", "ADI", "ADP", "ADSK", "AEP", "AMAT", "AMD", "AMGN",
        "AMZN", "APP", "ARM", "ASML", "AVGO", "AXON", "AZN", "BIIB", "BKNG", "BKR",
        "CCEP", "CDNS", "CDW", "CEG", "CHTR", "CMCSA", "COST", "CPRT", "CRWD", "CSCO",
        "CSGP", "CSX", "CTAS", "CTSH", "DASH", "DDOG", "DXCM", "EA", "EXC", "FANG",
        "FAST", "FTNT", "GEHC", "GFS", "GILD", "GOOG", "GOOGL", "HON", "IDXX", "INTC",
        "INTU", "ISRG", "KDP", "KHC", "KLAC", "LIN", "LRCX", "LULU", "MAR", "MCHP",
        "MDLZ", "MELI", "META", "MNST", "MRVL", "MSFT", "MSTR", "MU", "NFLX", "NVDA",
        "NXPI", "ODFL", "ON", "ORLY", "PANW", "PAYX", "PCAR", "PDD", "PEP", "PLTR",
        "PYPL", "QCOM", "REGN", "ROP", "ROST", "SBUX", "SHOP", "SNPS", "TEAM", "TMUS",
        "TRI", "TSLA", "TTD", "TTWO", "TXN", "VRSK", "VRTX", "WBD", "WDAY", "XEL",
        "ZS"
    ]

    china_a_shares_tickers = [
        "600519.SS", "601318.SS", "300750.SZ", "600036.SS", "000333.SZ", "000858.SZ", "600900.SS", "601166.SS",
        "601899.SS", "600030.SS",
        "600276.SS", "601398.SS", "600887.SS", "300059.SZ", "000651.SZ", "300760.SZ", "002594.SZ", "601328.SS",
        "600309.SS", "000725.SZ",
        "600919.SS", "002475.SZ", "300124.SZ", "601288.SS", "002415.SZ", "000568.SZ", "601012.SS", "601088.SS",
        "601816.SS", "600028.SS",
        "600809.SS", "601668.SS", "603259.SS", "002714.SZ", "000001.SZ", "300498.SZ", "600016.SS", "601857.SS",
        "601225.SS", "300308.SZ",
        "688981.SS", "000063.SZ", "601988.SS", "002352.SZ", "600406.SS", "600941.SS", "000338.SZ", "600050.SS",
        "002230.SZ", "600690.SS",
        "601728.SS", "300274.SZ", "002142.SZ", "600837.SS", "000792.SZ", "601601.SS", "000100.SZ", "601888.SS",
        "600000.SS", "600031.SS",
        "601985.SS", "600150.SS", "688041.SS", "601766.SS", "601169.SS", "002371.SZ", "600089.SS", "601688.SS",
        "601138.SS", "000625.SZ",
        "600438.SS", "600048.SS", "603501.SS", "600104.SS", "600660.SS", "000002.SZ", "300015.SZ", "601211.SS",
        "603288.SS", "600436.SS",
        "601919.SS", "600905.SS", "601390.SS", "601229.SS", "300122.SZ", "002027.SZ", "688012.SS", "688111.SS",
        "601006.SS", "002304.SZ",
        "601818.SS", "600019.SS", "688271.SS", "603019.SS", "600585.SS", "002050.SZ", "002466.SZ", "601658.SS",
        "601989.SS", "600938.SS",
        "600999.SS", "688036.SS", "000938.SZ", "601628.SS", "603986.SS", "002049.SZ", "601600.SS", "600111.SS",
        "688008.SS", "300014.SZ",
        "601939.SS", "600958.SS", "600893.SS", "002460.SZ", "601009.SS", "000538.SZ", "601669.SS", "600009.SS",
        "002129.SZ", "603993.SS",
        "600886.SS", "600760.SS", "000425.SZ", "000776.SZ", "601916.SS", "600795.SS", "000661.SZ", "000166.SZ",
        "600426.SS", "600015.SS",
        "300782.SZ", "601377.SS", "601186.SS", "000157.SZ", "002241.SZ", "600926.SS", "600547.SS", "600011.SS",
        "000977.SZ", "002252.SZ",
        "600674.SS", "603799.SS", "600584.SS", "600570.SS", "002236.SZ", "002179.SZ", "000596.SZ", "002311.SZ",
        "600188.SS", "300896.SZ",
        "688256.SS", "600010.SS", "002271.SZ", "601111.SS", "001979.SZ", "300408.SZ", "600845.SS", "603369.SS",
        "600989.SS", "600745.SS",
        "601788.SS", "600115.SS", "600029.SS", "002601.SZ", "601360.SS", "601901.SS", "002493.SZ", "600196.SS",
        "002459.SZ", "601699.SS",
        "601995.SS", "600085.SS", "601100.SS", "601800.SS", "000895.SZ", "002555.SZ", "003816.SZ", "600489.SS",
        "601066.SS", "000963.SZ",
        "300142.SZ", "300033.SZ", "000768.SZ", "601633.SS", "000786.SZ", "002920.SZ", "600600.SS", "601868.SS",
        "002648.SZ", "601021.SS",
        "603392.SS", "000301.SZ", "002001.SZ", "600741.SS", "601336.SS", "601689.SS", "688599.SS", "002812.SZ",
        "600346.SS", "000983.SZ",
        "601881.SS", "600588.SS", "600515.SS", "601117.SS", "601838.SS", "688126.SS", "300450.SZ", "002736.SZ",
        "002821.SZ", "300316.SZ",
        "300433.SZ", "600176.SS", "002709.SZ", "300347.SZ", "601618.SS", "601872.SS", "000408.SZ", "002180.SZ",
        "300661.SZ", "600372.SS",
        "601898.SS", "688396.SS", "300496.SZ", "000733.SZ", "601877.SS", "600233.SS", "000999.SZ", "600219.SS",
        "002007.SZ", "600023.SS",
        "002074.SZ", "002202.SZ", "300759.SZ", "600332.SS", "603806.SS", "600362.SS", "000876.SZ", "600183.SS",
        "601607.SS", "601799.SS",
        "301269.SZ", "601238.SS", "601878.SS", "601998.SS", "600918.SS", "300999.SZ", "300223.SZ", "603260.SS",
        "688303.SS", "300413.SZ",
        "601615.SS", "002410.SZ", "600875.SS", "002603.SZ", "600061.SS", "688223.SS", "600460.SS", "600803.SS",
        "300751.SZ", "600025.SS",
        "601319.SS", "002841.SZ", "600732.SS", "603659.SS", "300454.SZ", "300919.SZ", "600132.SS", "000617.SZ",
        "300763.SZ", "000069.SZ",
        "600018.SS", "000708.SZ", "300628.SZ", "002938.SZ", "002916.SZ", "605117.SS", "600039.SS", "605499.SS",
        "603195.SS", "600754.SS",
        "603899.SS", "603290.SS", "603833.SS", "601865.SS", "688363.SS", "000877.SZ", "688065.SS", "300957.SZ",
        "601236.SS", "601698.SS",
        "688187.SS", "688561.SS", "601155.SS", "600606.SS", "300979.SZ", "601808.SS", "603486.SS", "000800.SZ",
        "601059.SS", "001289.SZ"
    ]

    stock_data = {}

    print("Fetching P/E ratios, Market Cap, and calculating volatility for NASDAQ 100 stocks...")

    for ticker_symbol in china_a_shares_tickers:
        try:
            ticker = yf.Ticker(ticker_symbol)
            info = ticker.info

            # --- Fetch P/E Ratio ---
            pe_ratio = info.get('trailingPE')
            formatted_pe = f"{pe_ratio:.2f}" if pe_ratio is not None else "N/A"

            # --- Fetch Market Cap ---
            # 'marketCap' is the key for market capitalization
            market_cap = info.get('marketCap')
            formatted_market_cap = f"{market_cap:,.0f}" if market_cap is not None else "N/A" # Format with commas

            # --- Calculate Volatility ---
            hist = ticker.history(period=period)
            volatility = "N/A - Data Error" # Default in case of issues
            if not hist.empty:
                returns = hist['Close'].pct_change().dropna()
                if not returns.empty:
                    daily_volatility = returns.std()
                    annualized_volatility = daily_volatility * np.sqrt(252)
                    volatility = f"{annualized_volatility:.4f}"
                else:
                    volatility = "N/A - No returns data"
            else:
                volatility = "N/A - No historical data"


            stock_data[ticker_symbol] = {
                'PE_Ratio': formatted_pe,
                'Market_Cap': formatted_market_cap,
                'Volatility': volatility
            }
            print(f"  {ticker_symbol}: P/E={formatted_pe}, MCap={formatted_market_cap}, Volatility={volatility}")

        except Exception as e:
            stock_data[ticker_symbol] = {'PE_Ratio': "Error", 'Market_Cap': "Error", 'Volatility': "Error"}
            print(f"  Error fetching data for {ticker_symbol}: {e}")

    return stock_data

if __name__ == "__main__":
    nasdaq100_metrics_data = get_nasdaq100_data_with_metrics(period="1y")

    # Convert the dictionary of dictionaries into a Pandas DataFrame
    df_metrics = pd.DataFrame.from_dict(nasdaq100_metrics_data, orient='index')

    print("\n--- NASDAQ 100 P/E Ratios, Market Cap, and Volatility ---")
    print(df_metrics)

    # --- Code to save to Excel on Desktop ---
    desktop_path = "/Users/alexdengmbp21/Desktop"
    excel_filename = "NASDAQ_100_Metrics.xlsx" # Changed filename for comprehensive data
    full_path = os.path.join(desktop_path, excel_filename)

    try:
        df_metrics.to_excel(full_path, index=True)
        print(f"\nSuccessfully saved all metrics to: {full_path}")
    except Exception as e:
        print(f"\nError saving to Excel: {e}")
        print("Please ensure you have 'openpyxl' installed (pip install openpyxl).")