"""Test high-level api"""


def test_api_imports():
    """
    Imports of the public API work.

    """
    from marquez.api import binding, create_object_graph, defaults  # noqa
