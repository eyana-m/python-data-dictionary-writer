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

# July 12, 2017

Done:

1. `writefielddescriptions.py`
   * Check if csv has field descriptions already


Handling Common Fields

2. `retrieveuniquefields.py`
   * get unique fields and save as csv
   * allow user to manually define each unique field


3. `writefieldstocsv.py`
   * retrieve unique fields and description and write to respective table csv


Workflow so far:

1. Export table masterlist to csv (Google Sheets)
2. Write table description to each table html
   * `writetabledescriptiontohtml.py`
3. Retrieve all common and unique fields from all table. Save to CSV
   * `retrieveuniquefields.py`
3. User adds description to all common and unique fields in just one csv
   * `unique_fields.csv`
4. Retrieve fields from table html. Add descriptions of common and unique fields
   * `writefieldstocsv.py`
4. (Optional) User modifies description for specific table CSVSs
   * `Result/settlement_csv/`
5. Write field descriptions from table csv to each table html.
   * `writefieldescriptionstohtml.py`


To do:

* Add warning: "This job will overwrite the existing folder. Are you sure you want to proceed?"
* Add descriptions in `index.html` dynamically
* Fix gitignore


#July 13, 2017

Created `writeTableDescriptionToIndex.py`

Incorporated with `writeTableDescriptionToHTML.py` to optimize process

Workflow so far:

1. Export table list to CSV (c/o Google Sheets)
2. Update table descriptions of index and table pages using `writeTableDescriptiontoHTML.py`
3. If no more fields yet: 
   * Retrieve all unique fields to CSV using `retrieveUniqueFields.py`
   * Write fields to CSV using `writeFieldsToCSV.py`
4. If field descriptions are complete in CSV: Update field descriptions of all tables using `writeFieldDescriptionsToHTML.py`
