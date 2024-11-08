
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

def scrape_text(url):
    # Initialize Chrome WebDriver using webdriver-manager
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    try:
        # Open the URL
        driver.get(url)

        # Wait for the page to fully load
        time.sleep(10)

        # Extract text content from the body of the webpage
        text = driver.find_element(By.TAG_NAME, "body").text

    finally:
        # Close the browser
        driver.quit()

    return text

if __name__ == "__main__":
    # URL you want to scrape
    url = "https://careers.zebra.com/careers/job/343623229683?domain=zebra.com"

    # Scrape the webpage and extract text
    text = scrape_text(url)

    # Save the extracted text to a file
    with open("extracted_text.txt", "w", encoding="utf-8") as file:
        file.write(text)

    print("Text has been saved to extracted_text.txt")