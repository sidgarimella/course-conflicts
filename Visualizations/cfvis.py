from networkx.readwrite import json_graph

import json
import flask
import networkx as nx


with open('Visualizations/static/graph.json') as f:
    graph = json.load(f)
nodes = graph["nodes"]
links = graph["links"]

app = flask.Flask(__name__)

@app.route('/')
def serve():
    return flask.render_template("index.html", nodes=nodes, links=links)

print('\n When2Discrete is now available on http://localhost:5056 \n')
app.run(debug=True,port=5056)
