--- chrome/test/chromedriver/chrome_launcher.cc.orig	2022-10-01 07:40:07 UTC
+++ chrome/test/chromedriver/chrome_launcher.cc
@@ -65,6 +65,7 @@
 #include <fcntl.h>
 #include <sys/stat.h>
 #include <sys/types.h>
+#include <sys/wait.h>
 #include <unistd.h>
 #elif BUILDFLAG(IS_WIN)
 #include "chrome/test/chromedriver/keycode_text_conversion.h"
