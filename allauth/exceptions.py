class ImmediateHttpResponse(Exception):
    """
    This exception is used to interrupt the flow of processing to immediately
    return a custom HttpResponse.
    """
    def __init__(self, response):
        self.response = response


class SendingEmailFailed(Exception):
    """
    Used when sending an email is failed, failure can be anything,
    the error must be logged
    """
    pass
