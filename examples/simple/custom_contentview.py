"""
This example shows how one can add a custom contentview to mitmproxy.
The content view API is explained in the mitmproxy.contentviews module.
"""
from mitmproxy import contentviews
from typing import Tuple, Iterable, AnyStr, List


class ViewSwapCase(contentviews.View):
    name = "swapcase"

    # We don't have a good solution for the keyboard shortcut yet -
    # you manually need to find a free letter. Contributions welcome :)
    prompt = ("swap case text", "z")
    content_types = ["text/plain"]

    def __call__(self, data: AnyStr, **metadata) -> Tuple[str, Iterable[List[Tuple[str, AnyStr]]]]:
        return "case-swapped text", contentviews.format_text(data.swapcase())


view = ViewSwapCase()


def load(l):
    contentviews.add(view)


def done():
    contentviews.remove(view)
