[app]
title = Shuxin AI - Hologram Security
package.name = shuxinai
package.domain = id.shuxin
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1.0
requirements = python3,kivy==2.3.0
orientation = portrait
fullscreen = 0

android.permissions = INTERNET
android.api = 33
android.minapi = 24
android.ndk = 25b
android.accept_sdk_license = True
android.archs = arm64-v8a
android.private_storage = True

[buildozer]
log_level = 2
warn_on_root = 1
