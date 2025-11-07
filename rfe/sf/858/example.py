import matplotlib.pyplot as plt
import numpy as np

fig, (ax1, ax2) = plt.subplots(2, 1, layout='constrained')

dt = 0.01
t = np.arange(0, 30, dt)

# Fixing random state for reproducibility
np.random.seed(19680801)


nse1 = np.random.randn(len(t))                 # white noise 1
nse2 = np.random.randn(len(t))                 # white noise 2
r = np.exp(-t / 0.05)

cnse1 = np.convolve(nse1, r, mode='same') * dt   # colored noise 1
cnse2 = np.convolve(nse2, r, mode='same') * dt   # colored noise 2

# two signals with a coherent part and a random part
s1 = 0.01 * np.sin(2 * np.pi * 10 * t) + cnse1
s2 = 0.01 * np.sin(2 * np.pi * 10 * t) + cnse2

ax1.plot(t, s1, t, s2)
ax1.set_xlim(0, 5)
ax1.set_xlabel('Time (s)')
ax1.set_ylabel('s1 and s2')
ax1.grid(True)

cxy, f = ax2.csd(s1, s2, NFFT=256, Fs=1. / dt)
ax2.set_ylabel('CSD (dB)')

def get_rich_png_meta( w_in, h_in, plt ):
    text= []
    # find the first figure
    for fig_num in plt.get_fignums():
        fig = plt.figure(fig_num)
        if len(fig.axes)>0:
            break        
    #w_in, h_in = fig.get_size_inches()
    #dpi = fig.dpi
    canvasJson= '{ "size":[%d,%d], \n  "plots": [' % ( w_in, h_in )
    text.append(canvasJson)    
    plots= []
    for ax in fig.axes:
            bbox = ax.get_position()
            print(bbox)
            #w_in, h_in = fig.get_size_inches()
            #dpi = fig.dpi
            x0 = bbox.x0 * w_in 
            y0 = bbox.y0 * h_in 
            x1 = bbox.x1 * w_in 
            y1 = bbox.y1 * h_in 
            print( '%.2f %.2f ' % ( y0, y1 ), ax.get_ylabel())
            y0 = h_in - y0 # flip so that 0,0 is upper-left
            y1 = h_in - y1
            y1,y0=y0,y1
            print( '%.2f %.2f ' % ( y0, y1 ), ax.get_ylabel(), 'flip')            
            xlim= ax.get_xlim()
            xaxis= '{ "label": "%s", "min":%s, "max":%s, "units":"", "left":%.1f, "right":%.1f, "type":"lin" }' \
                % ( ax.get_xlabel(), xlim[0], xlim[1], x0, x1 )
            ylim= ax.get_ylim()
            yaxis= '{ "label": "%s", "min":%s, "max":%s, "units":"", "top":%.1f, "bottom":%.1f, "type":"lin" }' \
                % ( ax.get_ylabel(), ylim[0], ylim[1], y0, y1 )
            plotJson = '{ "title":"%s",\n "xaxis":%s,\n "yaxis":%s }' % ( ax.get_title(), xaxis, yaxis )
            
            plots.append(plotJson)
    text.append( ',\n'.join(plots) )
    text.append(' ], ')
    text.append( '"numberOfPlots":%d' % len(fig.axes)  )
    text.append('}')
    print('\n'.join(text))
    return '\n'.join(text)
    
def add_rich_png_meta( pngfile, richMeta ):
    from PIL import Image, PngImagePlugin
    import os
    # Open your existing PNG

    im = Image.open(pngfile)
    
    # Create metadata block
    meta = PngImagePlugin.PngInfo()
    meta.add_text("plotInfo", richMeta)

    # Save new PNG with tEXt chunks
    im.save(pngfile+'.1.png', pnginfo=meta)
    os.rename( pngfile+'.1.png',pngfile )

plt.savefig('example.png')
richMeta= get_rich_png_meta( 640, 480, plt )
add_rich_png_meta( 'example.png', richMeta )



