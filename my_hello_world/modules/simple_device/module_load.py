# © 2010 Intel Corporation

import cli

class_name = 'simple_device'

#
# ------------------------ info -----------------------
#

def get_info(obj):
    # USER-TODO: Return something useful here
    return [("Info",
             [("Description", obj.class_desc)])]

cli.new_info_command(class_name, get_info)

#
# ------------------------ status -----------------------
#

def get_status(obj):
    # USER-TODO: Return something useful here    
    return [("Attributes",
                [
                    ("reads_count", obj.reads_count),
                    ("register_selection", obj.register_selection)
                ]),
            ("Register Bank", 
                [
                    ("inputRegister0", obj.regs_inputRegister0),
                    ("inputRegister1", obj.regs_inputRegister1),
                    ("inputRegister2", obj.regs_inputRegister2),
                    ("inputRegister3", obj.regs_inputRegister3),
                    ("outputRegister", obj.regs_outputRegister)
                ]
            )]
                                  

cli.new_status_command(class_name, get_status)
