# directions
UP = 1
RIGHT = 2
DOWN = 3
LEFT = 4
DS = (UP, RIGHT, DOWN, LEFT)

# margins
MX = 10
MY = 10

# padding
PX = 4
PY = 4

# cells
CW = 82
CH = 82

# displace
DX = 2
DY = 6

# velocity
TIME_INTERVAL = 0.5

WALL_IMAGE = 0
SPACE_IMAGE = 1
FOOD_IMAGE = 2
TRACE_IMAGE = 3

MAZE_MAP = [
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0],
     [0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 2],
     [0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0],
     [0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0],
     [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0],
     [0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

START_POS = (1, 6)
FINISH_POS = (14, 2)

ROWS = len(MAZE_MAP)
COLS = len(MAZE_MAP[0])

W_CANVAS = COLS*CW + 2*MX + 2*PX
H_CANVAS = ROWS*CH + 2*MY + 2*PY
