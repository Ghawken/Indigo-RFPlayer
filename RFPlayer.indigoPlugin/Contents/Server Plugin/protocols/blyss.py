#! /usr/bin/env python
# -*- coding: utf-8 -*-

class Blyss(object):

    @classmethod
    def getAddress(cls, frameData):
        return "BLYSS-" + frameData['infos']['id']

    
    def __init__(self, device):
        self.logger = logging.getLogger("Plugin.Blyss")
        self.device = device
        self.logger.debug(u"%s: Starting Blyss device" % device.name)

    def handler(self, player, frameData):

        devAddress = "BLYSS-" + frameData['infos']['id']
        self.logger.threaddebug(u"%s: Sensor Blyss received: %s" % (player.device.name, devAddress))

