========
Crucible
========

This library was created by the News & Review for The Crucible.  This set of tools currently consists of one command - a calendar command to convert CSV data of Crucible course schedules into an InDesign compatible, docx styled listing.  Perhaps there will be more to come one day.


Installation and Usage
----------------------
::

    pip install nr-crucible

    # To see command line options
    $ crucible -h

    # To generate a calendar from a CSV file
    $ crucible calendar -i infile.csv -o outfile.docx
