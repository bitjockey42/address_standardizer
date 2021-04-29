from bottle import route, run, request, post, get, template

from address_standardizer.standardizer import standardize


@post("/api/address")
def standardize_address():
    address1 = request.json.get("address1")
    address2 = request.json.get("address2")
    return dict(address1=standardize(address1), address2=standardize(address2))


@get("/")
def home():
    return template('Hello {{name}}!', name='World')


def start_server(host, port, debug):
    return run(host=host, port=port, debug=debug, reloader=debug)
