def guide(player, board):
    d_new = player.direction
    p_new = player.move_pos(d_new)
    if board.check(p_new):
        return player.d

    while True:
        d_new = player.turn_left(d_new)
        p_new = player.move_pos(d_new)
        if board.check(p_new):
            return d_new


