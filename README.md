# TechnicalTest-RankCV
Technical test for the Senior QA position proposed by RankCV.

Test#1

This script uses the Selenium WebDriver library to automate the web browser and perform the required actions. Here's a breakdown of the steps:
The script initializes the Chrome driver using webdriver.Chrome().
It opens Google and performs a search for "Cars in London" by interacting with the search box.
After the search results are loaded, it extracts all the search result links and counts the number of Gumtree links.
For each Gumtree link, the script opens a new window, navigates to the link, and waits for the page to load.
It then extracts the title and the number of results from the page.
The script validates that the title is displayed and that the number of results is greater than 0.
After validating each Gumtree link, the script closes the current window and switches back to the main window.
Finally, the script closes the browser using driver.quit().
Note that this script assumes you have the Chrome WebDriver installed and configured correctly. You may need to adjust the code if you're using a different browser or a different version of Selenium WebDriver.

Test#2
