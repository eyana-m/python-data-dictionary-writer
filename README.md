# Python Data Dictionary Writer
Add custom html elements in [SchemaSpy](http://schemaspy.sourceforge.net/) pages

### Why did I write this script
I work in software development. Too busy (and lazy) to manually copy and paste descriptions of 144 tables to their respective HTML files

### What can this script do?

This mini- project involves the following activities:

1. Google Apps Scripts
- Export Tables Masterlist to CSV
2. Python
- Read Html Files from SchemaSpy folder (BeautifulSoup)
- Read CSV file from Google Sheets
- Write HTML in HTML Files based on CSV content (Pathlib)
3. HTML Files
- Design table description in HTML


### HTML Modification

`Done` - Line 92: Add the following tag

```
<!----Table Description---->
<br>
<div><strong>Description: </strong> {Insert description here from csv source}</div>
<br>
<!----Table Description---->
```

`Upcoming` - Line 40: Add `checked` for comments

```
<label for='showComments'><input type=checkbox checked id='showComments'>Comments</label>
```

### Libraries used:

1. [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/)
2. [Pathlib](https://docs.python.org/3/library/pathlib.html)

#### Resources:

1. [Inserting HTML String into BS4 Object](https://stackoverflow.com/questions/31229981/insert-html-string-into-beautifulsoup-object)

2. [Getting the filename dynamically](https://stackoverflow.com/questions/678236/how-to-get-the-filename-without-the-extension-from-a-path-in-python)

3. [Looping directory using python]( https://stackoverflow.com/questions/10377998/how-can-i-iterate-over-files-in-a-given-directory)
