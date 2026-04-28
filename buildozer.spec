[app]
title = My Music Player
package.name = losslessplayer
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy==2.3.0,sqlite3,requests
orientation = portrait
android.permissions = INTERNET, READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE
android.api = 33
android.minapi = 21
android.ndk = 25c
android.private_storage = True
android.archs = arm64-v8a

[buildozer]
log_level = 2
warn_on_root = 1
bin_dir = ./bin
