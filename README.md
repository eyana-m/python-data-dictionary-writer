# Python Data Dictionary Writer
Add custom html elements in [SchemaSpy](http://schemaspy.sourceforge.net/) pages using Python scripts


### Why did I write this script?
* I need to create a data dictionary that is useful and informative to the client, but...
* Too busy (and lazy) to manually copy and paste descriptions of 144 tables to their respective HTML files.

## Quick Start: How to use these scripts?

1. Export **table masterlist with descriptions** to csv (Google Sheets). 
	* Default Directory: `../../Google Drive/Python/CSV_dump/Settlement-Tables-Descriptions.csv`
2. Run `writetabledescriptiontohtml.py` 
	* Write table description to each table html page
	* Result: `Result/settlement_tables_desc/tables/`
3. Run `retrieveuniquefields.py`
	* Retrieve all common and unique fields from all table html pages. Save to CSV
	* Result: `Result/settlement_csv/unique_fields.csv`
3. Update `unique_fields.csv`
	* User can add description to all unique fields in just one csv
4. Run `writefieldstocsv.py` 
    * Retrieve fields from table html. Add descriptions of common and unique fields from `unique_fields.csv`
    * Result: `Result/settlement_csv/*`
4. (Optional) Update `Result/settlement_csv/*`  csv files
	* User can modify description for specific table CSVs
5. Run `writefieldescriptionstohtml.py`
	* Write field descriptions from table csv to each table html.
	* Result: `Result/settlement/tables`


### Features


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


### Progress Logs


Check out my [logs](https://github.com/eyana-m/python-data-dictionary-writer/blob/master/Logs.md)!


### HTML Customizations:

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

### Libraries used:

1. [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/)
2. [Pathlib](https://docs.python.org/3/library/pathlib.html)

### Resources:

1. [Inserting HTML String into BS4 Object](https://stackoverflow.com/questions/31229981/insert-html-string-into-beautifulsoup-object)

2. [Getting the filename dynamically](https://stackoverflow.com/questions/678236/how-to-get-the-filename-without-the-extension-from-a-path-in-python)

3. [Looping directory using python]( https://stackoverflow.com/questions/10377998/how-can-i-iterate-over-files-in-a-given-directory)

4. [Writing CSV using Python](https://stackoverflow.com/questions/14037540/writing-a-python-list-of-lists-to-a-csv-file)

5. [Finding html element by class](https://stackoverflow.com/questions/5041008/how-to-find-elements-by-class)

6. [Writing to BS4 Find object](https://stackoverflow.com/questions/17610438/beautifulsoup-insert-text-var-into-every-given-td-class)

7. [Python: How to check if cell in csv file is empty](https://stackoverflow.com/questions/34192705/python-how-to-check-if-cell-in-csv-file-is-empty)

8. [How to install pip in mac](https://stackoverflow.com/questions/17271319/how-do-i-install-pip-on-macos-or-os-x)

9. [How can I remove DS store files from a git repository](https://stackoverflow.com/questions/107701/how-can-i-remove-ds-store-files-from-a-git-repository)
