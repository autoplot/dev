from PIL import Image, PngImagePlugin

def get_rich_png_meta( plt ):
    for fig_num in plt.get_fignums():
        fig = plt.figure(fig_num)
        print 'fig'
        for ax in fig.axes:
            print(ax.get_title()) 
            print(ax.get_xlabel())
            print(ax.get_xlim())    
            for line in ax.lines:
                print(f"Figure {fig_num}: {line.get_label()} color={line.get_color()}")
            
def add_rich_png_meta( pngfile, richMeta ):
    'plt is a matplotlib plot'
    # Open your existing PNG
    im = Image.open(pngfile)
    
    # Create metadata block
    meta = PngImagePlugin.PngInfo()
    meta.add_text("plotInfo", richMeta)

    # Save new PNG with tEXt chunks
    im.save(pngfile+'.1.png', pnginfo=meta)
    os.rename( pngfile+'.1.png',pngfile )

