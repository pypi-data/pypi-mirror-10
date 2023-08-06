from requests import Session

from brownant.pipeline.base import PipelineProperty
from brownant.exceptions import NotSupported


class HTTPClientProperty(PipelineProperty):
    """The python-requests session property.

    :param session_class: the class of session instance. default be
                          :class:`~requests.Session`.
    """

    def prepare(self):
        self.options.setdefault("session_class", Session)

    def provide_value(self, obj):
        session_class = self.options["session_class"]
        session = session_class()
        return session


class URLQueryProperty(PipelineProperty):
    """The query argument property. The usage is simple::

        class MySite(Dinergate):
            item_id = URLQueryProperty(name="item_id", type=int)

    It equals to this::

        class MySite(Dinergate):
            @cached_property
            def item_id(self):
                value = self.request.args.get("item_id", type=int)
                if not value:
                    raise NotSupported
                return value

    A failure convertion with given type (:exc:`ValueError` be raised) will
    lead the value fallback to :obj:`None`. It is the same with the behavior of
    the :class:`~werkzeug.datastructures.MultiDict`.

    :param name: the query argument name.
    :param request_attr: optional. default: `"request"`.
    :param type: optionl. default: `None`. this value will be passed to
                 :meth:`~werkzeug.datastructures.MultiDict.get`.
    :param required: optionl. default: `True`. while this value be true, the
                     :exc:`~brownant.exceptions.NotSupported` will be raised
                     for meeting empty value.
    """

    required_attrs = {"name"}

    def prepare(self):
        self.attr_names.setdefault("request_attr", "request")
        self.options.setdefault("type", None)
        self.options.setdefault("required", True)

    def provide_value(self, obj):
        request = self.get_attr(obj, "request_attr")
        value = request.args.get(self.name, type=self.options["type"])
        if self.options["required"] and value is None:
            raise NotSupported
        return value


class ResponseProperty(PipelineProperty):
    """The base class of response properties.

    You can't use this class directly.

    :param content_method: required. it point to response content method.
    """
    def prepare(self):
        self.attr_names.setdefault("url_attr", "url")
        self.attr_names.setdefault("http_client_attr", "http_client")
        self.options.setdefault("method", "GET")

    def provide_value(self, obj):
        if "content_method" not in self.attr_names:
            raise KeyError("You need create a subclass which inheritance "
                           "ResponseProperty, and assign `content_method` "
                           "into self.attr_names")
        url = self.get_attr(obj, "url_attr")
        http_client = self.get_attr(obj, "http_client_attr")
        content_method = self.attr_names.get("content_method")
        response = http_client.request(url=url, **self.options)
        response.raise_for_status()
        content = getattr(response, content_method)
        if callable(content):
            content = content()
        return content


class TextResponseProperty(ResponseProperty):
    """The text response which returned by fetching network resource.

    Getting this property is network I/O operation in the first time. The
    http request implementations are all provided by :mod:`requests`.

    The usage example::

        class MySite(Dinergate):
            foo_http = requests.Session()
            foo_url = "http://example.com"
            foo_text = TextResponseProperty(url_attr="foo_url",
                                            http_client="foo_http",
                                            proxies=PROXIES)

    :param url_attr: optional. default: `"url"`. it point to the property which
                     could provide the fetched url.
    :param http_client_attr: optional. default: `"http_client"`. it point to
                             an http client property which is instance of
                             :class:`requests.Session`
    :param method: optional. default: `"GET"`. the request method which
                   used by http_client.
    :param kwargs: the optional arguments which will be passed to
                   :meth:`requests.Session.request`
    """

    def prepare(self):
        super(TextResponseProperty, self).prepare()
        self.attr_names.setdefault("content_method", "text")


class JSONResponseProperty(ResponseProperty):
    """The json response which returned by fetching network resource.

    Getting this property is network I/O operation in the first time. The
    http request implementations are all provided by :mod:`requests`.

    The usage example::

        class MySite(Dinergate):
            foo_http = requests.Session()
            foo_url = "http://example.com"
            foo_json = JSONResponseProperty(url_attr="foo_url",
                                            http_client="foo_http",
                                            proxies=PROXIES)

    :param url_attr: optional. default: `"url"`. it point to the property which
                     could provide the fetched url.
    :param http_client_attr: optional. default: `"http_client"`. it point to
                             an http client property which is instance of
                             :class:`requests.Session`
    :param method: optional. default: `"GET"`. the request method which
                   used by http_client.
    :param kwargs: the optional arguments which will be passed to
                   :meth:`requests.Session.request`
    """

    def prepare(self):
        super(JSONResponseProperty, self).prepare()
        self.attr_names.setdefault("content_method", "json")
