# Python Introduction

------

For your use case the first module you should learn is `requests`. This introduction will focus on the steps required to get you up and running with this module.

Python has a built in package manager, where C languages require you to manually download libraries and point your compiler to the right file, python installations come with `pip`  to install modules (A python module is equal to a library in any other language). This command has a lot of options however all you need to know is `pip install {module name}` and of course `pip uninstall {module name}`. Python also allows you to create virtual environments to keep the modules you need in one project separate from other projects. While this is not necessary for starting out it is a good and simple skill to have. Below is an example to explain both of these concepts.

#### Creating a Python Virtual Environment

*NOTE: There are extra steps required to associate this environment with your IDE however it varies and is sometimes finnicky so we can figure this step out together when needed.*

This process will create a Python virtual environment (venv). This is essentially a dedicated instance of a python installation which is isolated from your main installation and other virtual environments, allowing for a fresh template without conflicts occurring between multiple un-needed modules.

After installing Python go to your command line, I prefer PowerShell, either this or CMD will work fine. go to the directory you wish to store your environment in.

`$ cd Documents\python_environments`

Once in the directory run the below command

`$ python -m venv {environment_name}`  - This command tells python to run the venv module which you then supply with the name of the environment to create.

This will simply make a folder with the given environment name which contains a fresh instance of whichever python version you have installed. 

Once created you can *activate* the virtual environment by doing the following

##### PowerShell / CMD

While inside your python_environments directory (Ex. from above Documents\python_environments)

`$ .\{environment_name}\Scripts\activate`

##### Linux

`$ source /{environment_name}/bin/activate`

You should see the name of your environment populate in front of the current path on your command line prompt.

Now you are ready to start installing modules.

#### Installing a module in python

Installing a module in python is very straightforward. Find the module you want, go to your command line, and run the below command.

`$ pip install {module_name}`

So to install the requests module mentioned at the beginning of this introduction you would run the below

`# pip install requests` 

#### Using an Installed Module in your Code

The below is an example of how to import a module into your code and check its version (Note: not all modules follow this however it is standard)

```python
import requests
requests.__version__
```

When this is run you should get something similar to the below output. All this does is output the `__version__` attribute of the module.

```
'2.31.0'
```

#### Getting started with requests

The below will show how to use requests to pull down a webpage and retrieve a specific piece of information.

This example will use the Wikipedia page on Monkey. (https://en.wikipedia.org/wiki/Monkey) 

![](C:\Users\thorn\Documents\git-reps\python_intro\media\Wikipedia_page.png)

In this example the goal will be to find and download the picture of a monkey.

This example also requires the shutil module to write the image file. This module is a builtin and does not require installation.

```python
import requests
import shutil

# The URL to be requested, change this and see how the below examples change.
URL = 'https://en.wikipedia.org/wiki/Monkey'

# The below will send an HTTPS GET request to the URL
webpage_data = requests.get(URL)

# From the single text string received from the webpage, create individual strings from each line. \n is the newline character
lines = webpage_data.text.split('\n')

for line in lines:

	if 'class="image-section"' in line and 'src=' in line:

		# The below line is very complex, I did this to show some of the capabilities of python, I will explain better in person.
		image_URL = 'https://'+[src for src in line.split(' ') if src.startswith('src=')][0].strip('src="//')

		image_name = image_URL.split('/')[-1]

		image_file = requests.get(image_URL, stream=True)
		with open(image_name, 'wb') as downloaded_image:
			shutil.copyfileobj(image_file.raw, downloaded_image)
```

The 2 other files in this repository contain more comments to explain what is happening here. The basic idea here is that you are requesting a webpage from a webserver using the URL, the text received, which normally would be built into a webpage by your browser is then parsed through to find images, there is some extra processing done once a line of HTML containing an image is found to ensure that the URL is readable, then it is downloaded and saved as a file. 



**Disclaimers** 

- `shutil` is new to me and I am not exactly sure what it does.
- in the `image_file` variable I am not sure what `stream=True` does however removing it results in empty files being created, go ahead and try setting it to `False ` then you can edit the downloaded file with notepad to see that it is empty.
- The above example, (the same code is contained in `monkey_example.py`) will only work on that URL and possibly a few others, a less specialized example is also available under `requests_example.py` which works with *at least* the three URLs which are commented at the top of the file.
