# Import necessary libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import pandas as pd

# Specify the URL to scrape
url = "https://www.amazon.in"

# Initialize the Chrome WebDriver
driver = webdriver.Chrome()

# Open the specified URL in the browser
driver.get(url)

# Maximize the browser window for better visibility
driver.maximize_window()

# Find the search textbox by its ID and perform a search
txtbox_search = driver.find_element(By.ID, "twotabsearchtextbox")
txtbox_search.clear()
txtbox_search.send_keys("laptops under 100000")
driver.find_element(By.ID, "nav-search-submit-button").click()

# Filter the search results to show only Dell laptops
driver.find_element(By.XPATH, "//span[text()='Dell']").click()

# Find all the laptop elements in the search results
laptops = driver.find_elements(By.XPATH, '//div[@data-component-type="s-search-result"]')

# Initialize lists to store laptop information
laptop_name = []
laptop_price = []
no_reviews = []

# Loop through each laptop element to extract information
for laptop in laptops:
    # Extract laptop names
    names = laptop.find_elements(By.XPATH, ".//span[@class='a-size-medium a-color-base a-text-normal']")
    for name in names:
        laptop_name.append(name.text)

    try:
        # Extract laptop prices
        if len(laptop.find_elements(By.XPATH, ".//span[@class='a-price-whole']")) > 0:
            prices = laptop.find_elements(By.XPATH, ".//span[@class='a-price-whole']")
            for price in prices:
                laptop_price.append(price.text)
        else:
            laptop_price.append("0")
    except:
        pass

    try:
        # Extract number of reviews
        if len(laptop.find_elements(By.XPATH, ".//span[@class='a-size-base s-underline-text']")) > 0:
            reviews = laptop.find_elements(By.XPATH, ".//span[@class='a-size-base s-underline-text']")
            for review in reviews:
                no_reviews.append(review.text)
        else:
            no_reviews.append("0")
    except:
        pass

# Print the number of laptops, prices, and reviews
print('no of laptops==>', len(laptop_name))
print('no of prices==>', len(laptop_price))
print('no of reviews==>', len(no_reviews))

# Create a Pandas DataFrame with the extracted information
df = pd.DataFrame(zip(laptop_name, laptop_price, no_reviews), columns=['Laptop_Name', 'Laptop_Price', 'No_Reviews'])

# Ensure the 'Outputs' directory exists
output_directory = "./Output"
os.makedirs(output_directory, exist_ok=True)

# Write data to the Excel file in the 'Outputs' directory
df.to_excel(os.path.join(output_directory, "Dell_Laptops.xlsx"), index=False)

# Close the browser
driver.quit()
