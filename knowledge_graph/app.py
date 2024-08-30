from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import wiki.wiki_search as wiki_search
import llm.llm_query as llm_query
import graph.entity_relationship as entity_relationship


app = Flask(__name__)
CORS(app, support_credentials=True)
@app.route('/process', methods=['GET'])
@cross_origin(supports_credentials=True)
def process():
    try:
        # Get the 'query' parameters from the request
        print(request.args.get('query'))
        data = wiki_search.search_wikipedia(request.args.get('query'))

        json_strs = llm_query.get_results_open_ai(data)
        nodes, edges = entity_relationship.stream_network_graph(json_strs)

        json_return =  jsonify(
            {
                "type": "graph",
                "data": {
                    "nodes": nodes,
                    "edges": edges
                }
            }
        )
        print("----------------------------------------------------processing complete ----------------------------------------------------")
        print(json_return)
        return json_return
    except ValueError:
        return jsonify({"error": "Invalid input. Please provide numerical values."}), 400

# main driver function
if __name__ == '__main__':

    # run() method of Flask class runs the application
    # on the local development server.
    app.run()

