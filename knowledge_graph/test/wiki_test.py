import wiki.wiki_search as wiki_search
import llm.llm_query as llm_query
import graph.entity_relationship as entity_relationship
import ui.graph as graph

def test_wiki_search():
    data = wiki_search.search_wikipedia('Edison, NJ')

    json_strs = llm_query.get_results_open_ai(data)
    nodes, edges = entity_relationship.stream_network_graph(json_strs)
    print(nodes)
    print(edges)


test_wiki_search()
