--- deps/v8/tools/grokdump.py.orig	2018-06-10 08:55:46 UTC
+++ deps/v8/tools/grokdump.py
@@ -584,7 +584,7 @@ MD_CPU_ARCHITECTURE_ARM64 = 0x8003
 MD_CPU_ARCHITECTURE_AMD64 = 9
 
 OBJDUMP_BIN = None
-DEFAULT_OBJDUMP_BIN = '/usr/bin/objdump'
+DEFAULT_OBJDUMP_BIN = '/usr/local/bin/objdump'
 
 class FuncSymbol:
   def __init__(self, start, size, name):
