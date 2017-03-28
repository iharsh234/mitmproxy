from mitmproxy import http
import typing

def response(flow: http.HTTPFlow) -> typing.Any:
    flow.response.headers["newheader"] = "foo"
