import dominate
from dominate.tags import *

def num_lines():
	return sum(1 for line in open('README.md'))

def output_HTML():
	doc = dominate.document()
	with doc:
		p('Number of lines in README is ' + str(num_lines()))
	return doc

html_doc = output_HTML()

with open('lineCount.html', 'w') as f:
    f.write(html_doc.render())
    print('Outputted HTML to file')
