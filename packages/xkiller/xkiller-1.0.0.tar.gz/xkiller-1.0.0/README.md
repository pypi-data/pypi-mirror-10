py-xkiller
==========
A daemon that is intended for use in a "No X sessions" challenge.

Essentially, every so often, the daemon:

- Checks if the system time is past the time stored at
  http://time.kaashif.co.uk/end
- If it is, quit - the challenge is over
- Checks if there are any daemons with the binary name "X" or "Xorg"
  and kills them.

Installing
==========

	$ pip3 install xkiller

Running
=======

	$ xkiller

(it will daemonize itself)

You may want to run it as root, so it can actually kill sessions
started by display managers etc.

If run as root, /var/run/xkiller.pid will be the PIDfile, if not,
/tmp/xkiller.pid is the PIDfile. Also, you can specify a PIDfile like
so:

	$ xkiller /home/kaashif/mypidfile.pid

