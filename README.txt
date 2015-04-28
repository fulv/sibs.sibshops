Configuration Changes
=====================
Added the following line to develop.cfg under [sources]:

sibs.sibshops = git https://github.com/fulv/sibs.sibshops.git



From now on, the buildout must be run specifying this file explicitly:

bin/buildout -c develop.cfg

If you forget the "-c develop.cfg" part, the site will not start.



Code changes
============
In sibs/sibshops/vocabularies.py, I defined the list of states
and countries in their respective vocabularies.  Now all the states
and countries are visible in their dropdown menus on the add/edit
page for a sibshop content item.

I added a 'NA'/'Not Applicable' entry to the list of states, because
an empty value is not allowed.
