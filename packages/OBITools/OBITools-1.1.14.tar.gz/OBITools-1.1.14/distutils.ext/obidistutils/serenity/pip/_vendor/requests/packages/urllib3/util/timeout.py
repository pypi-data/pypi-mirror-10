from socket import _GLOBAL_DEFAULT_TIMEOUT
import time

from ..exceptions import TimeoutStateError


def current_time():
    """
    Retrieve the current time, this function is mocked out in unit testing.
    """
    return time.time()


_Default = object()
# The default timeout to use for socket connections. This is the attribute used
# by httplib to define the default timeout


class Timeout(object):
    """
    Utility object for storing timeout values.

    Example usage:

    .. code-block:: python

        timeout = urllib3.util.Timeout(connect=2.0, read=7.0)
        pool = HTTPConnectionPool('www.google.com', 80, timeout=timeout)
        pool.request(...) # Etc, etc

    :param connect:
        The maximum amount of time to wait for a connection attempt to a server
        to succeed. Omitting the parameter will default the connect timeout to
        the system default, probably `the global default timeout in socket.py
        <http://hg.python.org/cpython/file/603b4d593758/Lib/socket.py#l535>`_.
        None will set an infinite timeout for connection attempts.

    :type connect: integer, float, or None

    :param read:
        The maximum amount of time to wait between consecutive
        read operations for a response from the server. Omitting
        the parameter will default the read timeout to the system
        default, probably `the global default timeout in socket.py
        <http://hg.python.org/cpython/file/603b4d593758/Lib/socket.py#l535>`_.
        None will set an infinite timeout.

    :type read: integer, float, or None

    :param total:
        This combines the connect and read timeouts into one; the read timeout
        will be set to the time leftover from the connect attempt. In the
        event that both a connect timeout and a total are specified, or a read
        timeout and a total are specified, the shorter timeout will be applied.

        Defaults to None.

    :type total: integer, float, or None

    .. note::

        Many factors can affect the total amount of time for urllib3 to return
        an HTTP response. Specifically, Python's DNS resolver does not obey the
        timeout specified on the socket. Other factors that can affect total
        request time include high CPU load, high swap, the program running at a
        low priority level, or other behaviors. The observed running time for
        urllib3 to return a response may be greater than the value passed to
        `total`.

        In addition, the read and total timeouts only measure the time between
        read operations on the socket connecting the client and the server,
        not the total amount of time for the request to return a complete
        response. For most requests, the timeout is raised because the server
        has not sent the first byte in the specified time. This is not always
        the case; if a server streams one byte every fifteen seconds, a timeout
        of 20 seconds will not ever trigger, even though the request will
        take several minutes to complete.

        If your goal is to cut off any request after a set amount of wall clock
        time, consider having a second "watcher" thread to cut off a slow
        request.
    """

    #: A sentinel object representing the default timeout value
    DEFAULT_TIMEOUT = _GLOBAL_DEFAULT_TIMEOUT

    def __init__(self, total=None, connect=_Default, read=_Default):
        self._connect = self._validate_timeout(connect, 'connect')
        self._read = self._validate_timeout(read, 'read')
        self.total = self._validate_timeout(total, 'total')
        self._start_connect = None

    def __str__(self):
        return '%s(connect=%r, read=%r, total=%r)' % (
            type(self).__name__, self._connect, self._read, self.total)


    @classmethod
    def _validate_timeout(cls, value, name):
        """ Check that a timeout attribute is valid

        :param value: The timeout value to validate
        :param name: The name of the timeout attribute to validate. This is used
            for clear error messages
        :return: the value
        :raises ValueError: if the type is not an integer or a float, or if it
            is a numeric value less than zero
        """
        if value is _Default:
            return cls.DEFAULT_TIMEOUT

        if value is None or value is cls.DEFAULT_TIMEOUT:
            return value

        try:
            float(value)
        except (TypeError, ValueError):
            raise ValueError("Timeout value %s was %s, but it must be an "
                             "int or float." % (name, value))

        try:
            if value < 0:
                raise ValueError("Attempted to set %s timeout to %s, but the "
                                 "timeout cannot be set to a value less "
                                 "than 0." % (name, value))
        except TypeError: # Python 3
            raise ValueError("Timeout value %s was %s, but it must be an "
                             "int or float." % (name, value))

        return value

    @classmethod
    def from_float(cls, timeout):
        """ Create a new Timeout from a legacy timeout value.

        The timeout value used by httplib.py sets the same timeout on the
        connect(), and recv() socket requests. This creates a :class:`Timeout`
        object that sets the individual timeouts to the ``timeout`` value passed
        to this function.

        :param timeout: The legacy timeout value
        :type timeout: integer, float, sentinel default object, or None
        :return: a Timeout object
        :rtype: :class:`Timeout`
        """
        return Timeout(read=timeout, connect=timeout)

    def clone(self):
        """ Create a copy of the timeout object

        Timeout properties are stored per-pool but each request needs a fresh
        Timeout object to ensure each one has its own start/stop configured.

        :return: a copy of the timeout object
        :rtype: :class:`Timeout`
        """
        # We can't use copy.deepcopy because that will also create a new object
        # for _GLOBAL_DEFAULT_TIMEOUT, which socket.py uses as a sentinel to
        # detect the user default.
        return Timeout(connect=self._connect, read=self._read,
                       total=self.total)

    def start_connect(self):
        """ Start the timeout clock, used during a connect() attempt

        :raises urllib3.exceptions.TimeoutStateError: if you attempt
            to start a timer that has been started already.
        """
        if self._start_connect is not None:
            raise TimeoutStateError("Timeout timer has already been started.")
        self._start_connect = current_time()
        return self._start_connect

    def get_connect_duration(self):
        """ Gets the time elapsed since the call to :meth:`start_connect`.

        :return: the elapsed time
        :rtype: float
        :raises urllib3.exceptions.TimeoutStateError: if you attempt
            to get duration for a timer that hasn't been started.
        """
        if self._start_connect is None:
            raise TimeoutStateError("Can't get connect duration for timer "
                                    "that has not started.")
        return current_time() - self._start_connect

    @property
    def connect_timeout(self):
        """ Get the value to use when setting a connection timeout.

        This will be a positive float or integer, the value None
        (never timeout), or the default system timeout.

        :return: the connect timeout
        :rtype: int, float, :attr:`Timeout.DEFAULT_TIMEOUT` or None
        """
        if self.total is None:
            return self._connect

        if self._connect is None or self._connect is self.DEFAULT_TIMEOUT:
            return self.total

        return min(self._connect, self.total)

    @property
    def read_timeout(self):
        """ Get the value for the read timeout.

        This assumes some time has elapsed in the connection timeout and
        computes the read timeout appropriately.

        If self.total is set, the read timeout is dependent on the amount of
        time taken by the connect timeout. If the connection time has not been
        established, a :exc:`~urllib3.exceptions.TimeoutStateError` will be
        raised.

        :return: the value to use for the read timeout
        :rtype: int, float, :attr:`Timeout.DEFAULT_TIMEOUT` or None
        :raises urllib3.exceptions.TimeoutStateError: If :meth:`start_connect`
            has not yet been called on this object.
        """
        if (self.total is not None and
            self.total is not self.DEFAULT_TIMEOUT and
            self._read is not None and
            self._read is not self.DEFAULT_TIMEOUT):
            # in case the connect timeout has not yet been established.
            if self._start_connect is None:
                return self._read
            return max(0, min(self.total - self.get_connect_duration(),
                              self._read))
        elif self.total is not None and self.total is not self.DEFAULT_TIMEOUT:
            return max(0, self.total - self.get_connect_duration())
        else:
            return self._read
