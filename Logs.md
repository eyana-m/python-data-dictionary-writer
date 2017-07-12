# Logs
Add html elements in SchemaSpy pages using Python scripts

Things to do

### July 5, 2017

* Set up git
* Set up python

### July 8, 2017

* Reviewing [BeautifulSoup4 documentation](https://beautiful-soup-4.readthedocs.io/en/latest/)

Learning

soup.prettify() - displays html code  
soup.title - displays the title tag and contents    
soup.contents - displays first layer of contents, no children    
soup.children - displays children     

### July 10, 2017

* `Writetabledescription.py` completed

What can it do?
* Write table descriptions to each table page dynamically


Next Agenda:
   * Write table description in `index.html`
   * Auto-open comment column
   * Write field descriptions easily:
      * Export fields
      * Import fields with description. Attach to html.

### July 11, 2017

Wrote the following scripts:

1. `retrievefields.py`
   * Export table contents in html to csv file
2. `writefielddescriptions.py`
   * Import csv content with descriptions.
   * Attach to respective html pages.
   * Also auto-open comment column.

To do:

* Refactor code to **integrate** write table and field description jobs
  * Make `settlement_field_description` folder defunct
* Add field descriptions to 144 tables (lol, the only task I cannot automate)

# Jully 12, 2017

Done:

1. `writefielddescriptions.py`
   * Check if csv has field descriptions already

https://stackoverflow.com/questions/34192705/python-how-to-check-if-cell-in-csv-file-is-empty

https://stackoverflow.com/questions/17271319/how-do-i-install-pip-on-macos-or-os-x

To do:

* Add warning: "This job will overwrite the existing folder. Are you sure you want to proceed?"
* Add descriptions in `index.html` dynamically
* Fix gitignore 

