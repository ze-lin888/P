[app]
title = Private Lossless Player
package.name = losslessplayer
package.domain = org.lossless
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,txt
version = 0.1
requirements = python3,kivy==2.3.0,hostpython3
orientation = portrait
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE
android.api = 33
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license = True
android.archs = arm64-v8a, armeabi-v7a
android.entrypoint = main.py

[buildozer]
log_level = 2
warn_on_root = 1
