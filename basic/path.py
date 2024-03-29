def node_path(node):
    path = [node.state]

    while node.parent_node is not None:
        path.append(node.state)
        node = node.parent_node
    
    path.reverse()

    return path

def edge_path(node):
    path = []

    while node.parent_node is not None:
        if node.edge is not None:
            path.append(node.edge)
        node = node.parent_node

    path.reverse()

    return path