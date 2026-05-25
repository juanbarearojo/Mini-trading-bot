import yfinance as yf
import pandas as pd

ticker = ['AMZN', 'GOOGL', 'META', 'MSFT', 'NVDA', 'TSLA', 'SPY']

# Descargar los datos históricos de los tickers
data = yf.download(ticker, start='2014-01-01', end='2024-06-30',auto_adjust=True,
                   group_by='column')

#formato horizantal solo cierres
close_wide = data["Close"].copy()
close_wide.to_csv("datos/close_wide.csv")

# Formato horizontal: OHLCV completo con columnas planas
datos_anchos_planos = data.copy()
nombres_nuevos = []
for precio, ticker in datos_anchos_planos.columns:
    nombre = precio + "_" + ticker
    nombres_nuevos.append(nombre)
datos_anchos_planos.columns = nombres_nuevos
datos_anchos_planos.to_csv("datos/precios_ohlcv_wide.csv")

# 4. Formato vertical: OHLCV completo
data_long = (
    data
    .stack(level=1)
    .rename_axis(["Date", "Ticker"])
    .reset_index()
)
data_long.to_csv("datos/precios_ohlcv_long.csv", index=False)