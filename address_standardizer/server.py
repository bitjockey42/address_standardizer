from bottle import route, run, request, post


@post("/hello")
def hello():
    name = request.json.get("name")
    return dict(name=name)


def start_server(host, port, debug):
    return run(host=host, port=port, debug=debug, reloader=debug)
