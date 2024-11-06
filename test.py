from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

# Initialize Chrome WebDriver using webdriver-manager
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# URL you want to scrape
url = "https://careers.bakerhughes.com/global/en/job/BAHUGLOBALR128493/Early-Career-LEAD-Field-Engineer-India-2025-Opportunities?utm_source=linkedin&utm_medium=phenom-feeds"

# Open the URL
driver.get(url)

# Wait for the page to fully load
time.sleep(10)

# Extract text content
text = driver.find_element(By.TAG_NAME, "body").text

# Save the text content to a .txt file
with open("extracted_text.txt", "w", encoding="utf-8") as file:
    file.write(text)

# Close the browser
driver.quit()