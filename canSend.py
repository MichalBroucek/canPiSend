#!/usr/bin/env python3

import sys
import src.param
import src.can_simulator


# TODO:
# 1) needs to do heavy refactoring - new project!
# 2) do proper argparse module
# 3) add interface for ZF - generate messages (you'll need 2 buffers - to keep sending messages and update them latter)
# 4) control it via cmd + clever output on cmd (not just simple print out!)
# 5) Add simple GUI (on rpi directly)
# 6) Add Android App to control Rpi via mobile phone
# 7) Have fun ...

can_interface = 'vcan0'
#can_interface = 'can0'

if __name__ == "__main__":
    param = src.param.Param()
    simulator_parameters = param.parse_cmd_params(sys.argv)

    if simulator_parameters is None:
        exit()

    simulator = src.can_simulator.CanSimulator(simulator_parameters, can_interface)
    simulator.run_action()

    print("- Done -")
