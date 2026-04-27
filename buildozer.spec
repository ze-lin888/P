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

# (str) Application versioning
version = 0.1

# (list) Application requirements
# 核心：锁定稳定版 Kivy
requirements = python3,kivy==2.3.0,hostpython3

# (str) Supported orientations
orientation = portrait

# ----------------------------------
# Android specific
# ----------------------------------

# (list) Permissions - 加上网络和存储权限，听无损音乐必备
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

# (int) Target Android API - 设置为 33 是目前云端打包最稳的版本
android.api = 33

# (int) Minimum API your APK will support
android.minapi = 21

# (str) Android NDK version to use
android.ndk = 25b

# (bool) Accept SDK license without operator interaction
# 这是咱们刚才卡住的地方，这里必须是 True
android.accept_sdk_license = True

# (str) The Android arch to build for
# 同时支持 32 位和 64 位手机
android.archs = arm64-v8a, armeabi-v7a

# (str) Android entry point
android.entrypoint = main.py

[buildozer]
# (int) Log level (2 = 详细模式，方便咱们抓错)
log_level = 2

# (int) Display warning if buildozer is run as root
warn_on_root = 1
