[app]
title = Shuxin AI Proteksi
package.name = shuxinarasipro
package.domain = org.irfan.shuxinpro
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.1

requirements = python3,kivy

orientation = portrait
fullscreen = 0

android.permissions = ANSWER_PHONE_CALLS, CALL_PHONE, READ_PHONE_STATE, MODIFY_AUDIO_SETTINGS
android.api = 33
android.build_tools = 33.0.0
android.minapi = 21
android.ndk_api = 21
android.private_storage = 1

[buildozer]
log_level = 2
warn_on_root = 1
