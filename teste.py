import osmnx as ox
import networkx as nx
import matplotlib.pyplot as plt
     

def to_undirected_multigraph(G):
    """
    Converte um MultiDiGraph direcionado em um MultiGraph não-direcionado,
    preservando atributos dos nós e arestas.
    """
    H = nx.MultiGraph()
    # Copiar nós e seus atributos
    for n, data in G.nodes(data=True):
        H.add_node(n, **data)

    # Copiar arestas e seus atributos, sem direcionamento
    for u, v, data in G.edges(data=True):
        # Em um MultiGraph, se já existir uma aresta u-v, esta será adicionada como mais uma aresta paralela
        H.add_edge(u, v, **data)

    # Copiar atributos do grafo
    H.graph.update(G.graph)
    return H
     

# ============================================
# 1. Obter o grafo da cidade de Natal
# ============================================
place = "Natal, Rio Grande do Norte, Brazil"
G = ox.graph_from_place(place, network_type='drive')

# Converte para não-direcionado mantendo o tipo MultiGraph
G_undirected = to_undirected_multigraph(G)
     

# ============================================
# 2. Obter POIs de interesse (hospitais como exemplo)
# ============================================
tags = {'amenity': 'school'}
pois = ox.features.features_from_place(place, tags=tags)

# Extrair pontos representativos (centroides se for polígono)
hospital_points = []
for idx, row in pois.iterrows():
    if row.geometry.geom_type == 'Point':
        hospital_points.append((row.geometry.y, row.geometry.x))
    else:
        hospital_points.append((row.geometry.centroid.y, row.geometry.centroid.x))

if not hospital_points:
    print("Nenhuma escola encontrada. Tentando postos de gasolina...")
    tags = {'amenity': 'fuel'}
    pois = ox.features.features_from_place(place, tags=tags)
    for idx, row in pois.iterrows():
        if row.geometry.geom_type == 'Point':
            hospital_points.append((row.geometry.y, row.geometry.x))
        else:
            hospital_points.append((row.geometry.centroid.y, row.geometry.centroid.x))
    if not hospital_points:
        raise ValueError("Nenhum POI encontrado para as categorias tentadas.")
     

# ============================================
# 3. Encontrar nós mais próximos dos POIs
# ============================================
latitudes = [hp[0] for hp in hospital_points]
longitudes = [hp[1] for hp in hospital_points]
hospital_nodes = ox.distance.nearest_nodes(G_undirected, X=longitudes, Y=latitudes)
hospital_nodes = list(set(hospital_nodes))

if len(hospital_nodes) < 2:
    raise ValueError("POIs insuficientes para criar um MST (menos de 2 pontos).")
     

len(hospital_points)
# ============================================
# 4. Construir um grafo completo com menor rota entre POIs
# ============================================
G_interest = nx.Graph()
for i in range(len(hospital_nodes)):
    for j in range(i+1, len(hospital_nodes)):
        route = nx.shortest_path(G_undirected, hospital_nodes[i], hospital_nodes[j], weight='length')
        route_length = 0
        for k in range(len(route)-1):
            route_length += G_undirected[route[k]][route[k+1]][0]['length']  # Como é MultiGraph, usar [0]
        G_interest.add_edge(hospital_nodes[i], hospital_nodes[j], weight=route_length)
     

# ============================================
# 5. Calcular o MST
# ============================================
mst_edges = list(nx.minimum_spanning_edges(G_interest, data=True))
total_mst_length = sum([d['weight'] for (u, v, d) in mst_edges])
print("Comprimento total do MST entre os POIs selecionados:", total_mst_length, "metros")
mst_routes = []
for (u, v, d) in mst_edges:
    route = nx.shortest_path(G_undirected, u, v, weight='length')
    mst_routes.append(route)

# Plotar o grafo base
fig, ax = ox.plot_graph(
    G_undirected, node_size=0, edge_color="gray", edge_linewidth=0.5, show=False, close=False
)

# Destacar as rotas do MST em vermelho
for route in mst_routes:
    x = [G_undirected.nodes[n]['x'] for n in route]
    y = [G_undirected.nodes[n]['y'] for n in route]
    ax.plot(x, y, color='red', linewidth=2, zorder=4)

# Plotar também os POIs (hospitais) em azul
poi_x = [G_undirected.nodes[n]['x'] for n in hospital_nodes]
poi_y = [G_undirected.nodes[n]['y'] for n in hospital_nodes]
ax.scatter(poi_x, poi_y, c='blue', s=80, zorder=5, edgecolor='black')

plt.title("MST entre POIs (hospitais) em Natal", fontsize=14)
plt.show()