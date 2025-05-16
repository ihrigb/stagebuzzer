import argparse
import buzzer
import display
import config
import controls
import time
import dmx
import utils
import audio
import relay
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

terminate = False

def main():
    parser = argparse.ArgumentParser(description='Stagebuzzer')
    parser.add_argument('-l', '--log-level', action='store', dest='log_level', default='INFO',
                        help='Set log level, default: \'info\'')
    parser.add_argument('-d', '--log-destination', action='store', dest='log_destination', default='',
                        help='Set log destination (file), default \'\' (stdout)')
    options = parser.parse_args()

    utils.log_setup(options.log_level, options.log_destination)

    general_config = config.GeneralConfig()
    dmx_config = config.DmxConfig()
    audio_config = config.AudioConfig()
    relay_config = config.RelayConfig()

    lcd = display.EaDip203J4Nlw()
    button_lights = display.ButtonLights()

    main_view = display.MainView(lcd, button_lights)
    menu_view = display.MenuView(lcd, button_lights)
    general_menu_view = display.GeneralMenuView(lcd, button_lights, general_config)
    dmx_menu_view = display.DmxMenuView(lcd, button_lights, dmx_config)
    dmx_menu_buzzer_1_view = display.DmxBuzzerMenuView(lcd, button_lights, "dmx_menu_buzzer_1_view", "1", dmx_config)
    dmx_menu_buzzer_2_view = display.DmxBuzzerMenuView(lcd, button_lights, "dmx_menu_buzzer_2_view", "2", dmx_config)
    audio_menu_view = display.AudioMenuView(lcd, button_lights, audio_config)
    audio_file_menu_view = display.AudioFileMenuView(lcd, button_lights, audio_config)
    relay_menu_view = display.RelayMenuView(lcd, button_lights, relay_config)
    information_menu_view = display.InformationMenuView(lcd, button_lights)

    d = display.Display(
        [main_view, menu_view, general_menu_view, dmx_menu_view, dmx_menu_buzzer_1_view, dmx_menu_buzzer_2_view,
         audio_menu_view, relay_menu_view, information_menu_view])
    c = controls.Controls(d, button_lights)

    # callbacks
    callbacks = [main_view]

    dmx_output = dmx.DmxOutput()
    dmx_callback = dmx.DmxBuzzerCallback(dmx_output, dmx_config)
    callbacks.append(dmx_callback)

    audio_callback = audio.AudioCallback(audio_config)
    callbacks.append(audio_callback)

    relay_output = relay.RelayOutput()
    relay_callback = relay.RelayCallback(relay_output, relay_config)
    callbacks.append(relay_callback)

    buzzer_core = buzzer.BuzzerCore(general_config, callbacks)

    d.start()

    while not terminate:
        time.sleep(1)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        terminate = True
    finally:
        GPIO.cleanup()

    exit(0)
