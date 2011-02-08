#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import time
import OpenRTM_aist
import RTC
 
consoleout_spec = ["implementation_id", "ConsoleOut",
                  "type_name",         "ConsoleOut",
                  "description",       "Console output component",
                  "version",           "1.0",
                  "vendor",            "sample",
                  "category",          "example",
                  "activity_type",     "DataFlowComponent",
                  "max_instance",      "10",
                  "language",          "Python",
                  "lang_type",         "script",
                  ""]
 
class ConsoleOut(OpenRTM_aist.DataFlowComponentBase):
    def __init__(self, manager):
        OpenRTM_aist.DataFlowComponentBase.__init__(self, manager)
        self._data = RTC.TimedString(RTC.Time(0,0),"")
        self._inport = OpenRTM_aist.InPort("in", self._data)
    def onInitialize(self):
        # Set OutPort buffer
        self.registerInPort("in", self._inport)
        return RTC.RTC_OK
 
    def onExecute(self, ec_id):
        while self._inport.isNew():
            data = self._inport.read()
            print "command : %s" % data.data
        time.sleep(0.1)
        return RTC.RTC_OK
 
def MyModuleInit(manager):
    profile = OpenRTM_aist.Properties(defaults_str=consoleout_spec)
    manager.registerFactory(profile,
                            ConsoleOut,
                            OpenRTM_aist.Delete)
    comp = manager.createComponent("ConsoleOut")
 
def main():
    mgr = OpenRTM_aist.Manager.init(sys.argv)
    mgr.setModuleInitProc(MyModuleInit)
    mgr.activateManager()
    mgr.runManager()
 
if __name__ == "__main__":
    main()
