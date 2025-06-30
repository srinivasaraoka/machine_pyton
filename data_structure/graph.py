def add_node(v):
    global node_count
    if v in graph:
        print("node is already present")
    else:
        node_count = node_count + 1
        nodes.append(v)
        print(nodes)
        for n in graph:
            n.append(0)
        print(graph)
        temp = []
        for i in range(node_count):
            temp.append(0)
        graph.append(temp)


def add_edge(v1, v2, cost=1):
    if v1 not in nodes:
        print("given nde note in nodes")
    elif v2 not in nodes:
        print("given node not in nodes")
    else:
        index1 = nodes.index(v1)
        index2 = nodes.index(v2)
        graph[index1][index2] = cost
        graph[index2][index1] = cost


def print_graph():
    for i in range(node_count):
        for j in range(node_count):
            print(graph[i][j], end=' ')
        print()


def add_node_1(v):
    if v in graph_1:
        print("node alredy present")
    else:
        graph_1[v] = []


def add_edge_1(v1, v2, cost):
    if v1 not in graph_1:
        print("print v1 not in graph_1")
    elif v2 not in graph_1:
        print('v2 not in graph_2')
    else:
        list1 = [v2, cost]
        list2 = [v1, cost]
        graph_1[v1].append(list1)
        graph_1[v2].append(list2)


def delete_node(node):
    global node_count
    if node not in nodes:
        print("given node not in nodes")
    else:
        node_count= node_count-1
        index2= nodes.index(node)
        nodes.remove(node)
        print("graph",graph)
        graph.pop(index2)
        print(graph)
        for x in graph:
            print(x)
            x.pop(index2)

def delete_edge(v1,v2):
    if v1 not in nodes:
        print('v1 not present')
    elif v2 not in nodes:
        print('v2 not present')
    else:
        index1= nodes.index(v1)
        index2= nodes.index(v2)
        graph[index1][index2] =0
        graph[index2][index1] =0   
def delete_node_1(v1):
    if v1 not in graph_1:
        print("node not present")
    else:
        
            graph_1.pop(v1)
            for i in graph_1:
                list1= graph_1[i]
                if v1 in list1:
                    list1.remove(v1)
def DFS(node, visited, graph):
    #print(graph)
    if node not in graph:
        print("node not present")
        return 1
    if node not in visited:
        print(node, end=" ")
        visited.add(node)   
        for i in graph[node]:  # Corrected from graph(node) to graph[node]
            DFS(i[0], visited, graph)
             
                            
                       
                
nodes = []
graph = []
node_count = 0
print("before  addig node")
print(nodes)
print(graph)
print('after adding the node')
add_node('a')
add_node('b')
add_node('c')
add_edge("a", "b")
add_edge("b", "c")
add_edge("c", "a")
print(nodes)
print(graph)
print("befor delete the node")

print_graph()


#delete_node('a')
# print("after deleting the node")
# print_graph()
# delete_edge('a','c')
# print('grph=after delete edge', print_graph(), graph)
visited= set()


graph_1 = {}
add_node_1('A')
add_node_1('B')
add_node_1('C')
add_node_1('D')
print(graph_1)
add_edge_1("A", "B", 10)
add_edge_1("B", "C", 20)
add_edge_1("C", "D", 30)
print("DFS traversal of graph_1:", end=" ") 
DFS('A', visited, graph_1)
