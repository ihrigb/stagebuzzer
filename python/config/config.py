from usbdrive import File


class GeneralConfig:
    _hold_time = 10

    def set_hold_time(self, hold_time: int):
        if 0 < hold_time <= 99:
            self._hold_time = hold_time

    def get_hold_time(self) -> int:
        return self._hold_time


class BaseConfig:
    _active = True

    def activate(self):
        self._active = True

    def deactivate(self):
        self._active = False

    def set_active(self, active: bool):
        if active:
            self.activate()
        else:
            self.deactivate()

    def get_active(self):
        return self._active


class AudioConfig(BaseConfig):
    _audio_file: File = None

    def set_audio_file(self, audio_file: File):
        self._audio_file = audio_file

    def get_audio_file(self) -> File:
        return self._audio_file


class DmxConfig(BaseConfig):

    def __init__(self):
        self._addresses = dict()
        self._addresses["1"] = 1
        self._addresses["2"] = 2
        self._values = dict()
        self._values["1"] = 255
        self._values["2"] = 255

    def get_dmx_address(self, name: str) -> int:
        return self._addresses.get(name)

    def set_dmx_address(self, name: str, address: int):
        if address == 0:
            self._addresses[name] = 512
        elif address == 513:
            self._addresses[name] = 1
        elif 1 <= address <= 512:
            self._addresses[name] = address

    def get_dmx_value(self, name: str) -> int:
        return self._values.get(name)

    def set_dmx_value(self, name: str, value: int):
        if value == -1:
            self._values[name] = 255
        elif value == 256:
            self._values[name] = 0
        if 0 <= value <= 255:
            self._values[name] = value


class RelayConfig(BaseConfig):
    pass


class Config:
    general: GeneralConfig = GeneralConfig()
    audio: AudioConfig = AudioConfig()
    dmx: DmxConfig = DmxConfig()
    relay: RelayConfig = RelayConfig()

    def general(self):
        return self.general

    def audio(self):
        return self.audio

    def dmx(self):
        return self.dmx

    def relay(self):
        return self.relay
