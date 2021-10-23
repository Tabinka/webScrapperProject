import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)
driver.maximize_window()
driver.get('https://steamdb.info/')
x = 1
for _ in range(1, 3):
    y = 1
    for _ in range(1, 3):
        dictionary = {}
        game_names = []
        other_data = []
        column_data = driver.find_element(By.CSS_SELECTOR,
                                       f"div.row:nth-child({x}) > div.span6:nth-child({y}) > table > thead > tr > th:nth-child(3)")
        row_head = driver.find_element(By.CSS_SELECTOR, f"div.row:nth-child({x}) > div.span6:nth-child({y}) > table > thead > tr > th.table-title")
        names = driver.find_elements(By.CSS_SELECTOR, f"div.row:nth-child({x}) > div.span6:nth-child({y}) > table > tbody > tr > td:nth-child(2) > a")
        second_data = driver.find_elements(By.CSS_SELECTOR, f"div.row:nth-child({x}) > div.span6:nth-child({y}) > table > tbody > tr > td:nth-child(4)")
        for name in names:
            game_names.append(name.get_property("innerHTML"))
        for data in second_data:
            other_data.append(data.get_property("innerHTML"))
        row = row_head.get_property("textContent")
        column = column_data.get_property("textContent")
        y += 1
        dictionary = {"name": game_names, column: other_data}
        print(dictionary)
        df = pd.DataFrame(dictionary)
        df.to_csv(f"{row}.csv", index=False)
    x += 1
