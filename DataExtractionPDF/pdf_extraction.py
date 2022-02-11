"""
PDF extraction
The re module: regular expression syntax
Useful for string matching
"""

import PyPDF2
import re

#Assign the pdf file
file_name = "MS_2019.pdf"
doc = PyPDF2.PdfFileReader(file_name)

#Number of pages
pages = doc.getNumPages()

#Search term
search = "independent"

#List of tuples (all occurrences, page number)
list_pages = []

for i in range(pages):
	current_page = doc.getPage(i)
	text = current_page.extractText()
	if re.findall(search, text):
		#findall returns a list
		count_page = len(re.findall(search, text))
		list_pages.append((count_page, i))

#Number of pages that contain search term at least once
count = len(list_pages)

print(list_pages)

#Total word count
total = sum([tup[0] for tup in list_pages])
print(total)


print(f"The word '{search}' was found {total} times on {count} pages.")