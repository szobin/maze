import random


def guide(player, board):
    d_new = player.direction
    p_new = player.move_pos(d_new)
    if board.check(p_new):
        return player.d

    turn = random.choice((player.turn_left, player.turn_right))
    while True:
        d_new = turn(d_new)
        p_new = player.move_pos(d_new)
        if board.check(p_new):
            return d_new



