

class PmDataShowIllegalParameterException(Exception):

    def __init__(self, *args, **kwargs):
        self.error_message = 'Illegal arguments exception. %s' % kwargs.get('message')
