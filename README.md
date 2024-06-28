# URL Extractor

This script extracts URLs containing the path "arcgis/rest/services" from Google search results and stores them in a CSV file.

## Setup Instructions

1. Clone this repository.
2. Install the required dependencies:
    ```sh
    pip install requests beautifulsoup4 pandas
    ```
3. Run the script:
    ```sh
    python url.py
    ```
4. The extracted URLs will be saved in a file named `extracted_urls.csv`.

## Notes

- Ensure you have a stable internet connection.
- The script includes a delay (`time.sleep(2)`) to avoid being blocked by Google.
- Scraping Google search results is against Google's Terms of Service. Consider using the Google Search API for production use.
