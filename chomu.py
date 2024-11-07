from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def interact_with_chatbot(url, username, password, message):
    # Initialize Chrome WebDriver using webdriver-manager
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    try:
        # Open the URL
        driver.get(url)

        # Wait for the login page to fully load
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "login_field"))
        )

        # Locate the username/email and password fields and login button
        username_field = driver.find_element(By.ID, "login_field")
        password_field = driver.find_element(By.ID, "password")
        login_button = driver.find_element(By.NAME, "commit")

        # Enter login credentials
        username_field.send_keys(username)
        password_field.send_keys(password)

        # Click the login button
        login_button.click()

        # Wait for the page to load and the warning to appear
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".chat_chat-input-panel-inner___IQHi"))
        )

        # Send the ESC key to close the warning/modal if necessary
        driver.find_element(By.TAG_NAME, "body").send_keys(Keys.ESCAPE)

        # Wait for the chatbot input field to be present
        input_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "textarea.chat_chat-input__PQ_oF"))
        )

        # Clear the input field if necessary and send a message to the chatbot
        input_field.clear()
        input_field.send_keys(message)

        # Locate and click the Send button
        send_button = driver.find_element(By.CSS_SELECTOR, "button.chat_chat-input-send__GFQZo")
        send_button.click()

        # Wait for the chatbot to respond (adjust the sleep time as needed)
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".chatbot-response-class"))
        )

        # Locate and print the chatbot response
        response = driver.find_element(By.CSS_SELECTOR, ".chatbot-response-class")
        print("Chatbot response:", response.text)

    except Exception as e:
        print(f"An error occurred: {e}")
        driver.save_screenshot('error_screenshot.png')

    finally:
        # Close the browser
        driver.quit()

if __name__ == "__main__":
    # URL of the login page
    url = "https://d2qe5ja83hvocu.cloudfront.net/#/login"  # Adjust if needed

    # Login credentials
    username = "Alpha@killai.engineer"
    password = "Ninja#99999"

    # Message to send to the chatbot
    message = "Hello, how can I help you?"

    # Interact with the chatbot
    interact_with_chatbot(url, username, password, message)
