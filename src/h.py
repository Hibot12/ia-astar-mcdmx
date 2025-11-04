m = {}

def h(c: int, t: int) -> int:
    if c == t:
        return 0
    
    return m[c][t]
