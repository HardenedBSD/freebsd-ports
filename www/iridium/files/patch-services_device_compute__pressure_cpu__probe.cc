--- services/device/compute_pressure/cpu_probe.cc.orig	2022-10-05 07:34:01 UTC
+++ services/device/compute_pressure/cpu_probe.cc
@@ -63,6 +63,7 @@ std::unique_ptr<CpuProbe> CpuProbe::Create() {
 #elif BUILDFLAG(IS_MAC)
   return CpuProbeMac::Create();
 #else
+  NOTIMPLEMENTED();
   return std::make_unique<NullCpuProbe>();
 #endif  // BUILDFLAG(IS_ANDROID)
 }
