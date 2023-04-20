# © 2010 Intel Corporation

import simics

# Extend this function if your device requires any additional attributes to be
# set. It is often sensible to make additional arguments to this function
# optional, and let the function create mock objects if needed.
def create_plugin_module(name = None):
    '''Create a new plugin_module object'''
    plugin_module = simics.pre_conf_object(name, 'plugin_module')
    simics.SIM_add_configuration([plugin_module], None)
    return simics.SIM_get_object(plugin_module.name)
