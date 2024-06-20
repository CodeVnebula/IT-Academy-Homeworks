graph = {'A': ['B', 'C'],
        'B': ['C', 'D'],
        'C': ['D'],
        'D': ['F'],
        'E': ['F']
    }

# Python Patterns - implementing graphs modified
def check_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return True
    if start not in graph:
        return False
    for current_position in graph[start]:
        if current_position not in path:
            newpath = check_path(graph, current_position, end, path)
            if newpath:
                return True
    return False

def main():
    
    print(check_path(graph, 'F', 'A'))  # False
    print(check_path(graph, 'A', 'D'))  # True
    print(check_path(graph, 'B', 'C'))  # True
    print(check_path(graph, 'D', 'B'))  # False
    print(check_path(graph, 'C', 'D'))  # True
    print(check_path(graph, 'D', 'F'))  # True
    print(check_path(graph, 'E', 'F'))  # True
    print(check_path(graph, 'A', 'F'))  # True
    print(check_path(graph, 'E', 'D'))  # False
    print(check_path(graph, 'C', 'A'))  # False
    
if __name__ == "__main__":
    main()
