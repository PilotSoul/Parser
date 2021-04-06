import requests
from bs4 import BeautifulSoup

image_number = 0
storage_number = 1
link = f'https://www.zastavki.com/'

for storage in range(2450):
    response = requests.get(f'{link}/rus/{storage_number}/').text
    soup = BeautifulSoup(response, 'lxml')
    block = soup.find('div', id = 'day-list-content-block')
    all_image = block.find_all('div', class_ = 'col-sm-4 text-center image-line')

    for image in all_image:
        image_link = image.find('a').get('href')
        download_storage = requests.get(f'{link}{image_link}').text
        download_soup = BeautifulSoup(download_storage, 'lxml') #requests
        #looking for link
        download_block = download_soup.find('div', class_ = 'flex flex-between').find_all('div', class_ = 'row-fluid')[1]
        result_link = download_block.find('a').get('href')

        #download image
        image_bytes = requests.get(f'{link}{result_link}').content

        with open(f'image/{image_number}.jpg', 'wb') as file:
            file.write(image_bytes)

        image_number+=1

    storage_number += 1