[app]

# (str) Title of your application
title = Lossless Music Player

# (str) Package name
package.name = losslessplayer

# (str) Package domain (needed for android packaging)
package.domain = org.test

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (str) Application version (必须有这一行！)
version = 0.1

# (list) Application requirements
# 锁定版本，确保环境稳定
requirements = python3,kivy==2.3.0,hostpython3

# (str) Supported orientation (landscape, portrait or all)
orientation = portrait

# (list) Permissions
android.permissions = INTERNET, READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE

# (int) Target Android API
android.api = 33

# (int) Minimum API your APK will support
android.minapi = 21

# (str) Android NDK version to use
android.ndk = 25b

# (bool) Use --private data storage (True) or --dir public storage (False)
android.private_storage = True

# (list) Android architectures to build for
# 只编译 64 位，速度最快，成功率最高
android.archs = arm64-v8a

# (bool) Allow versioning from git
android.allow_skip_setup_py = True

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug)
log_level = 2

# (int) Display warning if buildozer is run as root
warn_on_root = 1

# (str) Path to bin directory
bin_dir = ./bin
