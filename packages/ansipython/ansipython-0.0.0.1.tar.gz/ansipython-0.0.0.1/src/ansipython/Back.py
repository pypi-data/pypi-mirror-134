ESC = '\x1b'

def RGB(r: int = 0, g: int = 0, b: int = 0) -> str:
    return ESC + f'[48;2;{r};{g};{b}m'

Default = ESC + '[5;49m'

Black   = ESC + '[48;5;0m'
Red     = ESC + '[48;5;1m'
Green   = ESC + '[48;5;2m'
Yellow  = ESC + '[48;5;3m'
Blue    = ESC + '[48;5;4m'
Magenta = ESC + '[48;5;5m'
Cyan    = ESC + '[48;5;6m'
White   = ESC + '[48;5;7m'

BrightBlack   = ESC + '[48;5;8m'
BrightRed     = ESC + '[48;5;9m'
BrightGreen   = ESC + '[48;5;10m'
BrightYellow  = ESC + '[48;5;11m'
BrightBlue    = ESC + '[48;5;12m'
BrightMagenta = ESC + '[48;5;13m'
BrightCyan    = ESC + '[48;5;14m'
BrightWhite   = ESC + '[48;5;15m'