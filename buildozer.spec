[app]
title = mymusicplayer
package.name = losslessplayer
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
# 锁定工业级稳定组合
requirements = python3,kivy==2.3.0,requests,certifi
orientation = portrait
android.permissions = INTERNET,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE
android.api = 31
android.minapi = 21
android.ndk = 23c
android.private_storage = True
# 策略：先打单架构，确保内存不溢出，拿到第一个 APK
android.archs = arm64-v8a
p4a.branch = release-2024.01.21

[buildozer]
log_level = 2
warn_on_root = 1
bin_dir = ./bin
