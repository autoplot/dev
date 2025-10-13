wget -N https://raw.githubusercontent.com/autoplot/orbits/refs/heads/main/psp/psp-aa25.txt
PWD=`pwd`
java -cp autoplot.jar org.autoplot.pngwalk.CreatePngWalk \
    --vap=psp-density.vap \
    --timeRange=orbit:file:${PWD}/psp-aa25.txt:1-24 \
    --timeFormat=\$\(o\;id=file:${PWD}/psp-aa25.txt\) 
    
