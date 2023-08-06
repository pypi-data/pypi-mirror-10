betamax_serializers
===================

Experimental set of Serializers for `Betamax 
<https://github.com/sigmavirus24/betamax>`_ that may possibly end up in the 
main package.

Pretty JSON Serializer
----------------------

Usage:

.. code-block:: python

    from betamax_serializers.pretty_json import PrettyJSONSerializer

    from betamax import Betamax

    import requests

    Betamax.register_serializer(PrettyJSONSerializer)

    session = requests.Session()
    recorder = Betamax(session)
    with recorder.use_cassette('testpretty', serialize_with='prettyjson'):
        session.request(method=method, url=url, ...)
