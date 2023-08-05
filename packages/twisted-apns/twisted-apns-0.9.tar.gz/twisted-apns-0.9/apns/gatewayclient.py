import logging

from twisted.internet import ssl
from twisted.internet.protocol import Protocol, ReconnectingClientFactory

from apns.errorresponse import ErrorResponse
from apns.listenable import Listenable


logger = logging.getLogger(__name__)


class GatewayClientError(Exception):
    pass


class GatewayClientNotSetError(GatewayClientError):
    pass


class GatewayClient(Protocol):
    def connectionMade(self):
        logger.debug('Gateway connection made: %s:%d', self.factory.hostname,
                     self.factory.port)
        self.factory.connectionMade(self)

    def send(self, notification):
        stream = notification.to_binary_string()
        self.transport.write(stream)

    def dataReceived(self, data):
        error = ErrorResponse()
        error.from_binary_string(data)
        self.factory.errorReceived(error)


class GatewayClientFactory(ReconnectingClientFactory, Listenable):
    protocol = GatewayClient
    maxDelay = 10
    ENDPOINTS = {
        'pub': ('gateway.push.apple.com', 2195),
        'dev': ('gateway.sandbox.push.apple.com', 2195)
    }
    EVENT_ERROR_RECEIVED = 'error received'

    def __init__(self, endpoint, pem):
        Listenable.__init__(self)
        self.hostname, self.port = self.ENDPOINTS[endpoint]
        self.client = None

        with open(pem) as f:
            self.certificate = ssl.PrivateCertificate.loadPEM(f.read())

    def connectionMade(self, client):
        self.client = client

    def _onConnectionLost(self):
        self.client = None

    def errorReceived(self, error):
        logger.debug('Gateway error received: %s', error)
        self.dispatchEvent(self.EVENT_ERROR_RECEIVED, error)

    def clientConnectionFailed(self, connector, reason):
        logger.debug('Gateway connection failed: %s',
                     reason.getErrorMessage())
        self._onConnectionLost()
        return ReconnectingClientFactory.clientConnectionFailed(self,
                                                                connector,
                                                                reason)

    def clientConnectionLost(self, connector, reason):
        logger.debug('Gateway connection lost: %s',
                     reason.getErrorMessage())
        self._onConnectionLost()
        return ReconnectingClientFactory.clientConnectionLost(self,
                                                              connector,
                                                              reason)

    @property
    def connected(self):
        return self.client is not None

    def send(self, notification):
        logger.debug('Gateway send notification')

        if self.client is None:
            raise GatewayClientNotSetError()

        self.client.send(notification)
