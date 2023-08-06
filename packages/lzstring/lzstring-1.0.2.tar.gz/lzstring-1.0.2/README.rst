lz-string-python
================

lz-string for python 2/3

Based on the LZ-String javascript found here: http://pieroxy.net/blog/pages/lz-string/index.html

Example
-------
::

  >>> import lzstring
  >>> x = lzstring.LZString()
  >>> compressed = x.compressToBase64(u"你好") # u'gbyl9NIA'
  >>> x.decompressFromBase64(compressed) # u'\u4f60\u597d'

Installation
------------
::

  $ pip install lzstring
