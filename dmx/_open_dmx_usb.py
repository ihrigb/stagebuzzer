import pyftdi.ftdi as ftdi
import threading
import time

vendor = 0x0403
product = 0x6001


class OpenDmxUsb(threading.Thread):
    def __init__(self):
        self.baud_rate = 250000
        self.data_bits = 8
        self.stop_bits = 2
        self.parity = 'N'
        self.flow_ctrl = ''
        self.rts_state = 0
        self.channel_values = [0] * 513
        self._init_dmx()

    def _init_dmx(self):
        self.ftdi = ftdi.Ftdi()
        self.ftdi.open(vendor, product, 0)
        self.ftdi.set_baudrate(self.baud_rate)
        self.ftdi.set_line_property(self.data_bits, self.stop_bits, self.parity, break_=False)
        self.ftdi.set_flowctrl(self.flow_ctrl)
        self.ftdi.purge_rx_buffer()
        self.ftdi.purge_tx_buffer()
        self.ftdi.set_rts(self.rts_state)

    def _send_dmx(self):
        self.ftdi.write_data(self.channel_values)
        # Need to generate two bits for break
        self.ftdi.set_line_property(self.data_bits, self.stop_bits, self.parity, break_=True)
        self.ftdi.set_line_property(self.data_bits, self.stop_bits, self.parity, break_=True)
        self.ftdi.set_line_property(self.data_bits, self.stop_bits, self.parity, break_=False)

    def set_channel_values(self, channel_values):
        self.channel_values = channel_values

    def run(self) -> None:
        while True:
            self._send_dmx()
            time.sleep(0.001)
