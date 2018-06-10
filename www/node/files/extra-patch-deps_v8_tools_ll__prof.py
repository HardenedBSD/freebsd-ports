--- deps/v8/tools/ll_prof.py.orig	2018-06-10 08:55:52 UTC
+++ deps/v8/tools/ll_prof.py
@@ -869,7 +869,7 @@ if __name__ == "__main__":
                     default="/tmp/__v8_gc__",
                     help="gc fake mmap file [default: %default]")
   parser.add_option("--objdump",
-                    default="/usr/bin/objdump",
+                    default="/usr/local/bin/objdump",
                     help="objdump tool to use [default: %default]")
   parser.add_option("--host-root",
                     default="",
