This demonstrates that the number of connections is low.  

On a unix terminal, run:
~~~~~
while [ 1 ]; do netstat -p | grep cdaweb; sleep 2; clear; done
~~~~~
so that the connections made by Autoplot can be seen.

Then run Autoplot and the script.
