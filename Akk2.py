import crypt

alg = 6  # SHA512
salt = '$6$tvzhOcQf'

encrypt='$6$tvzhOcQf$F42lMmwYB46wKcLJyD8Ya07RjlDeVq3Dr64StXPHizUFuwkCVVghcDOnPekO12rttUgEW9XISVv03wAjMwUWM0'
         

months=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
sins=['S1','S2','S3','S4','S5','S6','S7','S8','S9','S0']
for j in range(1940,1991):
     for month in months:
         for i in range(10,32):
             for sin in sins:
                 a = month+'-'+str(i)+'-'+str(j)+'-'+sin
                 print a
                 cryptWord = crypt.crypt(a,salt)
                 print cryptWord
                 if(encrypt==cryptWord):
                   print "cracked"
                   break