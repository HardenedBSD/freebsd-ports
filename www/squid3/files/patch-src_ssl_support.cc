--- src/ssl/support.cc.orig	2018-07-15 20:46:55 UTC
+++ src/ssl/support.cc
<<<<<<< HEAD
@@ -2159,7 +2159,11 @@ remove_session_cb(SSL_CTX *, SSL_SESSION
=======
@@ -2159,7 +2159,11 @@ remove_session_cb(SSL_CTX *, SSL_SESSION *sessionID)
>>>>>>> upstream/master
 }
 
 static SSL_SESSION *
-get_session_cb(SSL *, unsigned char *sessionID, int len, int *copy)
+get_session_cb(SSL *,
<<<<<<< HEAD
+#if defined(LIBRESSL_VERSION_NUMBER) && LIBRESSL_VERSION_NUMBER >= 0x20800000L
+const
+#endif
+unsigned char *sessionID, int len, int *copy)
=======
+#ifdef LIBRESSL_VERSION_NUMBER
+  const
+#endif
+  unsigned char *sessionID, int len, int *copy)
>>>>>>> upstream/master
 {
     if (!SslSessionCache)
         return NULL;
