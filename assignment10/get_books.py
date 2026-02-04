from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pandas as pd
import json
from time import sleep

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

url = "https://durhamcounty.bibliocommons.com/v2/search?query=learning%20spanish&searchType=smart"
driver.get(url)
sleep(5)  # даём странице прогрузиться

books = driver.find_elements(By.CSS_SELECTOR, "li.row.cp-search-result-item")

results = []

for book in books:
    try:
        title = book.find_element(By.CSS_SELECTOR, "span.title-content").text
        
        authors = book.find_elements(By.CSS_SELECTOR, "a.author-link")
        author_names = "; ".join([a.text for a in authors])
        
        format_year = book.find_element(By.CSS_SELECTOR, "span.display-info-primary").text

        results.append({
            "Title": title,
            "Author": author_names,
            "Format-Year": format_year
        })
    except:
        continue

driver.quit()

df = pd.DataFrame(results)
print(df)

df.to_csv("get_books.csv", index=False)

with open("get_books.json", "w") as f:
    json.dump(results, f, indent=4)
