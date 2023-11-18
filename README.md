# Data Wrangling with Python
This repository provides all codes, data, and notes covered in my YouTube playlist on Data Wrangling with Python. I added links to YouTube videos. You find all videos on our Channel [YUNIKARN](https://www.youtube.com/channel/UCb0qAKEAwNC0FNatapc-yZg)

## V1: Extracting data from pdf files using Python
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

## V2: Download Data from the Web in Python
This tutorial covers the Python HTTP library, Requests, which can be used to obtain data from the web. We write a Python code that downloads climate data from http://berkeleyearth.org/. The same principle can be used to download files from other urls. I show you how to download the data into a text file. Then we use NumPy to load the text file into a NumPy array. Finally, we convert the data into a Pandas DataFrame. If this sounds like crazy data fun for you, please join us!
### [YouTube video 2](https://youtu.be/vzdsbVz7MsA)

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

## V3: Download Financial Data from Yahoo Finance using Python
This tutorial covers the Python package yfinance, which enables us to connect to Yahoo Finance (API). We download data for the Bitcoin-USD trade and work with the Pandas DataFrame. Finally, we visualise the data using Matplotlib.
### [YouTube video 3](https://youtu.be/iGWg2gs7Nv4)

## V4: Common Words in PDF files: Let Python do the Reading
This is a detailed step-by-step guide that develops a Python code to read PDF files and determine the most common words. This is very useful if you want to get an idea about the content of PDF files without reading them yourself. Applications include systematic literature reviews or selecting newspaper articles. 

All material is on [GitHub](https://github.com/GerhardKling/DataWrangling/tree/main/CommonWords).

I show you how to create and activate a virtual environment (which is optional – but useful). Then we develop the code step-by-step. This will enable you to learn how to modify the code to suit your specific requirements. Please leave a comment if you have any questions.
### [YouTube video 4](https://youtu.be/3s0-TGLbB4M)

**Chapters**
- 0:00 Common Words in PDF Files
- 0:48 Virtual Environment
- 1:56 Main.py & Module
- 2:44 The word_rank Function
- 8:07 Counter Class

## V5: Is Gold an Inflation Hedge? A Data Analysis
This is a detailed step-by-step data analysis to explore whether investing in gold protects against inflation. The result might surprise you! We will explore free data sources (https://backtest.curvo.eu/market-index/gold-bullion) for gold spot prices and World Bank data. I will demonstrate how to import data into Stata and how to merge datasets. Finally, we explore the performance of our gold investment by controlling for inflation.

### [YouTube video 5](https://youtu.be/bXJPH8gXOg4)

## V6: Data from Reddit using Python: Errors with PSAW - try PMAW
I have been working on a project that uses Reddit posts to enhance stock market predictions. The Python script uses an API to collect posts from WallStreetBets. My code worked fine for years, but errors occurred recently when using the PSAW package. You might get the error message: Got non 200 code 404 unable to connect to pushshift.io - I could not find a good solution using PSAW. This video discusses an alternative approach using PMAW, which extracts data from WallStreetBets without any issues.

### [YouTube video 6](https://youtu.be/3pDZF4fWLBM)

## V7: World Inequality Database: Free Data
In this video, I want to show you the World Inequality Database or WID, in short. The WID provides access to free data focused on income and wealth inequality. It covers a wide range of countries, and time series data start in 1820, assuming the data is available. It is quite easy to select the time series, countries, and years for your data analysis. The tables can be rearranged, and you can select various data formats for download. For instance, CSV or Excel files can be imported into Pandas (Python) or Stata.

### [YouTube video 7](https://youtu.be/-2k1zD9nyfY)
