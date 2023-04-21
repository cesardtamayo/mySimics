# © 2010 Intel Corporation

import dev_util
import conf
import stest
import mux_device_common

# Create an instance of the device to test
# dev = mux_device_common.create_mux_device()
dev = pre_conf_object('dev', 'mux_device')
SIM_add_configuration([dev], None)
dev = conf.dev

# Create a register wrapper for the register
r = dev_util.Register_LE((dev, 'regs', 0))

# Test taht reading from register returns 42
stest.expect_equal(r.read(), 42)

# even if we write something else to it:
r.write(0x4711)
stest.expect_equal(r.read(), 42)

