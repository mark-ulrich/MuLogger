"""
Console MuLogger functions
"""

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

# TODO: Find a better way than just exposing this to the importing module
log_to_file: bool = False

log_file: str = "log.txt"
log_level: int = LOG_LEVEL_INFO
log_use_colors: bool = True


# TODO: DRY this code up


def generate_log_str(msg: any, level: int, use_colors: bool = False) -> str:
    """Generate log string"""
    if not isinstance(msg, str):
        msg = str(msg)
    log_str = f"{PREFIXES[level]} {msg}"
    if use_colors:
        log_str = f"\033{COLOR_CODES[level]}{log_str}\033[0m"
    return log_str


def set_log_level(level: int) -> None:
    """Set log level"""
    global log_level
    log_level = level


def log(level: int, msg: any) -> None:
    """Log message"""
    global log_level
    if level < log_level:
        return
    if log_to_file:
        with open(log_file, "a") as f:
            f.write(generate_log_str(msg, LOG_LEVEL_INFO))
    else:
        print(generate_log_str(msg, level, log_use_colors))


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
