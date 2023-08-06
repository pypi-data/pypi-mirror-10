import logging

class Client(object):
    """ This object autheticates the account to the api """

    def __init__(self, auth, **kwargs):
        self.auth = auth
        self.protocol = kwargs.get('protocol', 'https')
        self.domain = kwargs.get('domain', 'api.sumologic.com')
        self.api = kwargs.get('api', '/api/v1')
        api_path = '%s' % self.api
        self.url = '%s://%s%s' % (self.protocol, self.domain, api_path)
        self.debug_mode = kwargs.get('debug', False)

    def set_debug(self, debug):
        """ Enables or disables debug mode
            :param debug: boolean (True/False)
        """
        self.debug_mode = debug

    def debug(self, content=None):
        """ Print out the values of class variables
            :param content: contents to print out
        """
        if self.debug_mode:
            options = [
                'auth', 'protocol', 'domain', 'api', 'url', 'debug_mode'
            ]
            for option in options:
                logging.debug('%s => %s' % (option, getattr(self, option)))

            if content:
                logging.debug('Content: %s ' % content)

    def get_url(self):
        """ Returns full api url """
        return self.url

    def get_auth(self):
        """ Returns api auth details """
        return self.auth
