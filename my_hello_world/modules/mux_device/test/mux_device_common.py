# © 2010 Intel Corporation

import simics

# Extend this function if your device requires any additional attributes to be
# set. It is often sensible to make additional arguments to this function
# optional, and let the function create mock objects if needed.
def create_mux_device(name = None):
    '''Create a new mux_device object'''
    mux_device = simics.pre_conf_object(name, 'mux_device')
    simics.SIM_add_configuration([mux_device], None)
    return simics.SIM_get_object(mux_device.name)
