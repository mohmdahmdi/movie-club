from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
import time

# Initialize the WebDriver
driver_path = 'E:/codes/projects/movie-club/tools/webDriver/msedgedriver.exe'
service = Service(driver_path)
driver = webdriver.Edge(service=service)

# Function to scrape comments from a movie page
def scrape_comments():
    while True:
        try:
            # Wait for the "Load More" button to be clickable
            load_more_button = driver.find_element(By.ID, 'ajaxLoadMoreComments')
            load_more_button.click()
            time.sleep(2)  # Wait for new comments to load
        except (NoSuchElementException):
            # If the button is not found or another error occurs, break the loop
            print("No more comments to load.")
            break

    # Parse the loaded comments
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    comments = soup.find_all('div', class_='comment_text_cm')

    # Extract and return comments
    return [comment.text.strip() for comment in comments]

# Main loop to iterate through pages
for i in range(500, 600):  # Adjust the range as needed
    url = f"https://digimoviez.com/page/{i}"
    driver.get(url)
    time.sleep(5)  # Wait for the page to load

    # Find all movie buttons on the current page
    open_movie_buttons = driver.find_elements(By.CSS_SELECTOR, "div.read_more > a")
    
    for button in open_movie_buttons:
        try:
            # Open the movie page in a new tab
            button.click()
            driver.execute_script(f"window.open('{button.get_attribute("href")}', '_blank');")
            time.sleep(2)  # Wait for the new tab to open

            # Check if a new tab has been opened
            if len(driver.window_handles) < 2:
                print("No new tab opened. Skipping this movie.")
                continue  # Skip to the next movie

            # Switch to the new tab
            driver.switch_to.window(driver.window_handles[1])

            # Scrape comments from the movie page
            comments = scrape_comments()
            time.sleep(3)
            for idx, comment in enumerate(comments, 1):
                print(f"Comment {idx}: {comment}")

            # Close the movie tab and switch back to the main page
            driver.close()
            driver.switch_to.window(driver.window_handles[0])
        except StaleElementReferenceException:
            # Re-locate the button and try again
            open_movie_buttons = driver.find_elements(By.CSS_SELECTOR, "div.read_more > a")
        except Exception as e:
            print(f"Error processing movie: {e}")

# Close the WebDriver
driver.quit()