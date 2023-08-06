ESC = '\x1b'

def RGB(r: int = 0, g: int = 0, b: int = 0) -> str:
    return ESC + f'[38;2;{r};{g};{b}m'

Default = ESC + '[5;39m'

Black   = ESC + '[38;5;0m'
Red     = ESC + '[38;5;1m'
Green   = ESC + '[38;5;2m'
Yellow  = ESC + '[38;5;3m'
Blue    = ESC + '[38;5;4m'
Magenta = ESC + '[38;5;5m'
Cyan    = ESC + '[38;5;6m'
White   = ESC + '[38;5;7m'

BrightBlack   = ESC + '[38;5;8m'
BrightRed     = ESC + '[38;5;9m'
BrightGreen   = ESC + '[38;5;10m'
BrightYellow  = ESC + '[38;5;11m'
BrightBlue    = ESC + '[38;5;12m'
BrightMagenta = ESC + '[38;5;13m'
BrightCyan    = ESC + '[38;5;14m'
BrightWhite   = ESC + '[38;5;15m'