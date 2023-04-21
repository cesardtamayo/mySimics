# © 2010 Intel Corporation

import cli

class_name = 'plugin_device'

#
# ------------------------ info -----------------------
#

def get_info(obj):
    # USER-TODO: Return something useful here
    return []

cli.new_info_command(class_name, get_info)

#
# ------------------------ status -----------------------
#

def get_status(obj):
    # USER-TODO: Return something useful here
    return [
            ("Attributes",[
                ("mySignal", obj.mySignal)
                ]
            ), 
            ("Registers",[
                ("Bus", obj.regs_bus)
                ]
            )]

cli.new_status_command(class_name, get_status)
