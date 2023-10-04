def breadth_first_search(graph, start_node, target_node):
    # Initialisation
    queue = [start_node]
    discovered = [start_node]
    neighbours = []
    found = False

    # Repeat while there are items in the queue
    # and the target node has not been found
    while len(queue) != 0 and found == False:

        # Set the current node to the first item in the queue
        current_node = queue[0]

        # Remove the current node from the start of the queue
        queue = queue[1:]

        # Get the current node's list of neighbours
        neighbours = graph[current_node]

        # Repeat for each node in the neighbours list
        for node in neighbours:  # this line will check the neighbours of the current node
            # Check if the node has not already been discovered
            if node not in discovered:
                # Check if the target node has been found
                if node == target_node:
                    found = True
                else:
                    # Add the node to the stack
                    # and to the discovered list
                    queue.append(node)
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

    print(breadth_first_search(dict, "1", "8"))