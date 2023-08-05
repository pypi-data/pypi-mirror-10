aneris
======

Aneris is the __goddess__ of order and non_being.

aneris.py is intended to bring order and ultimately non_being to your work load.

1. Configure your team's available work hours in the dict defined in aneris_workers.py

2. Run aneris.py

3. In the ncurses tui:

	a: Add your projects and their deadlines.
	
	b: When highlighting a project, add tasks and the number of hour's work remaining to complete them.
	
	c: Edit your team's avaliable work hours to account for deviations from their default calendars.
	
Project completion dates are calculated.

Any deadlines that you're are on course for missing are highlighted.

Remedial action can then be taken early to add more available hours, remove tasks or re-order projects.

In the tui, press 'h' or '?' to see a list of control keys.

To install:
pip3 install aneris

TODO:

*	Add top level executable to package. Currently you have to faff around chmodding the installed aneris.py and then adding a symlink to it somewhere sensible, like /usr/local/bin.

*   Add editor for default calendars. Currently, upgrading aneris overwrites default calenders...



