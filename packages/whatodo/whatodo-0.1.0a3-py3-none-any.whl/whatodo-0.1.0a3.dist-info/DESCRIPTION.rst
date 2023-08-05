Whatodo
=======

![Build Status](https://travis-ci.org/masterkoppa/whatodo.svg)

# Description
In software development and any other area of coding it is a common occerance to use comments 
for TODO and FIXME for two examples. It can be difficult with large files and/or large numbers 
of files to locate these comments.

whatodo is created to make locating theses comments easier. This app can read through any 
number of files and locate these comments returning the line number of the contents of the actual comment.

The application is written in pure Python with the help of the pygments library. With this 
library we are able to parse through more than 100+ languages, for a more detailed description 
see [pygments docs](http://pygments.org/languages/)

# Usage
The most common use case would be scanning a whole source directory for tags, to achieve 
this you can do the following:  
```whatodo src/```

For more info and additional options see ```whatodo -h```

## Options
	- json
	- keyword
	- files

### JSON
Changes the output format to json, useful for automating with other tools.


### Keyword
The Keywords are the words searched for in the beginning of a comment to determine if this is a comment to extract.

Defaults to TODO, todo, FIXME


### Files
The Files are the files searched through to locate comments with the above mentioned Keywords.

A list of files or directories to analyze and look for TODO's. At least 1 file must be provided. 

# Installing

To install simply do:  
```
pip install whatodo
```

# License
MIT License for more details see /LICENSE



