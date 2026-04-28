[app]
title = MyMusicPlayer
package.name = losslessplayer
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy,sqlite3,requests
orientation = portrait
android.permissions = INTERNET, READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE
android.api = 31
android.minapi = 21
android.ndk = 23c
android.private_storage = True
android.archs = arm64-v8a
p4a.branch = master
[buildozer]
log_level = 2
warn_on_root = 1
bin_dir = ./bin
