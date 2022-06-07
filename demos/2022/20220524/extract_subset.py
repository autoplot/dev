import numpy as np
import datetime
from spacepy import pycdf
import os, sys

# export CDF_LIB='/home/jbf/local/cdf/lib/'

def do_extract_subset( flname, start, stop, varss ):
    outfiln= flname[:-4] + '.' + str(start) + '.' + str(stop) + '.cdf' 
    cdf = pycdf.CDF( flname )
    if ( os.path.exists( outfiln ) ):
        os.remove( outfiln )
    
    addus= []
    for v in varss:
        dep0= cdf[v].attrs['DEPEND_0']
        print( 'dep0='+dep0 )
        addus.append(dep0)
    addus.extend(varss)
    varss= addus
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
    start= int(sys.argv[2])
    stop= int(sys.argv[3])
    varss= sys.argv[4].split(',')
    newf= do_extract_subset( fln, start, stop, varss )
    print( newf )
