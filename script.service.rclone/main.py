#!/usr/bin/python3.4
import os, sys, xbmc, time, stat, xbmcvfs, xbmcaddon

src = os.path.join(xbmcaddon.Addon().getAddonInfo('path'), 'rclone-android-16-arm')
loc = xbmcvfs.translatePath("special://xbmcbin/../../../cache/lib/rclone-android-16-arm")

if not xbmcvfs.exists(loc):
    xbmcvfs.copy(src, loc)
    st = os.stat(loc)
    os.chmod(loc, st.st_mode | stat.S_IEXEC)

loc2 = xbmcvfs.translatePath("special://masterprofile/rclone.conf")
pidfile  = xbmcvfs.translatePath("special://temp/librclone.pid")
logfile  = xbmcvfs.translatePath("special://temp/librclone.log")
cachepath  = xbmcvfs.translatePath("special://temp")

while True:
    os.popen(loc + " serve webdav <insert your remote here>: --addr :23457 --config " + loc2 + " --log-file=" + logfile + " --dir-cache-time 2400h --poll-interval 10m")
    break
