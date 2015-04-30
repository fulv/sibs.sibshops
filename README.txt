Configuration Changes
=====================
Added the following line to develop.cfg under [sources]:

sibs.sibshops = git https://github.com/fulv/sibs.sibshops.git


From now on, the buildout must be run specifying this file explicitly:

bin/buildout -c develop.cfg

If you forget the "-c develop.cfg" part, the site will not start.



For some reason, I had to add 'six' to the list of eggs in buildout.cfg.
There is an 'import six' in z3c.form.  I'm not sure why this was not
required before.



Code changes
============
In sibs/sibshops/vocabularies.py, I defined the list of states
and countries in their respective vocabularies.  Now all the states
and countries are visible in their dropdown menus on the add/edit
page for a sibshop content item.

I added a 'NA'/'Not Applicable' entry to the list of states, because
an empty value is not allowed.


Configuring Faceted Search
==============================
Currently, there is some CSS (probably coming from the theme) that makes the
faceted nav configuration page mostly unusable.
The workaround is:

Go to the ZMI, and into portal_css, and select the "Development Mode"
checkbox, then save.

The configuration page is:
http://sibs.docentims.com/sibshops/configure_faceted.html

This means portal_css must be put in development mode every time you want to
make configuration changes, but hopefully this is a rare occurrence.  Once
done, you can put turn development mode back off.

Faceted Search for the Sibshops folder is configured as follows:

- Three dropdowns in the left column: Country, State and City
- Widget for Current search criteria in the center top slot
- Hidden criteria in the right column:
--- 5 results per page
--- Sort of Effective Date, descending
--- Only search in /sibshops folder
--- Only show items of content type Sibshops
- Display as: Standard View

Starting from scratch
=====================

Adding indexes to catalog
=========================
The following indexes are being created by Generic Setup when this product is
installed, or when the 'Catalog Tool' import step from the Sibshops Product is
imported in portal_setup in the ZMI:

- country
- state
- city

To verify they are present, go to the ZMI, then browse to portal_catalog,
and click the Indexes tab.  Look for city, country and state in the list.

If they don't exist, create them manually as follows:

- Choose FieldIndex from the dropdown, and click Add
- Enter the name 'city' in the Id field, click Add
- Back in the list of indexes, click the checkbox next to 'city'
- Note how the column '# distinct values' shows 0
- Click the Reindex button
- Now the third column should show some value greater than 0 if
there are some Sibshops already

- Choose KeywordIndex from the dropdown, and click Add
- Enter the name 'country' in the Id field, click Add
- Back in the list of indexes, click the checkbox next to 'country'
- Note how the column '# distinct values' shows 0
- Click the Reindex button
- Now the third column should show some value greater than 0 if
there are some Sibshops already

- Choose KeywordIndex from the dropdown, and click Add
- Enter the name 'state' in the Id field, click Add
- Back in the list of indexes, click the checkbox next to 'state'
- Note how the column '# distinct values' shows 0
- Click the Reindex button
- Now the third column should show some value greater than 0 if
there are some Sibshops already

Note:  city is a 'FieldIndex', country and state are 'KeywordIndex'es.
Note:  if you prefer, you can avoid reindexing each index separately,
and just go to the "Advanced" tab, and click 'Clear and Rebuild'.  This
will reindex everything at once.  If there is a lot of content, it would
take a long time, though.


Re-creating the Faceted Search configuration
============================================
To configure a new folder with the settings listed above, do the following:

- Actions menu: Enable faceted search
- Click on the Faceted Criteria tab
- Click the Import button
- Browse to the file sibshops.xml in the root of this repository (you might
want to download it to your local machine first)
- Cick View
- From the "Display" menu, choose "Standard view"  (do NOT try the other
views, you might break the page and make it unresponsive)

