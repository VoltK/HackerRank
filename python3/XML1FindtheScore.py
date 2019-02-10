

def get_attr_number(node):
    # your code goes here
    counter = 0
    for child in node.iter():
        counter += len(child.attrib)
    return counter




