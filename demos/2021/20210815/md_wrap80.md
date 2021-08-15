from java.awt import BorderLayout
from javax.swing import JTextArea,JPanel,JButton,BoxLayout
from java.lang import StringBuilder
setScriptTitle('Markdown refactor 80 Columns')
setScriptDescription('''Create an equivalent markdown file where each line is 80 columns or fewer.
This creates a new text window tab.''')

def refactorWidth( source ):
    ss = source.split('\n')
    sb = StringBuilder()
    for s in ss:
        i = 0
        lens= len(s)
        while i<lens:
            ni= s[i:i+80].rfind(' ')
            while ni>0 and s[ni-1]=='.':
                    ni= s[i:i+ni].rfind(' ')
            if ni>-1: ni= i+ni                 
            if ni==i: ni= s.find(' ',i) # special case long word (URL for example).
            if ni==-1: ni=lens
            if ni==i: ni=lens
            if ni>lens: ni=lens
            print i, ni, lens, s[i:ni]
            sb.append(s[i:ni])
            sb.append('\n')
            if ni<lens and s[ni]==' ':
                i = ni + 1
            else:
                i = ni
    return sb.toString()
             
def go( evt ):
    global ta
    text= ta.text
    text= refactorWidth( text )
    ta.text= text
    
ta= JTextArea()
panel = JPanel( BorderLayout() )
panel.add( ta, BorderLayout.CENTER )
gobutton= JButton( 'Wrap 80 columns', actionPerformed=go )

panel.add( gobutton, BorderLayout.SOUTH )

addTab( 'Wrap80', panel )
