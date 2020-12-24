"""
Import os module
if example.html isn't present
    print warning
else
    Open and read example.html, contents are called pageRead
    Create new write file called result
    print count of all special characters from example.html inro result
"""
import os
if not os.path.isfile('example.html'):
    print('Required file (example.html) does not exist.')
else:
    pageRead=open('example.html','r').read()
    result=open('result','w')
    print('Left Side Angle Brackets:',pageRead.count('<'),file=result)
    print('Right Side Angle Brackets:',pageRead.count('>'),file=result)
    print('Newlines:',pageRead.count('\\n'),file=result)
    print('e:',pageRead.count('e'),file=result)
    print('Comment Open:',pageRead.count('<!--'),file=result)
    print('Comment Close',pageRead.count('-->'),file=result)