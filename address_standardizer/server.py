from bottle import route, run, request, post, get, static_file

from address_standardizer.standardizer import standardize, standardize_business
from address_standardizer.utils import PARENT_DIR


@post("/api/address")
def standardize_address():
    address1 = request.json.get("address1")
    address2 = request.json.get("address2")
    business = request.json.get("business")
    return dict(
        address1=standardize(address1),
        address2=standardize(address2),
        business=standardize_business(business),
    )


@get("/")
def home():
    return static_file("index.html", root=str(PARENT_DIR.joinpath("views")))


def start_server(host, port, debug):
    return run(host=host, port=port, debug=debug, reloader=debug)
