# Amazon Web Scraper

## Overview

This is a web scraper implemented in Python using Selenium to extract information about laptops from Amazon.in. It specifically focuses on Dell laptops. The scraped data is stored in a Pandas DataFrame and exported to an Excel file.

## Project Structure

The project consists of the following files:

- `main.py`: The main Python script containing the web scraping code.
- `README.md`: This file providing an overview of the project, instructions, and information.
- `requirements.txt`: Lists the required Python libraries for the project.
- `Output/`: Directory where the scraped data (Excel file) is stored.

## Prerequisites

Make sure you have the following installed:

- [Python](https://www.python.org/) (version 3.7 or higher)
- [Google Chrome](https://www.google.com/chrome/) browser
- [ChromeDriver](https://sites.google.com/chromium.org/driver/) (ensure it's compatible with your Chrome version)

## Setup

1. Clone the repository:

```bash
git clone https://github.com/RonakR68/Amazon-Web-Scraper.git

2. Navigate to the project directory:

```bash
cd Amazon-Web-Scraper

3. Install the required dependencies:

```bash
pip install -r requirements.txt

## How to Run

1. Run the script:

```bash
python3 main.py

2. Check the Output directory for the generated Excel file (Dell_Laptops.xlsx) containing the scraped data.
