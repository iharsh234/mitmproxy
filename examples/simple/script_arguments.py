import argparse
from mitmproxy import http

class Replacer:
    def __init__(self, src: str, dst: str) -> None:
        self.src, self.dst = src, dst

    def response(self, flow: http.HTTPFlow) -> None:
        flow.response.replace(self.src, self.dst)


def load(l):
    parser = argparse.ArgumentParser()
    parser.add_argument("src", type=str)
    parser.add_argument("dst", type=str)
    args = parser.parse_args()
    l.boot_into(Replacer(args.src, args.dst))
