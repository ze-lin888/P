[app]
title = My Music Player
package.name = losslessplayer
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas

# 1. 必须有明确版本号，解决之前日志报的 version 缺失
version = 0.1

# 2. 这里的依赖要精简，sqlite3 必须加上
requirements = python3,kivy==2.3.0,sqlite3

orientation = portrait

# 3. 权限必须给够，日志里显示读写外部存储是必须的
android.permissions = INTERNET, READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE

# 4. 安卓工具链版本（根据你的日志环境对齐）
android.api = 33
android.minapi = 21
android.ndk = 25b
android.private_storage = True

# 5. 锁定 64 位架构，避免 32 位引起的链接库丢失
android.archs = arm64-v8a

[buildozer]
log_level = 2
warn_on_root = 1
bin_dir = ./bin
