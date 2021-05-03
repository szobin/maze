def guide(player, board):
    # try to turn left
    d_new = player.turn_left()
    p_new = player.move_pos(d_new)
    if board.check(p_new):
        return d_new

    # try to go forward
    d_new = player.direction
    p_new = player.move_pos(d_new)
    if board.check(p_new):
        return d_new

    # try to turn right
    d_new = player.turn_right()
    p_new = player.move_pos(d_new)
    if board.check(p_new):
        return d_new

    # try to turn over
    d_new = player.turn_right(d_new)
    p_new = player.move_pos(d_new)
    if board.check(p_new):
        return d_new

    return None


