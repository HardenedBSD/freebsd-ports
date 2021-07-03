--- tools/genv8constants.py.orig	2018-06-10 09:22:07.876673000 +0000
+++ tools/genv8constants.py	2018-06-10 09:22:18.437062000 +0000
@@ -18,7 +18,7 @@
 
 outfile = file(sys.argv[1], 'w');
 try:
-  pipe = subprocess.Popen([ 'objdump', '-z', '-D', sys.argv[2] ],
+  pipe = subprocess.Popen([ '/usr/local/bin/objdump', '-z', '-D', sys.argv[2] ],
       bufsize=-1, stdout=subprocess.PIPE).stdout;
 except OSError, e:
   if e.errno == errno.ENOENT:
