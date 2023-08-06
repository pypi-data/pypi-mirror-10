class CommandsMixin(object):
    """
    Some useful commands for the Gremlin Server.
    """

    def add_vertex(self, label=None):
        """
        Adds a new vertex to the graph.

        :params str label: Node label (optional)

        :returns: The created :py:class:`gremlinrestclient.commands.Vertex`
        """

        if label is not None:
            script = """graph.addVertex(label, vertex_label)"""
            bindings = {"vertex_label": label}
        else:
            script = """graph.addVertex()"""
            bindings = {}
        resp = self.execute(script, bindings=bindings)
        vertex = self.make_elem(resp, Vertex)
        return vertex

    def vertex(self, vid):
        """Get an existing vertex from the graph

        :params int vid: Unique node identifier
        :returns: The requested :py:class:`gremlinrestclient.commands.Vertex`
            or None
        """
        script = """g.V(vid)"""
        bindings = {"vid": vid}
        resp = self.execute(script, bindings=bindings)
        vertex = self.make_elem(resp, Vertex)
        return vertex

    def make_elem(self, resp, elem_class):
        try:
            data = resp.data[0]
        except IndexError:
            elem = None
        else:
            elem = elem_class(data, self)
        return elem

    def vertices(self):
        """
        Get all vertices in graph.

        :returns: :py:class:`list` of
            :py:class:`gremlinrestclient.commands.Vertex` objects
        """
        script = """g.V()"""
        resp = self.execute(script)
        vertices = [Vertex(v, self) for v in resp.data]
        return vertices

    def edge(self, eid):
        """Retrieves an existing edge from the graph

        :params str eid: Unique edge identifier

        :returns: The requested :py:class:`gremlinrestclient.commands.Edge`
            or None
        """
        # Bindings don't seem to work here...
        script = """g.E(%s)""" % (eid)
        resp = self.execute(script)
        edge = self.make_elem(resp, Edge)
        return edge

    def edges(self):
        """
        Get all edges in graph.

        :returns: :py:class:`list` of
            :py:class:`gremlinrestclient.commands.Edge`
        """
        script = """g.E()"""
        resp = self.execute(script)
        edges = [Edge(e, self) for e in resp.data]
        return edges


class Element(object):
    """A base class defining an Element object."""

    def __init__(self, element_data, gdb):
        self._gdb = gdb
        self._eid = element_data["id"]
        self._properties = element_data.get("properties", {})
        self._type = element_data["type"]
        self._label = element_data["label"]
        self._source = ""

    @property
    def label(self):
        return self._label

    @property
    def id(self):
        return self._eid

    @property
    def properties(self):
        return self._properties

    def _get_script(self):
        # Bindings acting wierd for edge lookups...
        script = """elem = g.%s(%s);""" % (self._source, self._eid)
        return script

    def values(self, prop):
        get_script = self._get_script()
        script = """%selem.values(prop);""" % (get_script)
        bindings = {"prop": prop}
        resp = self._gdb.execute(script, bindings=bindings)
        try:
            prop = resp.data[0]
        except IndexError:
            prop = None
        return prop

    def property(self, key, value=None):
        """Gets/sets the value of the property for the given key

        :param str key: The key which value is being retrieved.

        :param str value: The value to set the property to (optional).
            None by default.
        :returns: The property associated with the key"""
        if value is not None:
            script, bindings = self._set_property_script(key, value)
            resp = self._gdb.execute(script, bindings=bindings)
            if self._type == "vertex":
                output = self._gdb.make_elem(resp, Vertex)
            else:
                output = self._gdb.make_elem(resp, Edge)
        else:
            output = self.values(key)
        return output

    def _set_property_script(self, prop, value):
        get_script = self._get_script()
        script = """%selem.property(prop, val);""" % (get_script)
        bindings = {"prop": prop, "val": value}
        return script, bindings

    def keys(self):
        """
        Returns a set with the property keys of the element

        :returns: :py:class:`list` of property keys"""
        return self._properties.keys()

    def get_id(self):
        """Returns the unique identifier of the element

        :returns: The unique identifier of the element"""
        return self._eid

    def remove(self):
        get_script = self._get_script()
        script = """%s;elem.remove;""" % (get_script)
        self._gdb.execute(script)


class Vertex(Element):
    """
    Vertex

    :param dict vertex: Vertex data returned from server
    :param gdb: GraphDatabase instance associated with this vertex.
    """

    def __init__(self, vertex, gdb):
        super(Vertex, self).__init__(vertex, gdb)
        self._source = "V"

    def add_edge(self, label, vertex):
        script = """vert1 = g.V(vid1).next();
                    vert2 = g.V(vid2).next();
                    vert1.addEdge(lab, vert2)"""
        bindings = {"lab": label, "vid1": self._eid, "vid2": vertex.id}
        resp = self._gdb.execute(script, bindings=bindings)
        return self._gdb.make_elem(resp, Edge)

    def out_edges(self):
        """Gets all the outgoing edges of the node.

        :returns: A list of :py:class:`gremlinrestclient.commands.Edge`
        """
        script = """%s; elem.outE()""" % (self._get_script())
        resp = self._gdb.execute(script)
        return [Edge(e, self._gdb) for e in resp.data]

    def in_edges(self):
        """Gets all the outgoing edges of the node.

        :returns: A list of :py:class:`gremlinrestclient.commands.Edge`
        """
        script = """%s; elem.inE()""" % (self._get_script())
        resp = self._gdb.execute(script)
        return [Edge(e, self._gdb) for e in resp.data]

    def edges(self, label=None):
        """Gets all the outgoing edges of the node.

        :param str label: Label to filter the edges (optional)

        :returns: A list of :py:class:`gremlinrestclient.commands.Edge`
        """
        script = """%s; elem.bothE()""" % (self._get_script())
        resp = self._gdb.execute(script)
        return [Edge(e, self._gdb) for e in resp.data]


class Edge(Element):
    """
    Edge

    :param dict edge: Edge data returned from server
    :param gdb: GraphDatabase instance associated with this vertex.
    """

    def __init__(self, edge, gdb):
        super(Edge, self).__init__(edge, gdb)
        self._source = "E"
        self._out_vertex = edge["outV"]
        self._in_vertex = edge["inV"]
        self._out_label = edge["outVLabel"]
        self._out_label = edge["inVLabel"]

    def out_vertex(self):
        """
        Returns the origin Vertex of the relationship.

        :returns: The origin :py:class:`gremlinrestclient.commands.Vertex`"""
        return self._get_vertex(self._out_vertex)

    def in_vertex(self):
        """
        Returns the target Vertex of the relationship.

        :returns: The target :py:class:`gremlinrestclient.commands.Vertex`"""
        return self._get_vertex(self._in_vertex)

    def _get_vertex(self, vid):
        script = """g.V(vid)"""
        bindings = {"vid": vid}
        resp = self._gdb.execute(script, bindings=bindings)
        vertex = self._gdb.make_elem(resp, Vertex)
        return vertex
