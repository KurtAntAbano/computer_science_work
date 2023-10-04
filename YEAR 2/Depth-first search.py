def depth_first_search(graph, start_node, target_node):
    # Initialisation
    stack = [start_node]
    discovered = [start_node]
    neighbours = []
    found = False

    # Repeat while there are items in the stack
    # and the target node has not been found
    while len(stack) != 0 and found == False:

        # Pop the top item from the stack to be the current node
        current_node = stack.pop()

        # Get the current node's list of neighbours
        neighbours = graph[current_node]

        # Repeat for each node in the neighbours list
        for node in neighbours:
            # Check if the node has not already been discovered
            if node not in discovered:
                # Check if the target node has been found
                if node == target_node:
                    found = True
                else:
                    # Push the node onto the stack
                    # and add it to the discovered list
                    stack.append(node)
                    discovered.append(node)

    return found


if __name__ == "__main__":
    dict = {
        "1": ["2", "9"],
        "2": ["1"],
        "3": ["4", "5", "6", "9"],
        "4": ["3"],
        "5": ["3", "8"],
        "6": ["3", "7"],
        "7": ["6", "8", "9"],
        "8": ["5", "7"],
        "9": ["1", "3", "7"]}

    print(depth_first_search(dict, "1", "8"))