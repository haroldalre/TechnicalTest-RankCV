from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize the Chrome driver
driver = webdriver.Chrome()

# Open Google and perform a search for "Cars in London"
driver.get("https://www.google.com")
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Cars in London")
search_box.submit()

# Wait for the search results to load
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.g")))

# Get all search result links
search_results = driver.find_elements(By.CSS_SELECTOR, "div.g a")

# Count the number of Gumtree links
gumtree_links = [link.get_attribute("href") for link in search_results if "gumtree.com" in link.get_attribute("href")]
print(f"Number of Gumtree links found: {len(gumtree_links)}")

# Navigate to each Gumtree link and validate the title and number of results
for link in gumtree_links:
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[-1])
    driver.get(link)

    # Wait for the page to load
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "h1.listing-title")))

    # Get the title and number of results
    title = driver.find_element(By.CSS_SELECTOR, "h1.listing-title").text
    num_results = driver.find_element(By.CSS_SELECTOR, "span.listing-results-count").text

    print(f"Title: {title}")
    print(f"Number of results: {num_results}")

    # Validate that the title is displayed and the number of results is greater than 0
    assert title, "Title is not displayed"
    assert int(num_results.split()[0]) > 0, "Number of results is 0"

    # Close the current window
    driver.close()
    driver.switch_to.window(driver.window_handles[0])

# Close the browser
driver.quit()
