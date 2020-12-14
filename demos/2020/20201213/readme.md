# Initial Experiments with UDP to Read Data from Tempest

This shows how Java UDP can be used to read data from a Tempest Weather Station. 
The station broadcasts data onto the network, using UDP.  Here are specs on the 
different messages.  For example, a wind speed measurement is broadcast every
three seconds.

The script <a href='udplistener.jy'>udplistener.jy</a> loops to listen to each
packet broadcase on the Tempest port.

The Tempest local UDP API: https://weatherflow.github.io/Tempest/api/udp/v143/
