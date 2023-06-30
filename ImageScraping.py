import requests
from bs4 import BeautifulSoup
import os

def scrape_images(url, folder_path):
    # Send a GET request to the URL
    response = requests.get(url)
    # Create BeautifulSoup object
    soup = BeautifulSoup(response.content, 'html.parser')
    # Find all image tags
    images = soup.find_all('img')
    
    # Create the folder if it doesn't exist
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    
    # Download and save the images
    for i, image in enumerate(images):
        image_url = image['src']
        try:
            response = requests.get(image_url)
            image_path = os.path.join(folder_path, f'image_{i}.jpg')
            with open(image_path, 'wb') as f:
                f.write(response.content)
            print(f'Saved image {i+1}/{len(images)}')
        except:
            print(f'Failed to download image {i+1}/{len(images)}')

# Example usage
url1 = 'https://www.amazon.com/s?k=mobile+phones'
url2 = 'https://www.flipkart.com/search?q=mobile+phones'
folder_path = 'C:\Users\princ\Desktop\Hackathon\mobileimage'
  
scrape_images(url1, folder_path)
scrape_images(url2, folder_path)

