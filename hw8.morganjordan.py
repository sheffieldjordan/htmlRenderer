#!/usr/bin/env python


###############################################################################
#######################   Element and Its Sub Classes   #######################
###############################################################################

class Element(object):
	indent = ""
	# content = []
	tag_name = ""
	def __init__(self, content = None, **kwargs):
		#print("Element created")
		if content == None:
			self.contents = []
		else:
			self.contents = [content] 
		self.kwargs = kwargs

	def append(self, more_content = ""):
		self.more_content = more_content
		self.contents.append(more_content)
		
	def render(self, file_out, ind = ""): # if it contains a string, print it. but if it's another class, call the class's render
		file_out.write(self.indent + "<{}".format(self.tag_name, )) 
		for arg, val in self.kwargs.items(): #for key, value in key-word arguments passed in kwargs
			file_out.write(" {}='{}'".format(arg, val)) #set them equal and write thm 
		file_out.write(">")
		for line in self.contents:
			try:
				line.render(file_out, self.indent)
			except:
				pass
			# file_out.write("\n")
			file_out.write(self.indent)
			try:
				file_out.write(self.indent + line) #converting line to str will cause ObjTypes to be writtent to file
			except:
				pass
		# file_out.write("\n")
		file_out.write(self.indent + "</{}>".format(self.tag_name))
		
		"""file_out is any file-like object--- it could have a write method within in
		ind is a string with the indentation level in it (i.e. the amount that the tag should be intended to be pretty)
		The amount of indentation should be set by the class attribute indent
		"""
class Html(Element):
	tag_name = "html"
	indent = "\n"
	def render(self, file_out, ind=""):
		file_out.write("<!DOCTYPE html>")
		super(self.__class__, self).render(file_out, ind)

class Head(Element):
	tag_name = "head"
	indent = "\n" + "    "

class OneLineTag(Element):
	tag_name = ""
	indent = ""

	def render(self, file_out, ind = ""): #render everything on one line, like for the <title> tag
		file_out.write(self.indent + "<{}>".format(self.tag_name))

		for line in self.contents:
			try:
				line.render(file_out)
			except:
				pass

			try:
				file_out.write(line) #converting line to str will cause ObjTypes to be writtent to file
			except:
				pass
		# file_out.write("\n")
		file_out.write("</{}>".format(self.tag_name))

class Title(OneLineTag):
	tag_name = "title"
	indent = "    "

class Body(Element):
	tag_name = "body"
	indent = "\n" + "    "

class P(Element):
	tag_name = "p"
	indent = "\n" + "        "


class SelfClosingTag(Element):
	def __init__(self, **kwargs):
		self.kwargs = kwargs
	def render(self, file_out, ind = ""): # if it contains a string, print it. but oif it's anothe rclass, call the classes render

		file_out.write(self.ind + "<{} ".format(self.tag_name))
		for arg, val in self.kwargs.items():
			file_out.write('{}="{}"'.format(arg, val) + "/>")

class Hr(Element):
	tag_name = "hr"
	indent = "\n" + "        "
	def render(self, file_out, ind = ""):
		file_out.write(self.indent + "<{}/>".format(self.tag_name))

class Br(SelfClosingTag):
	tag_name = "br"
	indent = "        "

class A(OneLineTag):
	tag_name = "a"
	indent = "\n" + "                "
	def __init__(self, content, link, **kwargs):
		kwargs["href"] = "link"
		super(self.__class__, self).__init__(content, **kwargs)

class Ul(Element):
	tag_name = "ul"
	indent = "\n" + "        "

class Li(Element):
	tag_name = "li"
	indent = "\n" + "            "

class H(OneLineTag):
	indent = "\n" + "        "
	def __init__(self, number, content, **kwargs):
		OneLineTag.__init__(self, content, **kwargs)
		self.tag_name = "h" + str(number)

class Meta(SelfClosingTag):
	tag_name = "meta"
	ind = "\n" + "        "


		
