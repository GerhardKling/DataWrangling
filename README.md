# Data Wrangling with Python
This repository provides all codes, data, and notes covered in my YouTube playlist on Data Wrangling with Python. I added links to YouTube videos. You find all videos on our Channel [YUNIKARN](https://www.youtube.com/channel/UCb0qAKEAwNC0FNatapc-yZg)

## Extracting data from pdf files using Python
This is a detailed step-by-step guide that develops a Python code to extract information from pdf files. This is very useful if you have to handle a large number of files. The Python code returns the number of all search term occurrences in the document and identifies the page numbers. I introduce the PyPDF2 package, which we need to install. 
### [YouTube video 1](https://youtu.be/y_ORF4FpZYo)

*Installation on Anaconda:*
conda install -c conda-forge pypdf2

*Installation using the pip installer:*
pip install PyPDF2

I show you how to create and activate a virtual environment (which is optional – but useful to do). Then we develop the code step-by-step. This will enable you to learn how to modify the code to suit your specific requirements. Please leave a comment if you have any questions.

Finally, we will refactor the code. We define a function that takes a search term and filename and returns a tuple containing the total number of occurrences and the number of pages that contain the search term at least once.

**Chapters**
- 0:00 Welcome
- 0:15 Return all occurrences & page numbers
- 0:44 Example pdf
- 2:23 Python setup
- 3:55 Virtual environment
- 6:16 Coding fun
- 28:05 Refactoring

## Download Data from the Web in Python
This tutorial covers the Python HTTP library, Requests, which can be used to obtain data from the web. We write a Python code that downloads climate data from http://berkeleyearth.org/. The same principle can be used to download files from other urls. I show you how to download the data into a text file. Then we use NumPy to load the text file into a NumPy array. Finally, we convert the data into a Pandas DataFrame. If this sounds like crazy data fun for you, please join us!
### [YouTube video 2 01/04/2022 at 10am GMT](https://youtu.be/vzdsbVz7MsA)

I show you how to create and activate a virtual environment (which is optional – but useful to do). We use the pip installer. 

If you do not have the pip installer, download get-pip.py. The download needs to be in same path as your Python installation - then change the directory into the folder. Using the command line, type: python get-pip.py, and finally check the installation: pip -V.

To install virtual environments, use: pip install virtualenv

We develop the code step-by-step. This will enable you to learn how to modify the code to suit your specific requirements. Please leave a comment if you have any questions. Python is the way!

**Chapters**
- 0:00 Data from the Web
- 0:36 Virtual Environment
- 2:26 Using Requests
- 4:02 Save Data to File
- 5:03 DataFrame 
