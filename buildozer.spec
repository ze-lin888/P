[app]
# (str) Title of your application
title = Private Lossless Player

# (str) Package name
package.name = losslessplayer

# (str) Package domain (needed for android packaging)
package.domain = org.lossless

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas,txt

# (str) Application versioning (method 1)
version = 0.1

# (list) Application requirements
# 核心：固定 Kivy 版本以确保兼容性
requirements = python3,kivy==2.3.0,hostpython3

# (str) Supported orientations
orientation = portrait

# ----------------------------------
# Android specific
# ----------------------------------

# (bool) Indicate if the application should be fullscreen
fullscreen = 0

# (list) Permissions
# 加上网络和存储权限，听歌必备
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support.
android.minapi = 21

# (str) Android NDK version to use
android.ndk = 25b

# (bool) Use --private data storage (True) or --dir public storage (False)
android.private_storage = True

# (str) Android entry point, default is to use start.py
android.entrypoint = main.py

# (str) Android app theme, default is ok for now
android.theme = @android:style/Theme.NoTitleBar

# (bool) Accept SDK license without operator interaction
android.accept_sdk_license = True

# (str) The Android arch to build for, latest devices use arm64-v8a
android.archs = arm64-v8a, armeabi-v7a

# (list) List of Java files to add to the android project
# android.add_src =

[buildozer]
# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = off, 1 = on)
warn_on_root = 1
