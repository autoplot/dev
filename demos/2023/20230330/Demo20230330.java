package test;

import gov.nasa.gsfc.spdf.cdfj.CDFException;
import gov.nasa.gsfc.spdf.cdfj.CDFWriter;
import java.io.IOException;

/**
 * demo insert of data into empty file.  This doesn't work for me, but we think it could be made to work.
 * @author jbf
 */
public class Demo20230330 {
    public static void main( String[] args ) throws CDFException.WriterError, IOException, CDFException.ReaderError {
        CDFWriter cdf= new CDFWriter( "test.cdf", false );
        float[] data= new float[] { 101,102,103,104,105,106,107,108,109,110 };
        cdf.addData("period",data );
        long[] ttag= new long[] { 1,2,3,4,5,6,7,8,9,10 };
        for ( int i=0; i<ttag.length; i++ ) {
            ttag[i]= ttag[i] * 10000000000L + 733492869184000000L;
        }
        cdf.addData("Epoch",ttag );
        cdf.write( "test.cdf" );
    }
}
