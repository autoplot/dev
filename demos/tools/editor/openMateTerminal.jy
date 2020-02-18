setScriptTitle('Open Mate Terminal')
setScriptDescription('Open terminal in the script directory')

script= getApplication().getScriptPanel().getFilename()

from java.io import File
from org.autoplot.datasource import AutoplotSettings
autoplotData= AutoplotSettings.settings().resolveProperty( AutoplotSettings.PROP_AUTOPLOTDATA )

exe= 'mate-terminal'

from java.lang import ProcessBuilder

pb= ProcessBuilder(exe.split(' '))
pb.directory( File( script ).parentFile )

log= File( autoplotData, 'log' )
log= File( log, 'editor.openterminal.txt' )

pb.redirectErrorStream(True)
pb.redirectOutput( ProcessBuilder.Redirect.to(log) )

p= pb.start()

setStatus( "mate-terminal complete, see " + str(log) )

