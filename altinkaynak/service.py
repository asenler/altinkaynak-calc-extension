# -*- coding: utf-8 -*-

import unohelper

from com.sun.star.task import XJobExecutor

from .update import update_current_sheet


class AltinkaynakService(unohelper.Base, XJobExecutor):

    def __init__(self, ctx):
        self.ctx = ctx

    def trigger(self, args):

        desktop = self.ctx.ServiceManager.createInstanceWithContext(
            "com.sun.star.frame.Desktop",
            self.ctx
        )

        doc = desktop.getCurrentComponent()

        update_current_sheet(doc)


g_ImplementationHelper = unohelper.ImplementationHelper()

g_ImplementationHelper.addImplementation(
    AltinkaynakService,
    "com.altinkaynak.Service",
    ("com.sun.star.task.Job",),
)
