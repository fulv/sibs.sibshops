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


Configuring Faceted Navigation
==============================
Currently, there is some CSS (probably coming from the theme) that makes the faceted nav configuration page mostly unusable.
The workaround is:
Go to the ZMI, and into portal_css, and select the "Development Mode" checkbox, then save.

The configuration page is:  http://sibs.docentims.com/sibshops/configure_faceted.html

This means portal_css must be put in development mode every time you want to make configuration changes, but hopefully this is a rare occurrence.  Once done, you can put turn development mode back off.

