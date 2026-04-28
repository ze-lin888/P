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

# (list) Application requirements
# 核心重点：锁定版本，防止编译环境混乱
requirements = python3,kivy==2.3.0,hostpython3

# (str) Custom source folders for requirements
# 可选，如果后面要加 ffpyplayer 再改这里
# requirements.source.kivy = 

# (str) Presplash of the application
# presplash.filename = %(source.dir)s/data/presplash.png

# (str) Icon of the application
# icon.filename = %(source.dir)s/data/icon.png

# (str) Supported orientation (landscape, portrait or all)
orientation = portrait

# (list) Permissions
android.permissions = INTERNET, READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support.
android.minapi = 21

# (str) Android NDK version to use
# 锁定版本，防止 GitHub 环境乱选
android.ndk = 25b

# (bool) Use --private data storage (True) or --dir public storage (False)
android.private_storage = True

# (str) Android NDK directory (if empty, it will be automatically downloaded)
# android.ndk_path = 

# (str) Android SDK directory (if empty, it will be automatically downloaded)
# android.sdk_path = 

# (str) ANT directory (if empty, it will be automatically downloaded)
# android.ant_path = 

# (list) Android architectures to build for
# 核心重点：只编译 64 位，极大降低失败率和减少编译时间
android.archs = arm64-v8a

# (bool) Allow versioning from git
android.allow_skip_setup_py = True

# (list) The Android libs to copy in the vendor/libs dir
# android.add_libs_armeabi_v7a = libs/armeabi-v7a/*.so
# android.add_libs_arm64_v8a = libs/arm64-v8a/*.so

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = off, 1 = on)
warn_on_root = 1

# (str) Path to build artifacts (default is ./.buildozer)
# build_dir = ./.buildozer

# (str) Path to bin directory (default is ./bin)
bin_dir = ./bin
