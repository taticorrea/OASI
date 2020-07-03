!ls Bias_*.fit > bias.txt
zerocombine @bias.txt
!ls Flat_1.2s_*.fit > flat.txt
flatcombine @flat.txt
!ls Dark_40s_*.fit > dark.txt
darkcombine @dark.txt
!ls 1998NU_*.fit > 1998NU.txt 
ccdproc @1998NU.txt overscan-	
display masterbias.fits 1 fill+
display masterflat.fits 2 fill+
display masterdark.fits 3 fill+
display 1998NU_40s_b2x2-100_R.fit 4 fill+
display 1998NU_40s_b2x2-100_R_c.fit 5 fill+
