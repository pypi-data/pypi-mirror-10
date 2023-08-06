"""A simple tool to test the ZMQ kernel by publishing messages and checking the response."""

# Copyright (c) IPython Development Team.
# Distributed under the terms of the Modified BSD License.

from __future__ import absolute_import, print_function

import atexit

try:
    from queue import Empty  # Py 3
except ImportError:
    from Queue import Empty  # Py 2

import nose.tools as nt
from jupyter_client import manager

#-------------------------------------------------------------------------
# Globals
#-------------------------------------------------------------------------

STARTUP_TIMEOUT = 60
TIMEOUT = 15

KM = None
KC = None
validate_message = None

#-------------------------------------------------------------------------
# Code to setup the kernel for testing
#-------------------------------------------------------------------------


def start_new_kernel(kernel='python', **kwargs):
    """start a new kernel, and return its Manager and Client
    """
    return manager.start_new_kernel(startup_timeout=STARTUP_TIMEOUT, kernel_name=kernel, **kwargs)


def flush_channels(kc=None):
    """flush any messages waiting on the queue"""

    if kc is None:
        kc = KC
    for channel in (kc.shell_channel, kc.iopub_channel):
        while True:
            try:
                msg = channel.get_msg(block=True, timeout=0.1)
            except Empty:
                break
            else:
                validate_message(msg)


def execute(code='', kc=None, **kwargs):
    """wrapper for doing common steps for validating an execution request"""
    if kc is None:
        kc = KC
    msg_id = kc.execute(code=code, **kwargs)
    reply = kc.get_shell_msg(timeout=TIMEOUT)
    validate_message(reply, 'execute_reply', msg_id)
    busy = kc.get_iopub_msg(timeout=TIMEOUT)
    validate_message(busy, 'status', msg_id)
    nt.assert_equal(busy['content']['execution_state'], 'busy')

    if not kwargs.get('silent'):
        execute_input = kc.get_iopub_msg(timeout=TIMEOUT)
        validate_message(execute_input, 'execute_input', msg_id)
        nt.assert_equal(execute_input['content']['code'], code)

    return msg_id, reply['content']


def start_global_kernel(kernel='python'):
    """start the global kernel (if it isn't running) and return its client"""
    global KM, KC
    if KM is None:
        KM, KC = start_new_kernel(kernel)
        atexit.register(stop_global_kernel)
    else:
        flush_channels(KC)
    return KC


def stop_global_kernel():
    """Stop the global shared kernel instance, if it exists"""
    global KM, KC
    KC.stop_channels()
    KC = None
    if KM is None:
        return
    KM.shutdown_kernel(now=True)
    KM = None

#-----------------------------------------------------------------------------
# Test methods
#-----------------------------------------------------------------------------

# Shell channel


def check_execute(test_code):
    flush_channels()

    msg_id = KC.execute(code=test_code)
    reply = KC.get_shell_msg(timeout=TIMEOUT)
    validate_message(reply, 'execute_reply', msg_id)
    return reply


def check_user_expressions(test_code, user_expression):
    flush_channels()

    msg_id, reply = execute(
        code=test_code, user_expressions=dict(foo=user_expression))
    user_expressions = reply['user_expressions']
    return user_expressions


def check_oinfo(inspect_object):
    flush_channels()

    msg_id = KC.inspect(inspect_object)
    reply = KC.get_shell_msg(timeout=TIMEOUT)
    validate_message(reply, 'inspect_reply', msg_id)
    return reply


def check_complete(test_code):
    flush_channels()

    msg_id = KC.complete(test_code, 2)
    reply = KC.get_shell_msg(timeout=TIMEOUT)
    validate_message(reply, 'complete_reply', msg_id)
    return reply


def check_kernel_info():
    flush_channels()

    msg_id = KC.kernel_info()
    reply = KC.get_shell_msg(timeout=TIMEOUT)
    # Do not validate because kernel info versions will be different
    # for each kernel - leave it to developer to check the result
    #validate_message(reply, 'kernel_info_reply', msg_id)
    return reply


def check_single_payload(test_code):
    flush_channels()
    msg_id, reply = execute(code=test_code)
    payload = reply['payload']
    return payload


def check_is_complete(test_code):
    flush_channels()

    msg_id = KC.is_complete(test_code)
    reply = KC.get_shell_msg(timeout=TIMEOUT)
    validate_message(reply, 'is_complete_reply', msg_id)
    return reply


# The below 3 history tests are run for the last one command and
# with a .* pattern so that we only check the test code. This is 
# enough to validate all the parts of the message spec

def check_history_range(test_code):
    flush_channels()

    msg_id_exec = KC.execute(code=test_code, store_history=True)
    reply_exec = KC.get_shell_msg(timeout=TIMEOUT)

    msg_id = KC.history(
        hist_access_type='range', raw=True, output=True, start=1, stop=2, session=0)
    reply = KC.get_shell_msg(timeout=TIMEOUT)
    validate_message(reply, 'history_reply', msg_id)
    content = reply['content']
    return content


def check_history_tail(test_code):
    flush_channels()

    msg_id_exec = KC.execute(code=test_code, store_history=True)
    reply_exec = KC.get_shell_msg(timeout=TIMEOUT)

    msg_id = KC.history(
        hist_access_type='tail', raw=True, output=True, n=1, session=0)
    reply = KC.get_shell_msg(timeout=TIMEOUT)
    validate_message(reply, 'history_reply', msg_id)
    content = reply['content']
    return content


def check_history_search(test_code):
    flush_channels()

    msg_id_exec = KC.execute(code=test_code, store_history=True)
    reply_exec = KC.get_shell_msg(timeout=TIMEOUT)

    msg_id = KC.history(
        hist_access_type='search', raw=True, output=True, n=1, pattern='.*', session=0)
    reply = KC.get_shell_msg(timeout=TIMEOUT)
    validate_message(reply, 'history_reply', msg_id)
    content = reply['content']
    return content

# IOPub channel


def check_stream(test_code):
    flush_channels()

    msg_id, reply = execute(test_code)

    stdout = KC.iopub_channel.get_msg(timeout=TIMEOUT)
    validate_message(stdout, 'stream', msg_id)
    content = stdout['content']
    return content


def check_display_data(test_code):
    flush_channels()

    msg_id, reply = execute(test_code)

    display = KC.iopub_channel.get_msg(timeout=TIMEOUT)
    validate_message(display, 'display_data', parent=msg_id)
    data = display['content']['data']
    return data
