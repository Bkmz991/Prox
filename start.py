import os
o=True
P=os.chmod
j=os.chdir
x=os.system
import subprocess
y=subprocess.run
x("git clone https://github.com/Bkmz991/proxi2.git")
j('proxyteam')
P('NPPRPROXY.sh',0o755)
y(['./NPPRPROXY.sh'],check=o)
