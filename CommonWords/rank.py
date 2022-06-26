"""
Rank words
"""
import PyPDF2
import re
from collections import Counter
from gensim.parsing.preprocessing import remove_stopwords

def word_rank(file_name: str, top_num: int = 10):
	"""
	file_name: name of pdf file
	"""
	#Assign the pdf file
	doc = PyPDF2.PdfFileReader(file_name)

	#Number of pages
	pages = doc.getNumPages()

	#Combine list of words
	all_words = []

	for i in range(pages):
		current_page = doc.getPage(i)
		text = current_page.extractText()
		# print(type(text))
		# print(text)
		#All in lower case
		text = text.lower()
		#Remove stopwords
		text_filter = remove_stopwords(text)
		#Split string into list
		text_list = text_filter.split()
		# print(text_list)
		all_words.extend(text_list)
  	
  	#Remove symbols
	all_words_alnum = [word for word in all_words if word.isalnum()]
	ignore_list = ['The', 'year', 'financial', 'FINANCIAL', 'Marks', 'Spencer']
	all_words_filtered = [word for word in all_words_alnum if word not in ignore_list]

	#Use Counter class and the most_common method
	top_words = Counter(all_words_filtered).most_common(top_num)
	  
	return top_words
