# 引入函式庫（include套件）
import yfinance as yf   # 負責抓股票資料
import pandas as pd     # 負責處理及儲存資料
import time             # 負責間隔時間設定
import os               # 負責檔案操作（確認檔案存在與否）

# 定義要追蹤的股票代號
stock_codes = ['2330.TW', 'AAPL', 'BTC-USD']  # 台積電、蘋果、比特幣

# CSV檔案名稱
csv_filename = 'stock_prices.csv'

# 檢查CSV是否已存在，若無則建立
if not os.path.exists(csv_filename):
    df = pd.DataFrame(columns=['Datetime', 'Stock', 'Price'])
    df.to_csv(csv_filename, index=False)
    print("成功建立新的 CSV 檔案！✨")

# 開始無限循環抓取股價
while True:
    for code in stock_codes:
        try:
            # 抓取最新股價
            stock = yf.Ticker(code)
            current_price = stock.history(period='1mo')['Close'].iloc[-1]

            # 抓取當前時間
            current_time = pd.Timestamp.now()

            # 顯示抓取的資料
            print(f"{current_time} | {code} | 股價：{current_price}")

            # 將資料存入CSV檔案
            new_data = pd.DataFrame({
                'Datetime': [current_time],
                'Stock': [code],
                'Price': [current_price]
            })

            new_data.to_csv(csv_filename, mode='a', header=False, index=False)

        except Exception as e:
            print(f"抓取 {code} 出現錯誤：{e}")

    # 每5分鐘（300秒）更新一次股價
    print("休息5分鐘...")
    time.sleep(300)
