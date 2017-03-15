#!/usr/bin/env python

"""
Python class example.
"""

###############################################################################
#######################   Element and Its Sub Classes   #######################
###############################################################################

class Element(object):
	indent = "    "
	content = ""
	tag_name = ""
	def __init__(self, content = None):
		print("Element created")
	
	def append(self, more_content):
		self.more_content = more_content
		self.content += (more_content + "\n")
		
		


	def render(self, file_out, ind = indent): # if it contains a string, print it. but oif it's anothe rclass, call the classes render
		file_out.write("<>" + "\n" + ind + self.content + "<\>")

		 
		
		"""file_out is any file-like object--- it could have a write method within in
		ind is a string with the indentation level in it (i.e. the amount that the tag should be intended to be pretty)
		The amount of indentation should be set by the class attribute indent
		"""
class Html(Element):
	def __init__(self, content = None):
		print("HTML tag created")



class Body(Element):
	def __init__(self, content = None):
		print("Body tag created!")
	
	def append(self, more_content):
		self.more_content = more_content
		self.content = P.content
	

	def render(self, file_out, ind = "        "):
		file_out.write("<body>" + "\n" + ind + self.content + "<'\body>")



class P(Element):
	def __init__(self, content = None):
		print("paragraph tag created!")

	def render(self, file_out, ind = "            "):
		file_out.write("<p>" + "\n" + ind + self.content + "<\p>")
