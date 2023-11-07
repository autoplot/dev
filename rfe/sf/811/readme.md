The "fix layout" operation will rearrange existing plots so that titles and labels don't overlap 
while using the space effectively.  This has been implemented and reimplemented several times, 
and with a nice block of time I was able to finally implement this as it was always intended.  This
will preserve relative heights of the plots, and will respect plots which are a fixed height as
with an events bar which is 1em high.

The script grandTest.jy tries to thoughly test the code, and will be run regularly to verify that
things do not change.

There are still items to be done:
* plots with a combination of full-width plots and multi-column plots are not supported presently.
* fixed-sizes are only supported for ems, and pixel offsets are ignored.

See https://sourceforge.net/p/autoplot/feature-requests/811/
