# These and other macros are documented in dhd/droid-hal-device.inc
# Feel free to cleanup this file by removing comments, once you have memorised them ;)

%define device Z01R
%define vendor asus

%define rpm_device 5z
%define rpm_vendor asus

%define vendor_pretty ASUS
%define device_pretty Zenfone 5z

%define installable_zip 1
%define droid_target_aarch64 1

%define android_config \
#define WANT_ADRENO_QUIRKS 1\
%{nil}

%include rpm/dhd/droid-hal-device.inc

# IMPORTANT if you want to comment out any macros in your .spec, delete the %
# sign, otherwise they will remain defined! E.g.:
#define some_macro "I'll not be defined because I don't have % in front"

