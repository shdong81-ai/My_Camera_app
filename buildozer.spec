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
android.api = 33
android.ndk = 25b
android.private_storage = True
android.accept_sdk_license = True
#android.gradle_version = 8.0
#android.android_build_tools_version = 8.1.0
android.java_version = 17
# 1. 그래들 배포 버전을 8.0 수준으로 완전히 주소를 고정해버립니다. (가장 중요)
android.gradle_dist_link = https://services.gradle.org/distributions/gradle-8.0-all.zip

# 2. 안드로이드 빌드 툴 플러그인 버전을 안정 버전으로 다운그레이드 연동합니다.
android.gradle_dependencies = com.android.tools.build:gradle:8.0.2

[buildozer]
log_level = 2
warn_on_root = 0
