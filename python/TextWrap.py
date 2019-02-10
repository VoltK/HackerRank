

def wrap(string, max_width):
    return "\n".join(string[c:c+max_width] for c in range(0,len(string),max_width))

