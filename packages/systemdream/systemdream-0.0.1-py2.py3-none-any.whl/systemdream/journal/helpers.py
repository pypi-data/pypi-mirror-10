from __future__ import division

__all__ = ('send') #, 'stream')

import traceback as _traceback
import os as _os
from syslog import (LOG_EMERG, LOG_ALERT, LOG_CRIT, LOG_ERR,
                    LOG_WARNING, LOG_NOTICE, LOG_INFO, LOG_DEBUG)

from .utils import _make_line, sendv


def send(MESSAGE, MESSAGE_ID=None,
         CODE_FILE=None, CODE_LINE=None, CODE_FUNC=None,
         **kwargs):
    r"""Send a message to the journal.

    >>> journal.send('Hello world')
    >>> journal.send('Hello, again, world', FIELD2='Greetings!')
    >>> journal.send('Binary message', BINARY=b'\xde\xad\xbe\xef')

    Value of the MESSAGE argument will be used for the MESSAGE=
    field. MESSAGE must be a string and will be sent as UTF-8 to
    the journal.

    MESSAGE_ID can be given to uniquely identify the type of
    message. It must be a string or a uuid.UUID object.

    CODE_LINE, CODE_FILE, and CODE_FUNC can be specified to
    identify the caller. Unless at least on of the three is given,
    values are extracted from the stack frame of the caller of
    send(). CODE_FILE and CODE_FUNC must be strings, CODE_LINE
    must be an integer.

    Additional fields for the journal entry can only be specified
    as keyword arguments. The payload can be either a string or
    bytes. A string will be sent as UTF-8, and bytes will be sent
    as-is to the journal.

    Other useful fields include PRIORITY, SYSLOG_FACILITY,
    SYSLOG_IDENTIFIER, SYSLOG_PID.
    """

    args = ['MESSAGE=' + MESSAGE]

    if MESSAGE_ID is not None:
        id = getattr(MESSAGE_ID, 'hex', MESSAGE_ID)
        args.append('MESSAGE_ID=' + id)

    if CODE_LINE == CODE_FILE == CODE_FUNC == None:
        CODE_FILE, CODE_LINE, CODE_FUNC = \
            _traceback.extract_stack(limit=2)[0][:3]
    if CODE_FILE is not None:
        args.append('CODE_FILE=' + CODE_FILE)
    if CODE_LINE is not None:
        args.append('CODE_LINE={:d}'.format(CODE_LINE))
    if CODE_FUNC is not None:
        args.append('CODE_FUNC=' + CODE_FUNC)

    args.extend(_make_line(key, val) for key, val in kwargs.items())
    return sendv(*args)

def stream(identifier, priority=LOG_DEBUG, level_prefix=False):
    r"""Return a file object wrapping a stream to journal.

    Log messages written to this file as simple newline sepearted
    text strings are written to the journal.

    The file will be line buffered, so messages are actually sent
    after a newline character is written.

    >>> stream = journal.stream('myapp')
    >>> stream
    <open file '<fdopen>', mode 'w' at 0x...>
    >>> stream.write('message...\n')

    will produce the following message in the journal::

      PRIORITY=7
      SYSLOG_IDENTIFIER=myapp
      MESSAGE=message...

    Using the interface with print might be more convinient:

    >>> from __future__ import print_function
    >>> print('message...', file=stream)

    priority is the syslog priority, one of `LOG_EMERG`,
    `LOG_ALERT`, `LOG_CRIT`, `LOG_ERR`, `LOG_WARNING`,
    `LOG_NOTICE`, `LOG_INFO`, `LOG_DEBUG`.

    level_prefix is a boolean. If true, kernel-style log priority
    level prefixes (such as '<1>') are interpreted. See
    sd-daemon(3) for more information.
    """

    fd = stream_fd(identifier, priority, level_prefix)
    return _os.fdopen(fd, 'w', 1)

