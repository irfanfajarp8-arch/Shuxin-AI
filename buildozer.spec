[app]
title = Shuxin AI
package.name = shuxinarasipro
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1

requirements = python3, kivy==2.3.0, sqlite3, hostpython3

orientation = portrait
osx.kivy_version = 2.3.0
fullscreen = 1

android.permissions = ANSWER_PHONE_CALLS, SEND_SMS, RECEIVE_SMS, READ_PHONE_STATE
android.api = 33
android.build_tools = 33.0.0
android.minapi = 24
android.private_storage = 1
android.accept_sdk_license = True
android.archs = arm64-v8a
android.ndk = 25c
