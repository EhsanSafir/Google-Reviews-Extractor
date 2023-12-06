# Google Reviews Extractor

This Python repository contains a basic web scraper using Selenium to extract Google reviews from a specified URL. The
scraper exports the extracted data to an Excel file.

## Installation

Install the required dependencies:

```bash
    pip install -r requirements.txt
  ```

# Usage

Below is an example of how to use the Google Review Scraper in your own Python script.

```python
    from extractor import GoogleReviewExtractor

# Specify the Google search URL for the business or location
url = '.....'
# Create an instance of GoogleReviewExtractor
scrapper = GoogleReviewExtractor(url)
# Run the scraper to extract reviews and save to Excel
scrapper.start_scrapping()
```

## Dependencies

- `selenium==4.15.2`
- `openpyxl==3.1.2`

## Configuration

- `review_extractor.py`: Defines the web scraper class (`GoogleReviewExtractor`) and contains the necessary Selenium
  selectors.
- `example1.py`: Example usage of the scraper on a specific Google search URL.
- `requirements.txt`: Lists the required Python packages.

## Notes

- The scraper is designed to extract Google reviews for a given business or location.
- The extracted data is saved in an Excel file named `reviews.xlsx`.
- Make sure to have the appropriate web driver for Selenium installed.
- Extracted Image Uls for each review joined using || seperator e.g :
    - ```text
    https://lh5.googleusercontent.com/p/AF1QipMqsDo9zi3fELhMKkHSi6-ysvOjePH-llH4nruk=w100-h100-p-n-k-no || https://lh5.googleusercontent.com/p/AF1QipOD0hYt6bbEWwFHTAV-tZ62NHDK51HBV_bvlcym=w100-h100-p-n-k-no
    ```