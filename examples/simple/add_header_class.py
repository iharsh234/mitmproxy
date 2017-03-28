from mitmproxy import http
import typing
class AddHeader:
    def response(self, flow: http.HTTPFlow) -> typing.Any:
        flow.response.headers["newheader"] = "foo"


def start():
    return AddHeader()
