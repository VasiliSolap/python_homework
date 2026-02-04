from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import csv
import pandas as pd
from time import sleep

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://owasp.org/Top10/2025/")
sleep(5)

vulnerabilities = driver.find_elements(By.XPATH, '//main//a[contains(@href, "/Top10/2025/A")]')

results = []

for v in vulnerabilities:
    name = v.text.strip()
    url = v.get_attribute("href")
    if name and url:
        results.append({"Vulnerability": name, "Link": url})

driver.quit()

for r in results:
    print(r)

df = pd.DataFrame(results)
print(df)

df.to_csv("owasp_top_10.csv", index=False)