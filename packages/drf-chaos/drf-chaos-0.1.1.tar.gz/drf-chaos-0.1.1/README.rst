drf-chaos extension
===================

drf-chaos is a small collection of decorators and middlewares for
testing `Django REST Framework`_ API under unexpected circumstances.

Decorators
==========

Delay
-----

Delay response of a specific amount of seconds

``@delay(rate, seconds)``

Params:

``rate``: probability that an unexpected event happens

``seconds``: suspend execution of the current thread for the given
number of seconds

Error
-----

Return a different response HTTP status code

``@error(rate, status)``

Params:

``rate``: probability that an unexpected event happens

``status``: integer corresponding to any valid HTTP status code. See
`DRF HTTP status codes`_

Chaos
-----

Apply a random unexpected event to the HTTP response. (A delay between 0
to 3 second and a random HTTP status code)

``@chaos(rate)``

Params:

``rate``: probability that an unexpected event happens

Middlewares
===========

-  ChaosMiddleware

Example
=======

::

    from rest_framework import status
    from rest_framework.response import Response
    from rest_framework.views import APIView

    from drf_chaos.decorators import chaos, delay, error


    class ChaosApiView(APIView):
        @chaos(rate=0.5)
        def get(self, request):
            return Response(status=status.HTTP_204_NO_CONTENT)


    class DelayApiView(APIView):
        @delay(rate=0.5, seconds=3)
        def get(self, request):
            return Response(status=status.HTTP_204_NO_CONTENT)


    class ErrorApiView(APIView):
        @error(rate=0.5, status=500)
        def get(self, request):
            return Response(status=status.HTTP_204_NO_CONTENT)

Requirements
============

-  Python (2.7)
-  Django (1.6+, 1.7+, 1.8)

Installation
============

Install using ``pip``\ …

::

    pip install drf-chaos

.. _Django REST Framework: https://github.com/tomchristie/django-rest-framework
.. _DRF HTTP status codes: https://github.com/tomchristie/django-rest-framework/blob/master/rest_framework/status.py