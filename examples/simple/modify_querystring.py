from mitmproxy import http
import typing

def request(flow: http.HTTPFlow) -> typing.Any:
    flow.request.query["mitmproxy"] = "rocks"
