def suggest_maneuver(position):
    """
    Simple AI rule to change orbit altitude slightly to avoid collision.
    """
    # Simple upward bump to avoid collision
    x, y, z = position
    return (x + 5, y, z + 5)
