# Python Data Dictionary Writer
Add custom html elements in [SchemaSpy](http://schemaspy.sourceforge.net/) pages using Python scripts

**Keywords:** Python, Web scraping, CSV, HTML, automation

## Why did I write this script?
* To automate my process of inserting descriptions for multiple tables and fields in the data dictionary.
* I also want to optimize my workflow in writing the descriptions for more than a thousand fields by retrieving the unique fields instead.

## What can the scripts do?

1. Add table descriptions dynamically in SchemaSpy index page
![Index Before](/Screenshots/index-before.png)
<small>*Original index.html*</small>
<br><br>
![Index After](/Screenshots/index-after.png)
<small>*Resulting index.html with table descriptions for all 139 tables*</small>
<br><br>

2. Add field descriptions dynamically in each SchemaSpy table page
![Table Before](/Screenshots/table-before.png)
<small>*Original cfg_billing_id.html*</small>
<br><br>
![Table After](/Screenshots/table-after.png)
<small>*Resulting cfg_billing_id.html with its table description (same with the index) and field descriptions*</small>
<br><br>


## Prerequisites

1. Install [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/). 

Go to Beautifulsoup folder, and 

```
cd beautifulsoup4-4.6.0
python setup.py install 
```

2. Install [Pathlib](https://docs.python.org/3/library/pathlib.html)

```
sudo pip install pathlib

```

## Releases

**Release 1 - Settlement SOW9 (July 2017)**


<img src="/Screenshots/fc-r1.png" alt="Release 1" height="800px">


* Date: July 13, 2017
* Table Count: 139
* Field Count: 2,862
* Note: Forgot to publish release (Sorry!)

**Release 2 - Settlement SOW10 (October 2017)**

<img src="/Screenshots/fc-r2.png" alt="Release 2" height="800px">


* Date: October 16, 2017  
* Table Count: 186  
* Field Count: 4,066  
* Note: Applied web scrapping to new tables and fields



## Quick Start

1. Export table list to CSV (c/o Google Sheets)
2. Update table descriptions of index and table pages using `writetabledescriptiontohtml.py`
3. If no fields yet:
   * Retrieve and save all unique fields to CSV using `retrieveuniquefields.py`
   * Write fields and field descriptions to CSV using `writefieldstocsv.py`
4. If field descriptions are complete in CSV: Update field descriptions of all tables using `writefielddescriptionstohtml.py`

## TL;DR version: How to use these scripts?

1. Export **table masterlist with descriptions** to csv (Google Sheets).
	* Default Directory: `../../Google Drive/Python/CSV_dump/Settlement-Tables-Descriptions.csv`

2. Run `writetabledescriptiontohtml.py`
	* Write table description to each table html page
	* Result: `Result/settlement_tables_desc/tables/`

3. Run `retrieveuniquefields.py`
	* Retrieve all common and unique fields from all table html pages. Save to CSV
	* Result: `Result/settlement_csv/unique_fields.csv`

3. Update `unique_fields.csv`
	* User can add description to all unique fields in just one CSV file

4. Run `writefieldstocsv.py`
    * Retrieve fields from table html. Add descriptions of common and unique fields from `unique_fields.csv`
    * Result: `Result/settlement_csv/*`

5. (Optional) Update `Result/settlement_csv/*` csv files
	* User can modify descriptions for specific table CSV files

6. Run `writefielddescriptionstohtml.py`
	* HTML Source: `Result/settlement_tables_desc/tables/`
	* Content Source: `Result/settlement_csv/*`
	* Write field descriptions from table csv to each table html.
	* Result: `Result/settlement/tables`


## Things I learned from this mini project:

1. Google Apps Scripts
- Export Tables Masterlist to CSV
- Script not in this repository

2. Python
- Read html files from SchemaSpy folder (BeautifulSoup)
- Retrieve select items from html pages (BeautifulSoup)
- Modify html tag attributes (BeautifulSoup)
- Read CSV files
- Write CSV files
- Write HTML in HTML Files based on CSV content (Pathlib)


## Project Logs

Check out my [logs](https://github.com/eyana-m/python-data-dictionary-writer/blob/master/Logs.md)!


## HTML Customizations:

`Done` - Line 92: Add the following tag

```
<!----Table Description---->
<br>
<div><strong>Description: </strong> {Insert description here from csv source}</div>
<br>
<!----Table Description---->
```

`Done` - Line 40: Add `checked` for comments

```
<label for='showComments'><input type=checkbox checked id='showComments'>Comments</label>
```

## Resources:

### Libraries used:

1. [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/)
2. [Pathlib](https://docs.python.org/3/library/pathlib.html)

### Stackoverflow resources:

1. [Inserting HTML String into BS4 Object](https://stackoverflow.com/questions/31229981/insert-html-string-into-beautifulsoup-object)

2. [Getting the filename dynamically](https://stackoverflow.com/questions/678236/how-to-get-the-filename-without-the-extension-from-a-path-in-python)

3. [Looping directory using python]( https://stackoverflow.com/questions/10377998/how-can-i-iterate-over-files-in-a-given-directory)

4. [Writing CSV using Python](https://stackoverflow.com/questions/14037540/writing-a-python-list-of-lists-to-a-csv-file)

5. [Finding html element by class](https://stackoverflow.com/questions/5041008/how-to-find-elements-by-class)

6. [Writing to BS4 Find object](https://stackoverflow.com/questions/17610438/beautifulsoup-insert-text-var-into-every-given-td-class)

7. [Python: How to check if cell in csv file is empty](https://stackoverflow.com/questions/34192705/python-how-to-check-if-cell-in-csv-file-is-empty)

8. [How to install pip in mac](https://stackoverflow.com/questions/17271319/how-do-i-install-pip-on-macos-or-os-x)

9. [How can I remove DS store files from a git repository](https://stackoverflow.com/questions/107701/how-can-i-remove-ds-store-files-from-a-git-repository)
