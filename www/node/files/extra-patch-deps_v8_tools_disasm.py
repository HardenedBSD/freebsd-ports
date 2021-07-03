--- deps/v8/tools/disasm.py.orig	2018-06-10 08:55:38 UTC
+++ deps/v8/tools/disasm.py
@@ -34,7 +34,7 @@ import tempfile
 
 
 # Avoid using the slow (google-specific) wrapper around objdump.
-OBJDUMP_BIN = "/usr/bin/objdump"
+OBJDUMP_BIN = "/usr/local/bin/objdump"
 if not os.path.exists(OBJDUMP_BIN):
   OBJDUMP_BIN = "objdump"
 
