class Tile:
    """
    Tile on the map. 
    May or may not be blocked.
    May or may not block sight.
    """
    def __init__(self, blocked, block_sight=None):
        self.blocked = blocked

        # Defaults to same value as blocked, if blocked it blocks sight
        if block_sight is None:
            block_sight = blocked

        self.block_sight = block_sight