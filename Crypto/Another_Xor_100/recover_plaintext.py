from libnum import *

cipher = n2s(int('274c10121a0100495b502d551c557f0b0833585d1b27030b5228040d3753490a1c025415051525455118001911534a0052560a14594f0b1e490a010c4514411e070014615a181b02521b580305170002074b0a1a4c414d1f1d171d00151b1d0f480e491e0249010c150050115c505850434203421354424c1150430b5e094d144957080d4444254643',16))

s='flag{' + '_'*(38-6) + '}A qua' + '_'*(67-5)
a='A qua' + '_'*(67-5) + 'A qua' + '_'*(67-5) + 'A q'

prev = ''
while prev != s:
  prev = s
  s=list(s)
  a=list(a)

  for i in range(0, len(s)):
    if s[i] == '_' and a[i] != '_':
      s[i] = chr(ord(cipher[i]) ^ ord(a[i]))
    if s[i] != '_' and a[i] == '_':
      a[i] = chr(ord(cipher[i]) ^ ord(s[i]))

  s=''.join(s)
  a=''.join(a)

  print s
  a = s[38:]*2 + 'A q'

print 'Plaintext: '+s[:38]
