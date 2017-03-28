"""
This example shows two ways to redirect flows to another server.
"""
from mitmproxy import http
import typing

def request(flow: http.HTTPFlow) -> typing.Any:
    # pretty_host takes the "Host" header of the request into account,
    # which is useful in transparent mode where we usually only have the IP
    # otherwise.
    if flow.request.pretty_host == "example.org":
        flow.request.host = "mitmproxy.org"
