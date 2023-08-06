# InfluxDispatcher

A simple asynchronous/non-asynchronous package for sending requests. I made this because I
was tired of using a bunch of try/except statements in my code when sending requests to my apis.
This package will attempt to send requests twice. It returns the response object and a boolean indicating whether the request
was successful or not. The format for the response is a tuple of the following (response_from_request, boolean)