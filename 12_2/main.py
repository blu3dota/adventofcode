import os

paths = []

class Node:
    def __init__(self, name):
        self.name = name
        self.edges = []

    def is_big(self):
        return str.isupper(self.name) and self.name != "start" and self.name != "end"

    def __repr__(self):
        return self.name

class Edge:
    def __init__(self, src, dest):
        self.src = src
        self.dest = dest

    def __repr__(self):
        return f"({self.src},{self.dest})"

class Graph:
    def __init__(self):
        self.nodes = []
        pass

    def add_edge(self, source, dest):
        source.edges.append(Edge(source, dest))
        dest.edges.append(Edge(dest, source))

    def get_node(self, name):
        node_src = list(filter(lambda node: node.name == name, self.nodes))
        return node_src[0] if len(node_src) > 0 else None

    def add_node(self, name):
        node_src = list(filter(lambda node: node.name == name, self.nodes))
        if len(node_src) == 0:
            self.nodes.append(Node(name))

def main():
    global paths
    filepath = os.path.join(os.getcwd(), "input.txt")
    graph = Graph()
    with open(filepath) as file:
        for line in file:
            source_name, destination_name = line.strip('\n').split("-")

            graph.add_node(source_name)
            graph.add_node(destination_name)
            graph.add_edge(graph.get_node(source_name), graph.get_node(destination_name))

            #print(f"Edges of {source}: {get_node(graph, source).edges}")

    for node in graph.nodes:
        if node.is_big() or node.name == "start" or node.name == "end":
            continue
        search(graph, [], graph.get_node("start"), [], node, False)

    for path in paths:
        print(path)
    print(len(paths))

def search(graph, path, cur, visited, special_cave, special_cave_visited):
    global paths
    path.append(cur)
    queue = []
    now_visited = False

    if cur == special_cave and special_cave_visited == False:
        now_visited = True

    if cur.is_big() == False:
        if cur == special_cave and special_cave_visited == True and cur not in visited:
            visited.append(cur)
        elif cur != special_cave:
            visited.append(cur)
    #print(f"Edges of {cur.name}: {cur.edges}")
    for edge in cur.edges:
        if edge.dest not in visited:
            queue.append(edge.dest)

    if len(queue) == 0 or cur.name == "end":
        if cur.name == "end" and path not in paths:
            paths.append(path)
        return

    for e in queue:
        search(graph, path.copy(), e, visited.copy(), special_cave, now_visited if special_cave_visited == False else special_cave_visited)

if __name__ == "__main__":
    main()