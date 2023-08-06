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

Any deadlines that you're on course for missing are highlighted.

Remedial action can then be taken early to add more available hours, remove tasks or re-order projects.

In the tui, press 'h' or '?' to see a list of control keys.

To install:

pip3 install aneris


Windows users:
A rudimentary binary installer is included for you in case you find it useful. However, as Aneris uses curses (and the python curses library is unix only) this will not work "out of the box".
Aneris DOES however run very nicely under cygwin...

---

Fixed in version 0.5 - (Beta)
	BUGFIX:
		Fixed exception thrown on save under some circumstances:
			for day in self.m_worker_calendar_exceptions.keys():
			RuntimeError: dictionary changed size during iteration

	TASK:
		Added top level executable script (installed as /usr/local/bin/aneris)

Fixed in version 0.4 = (Beta)
	First (just about) usable release.

---

TODO:

*   Add editor for default calendars. Currently, upgrading aneris overwrites default calenders...
	Unfortunately it is likely to be a while before this issue gets resolved as although annoying, it's not really blocking me. If lots of people moan, I might bother sooner.


