import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

# Download necessary NLTK data files
nltk.download('punkt_tab', force = True)
nltk.download('stopwords', force=True)

def extract_keywords(text):
    # Tokenize the text into words
    words = word_tokenize(text.lower())

    # Define stopwords and punctuation to remove
    stop_words = set(stopwords.words('english'))
    punctuation = {'.', ',', ';', ':', '(', ')', '[', ']', '{', '}', '!', '?', '-', '_', '"', "'s", "'m", "'re", "'ve"}

    # Filter words to remove stopwords and punctuation
    filtered_words = [word for word in words if word not in stop_words and word not in punctuation]

    # Count the frequency of each word
    word_freq = Counter(filtered_words)

    # Get the most common words (you can adjust the number as needed)
    common_words = word_freq.most_common(150)

    return [word for word, freq in common_words]

def format_bullet_points(keywords):
    return "\n".join([f"- {keyword}" for keyword in keywords])

def scrape_and_extract(url):
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

    # Extract keywords and format them as bullet points
    keywords = extract_keywords(text)
    bullet_points = format_bullet_points(keywords)

    return bullet_points

if __name__ == "__main__":
    # URL you want to scrape
    url = "https://careers.bakerhughes.com/global/en/job/BAHUGLOBALR128493/Early-Career-LEAD-Field-Engineer-India-2025-Opportunities?utm_source=linkedin&utm_medium=phenom-feeds"

    # Scrape the webpage and extract keywords
    bullet_points = scrape_and_extract(url)

    # Print the bullet points
    print("Bullet Points:\n")
    print(bullet_points)
