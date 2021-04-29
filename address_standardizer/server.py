from bottle import route, run, request, post


@post("/standardize")
def standardize():
    address1 = request.json.get("address1")
    address2 = request.json.get("address2")
    return dict(address1=address1, address2=address2)


def start_server(host, port, debug):
    return run(host=host, port=port, debug=debug, reloader=debug)
