def colorOutput(color, text):
    COLORS = {
        "BLACK":           "\x1b[30m",
        "LIGHTBLUE_EX":    "\x1b[94m",
        "LIGHTWHITE_EX":   "\x1b[97m",
        "WHITE":           "\x1b[37m",
        "BLUE":            "\x1b[34m",
        "LIGHTCYAN_EX":    "\x1b[96m",
        "LIGHTYELLOW_EX":  "\x1b[93m",
        "YELLOW":          "\x1b[33m",
        "CYAN":            "\x1b[36m",
        "LIGHTGREEN_EX":   "\x1b[92m",
        "MAGENTA":         "\x1b[35m",
        "GREEN":           "\x1b[32m",
        "LIGHTMAGENTA_EX": "\x1b[95m",
        "RED":             "\x1b[31m",
        "LIGHTBLACK_EX":   "\x1b[90m",
        "LIGHTRED_EX":     "\x1b[91m",
        "RESET":           "\x1b[39m"
    }

    return f"{COLORS[color]}{text}{COLORS['RESET']}"
