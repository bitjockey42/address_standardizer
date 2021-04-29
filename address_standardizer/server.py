from bottle import route, run, request, post

from address_standardizer.standardizer import standardize


@post("/address")
def standardize_address():
    address1 = request.json.get("address1")
    address2 = request.json.get("address2")
    return dict(
        address1=standardize(address1), address2=standardize(address2)
    )


def start_server(host, port, debug):
    return run(host=host, port=port, debug=debug, reloader=debug)
