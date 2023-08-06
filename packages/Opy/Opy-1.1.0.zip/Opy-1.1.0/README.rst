	.. figure:: http://www.qquick.org/opy.jpg
		:alt: Image of Phaistos Disc
		
		**The famous Phaistos Disc from Crete, obfuscation unbroken after thousands of years.**

Opy will obfuscate your extensive, real world, multi module Python source code for free!
And YOU choose per project what to obfuscate and what not, by editting the config file:

- You can recursively exclude all identifiers from certain modules from obfuscation.
- You can exclude human readable configuration files containing Python code.
- You can use getattr, setattr, exec and eval by excluding the identifiers they use.
- You can even obfuscate module file names.
- You can run your obfuscated code from any platform.

Installation:

- Download and unzip Opy into an arbitrary directory of your computer.
- You only need the files opy.py and py_config.txt. They are in the opy subdirectory of your unzipped Opy version.
- Put opy.py or a script to launch it in the path of your OS, or simply copy opy.py to the topdirectory of your project.

Use:

- For safety, backup your sourcecode and valuable data to an off-line medium.
- Put a copy of opy_config.txt in the top directory of your project.
- Adapt it to your needs according to the remarks in opy_config.txt.
- This file only contains plain Python and is exec'ed, so you can do anything clever in it.
- Open a command window, go to the top directory of your project and run opy.py from there.
- If the topdirectory of your project is e.g. ../work/project1 then the obfuscation result wil be in ../work/project1_opy.
- Further adapt opy_config.txt until you're satisfied with the result.
- Type 'opy ?' or 'python opy.py ?' (without the quotes) on the command line to display a help text and the licence.

Important remark:

- Obfuscate your Python code only when stricktly needed. Freedom is one of the main benefits of the Python community. In line with this the source of Opy is not obfuscated.

Example of obfuscated code: ::

	import threading as x_opy991_x
	import Tkinter as x_opy231_x
	import os

	from x_opy912_x import *
	from x_opy843_x import *

	class x_opy884_x (x_opy319_x, x_opy271_x):
		def __init__ (self):
			x_opy319_x.__init__ (self)
			x_opy271_x.__init__ (self)
							
			self.x_opy907_x = False	
			self.x_opy317_x = False	
			self.x_opy360_x ()

			self.x_opy889_x = x_opy231_x.Frame (self.x_opy981_x)
			self.x_opy973_x = x_opy231_x.Frame (self.x_opy981_x)
			self.x_opy971_x = x_opy231_x.Frame (self.x_opy981_x)

Known limitations:

- A comment after a string literal should be preceded by whitespace.
- A ' or " inside a string literal should be escaped with \\ rather then doubled.
- A # in a string literal can only be used at the start, so use 'p''#''r' rather than 'p#r'.
			
That's it, enjoy!

Jacques de Hooge

jacques.de.hooge@qquick.org

