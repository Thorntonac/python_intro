import requests
import shutil

# The URL to be requested, change this and see how the below examples change.
URL = 'https://en.wikipedia.org/wiki/Monkey'

# The below will send an HTTPS GET request to the URL
webpage_data = requests.get(URL)

# From the single text string received from the webpage, create individual strings from each line. \n is the newline character
lines = webpage_data.text.split('\n')

# The below line is where I got some of the information I used to find which lines to look for. The key here was the class="image-section"
# <td colspan="2" class="image-section"><span class="mw-default-size" typeof="mw:File/Frameless"><a href="/wiki/File:Bonnet_macaque_(Macaca_radiata)_Photograph_By_Shantanu_Kuveskar.jpg" class="mw-file-description"><img alt="Bonnet macaque Macaca radiata Mangaon, Maharashtra, India" src="//upload.wikimedia.org/wikipedia/commons/thumb/4/43/Bonnet_macaque_%28Macaca_radiata%29_Photograph_By_Shantanu_Kuveskar.jpg/220px-Bonnet_macaque_%28Macaca_radiata%29_Photograph_By_Shantanu_Kuveskar.jpg" decoding="async" width="220" height="373" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/4/43/Bonnet_macaque_%28Macaca_radiata%29_Photograph_By_Shantanu_Kuveskar.jpg/330px-Bonnet_macaque_%28Macaca_radiata%29_Photograph_By_Shantanu_Kuveskar.jpg 1.5x, //upload.wikimedia.org/wikipedia/commons/4/43/Bonnet_macaque_%28Macaca_radiata%29_Photograph_By_Shantanu_Kuveskar.jpg 2x" data-file-width="354" data-file-height="600" /></a></span>

for line in lines:

	if 'class="image-section"' in line and 'src=' in line:
		'''
		The below line is very complex, I did this to show some of the capabilities of python
		for each line of HTML it is splitting into multiple strings wherever there is a space character
		then if a section of the line starts with src= it will remove the beginning of the line to leave
		behind only the URL of the image, I can explain this much better in person'''
		image_URL = 'https://'+[src for src in line.split(' ') if src.startswith('src=')][0].strip('src="//')

		image_name = image_URL.split('/')[-1]

		# uncomment the below to show the URL and image name pulled from the data
		# print(image_URL)
		# print(image_name)

		image_file = requests.get(image_URL, stream=True)
		with open(image_name, 'wb') as downloaded_image:
			shutil.copyfileobj(image_file.raw, downloaded_image)