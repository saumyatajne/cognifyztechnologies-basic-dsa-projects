import requests
from bs4 import BeautifulSoup

def fetch_data(url):
    try:
        # Send a GET request to the URL
        response = requests.get(url)
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the HTML content of the webpage
            soup = BeautifulSoup(response.text, 'html.parser')
            return soup
        else:
            print("Failed to fetch data. Status code:", response.status_code)
            return None
    except requests.exceptions.RequestException as e:
        print("Error:", e)
        return None

def present_data(soup):
    if soup:
        # Display title
        title = soup.title.string
        print("Title:", title)
        
        # Display headers (if any)
        headers = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
        for header in headers:
            print("Header:", header.text.strip())
        
        # Display main content
        main_content = soup.find('main')  # Assuming main tag contains main content
        if main_content:
            print("Main Content:", main_content.text.strip())
        
        # Display links
        links = soup.find_all('a', href=True)
        if links:
            print("Links:")
            for link in links:
                print(link['href'])
    else:
        print("No data to present.")



# Test the program with different websites
if __name__ == "__main__":
    # Example URL to scrape
    url = "https://webscraper.io/test-sites/e-commerce/allinone"
    # Fetch data from the website
    soup = fetch_data(url)
    # Present the fetched data
    present_data(soup)
