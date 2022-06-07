import numpy as np
import datetime
from spacepy import pycdf
import os, sys

# export CDF_LIB='/home/jbf/local/cdf/lib/'

def do_extract_subset( fln, start, stop, varss ):
    outfiln= fln[:-4] + '.' + str(start) + '.' + str(stop) + '.cdf' 
    cdf = pycdf.CDF( fln )
    if ( os.path.exists( outfiln ) ):
        os.remove( outfiln )
        
    cdfout= pycdf.CDF( outfiln,'')
    for v in varss:
         vdata= cdf[v][start:stop]
         cdfout[v]= vdata
         cdfout[v].attrs= cdf[v].attrs
    cdf.close()     
    return outfiln

if __name__=='__main__':
    if ( len(sys.argv)!=5 ):
        print( sys.argv[0] + ' <cdf> <start> <stop> <v1,v2>' )
        sys.exit(-1)
    
    fln= sys.argv[1]

    if sys.argv[4]=='*':
        cdf = pycdf.CDF( fln )
        varss1= ''
        for k in cdf:
            varss1= varss1 + ',' + k
        cdf.close()
        varss1= varss1[1:] # remove the comma
        varss= varss1.split(',')
    else:
        varss= sys.argv[4].split(',')
        
    start= int(sys.argv[2])
    stop= int(sys.argv[3])

    newf= do_extract_subset( fln, start, stop, varss )
    print( newf )
