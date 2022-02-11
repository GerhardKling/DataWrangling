"""
PDF extraction
The re module: regular expression syntax
Useful for string matching

Refactoring
"""

import PyPDF2
import re

def word_page_count(file_name: str, search: str):
	"""
	file_name: name of pdf file
	search: search term
	returns: tuple (total, count)
	total: all occurrences
	count: number of pages with at least one occurence
	"""
	#Assign the pdf file
	doc = PyPDF2.PdfFileReader(file_name)

	#Number of pages
	pages = doc.getNumPages()

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

	#Total word count
	total = sum([tup[0] for tup in list_pages])

	return (total, count)

#Arguments
file_name = "MS_2019.pdf"
search = "independent"

#Call function
result = word_page_count(file_name, search)

#Print output
print(f"The word '{search}' was found {result[0]} times on {result[1]} pages.")

#Call function
search = "director"
result = word_page_count(file_name, search)

#Print output
print(f"The word '{search}' was found {result[0]} times on {result[1]} pages.")