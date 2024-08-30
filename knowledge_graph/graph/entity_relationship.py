import json


def stream_matplotlib(json_strs):
    "Take the Json Named Entity and Relationships give by LLM and convert it into a form that is understood by UI"
    edges = []
    edge_labels = {}
    nodes = {}
    for json_str in json_strs:
        data = json.loads(json_str)
        for edge in data['edges']:
            edges.append([edge['source'], edge['target']])
            edge_labels[(edge['source'], edge['target'])] = edge['relationship']
        for node in data['nodes']:
            nodes[node['label']] = node['type']

    return nodes, edges, edge_labels

def stream_network_graph(json_strs):
    "Take the Json Named Entity and Relationships give by LLM and convert it into a form that is understood by UI"
    edges = []
    nodes = []
    nodes_map = {}
    idx = 0
    for json_str in json_strs:
        data = json.loads(json_str)
        for node in data['nodes']:
            nodes_map[node['label']] = idx
            nodes.append({"id": idx, "label": node['label']})
            idx += 1
        for edge in data['edges']:
            if edge['source'] in nodes_map and edge['target'] in nodes_map:
                _from = nodes_map[edge['source']]
                _to = nodes_map[edge['target']]
                _label = edge['relationship']
                edges.append({"from": _from, "to": _to, "label": _label})

    return nodes, edges
