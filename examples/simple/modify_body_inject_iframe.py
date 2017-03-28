# Usage: mitmdump -s "iframe_injector.py url"
# (this script works best with --anticache)
import sys
from bs4 import BeautifulSoup
from mitmproxy import http
import typing


class Injector:
    def __init__(self, iframe_url : str) -> None:
        self.iframe_url = iframe_url

    def response(self, flow: http.HTTPFlow) -> typing.Any:
        if flow.request.host in self.iframe_url:
            return
        html = BeautifulSoup(flow.response.content, "html.parser")
        if html.body:
            iframe = html.new_tag(
                "iframe",
                src=self.iframe_url,
                frameborder=0,
                height=0,
                width=0)
            html.body.insert(0, iframe)
            flow.response.content = str(html).encode("utf8")


def start():
    if len(sys.argv) != 2:
        raise ValueError('Usage: -s "iframe_injector.py url"')
    return Injector(sys.argv[1])
