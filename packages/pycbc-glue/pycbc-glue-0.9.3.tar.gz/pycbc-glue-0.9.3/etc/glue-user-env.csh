# Source this file to access GLUE
setenv GLUE_PREFIX /usr
setenv PATH /usr/bin:${PATH}
if ( $?PYTHONPATH ) then
  setenv PYTHONPATH /usr/lib64/python2.7/site-packages:/usr/lib/python2.7/site-packages:${PYTHONPATH}
else
  setenv PYTHONPATH /usr/lib64/python2.7/site-packages:/usr/lib/python2.7/site-packages
endif
if ( $?LD_LIBRARY_PATH ) then
  setenv LD_LIBRARY_PATH /usr/lib64/python2.7/site-packages:${LD_LIBRARY_PATH}
else
  setenv LD_LIBRARY_PATH /usr/lib64/python2.7/site-packages
endif
if ( $?DYLD_LIBRARY_PATH ) then
  setenv DYLD_LIBRARY_PATH /usr/lib64/python2.7/site-packages:${DYLD_LIBRARY_PATH}else
  setenv DYLD_LIBRARY_PATH /usr/lib64/python2.7/site-packages
endif
