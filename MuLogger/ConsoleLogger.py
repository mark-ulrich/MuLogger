"""
Console MuLogger functions
"""
from io import TextIOWrapper

# TODO: Buffer log messages and write them to file in a separate thread

LOG_LEVEL_DEBUG = 0x00
LOG_LEVEL_INFO = 0x01
LOG_LEVEL_VERBOSE = 0x02
LOG_LEVEL_WARNING = 0x03
LOG_LEVEL_ERROR = 0x04
LOG_LEVEL_FATAL = 0x05

COLOR_CODES = {
    LOG_LEVEL_DEBUG: "\033[93m",
    LOG_LEVEL_INFO: "\033[92m",
    LOG_LEVEL_VERBOSE: "\033[93m",
    LOG_LEVEL_WARNING: "\033[93m",
    LOG_LEVEL_ERROR: "\033[91m",
    LOG_LEVEL_FATAL: "\033[91m",
}

PREFIXES = {
    LOG_LEVEL_DEBUG: "[D]",
    LOG_LEVEL_INFO: "[+]",
    LOG_LEVEL_VERBOSE: "[+]",
    LOG_LEVEL_WARNING: "[!]",
    LOG_LEVEL_ERROR: "[!]",
    LOG_LEVEL_FATAL: "[!]",
}

config = {
    "log_to_file": False,
    "log_file_path": "log.txt",
    "log_level": LOG_LEVEL_INFO,
    "log_use_colors": True,
}

log_file: (TextIOWrapper, None) = None


def initialize(
    log_level: int = LOG_LEVEL_INFO,
    log_to_file: bool = False,
    log_file_path: str = "log.txt",
    color: bool = False,
) -> None:
    """Initialize the logger"""
    global config
    config["log_level"] = log_level
    config["log_to_file"] = log_to_file
    config["log_file_path"] = log_file_path
    config["log_use_colors"] = color
    if log_to_file:
        global log_file
        log_file = open(log_file_path, "w")


def close() -> None:
    """Close the logger"""
    global log_file
    if log_file and isinstance(log_file, TextIOWrapper) and not log_file.closed:
        log_file.close()


def generate_log_str(msg: any, level: int, use_color: bool) -> str:
    """Generate log string"""
    if not isinstance(msg, str):
        msg = str(msg)
    log_str = f"{PREFIXES[level]} {msg}"
    if use_color:
        log_str = f"\033{COLOR_CODES[level]}{log_str}\033[0m"
    return log_str


def set_log_level(level: int) -> None:
    """Set log level"""
    global config
    config["log_level"] = level


def log(level: int, msg: any) -> None:
    """Log message"""
    global config
    if level < config["log_level"]:
        return
    if config["log_to_file"]:
        if not log_file or not isinstance(log_file, TextIOWrapper):
            raise Exception("Log file not initialized")
        log_file.write(generate_log_str(msg, level, use_color=False) + "\n")
    print(generate_log_str(msg, level, config["log_use_colors"]))


def log_info(msg: any) -> None:
    """Log info message"""
    log(LOG_LEVEL_INFO, msg)


def log_warning(msg: any) -> None:
    """Log warning message"""
    log(LOG_LEVEL_WARNING, msg)


def log_error(msg: any) -> None:
    """Log error message"""
    log(LOG_LEVEL_ERROR, msg)


def log_fatal(msg: any) -> None:
    """Log fatal message"""
    log(LOG_LEVEL_FATAL, msg)
    # sys.exit()


def log_debug(msg: any) -> None:
    """Log debug message"""
    log(LOG_LEVEL_DEBUG, msg)


def log_verbose(msg: any) -> None:
    """Log verbose message"""
    log(LOG_LEVEL_VERBOSE, msg)
