# SonicWall SSL-VPN NetExtender NELaunchCtrl ActiveX control
# CVE-2007-5603 (AddRouteEntry)

import logging
log = logging.getLogger("Thug")

def AddRouteEntry(self, arg0, arg1):
    if len(arg0) > 20 or len(arg1) > 20:
        log.MAEC.add_behavior_warn('[SonicWall SSL-VPN NetExtender NELaunchCtrl ActiveX] Overflow in AddRouteEntry',
                                   'CVE-2007-5603')

	
