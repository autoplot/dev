# Purpose
Write a demo showing how SAMP is used to push file reference URLs into Autoplot, 
to evaluate if the mechanism could be used by CDAWeb.

# Background
CDAWeb has been using Webstart and a CGI-BIN server which generates dynamic JNLP
files to launch Autoplot with a given filename.  When Autoplot was moved from 
Amazon to a simpler server, this mechanism was moved to a server at the University
of Iowa.  

This hasn't worked reliably, and with fewer and fewer webstart launches, plus
new versions of Java which no longer support Webstart, it seems timely to consider
the SAMP mechanism.

# Demo
* Load the web page at https://soar.esac.esa.int/soar/
* Search
* 2021-08-01 to 2021-08-31; All; All
* Select solo_L1_epd-epthet2-sc_20210801 
* click the SAMP broadcast button, "Send Products"
* A popup shows that no software is running to receive the message.
* Launch Autoplot
* Tools -> "Start SAMP Hub and Listener"
* click the SAMP broadcast button, "Send Products"
* The connection must be authorized
* click the SAMP broadcast button, "Send Products"
* Autoplot now receives the URL reference and handles it properly.
