import display
import config
import keyboard

general_config = config.GeneralConfig()
dmx_config = config.DmxConfig()
audio_config = config.AudioConfig()
relay_config = config.RelayConfig()

main_view = display.MainView()
menu_view = display.MenuView()
general_menu_view = display.GeneralMenuView(general_config)
dmx_menu_view = display.DmxMenuView(dmx_config)
dmx_menu_buzzer_1_view = display.DmxBuzzerMenuView("dmx_menu_buzzer_1_view", "1", dmx_config)
dmx_menu_buzzer_2_view = display.DmxBuzzerMenuView("dmx_menu_buzzer_2_view", "2", dmx_config)
audio_menu_view = display.AudioMenuView(audio_config)
audio_file_menu_view = display.AudioFileMenuView(audio_config)
relay_menu_view = display.RelayMenuView(relay_config)
d = display.Display(
    [main_view, menu_view, general_menu_view, dmx_menu_view, dmx_menu_buzzer_1_view, dmx_menu_buzzer_2_view,
     audio_menu_view, audio_file_menu_view, relay_menu_view])


def esc(e):
    d.esc()


def ok(e):
    d.ok()


def up(e):
    d.up()


def down(e):
    d.down()


def main():
    keyboard.on_press_key("left", esc)
    keyboard.on_press_key("right", ok)
    keyboard.on_press_key("up", up)
    keyboard.on_press_key("down", down)
    keyboard.wait()


if __name__ == "__main__":
    main()