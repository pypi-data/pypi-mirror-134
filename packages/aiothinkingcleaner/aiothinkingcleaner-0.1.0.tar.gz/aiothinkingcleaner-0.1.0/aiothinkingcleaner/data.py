from enum import Enum


class TCCommand(Enum):
    """Enum of commands available."""

    CLEAN = "clean"
    MAX = "max"
    DELAYED_CLEAN = "delayedclean"
    SPOT = "spot"
    DOCK = "dock"
    FIND_ME = "find_me"
    STOP = "stop"
    EXIT_DOCK = "leavehomebase"
    POWER_OFF = "poweroff"


class TCDeviceState(Enum):
    """Current device state of the Roomba."""

    BASE = "st_base"
    BASE_RECON = "st_base_recon"
    BASE_FULL = "st_base_full"
    BASE_TRICKLE = "st_base_trickle"
    BASE_WAIT = "st_base_wait"
    PLUG = "st_plug"
    PLUG_RECON = "st_plug_recon"
    PLUG_FULL = "st_plug_full"
    PLUG_TRICKLE = "st_plug_trickle"
    PLUG_WAIT = "st_plug_wait"
    STOPPED = "st_stopped"
    CLEANING = "st_clean"
    SPOT_CLEANING = "st_clean_spot"
    MAX_CLEANING = "st_clean_max"
    DOCKING = "st_dock"
    PICK_UP = "st_pickup"
    REMOTE = "st_remote"
    WAIT = "st_wait"
    OFF = "st_off"
    CLEAN_STOP = "st_cleanstop"
    LOCATE = "st_locate"
    UNKNOWN = "st_unknown"
    ERROR_CHARGE = "error_charge"
    ERROR_LEFT_L = "error_left_l"
    ERROR_RIGHT_L = "error_right_l"
    ERROR_CLIFF = "error_cliff"
    ERROR_LEFT_W = "error_left_w"
    ERROR_RIGHT_W = "error_right_w"
    ERROR_BRUSH = "error_brush"
    ERROR_SIDE = "error_side"
    ERROR = "error"
    OFFLINE = "offline"


class TCDeviceStatus:
    """Current status of the Roomba."""

    name: str
    """The name of the device."""

    battery_charge: float
    """The battery percentage (between 0 and 100)."""

    capacity: int
    """The current battery capacity in mAh."""

    state: TCDeviceState
    """The current state of the Roomba."""

    is_cleaning: bool
    """True when the Roomba is currently cleaning."""

    is_near_homebase: bool
    """True when the Roomba has visual contact with a homebase."""

    def __init__(
        self,
        name: str,
        battery_charge: float,
        capacity: int,
        cleaner_state: str,
        cleaning: str,
        near_homebase: str,
    ) -> None:
        self.name = name
        self.battery_charge = battery_charge
        self.capacity = capacity
        self.state = TCDeviceState(cleaner_state)
        self.is_cleaning = cleaning == "1"
        self.is_near_homebase = near_homebase == "1"
