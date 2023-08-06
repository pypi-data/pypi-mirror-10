# Source this file to access GLUE
GLUE_PREFIX=/usr
export GLUE_PREFIX
PATH=/usr/bin:${PATH}
PYTHONPATH=/usr/lib64/python2.7/site-packages:/usr/lib/python2.7/site-packages:${PYTHONPATH}
LD_LIBRARY_PATH=/usr/lib64/python2.7/site-packages:${LD_LIBRARY_PATH}
DYLD_LIBRARY_PATH=/usr/lib64/python2.7/site-packages:${DYLD_LIBRARY_PATH}
export PATH PYTHONPATH LD_LIBRARY_PATH DYLD_LIBRARY_PATH
