import buzzer
import dmx

buzzer_1_name: str = "buzzer_1"
buzzer_2_name: str = "buzzer_2"


def config():
    dmx_output = dmx.DmxOutput
    dmx_buzzer_config_1 = dmx.BuzzerDmxCallbackConfiguration(channel=1, value=255)
    dmx_buzzer_config_2 = dmx.BuzzerDmxCallbackConfiguration(channel=2, value=255)
    dmx_config = dmx.DmxCallbackConfiguration({buzzer_1_name: dmx_buzzer_config_1, buzzer_2_name: dmx_buzzer_config_2})
    dmx_callback = dmx.DmxBuzzerCallback(output=dmx_output, config=dmx_config)

    buzzer_1 = buzzer.Buzzer(name=buzzer_1_name)
    buzzer_2 = buzzer.Buzzer(name=buzzer_2_name)

    buzzer_1.register_buzzer_callback(dmx_callback)
    buzzer_2.register_buzzer_callback(dmx_callback)


class InitConfig:
    pass
