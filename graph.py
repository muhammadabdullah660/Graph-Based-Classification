import os
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

def construct_graph(file_path):
    G = nx.Graph()
    with open(file_path, 'r', encoding='utf-8',errors='ignore') as file:
        words = file.read().split()
        for i in range(len(words) - 1):
            current_word = words[i]
            next_word = words[i + 1]
            if G.has_edge(current_word, next_word):
                print(G[current_word][next_word])
            else:
                G.add_edge(current_word, next_word)
    return G
def print_adjacency_matrix(G):
    nodes = sorted(G.nodes())
    print("\t" + "\t".join(nodes))
    for node1 in nodes:
        row = [str(G[node1].get(node2, {'weight': 0})['weight']) for node2 in nodes]
        print(f"{node1}\t{'\t'.join(row)}")
        
def print_adjacency_list(G):
    for node in G.nodes():
        neighbors = list(G.neighbors(node))
        if neighbors:
            print(f"{node}: {', '.join(neighbors)}")
        else:
            print(f"{node}:")          

def visualize_graph(G, file_path):
    plt.figure(figsize=(10, 10))
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=10, edge_color='black', linewidths=1, arrows=True, arrowsize=20)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.title(f'Directed Graph of Words in {os.path.basename(file_path)}')
    plt.show()

def makeAllGraphs(folder):
    graphs = []
    for file_name in os.listdir(folder):
        if file_name.startswith('preprocessed_') and file_name.endswith('.txt'):
            file_path = os.path.join(folder, file_name)
            G = construct_graph(file_path)
            graphs.append(G)
            # print_adjacency_matrix(G)
            # print_adjacency_list(G)
            # visualize_graph(G, file_path)
    return graphs

def graphToVector(graph):
    num_nodes = graph.number_of_nodes()
    return np.array([num_nodes])

def graphsToVectors(graphs):
    return np.array([graphToVector(graph) for graph in graphs])

def returnTravel():
    preprocess_files_folder = './traveldata/training'
    graphs= makeAllGraphs(preprocess_files_folder)
    print('travel')
    return graphs

def returnFashion():
    preprocess_files_folder = './fashiondata/training'
    graphs= makeAllGraphs(preprocess_files_folder)
    print('fashion')
    return graphs

def returnDisease():
    preprocess_files_folder = './diseasedata/training'
    graphs= makeAllGraphs(preprocess_files_folder)
    print('disease')
    return graphs

