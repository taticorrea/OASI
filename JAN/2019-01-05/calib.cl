!ls Bias_*.fit > bias.txt
zerocombine @bias.txt
!ls Flat_*.fit > flat.txt
flatcombine @flat.txt
!ls Dark_80s*.fit > dark.txt
darkcombine @dark.txt
!ls 2009SV17_*.fit > 2009SV17.txt 
ccdproc @2009SV17.txt overscan-	
display masterbias.fits 1 fill+
display masterflat.fits 2 fill+
display masterdark.fits 3 fill+
display 2009SV17_80s_b2x2-001_R.fit 4 fill+
display 2009SV17_80s_b2x2-001_R_c.fit 5 fill+
