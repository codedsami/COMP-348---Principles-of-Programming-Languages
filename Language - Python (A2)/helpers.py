def safe_int(val, default=0):
    """
    Safely convert a value to an integer.

    Args:
        val: The value to convert.
        default (int, optional): The value to return if conversion fails. Defaults to 0.

    Returns:
        int: The converted integer or the default if conversion fails.
    """
    
    try:
        return int(val)
    except (ValueError, TypeError):
        return default

def safe_float(val, default=0.0):
    """
    Safely convert a value to a float.

    Args:
        val: The value to convert.
        default (float, optional): The value to return if conversion fails. Defaults to 0.0.

    Returns:
        float: The converted float or the default if conversion fails.
    """
    try:
        return float(val)
    except (ValueError, TypeError):
        return default
