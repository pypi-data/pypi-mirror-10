from .exception import ApiException


class Response:
    def __init__(self, method, kwargs, error, data):
        self.method = method
        self.error = error
        self.args = kwargs
        self.data = data

    def __repr__(self):
        if self.error:
            raise ApiException('Error: {}'.format(self.error))
        return repr(self.data)
