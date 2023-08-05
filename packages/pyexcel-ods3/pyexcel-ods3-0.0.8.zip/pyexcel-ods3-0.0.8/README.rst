===================================================================
pyexcel-ods3 - Let you focus on data, instead of ods format
===================================================================


**pyexcel-ods3** is a tiny wrapper library to read, manipulate and write data in ods fromat using python version 2.6(since v0.0.8), 2.7, 3.3 and 3.4. You are likely to use `pyexcel <https://github.com/chfw/pyexcel>`__ together with this library. `pyexcel-ods <https://github.com/chfw/pyexcel-ods>`__ is a sister library, having no dependency on lxml. However it has no support for python 3.

Known constraints
==================

Only when `the custom version of ezodf <https://github.com/chfw/ezodf>`__ is installed, this library would (0.0.2+) support files in memory. **pyexcel-ods3 v0.0.1** does not support memory file. 

Fonts, colors and charts are not supported. 

Installation
============

You can install it via pip::

    $ pip install git+https://github.com/T0ha/ezodf.git
    $ pip install pyexcel-ods3

or clone it and install it::

    $ pip install git+https://github.com/T0ha/ezodf.git
    $ pip install git+https://github.com/chfw/pyexcel-ods3.git
    $ cd pyexcel-ods3
    $ python setup.py install


The installation of `lxml` will be tricky on Widnows platform. It is recommended that you download a lxml's own windows installer instead of using pip.

Usage
=====

As a standalone library
------------------------


Write to an ods file
*********************

Here's the sample code to write a dictionary to an ods file::

    >>> from pyexcel_ods3 import save_data
    >>> data = OrderedDict()
    >>> data.update({"Sheet 1": [[1, 2, 3], [4, 5, 6]]})
    >>> data.update({"Sheet 2": [["row 1", "row 2", "row 3"]]})
    >>> save_data("your_file.ods", data)

Read from an ods file
**********************

Here's the sample code::

    >>> from pyexcel_ods3 import get_data
    >>> data = get_data("your_file.ods")
    >>> import json
    >>> print(json.dumps(data))
    {"Sheet 1": [[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]], "Sheet 2": [["row 1", "row 2", "row 3"]]}

Write an ods file to memory
******************************

Here's the sample code to write a dictionary to an ods file::

    >>> from pyexcel_ods3 import save_data
    >>> data = OrderedDict()
    >>> data.update({"Sheet 1": [[1, 2, 3], [4, 5, 6]]})
    >>> data.update({"Sheet 2": [[7, 8, 9], [10, 11, 12]]})
    >>> io = StringIO()
    >>> save_data(io, data)
    >>> # do something with the io
    >>> # In reality, you might give it to your http response
    >>> # object for downloading


Read from an ods from memory
*****************************



Here's the sample code::

    >>> # This is just an illustration
    >>> # In reality, you might deal with ods file upload
    >>> # where you will read from requests.FILES['YOUR_ODS_FILE']
    >>> data = get_data(io)
    >>> print(json.dumps(data))
    {"Sheet 1": [[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]], "Sheet 2": [[7.0, 8.0, 9.0], [10.0, 11.0, 12.0]]}


As a pyexcel plugin
--------------------

Import it in your file to enable this plugin::

    from pyexcel.ext import ods3

Please note only pyexcel version 0.0.4+ support this.

Reading from an ods file
************************

Here is the sample code::

    >>> import pyexcel as pe
    >>> from pyexcel.ext import ods3
    >>> sheet = pe.get_book(file_name="your_file.ods")
    >>> sheet
    Sheet Name: Sheet 1
    +---+---+---+
    | 1 | 2 | 3 |
    +---+---+---+
    | 4 | 5 | 6 |
    +---+---+---+
    Sheet Name: Sheet 2
    +-------+-------+-------+
    | row 1 | row 2 | row 3 |
    +-------+-------+-------+

Writing to an ods file
**********************

Here is the sample code::

    >>> sheet.save_as("another_file.ods")

Reading from a IO instance
================================

You got to wrap the binary content with StringIO to get odf working::


    >>> # This is just an illustration
    >>> # In reality, you might deal with xl file upload
    >>> # where you will read from requests.FILES['YOUR_ODS_FILE']
    >>> odsfile = "another_file.ods"
    >>> with open(odsfile, "rb") as f:
    ...     content = f.read()
    ...     r = pe.get_book(file_type="ods", file_content=content)
    ...     print(r)
    ...
    Sheet Name: Sheet 1
    +---+---+---+
    | 1 | 2 | 3 |
    +---+---+---+
    | 4 | 5 | 6 |
    +---+---+---+
    Sheet Name: Sheet 2
    +-------+-------+-------+
    | row 1 | row 2 | row 3 |
    +-------+-------+-------+


Writing to a StringIO instance
================================

You need to pass a StringIO instance to Writer::

    >>> data = [
    ...     [1, 2, 3],
    ...     [4, 5, 6]
    ... ]
    >>> io = StringIO()
    >>> sheet = pe.Sheet(data)
    >>> sheet.save_to_memory("ods", io)
    >>> # then do something with io
    >>> # In reality, you might give it to your http response
    >>> # object for downloading

License
===========

New BSD License


Dependencies
============

1. ezodf
2. pyexcel-io >= 0.0.4

