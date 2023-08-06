from distutils.core import setup

setup(name='dropcols',
	version='2.0.1',
	author='Dreas Nielsen',
	author_email='dreas.nielsen@gmail.com',
	scripts=['dropcols/dropcols.py'],
	classifiers=[
		'Development Status :: 5 - Production/Stable',
		'Environment :: Console',
		'Intended Audience :: End Users/Desktop',
		'License :: OSI Approved :: GNU General Public License (GPL)',
		'Natural Language :: English',
		'Operating System :: OS Independent',
		'Topic :: Text Processing :: General',
		'Topic :: Office/Business'
		],
	description="""Filters a CSV file, extraction or dropping columns selected by name or position.
       | Removes (or conversely, extracts) 
selected columns from a delimited text file, such as a CSV file. It is analogous 
to the "cut" program, except that it works on CSV files and allows columns 
to be selected by name (regular expressions) in addition to by number. Either the 
columns to keep, or the columns to remove, or both, can be specified.
"""
	)
