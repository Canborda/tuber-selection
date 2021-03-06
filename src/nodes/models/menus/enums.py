from enum import Enum, auto

# region FIRST level menu


class MainMenu(Enum):
    Start = auto()
    Calibration = auto()
    Classification = auto()
    Settings = auto()
    Exit = auto()

# endregion

# region SECOND level menus


class CalibrationMenu(Enum):
    Flip = auto()
    Blur = auto()
    Hue = auto()
    Region = auto()
    Save_params = auto()


class ClassificationMenu(Enum):
    Set_network = auto()
    Image_size = auto()
    Bounding_box_margin = auto()
    Show_network_summary = auto()


class SettingsMenu(Enum):
    OPTION_1 = auto()
    OPTION_2 = auto()
    OPTION_3 = auto()

# endregion

# region THIRD level menus


class HueMenu(Enum):
    Min = auto()
    Max = auto()


class RegionMenu(Enum):
    Center = auto()
    Size = auto()


class NetworkType(Enum):
    Binary_CNN = auto()
    Multiclass_CNN = auto()
    Autoencoder = auto()

# endregion
