"""Holds all the bars"""
from libqtile.widget import (
    Battery,
    CPU,
    CapsNumLockIndicator,
    Clock,
    CurrentLayout,
    GroupBox,
    HDDGraph,
    Memory,
    Net,
    Prompt,
    QuickExit,
    Spacer,
    Systray,
    TextBox,
    Volume,
    WindowName,
)

from libqtile.bar import Bar, STRETCH

def autorandr(config):
    from libqtile import qtile
    qtile.cmd_spawn(f"/opt/qtile/bin/autorandr {config}")

def get_top_bar():
    current_layout = CurrentLayout()
    system_tray = Systray()
    capslock_numlock_indicator = CapsNumLockIndicator()
    cpu_indicator = CPU()
    memory_indicator = Memory()
    hdd_indicator = HDDGraph()
    volume_control = Volume(cardid="1")
    autorandr_home_button = TextBox(text="HOME", mouse_callbacks={"Button1": lambda: autorandr("home")})
    autorandr_external_button = TextBox(text="EXT", mouse_callbacks={"Button1": lambda: autorandr("external")})
    autorandr_mobile_button = TextBox(text="MOBILE", mouse_callbacks={"Button1": lambda: autorandr("mobile")})

    network_indicator = Net()

    default_size = 24

    default_top_bar = Bar(
        [
            current_layout,
            Spacer(length=10),
            autorandr_home_button,
            autorandr_external_button,
            autorandr_mobile_button,
            Spacer(length=STRETCH),
            TextBox(text="CPU:"),
            cpu_indicator,
            TextBox(text="Memory:"),
            memory_indicator,
            TextBox(text="HDD:"),
            hdd_indicator,
            system_tray,
            TextBox(text="Net:"),
            network_indicator,
            TextBox(text="Vol:"),
            volume_control,
            capslock_numlock_indicator,
        ],
        default_size,
    )
    return default_top_bar


def get_bottom_bar():
    group_box = GroupBox(
        active="FFFFFF",
        inactive="888888",
        # this_screen_border="007700",
        this_current_screen_border="770000",
        # other_current_screen_border="215578",
        # other_screen_border="0215578",
        use_mouse_wheel=False,
        highlight_method="block",
        default_font="serif",
    )
    window_name = WindowName()
    clock_widget = Clock(format="%Y-%m-%d %a %I:%M %p")
    quick_exit = QuickExit()

    # TODO: Only add this if this is a laptop, control through config.
    battery_indicator = Battery()

    default_size = 24

    default_bottom_bar = Bar(
        [
            group_box,
            window_name,
            clock_widget,
            TextBox(text="Battery ["),
            battery_indicator,
            TextBox(text="]"),
            quick_exit,
        ],
        default_size,
    )
    return default_bottom_bar
