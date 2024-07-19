# © Copyright 2024 egoistpizza
#
# This file is part of BIST Tracker.
#
# BIST Tracker is free software: you can redistribute it and/or modify it under the terms of the GNU General
# Public License as published by the Free Software Foundation, either version 3 of the License, or (at your
# option) any later version.
#
# BIST Tracker is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even
# the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with EgoistBot. If not, see
# <https://www.gnu.org/licenses/>.

import requests
from bs4 import BeautifulSoup
import csv
import time

url = 'https://www.getmidas.com/canli-borsa/xu100-bist-100-hisseleri'

csv_file = 'BIST.csv'

while True:
    html = requests.get(url)
    soup = BeautifulSoup(html.content, 'html.parser')

    symbols = soup.find_all("a", class_="title stock-code")
    symbolsText = [s.text.strip() for s in symbols]

    dailyChanges = soup.find_all("td", class_="val dailyChangePercent")
    dailyChangesText = [c.text.strip() for c in dailyChanges]

    prices = []
    rows = soup.find_all("tr")

    for row in rows:
        cells = row.find_all("td", class_="val")
        if len(cells) > 1:
            price = cells[1].text.strip()
            prices.append(price)

    with open(csv_file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['SYMBOL', 'DAILY CHANGE', 'PRICE'])

        for i in range(len(symbolsText)):
            symbol = symbolsText[i]
            change = dailyChangesText[i]
            price = prices[i]
            writer.writerow([symbol, change, price])

    print(f"All stock data updated. {time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())}")
    time.sleep(300)
