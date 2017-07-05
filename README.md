# python-data-dictionary-writer
Add html elements in SchemaSpy pages

Things to do

July 5, 2017

* Set up git
* Set up python


Backlog

1. Google Apps Scripts - Export Tables Masterlist to CSV
2. Python 
- Read Html Files from SchemaSpy folder
- Read CSV file from Google sheets
- Write HTML in HTML Files based on CSV content
3. HTML Files
- Design table description in htmls


HTML

Line 92: Add the following tag

```
<!----Table Description----> 
<br>
<div><strong>Description: </strong> {Insert description here from csv source}</div>
<br>
<!----Table Description---->
```


Line 40: Add `checked` for comments

```
<label for='showComments'><input type=checkbox checked id='showComments'>Comments</label>
```

