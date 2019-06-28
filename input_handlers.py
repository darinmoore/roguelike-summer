import tcod

def handle_keys(key):
    # Movements
    if key.vk == tcod.KEY_UP:
        return {'move' : (0, -1)}
    if key.vk == tcod.KEY_DOWN:
        return {'move' : (0, 1)}
    if key.vk == tcod.KEY_LEFT:
        return {'move' : (-1, 0)}
    if key.vk == tcod.KEY_RIGHT:
        return {'move' : (1, 0)}

    # Fullscreen toggle
    if key.vk == tcod.KEY_ENTER and key.lalt:
        return {'fullscreen' : True}

    # Exit game
    if key.vk == tcod.KEY_ESCAPE:
        return {'exit' : True}
    
    return {}
    