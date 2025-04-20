To demo the bug:
1. plot https://github.com/autoplot/dev/blob/master/bugs/sf/2687/demoBug2687.jyds
2. vertical slice, note axis units are Hz
3. right click on yaxis of spectrogram, reset axis units to... kHz
4. Note the xaxis units on the slice are still in Hz.
5. resize the slice to trigger a repaint.
6. Note the xaxis units are now kHz.

