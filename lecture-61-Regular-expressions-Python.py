#         Regular expressions (regex or regexp) 
#                     in Python
                    
# Regular expressions (regex or regexp) are sequences of characters that define a search pattern. They are used for pattern matching within strings. 


import re


text = """From Wikipedia, the free encyclopedia

Old Python logo, 1990s–2006

New Python logo, 2006–present

Guido van Rossum in 2014
Main article: Python (programming language)
The programming language Python was conceived in the late 1980s,[1] and its implementation was started in December 1989[2] by Guido van Rossum at CWI in the Netherlands as a successor to ABC capable of exception handling and interfacing with the Amoeba operating system.[3] Van Rossum is Python's principal author, and his continuing central role in deciding the direction of Python is reflected in the title given to him by the Python community, Benevolent Dictator for Life (BDFL).[4][5] (However, Van Rossum stepped down as leader on July 12, 2018.[6]). Python was named after the BBC TV show Monty Python's Flying Circus.[7]

Python 2.0 was released on October 16, 2000, with many major new features, including a cycle-detecting garbage collector (in addition to reference counting) for memory management and support for Unicode. However, the most important change was to the development process itself, with a shift to a more transparent and community-backed process.[8]

Python 3.0, a major, backwards-incompatible release, was released on December 3, 2008[9] after a long period of testing. Many of its major features have also been backported to the backwards-compatible, though now-unsupported, Python 2.6 and 2.7.[10]

Early history
In February 1991, Van Rossum published the code (labeled version 0.9.0) to alt.sources.[11][12] Already present at this stage in development were classes with inheritance, exception handling, functions, and the core datatypes of list, dict, str and so on. Also in this initial release was a module system borrowed from Modula-3; Van Rossum describes the module as "one of Python's major programming units".[1] Python's exception model also resembles Modula-3's, with the addition of an else clause.[3] In 1994 comp.lang.python, the primary discussion forum for Python, was formed, marking a milestone in the growth of Python's userbase.[1]"""


ptrn = "\d\d\d\d"


# matches = re.search(ptrn, text)

# matches = re.finditer(ptrn, text)


# print(matches)

# for i in matches:
#     print(i)


matches = re.findall(ptrn, text)

print(matches)


