[app]
title = My Camera App
package.name = mycameraapp
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy

orientation = portrait
fullscreen = 1

# Android 패키징 상세 가이드 버전 지정
android.api = 34
android.ndk = 25b
android.private_storage = True
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 0
