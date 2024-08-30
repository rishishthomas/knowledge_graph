import graph.entity_relationship

def test_stream():
    json ='''{
        "nodes": [
            {"label": "Social media", "type": "platform"},
            {"label": "Fashion industry", "type": "industry"},
            {"label": "Fashion designers", "type": "profession"},
            {"label": "Consumers", "type": "audience"},
            {"label": "COVID-19 pandemic", "type": "event"},
            {"label": "Fashion houses", "type": "business"},
            {"label": "Luxury fashion brands", "type": "business"},
            {"label": "Influencers", "type": "profession"},
            {"label": "Social media platforms", "type": "platform"},
            {"label": "Instagram", "type": "platform"},
            {"label": "TikTok", "type": "platform"},
            {"label": "Generation Y and Z", "type": "audience"},
            {"label": "Online communities", "type": "community"},
            {"label": "Industry leaders", "type": "profession"}
        ],
        "edges": [
            {"source": "Social media", "target": "Fashion industry", "relationship": "refers to"},
            {"source": "Social media", "target": "Fashion designers", "relationship": "used by"},
            {"source": "Social media", "target": "Consumers", "relationship": "used by"},
            {"source": "COVID-19 pandemic", "target": "Fashion industry", "relationship": "affected"},
            {"source": "COVID-19 pandemic", "target": "Consumers", "relationship": "affected"},
            {"source": "Social media", "target": "Fashion houses",
             "relationship": "created new channels for advertising"},
            {"source": "Social media", "target": "Luxury fashion brands", "relationship": "used by"},
            {"source": "Luxury fashion brands", "target": "Consumers", "relationship": "engage with"},
            {"source": "Social media", "target": "Influencers", "relationship": "created new way of advertising"},
            {"source": "Social media", "target": "Influencers", "relationship": "maintain customer relationships"},
            {"source": "Social media", "target": "Instagram", "relationship": "popular among"},
            {"source": "Social media", "target": "TikTok", "relationship": "popular among"},
            {"source": "Instagram", "target": "Generation Y and Z", "relationship": "popular among"},
            {"source": "TikTok", "target": "Generation Y and Z", "relationship": "popular among"},
            {"source": "Social media", "target": "Online communities", "relationship": "created"},
            {"source": "Industry leaders", "target": "Consumers", "relationship": "direct communication with"}
        ]
        }'''
    assert(graph.entity_relationship.stream([json]))

test_stream()