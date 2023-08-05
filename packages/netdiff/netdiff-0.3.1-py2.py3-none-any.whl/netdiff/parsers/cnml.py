import networkx
import libcnml
import os
import six

try:
    import urlparse
except ImportError:
    import urllib.parse as urlparse

from .base import BaseParser
from ..exceptions import NetParserException


class CnmlParser(BaseParser):
    """ CNML 0.1 parser """
    protocol = 'static'
    version = '0.1'
    metric = None

    def _to_python(self, data):
        if isinstance(data, six.string_types):
            up = urlparse.urlparse(data)
            # if it looks like a file path
            if os.path.isfile(data) or up.scheme in ['http', 'https']:
                return libcnml.CNMLParser(data)
            else:
                raise NetParserException('Could not decode CNML data')
        elif isinstance(data, libcnml.CNMLParser):
            return data
        else:
            raise NetParserException('Could not find valid data to parse')

    def parse(self, data):
        """
        Extract information from a CNML file to generate a NetworkX Graph object.
        """
        graph = networkx.Graph()

        # loop over links and create networkx graph
        # Add only working nodes with working links
        for link in data.get_inner_links():
            if link.status != libcnml.libcnml.Status.WORKING:
                continue
            interface_a, interface_b = link.getLinkedInterfaces()
            source = interface_a.ipv4
            dest = interface_b.ipv4
            # add link to Graph
            graph.add_edge(source, dest, weight=1)

        self.graph = graph
