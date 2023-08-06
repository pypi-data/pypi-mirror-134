import cmd, sys
from typing import Optional

from hv.hv_device import HVDevice, create_test_device


def device_info(device: HVDevice):
    return str(device.device) + "\n" + str(device.data)


class HVShell(cmd.Cmd):
    intro = """Welcome to the HV-controls shell.
Type help or ? to list commands, and Ctrl+D to exit.
Type list for get list of device and nextly attach device
"""
    _empty_promt = '(HV-controls): '
    prompt = _empty_promt

    device : Optional[HVDevice] = None
    devices = []

    def __init__(self, args):
        super(HVShell, self).__init__()
        self.args = args

    def preloop(self) -> None:
        if self.args.fake_device:
            self.devices = [create_test_device()]
        else:
            self.devices = HVDevice.find_all_devices()

    def do_list(self, arg):
        "Print list of all devices."
        for i, dev in enumerate(self.devices):
            print("Device ID: {}".format(i))
            print(device_info(dev))

    def do_attach(self, arg):
        'Attach to device by ID: attach 0'
        try:
            device_id = int(arg[0])
            if len(self.devices) > device_id:
                self.device = self.devices[device_id]
                self.device.open()
                self.prompt = '({}): '.format(self.device.device)
                return
        except Exception:
            print("Bad device ID")

    def do_detach(self, arg):
        "Detach device from shell."
        self.device.close()
        self.device = None
        self.prompt = self._empty_promt

    def do_setup(self, arg):
        'Setup the voltage:  setup 1500'
        try:
            voltage = float(arg[0])
            if self.device is not None:
                self.device.set_value(voltage)
        except Exception:
            pass
        finally:
            print("Bad voltage")

    def do_apply(self, arg):
        'Apply the established voltage.'
        if self.device is not None:
            self.device.update_value()

    def do_reset(self, arg):
        'Turn off.'
        if self.device is not None:
            self.device.reset_value()

    def do_get(self, arg):
        "Get voltage and current"
        if self.device is not None:
            I, U = self.device.get_IU()
            print("I = {}, U = {}".format(I, U))

    def do_exit(self, arg):
        self.close()
        sys.exit()

    def do_eof(self, arg):
        self.close()
        sys.exit()

    def precmd(self, line):
        line = line.lower()
        return line

    def close(self):
        for dev in list(self.devices):
            dev.close()
            self.devices.remove(dev)

    def parse(arg):
        'Convert a series of zero or more numbers to an argument tuple'
        return tuple(map(int, arg.split()))

if __name__ == '__main__':
    try:
        shell = HVShell()
        shell.cmdloop()
    finally:
        shell.close()