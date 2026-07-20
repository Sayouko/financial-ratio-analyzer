# Pobranie danych
# Obliczenie ROE, ROA, marża netto, current ratio, debt-to-equity
# Wyniki w tabeli pandas
# + wykres w matplotlib -> pokazuje trend wskaźnika ROE przez 4 lata

import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf

# Pobranie danych z yfinance

ticker_symbol = 'AAPL'
ticker = yf.Ticker(ticker_symbol)

balance_sheet = ticker.balance_sheet
income_stmt = ticker.income_stmt

net_income = income_stmt.loc['Net Income']
equity = balance_sheet.loc['Stockholders Equity']
assets = balance_sheet.loc['Total Assets']
revenue = income_stmt.loc['Total Revenue']
current_assets = balance_sheet.loc['Current Assets']
current_liabilities = balance_sheet.loc['Current Liabilities']
total_debt = balance_sheet.loc['Total Debt']

# Obliczenie wskaźników

roe = (net_income / equity) * 100
roa = (net_income / assets) * 100
net_margin = (net_income / revenue) * 100
current_ratio = current_assets / current_liabilities
debt_to_equity = total_debt / equity

# Połączenie wyników w jedną tabele

ratios_df = pd.DataFrame({
    'ROE (%)': roe,
    'ROA (%)': roa,
    'Net Margin (%)': net_margin,
    'Current Ratio': current_ratio,
    'Debt-to-equity': debt_to_equity
})

ratios_df = ratios_df.round(2)

print(ratios_df)

# Wykres ROE dla 4 lat wstecz

plt.figure(figsize=(8, 5))
plt.plot(roe.index, roe.to_numpy(), marker='o')
plt.grid()
plt.title(f'ROE {ticker_symbol} (%)')
plt.xticks(rotation=45)
plt.xlabel('Data')
plt.ylabel('ROE (%)')
plt.tight_layout()
plt.savefig("roe_wykres.png")
