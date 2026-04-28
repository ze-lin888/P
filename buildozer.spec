[app]

# 项目基本信息
title = Lossless Music Player
package.name = losslessplayer
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas

# 版本号 (之前报错的核心点)
version = 0.1

# 依赖库锁定
requirements = python3,kivy==2.3.0

# 屏幕设置与权限
orientation = portrait
android.permissions = INTERNET, READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE

# 安卓工具链配置
android.api = 33
android.minapi = 21
android.ndk = 25b
android.private_storage = True

# 架构锁定 (仅 arm64-v8a，提高成功率与速度)
android.archs = arm64-v8a

[buildozer]

# 日志与输出配置
log_level = 2
warn_on_root = 1
bin_dir = ./bin
