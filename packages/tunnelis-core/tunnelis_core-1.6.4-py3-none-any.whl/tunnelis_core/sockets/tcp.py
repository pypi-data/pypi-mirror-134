from typing import Callable, Set, Tuple
from uuid import uuid1
from zmq import IDENTITY as ZMQ_IDENTITY, STREAM as ZMQ_STREAM
from zmq.eventloop.zmqstream import ZMQStream
from zmq.sugar.context import Context

TCPMessageCallback = Callable[['TCPSocket', bytes, bytes], None]
TCPConnectionCallback = Callable[['TCPSocket', bytes], None]


class TCPSocket:
    """
    A socket for asynchronous TCP communications.

    A wrapper class around ZMQ sockets of type ZMQ_STREAM.

    """

    __message_handler: TCPMessageCallback = None
    __connection_handler: TCPConnectionCallback = None
    __disconnection_handler: TCPConnectionCallback = None

    __connected_clients: Set[bytes] = set()

    def __init__(self):
        """
        Initializes socket.

        """

        self.id = str(uuid1()).encode()

        self.__zmq_context = Context()

        self.__socket = self.__zmq_context.socket(ZMQ_STREAM)
        self.stream = ZMQStream(self.__socket)
        self.stream.on_recv(self.__message_handler)

    def bind(self, port: int) -> None:
        """
        Bind socket to a TCP address and start listening for communications.

        Parameters
        ----------
        port : int
            The network port at which to bind the socket.
            When set to a non-positive integer the socket will bind to a random free port.

        """

        if port > 0:
            self.__socket.bind(f'tcp://*:{port}')
            self.port = port
        else:
            self.port = self.__socket.bind_to_random_port('tcp://*', min_port=30000)

    def connect(self, address: Tuple[str, int]) -> None:
        """
        Connect to a TCP address.

        Parameters
        ----------
        address : Tuple(str, int)
            The TCP network address to which to connect to.

        """

        host, port = address
        self.__socket.connect(f'tcp://{host}:{port}')

        # It is only required to set an identity when in client mode.
        self.identity = self.__socket.getsockopt(ZMQ_IDENTITY)

    def send(self, client_identity: bytes, message: bytes) -> None:
        """
        Send raw application data to a remote client.

        Parameters
        ----------
        identity : bytes
            The identity (ZMQ_IDENTITY) of the remote client.

        message : bytes
            The TCP message to be sent.

        """
        if client_identity:  # server mode
            self.stream.send_multipart([client_identity, message])
        else:  # client mode
            self.stream.send_multipart([self.identity, message])

    def close(self) -> None:
        """
        Close endpoint.

        """
        self.stream.close()
        self.__socket.close()
        self.__zmq_context.term()

    def set_message_handler(self, handler: TCPMessageCallback) -> None:
        """
        Set the callback function to handle incoming TCP messages.

        Parameters
        ----------
        handler : Callable(TCPSocket, bytes, bytes) -> None
            The callback function.

        """
        self.__message_handler = handler

    def set_connection_handler(self, handler: TCPConnectionCallback) -> None:
        """
        Set the callback function to handle new connections to/from other TCP applications.

        Parameters
        ----------
        handler : Callable(TCPSocket, bytes) -> None
            The callback function.

        """
        self.__connection_handler = handler

    def set_disconnection_handler(self, handler: TCPConnectionCallback) -> None:
        """
        Set the callback function to handle disconnections from other TCP applications.

        Parameters
        ----------
        handler : Callable(TCPSocket, bytes) -> None
            The callback function.

        """
        self.__disconnection_handler = handler

    def unset_message_handler(self) -> None:
        """
        Stop handling incoming TCP messages.

        """
        self.__message_handler = None

    def unset_connection_handler(self) -> None:
        """
        Stop handling connections to/from other TCP applications.

        """
        self.__connection_handler = None

    def unset_disconnection_handler(self) -> None:
        """
        Stop handling disconnections from other TCP applications.

        """
        self.__disconnection_handler = None

    def __message_handler(self, message: Tuple[bytes, bytes]) -> None:
        """
        A generic message handler.
        Forwards received messages to their proper message handlers.

        Parameters
        ----------
        message : Tuple(bytes, bytes)
            The received message.

        """

        identity, payload = message

        if not payload:

            if identity not in self.__connected_clients:

                if identity != self.id:

                    self.__connected_clients.add(identity)
                    if self.__connection_handler:
                        self.__connection_handler(self, identity)

            else:

                self.__connected_clients.remove(identity)
                if self.__disconnection_handler:
                    self.__disconnection_handler(self, identity)

        else:

            if self.__message_handler:
                self.__message_handler(self, identity, payload)
