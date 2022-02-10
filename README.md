# Data Wrangling with Python
This repository provides all codes, data, and notes covered in my YouTube playlist on Data Wrangling with Python. I added links to YouTube videos. You find all videos on our Channel [YUNIKARN](https://www.youtube.com/channel/UCb0qAKEAwNC0FNatapc-yZg)

## Extracting data from pdf files using Python
This is a detailed step-by-step guide that develops a Python code to extract information from pdf files. This is very useful if you have to handle a large number of files. The Python code returns the number of all search term occurrences in the document and identifies the page numbers. I introduce the PyPDF2 package, which we need to install. [YouTube video - 11/02/2022 10am GMT](https://youtu.be/y_ORF4FpZYo)

*Installation on Anaconda:*
conda install -c conda-forge pypdf2

*Installation using the pip installer:*
pip install PyPDF2

I show you how to create and activate a virtual environment (which is optional – but useful to do). Then we develop the code step-by-step. This will enable you to learn how to modify the code to suit your specific requirements. Please leave a comment if you have any questions.

Finally, we will refactor the code. We define a function that takes a search term and filename and returns a tuple containing the total number of occurrences and the number of pages that contain the search term at least once.

*Chapters*
- 0:00 Welcome
- 0:15 Return all occurrences & page numbers
- 0:44 Example pdf
- 2:23 Python setup
- 3:55 Virtual environment
- 6:16 Coding fun
- 28:05 Refactoring

