# Copyright (C) 2007-2015 various contributors (see AUTHORS)
#
# This file is part of Python-EFL.
#
# Python-EFL is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 3 of the License, or (at your option) any later version.
#
# Python-EFL is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this Python-EFL.  If not, see <http://www.gnu.org/licenses/>.
#

"""

:mod:`general` Module
#####################


.. _General:

General
=======

General Elementary API. Functions that don't relate to
Elementary objects specifically.

Here are documented functions which init/shutdown the library,
that apply to generic Elementary objects, that deal with
configuration, et cetera.


.. _Fingers:

Fingers
=======

Elementary is designed to be finger-friendly for touchscreens,
and so in addition to scaling for display resolution, it can
also scale based on finger "resolution" (or size). You can then
customize the granularity of the areas meant to receive clicks
on touchscreens.

Different profiles may have pre-set values for finger sizes.


Enumerations
============

.. _Elm_Object_Layer:

Object layers
-------------

.. versionadded:: 1.14

.. data:: ELM_OBJECT_LAYER_BACKGROUND

    where to place backgrounds

.. data:: ELM_OBJECT_LAYER_DEFAULT

    Evas_Object default layer (and thus for Elementary)

.. data:: ELM_OBJECT_LAYER_FOCUS

    where focus object visualization is

.. data:: ELM_OBJECT_LAYER_TOOLTIP

    where to show tooltips

.. data:: ELM_OBJECT_LAYER_CURSOR

    where to show cursors

.. data:: ELM_OBJECT_LAYER_LAST

    last layer known by Elementary


.. _Elm_Policy:

Policy types
------------

.. data:: ELM_POLICY_QUIT

    Under which circumstances the application should quit automatically.

.. data:: ELM_POLICY_EXIT

    Defines elm_exit() behaviour. (since 1.8)

.. data:: ELM_POLICY_THROTTLE

    Defines how throttling should work (since 1.8)


.. _Elm_Policy_Quit:

Quit policy types
-----------------

.. data:: ELM_POLICY_QUIT_NONE

    Never quit the application automatically

.. data:: ELM_POLICY_QUIT_LAST_WINDOW_CLOSED

    Quit when the application's last window is closed


.. _Elm_Policy_Exit:

Exit policy types
-----------------

Possible values for the ELM_POLICY_EXIT policy.

.. data:: ELM_POLICY_EXIT_NONE

    Just quit the main loop on exit().

.. data:: ELM_POLICY_EXIT_WINDOWS_DEL

    Delete all the windows after quitting the main loop.


.. _Elm_Policy_Throttle:

Throttle policy types
---------------------

Possible values for the #ELM_POLICY_THROTTLE policy.

.. data:: ELM_POLICY_THROTTLE_CONFIG

    Do whatever elementary config is configured to do.

.. data:: ELM_POLICY_THROTTLE_HIDDEN_ALWAYS

    Always throttle when all windows are no longer visible.

.. data:: ELM_POLICY_THROTTLE_NEVER

    Never throttle when windows are all hidden, regardless of config settings.


.. _Elm_Process_State:

Elm_Process_State
-----------------

.. data:: ELM_PROCESS_STATE_FOREGROUND

    The process is in a foreground/active/running state - work as normal.

    .. versionadded:: 1.12

.. data:: ELM_PROCESS_STATE_BACKGROUND

    The process is in the bacgkround, so you may want to stop animating,
    fetching data as often etc.

    .. versionadded:: 1.12


.. _Elm_Sys_Notify_Closed_Reason:

Notify close reasons
--------------------

The reason the notification was closed

.. data:: ELM_SYS_NOTIFY_CLOSED_EXPIRED

    The notification expired.

    .. versionadded:: 1.10

.. data:: ELM_SYS_NOTIFY_CLOSED_DISMISSED

    The notification was dismissed by the user.

    .. versionadded:: 1.10

.. data:: ELM_SYS_NOTIFY_CLOSED_REQUESTED

    The notification was closed by a call to CloseNotification method.

    .. versionadded:: 1.10

.. data:: ELM_SYS_NOTIFY_CLOSED_UNDEFINED

    Undefined/reserved reasons.

    .. versionadded:: 1.10


.. _Elm_Sys_Notify_Urgency:

Notify urgency levels
---------------------

Urgency levels of a notification

:see: :py:func:`sys_notify_send`

.. data:: ELM_SYS_NOTIFY_URGENCY_LOW

    Low

    .. versionadded:: 1.10

.. data:: ELM_SYS_NOTIFY_URGENCY_NORMAL

    Normal

    .. versionadded:: 1.10

.. data:: ELM_SYS_NOTIFY_URGENCY_CRITICAL

    Critical

    .. versionadded:: 1.10


.. _Elm_Glob_Match_Flags:

Glob matching
-------------

Glob matching bitfiled flags

.. data:: ELM_GLOB_MATCH_NO_ESCAPE

    Treat backslash as an ordinary character instead of escape.

    .. versionadded:: 1.11

.. data:: ELM_GLOB_MATCH_PATH

    Match a slash in string only with a slash in pattern and not by an
    asterisk (*) or a question mark (?) metacharacter, nor by a bracket
    expression ([]) containing a slash.

    .. versionadded:: 1.11

.. data:: ELM_GLOB_MATCH_PERIOD

    Leading period in string has to be matched exactly by a period in
    pattern. A period is considered to be leading if it is the first
    character in string, or if both ELM_GLOB_MATCH_PATH is set and the
    period immediately follows a slash.

    .. versionadded:: 1.11

.. data:: ELM_GLOB_MATCH_NOCASE

    The pattern is matched case-insensitively.

    .. versionadded:: 1.11


Inheritance diagram
===================

.. inheritance-diagram:: efl.elementary.general
    :parts: 2

"""

from cpython cimport PyUnicode_AsUTF8String, PyMem_Malloc, Py_DECREF, Py_INCREF
from libc.string cimport memcpy

from efl.evas cimport Object as evasObject

from efl.utils.conversions cimport _touni, _ctouni, \
    python_list_strings_to_eina_list, eina_list_strings_to_python_list

from efl.utils.logger cimport add_logger

from efl.eina cimport EINA_LOG_DOM_DBG, EINA_LOG_DOM_INFO, \
    EINA_LOG_DOM_WARN, EINA_LOG_DOM_ERR, EINA_LOG_DOM_CRIT

from efl.ecore cimport Event, EventHandler, _event_mapping_register

import sys
import traceback
import atexit


elm_log = add_logger("efl.elementary")
cdef int PY_EFL_ELM_LOG_DOMAIN = elm_log.eina_log_domain


cdef class ConfigAllChanged(Event):
    cdef int _set_obj(self, void *o) except 0:
        return 1

    def __repr__(self):
        return "<%s()>" % (self.__class__.__name__,)


cdef class PolicyChanged(Event):

    cdef:
        public unsigned int policy
        public int new_value
        public int old_value

    cdef int _set_obj(self, void *o) except 0:
        cdef Elm_Event_Policy_Changed *obj
        obj = <Elm_Event_Policy_Changed *>o
        self.policy = obj.policy
        self.new_value = obj.new_value
        self.old_value = obj.old_value
        return 1

    def __repr__(self):
        return "<%s(policy=%d, new_value=%d, old_value=%d)>" % (
            self.__class__.__name__,
            self.policy, self.new_value, self.old_value)


cdef class ProcessBackground(Event):
    cdef int _set_obj(self, void *o) except 0:
        return 1

    def __repr__(self):
        return "<%s()>" % (self.__class__.__name__,)


cdef class ProcessForeground(Event):
    cdef int _set_obj(self, void *o) except 0:
        return 1

    def __repr__(self):
        return "<%s()>" % (self.__class__.__name__,)


def init():
    """Initialize Elementary

    :return int: The init counter value.

    This function initializes Elementary and increments a counter of the number
    of calls to it. It returns the new counter's value.

    .. versionchanged:: 1.14

        The Python module calls this function when it is imported so you
        should no longer have any need to call this manually. Calling it does
        not carry any penalty though.

    """
    EINA_LOG_DOM_INFO(PY_EFL_ELM_LOG_DOMAIN,
        "Initializing efl.elementary", NULL)

    # FIXME: Why are we passing the cl args to elm_init here?

    cdef:
        int argc, i, arg_len
        char **argv
        char *arg
        int ret

    argc = len(sys.argv)
    argv = <char **>PyMem_Malloc(argc * sizeof(char *))
    for i in range(argc):
        t = sys.argv[i]
        if isinstance(t, unicode): t = PyUnicode_AsUTF8String(t)
        arg = t
        arg_len = len(arg)
        argv[i] = <char *>PyMem_Malloc(arg_len + 1)
        memcpy(argv[i], arg, arg_len + 1)

    return elm_init(argc, argv)

def shutdown():
    """Shut down Elementary

    :return int: The init counter value.

    This should be called at the end of your application, just before it ceases
    to do any more processing. This will clean up any permanent resources your
    application may have allocated via Elementary that would otherwise persist.

    .. note::

        shutdown() will iterate main loop until all ecore_evas are freed. There
        is a possibility to call your ecore callbacks(timer, animator, event,
        job, and etc.) in shutdown()

    .. versionchanged:: 1.14

        The Python module calls this function when it is exiting so you
        should no longer have any need to call this manually. Calling it does
        not carry any penalty though.

    """
    EINA_LOG_DOM_INFO(PY_EFL_ELM_LOG_DOMAIN,
        "Shutting down efl.elementary", NULL)
    return elm_shutdown()


init()
atexit.register(shutdown)

_event_mapping_register(ELM_EVENT_CONFIG_ALL_CHANGED, ConfigAllChanged)
_event_mapping_register(ELM_EVENT_POLICY_CHANGED, PolicyChanged)
_event_mapping_register(ELM_EVENT_PROCESS_BACKGROUND, ProcessBackground)
_event_mapping_register(ELM_EVENT_PROCESS_FOREGROUND, ProcessForeground)


cdef void py_elm_sys_notify_send_cb(void *data, unsigned int id):
    cdef object func, func_data
    func, func_data = <object>data
    # FIXME: Is this cb called more than once? Py_DECREF if not.
    try:
        func(func_data, id)
    except Exception:
        traceback.print_exc()


def on_ethumb_connect(func, *args, **kwargs):
    """Use this to set a handler for the ethumb connect event.

    .. versionadded:: 1.14
    """
    return EventHandler(ELM_ECORE_EVENT_ETHUMB_CONNECT, func, *args, **kwargs)


def on_config_all_changed(func, *args, **kwargs):
    """Use this to set a handler for the config all changed event.

    Emitted when the application has reconfigured elementary settings due to an
    external configuration tool asking it to.

    .. versionadded:: 1.14
    """
    return EventHandler(ELM_EVENT_CONFIG_ALL_CHANGED, func, *args, **kwargs)


def on_policy_changed(func, *args, **kwargs):
    """Use this to set a handler for the policy changed event.

    Emitted when any Elementary's policy value is changed.

    .. versionadded:: 1.14
    """
    return EventHandler(ELM_EVENT_POLICY_CHANGED, func, *args, **kwargs)


def on_process_background(func, *args, **kwargs):
    """Use this to set a handler for the process background event.

    Emitted when nothing is visible and the process as a whole should go into a
    background state.

    .. versionadded:: 1.14
    """
    return EventHandler(ELM_EVENT_PROCESS_BACKGROUND, func, *args, **kwargs)


def on_process_background(func, *args, **kwargs):
    """Use this to set a handler for the process foreground event.

    Emitted when going from nothing being visible to at least one window being
    visible.

    .. versionadded:: 1.14
    """
    return EventHandler(ELM_EVENT_PROCESS_FOREGROUND, func, *args, **kwargs)


def on_sys_notify_notification_closed(func, *args, **kargs):
    return EventHandler(
        ELM_EVENT_SYS_NOTIFY_NOTIFICATION_CLOSED, func, *args, **kargs
        )


def on_sys_notify_action_invoked(func, *args, **kargs):
    return EventHandler(
        ELM_EVENT_SYS_NOTIFY_NOTIFICATION_CLOSED, func, *args, **kargs
        )


cdef class FontProperties(object):

    """Elementary font properties"""

    cdef Elm_Font_Properties *efp

    property name:
        """:type: unicode"""
        def __set__(self, value):
            if isinstance(value, unicode): value = PyUnicode_AsUTF8String(value)
            self.efp.name = value

        def __get__(self):
            return _ctouni(self.efp.name)

    property styles:
        """:type: list of strings"""
        def __set__(self, value):
            self.efp.styles = python_list_strings_to_eina_list(value)

        def __get__(self):
            return eina_list_strings_to_python_list(self.efp.styles)


def run():
    """Run Elementary's main loop

    This call should be issued just after all initialization is completed. This
    function will not return until exit() is called. It will keep looping,
    running the main (event/processing) loop for Elementary.

    """
    EINA_LOG_DOM_DBG(PY_EFL_ELM_LOG_DOMAIN,
        "Starting up main loop.", NULL)
    with nogil:
        elm_run()

def exit():
    """Ask to exit Elementary's main loop

    If this call is issued, it will flag the main loop to cease processing and
    return back to its parent function (usually your elm_main() function). This
    does not mean the main loop instantly quits. So your ecore callbacks(timer,
    animator, event, job, and etc.) have chances to be called even after
    exit().

    .. note::

        By using the appropriate :attr:`ELM_POLICY_QUIT` on your Elementary
        applications, you'll be able to get this function called automatically
        for you.

    """
    EINA_LOG_DOM_DBG(PY_EFL_ELM_LOG_DOMAIN,
        "Ending main loop.", NULL)
    elm_exit()

def policy_set(Elm_Policy policy, value):
    """Set new policy value.

    This will emit the ecore event ``ELM_EVENT_POLICY_CHANGED`` in the main
    loop giving the event information Elm_Event_Policy_Changed with
    policy identifier, new and old values.

    :param policy: policy identifier as in Elm_Policy.
    :type policy: :ref:`Elm_Policy`
    :param value: policy value, depends on identifiers, usually there is
        an enumeration with the same prefix as the policy name, for
        example: ELM_POLICY_QUIT and Elm_Policy_Quit
        (ELM_POLICY_QUIT_NONE, ELM_POLICY_QUIT_LAST_WINDOW_CLOSED).
    :type value: :ref:`Elm_Policy_Quit`

    :return: True on success or False on error (right
        now just invalid policy identifier, but in future policy
        value might be enforced).

    """
    # TODO: add a function for setting a callback for the event described above
    return bool(elm_policy_set(policy, value))

def policy_get(Elm_Policy policy):
    """Gets the policy value set for given identifier.

    :param policy: policy identifier as in Elm_Policy.
    :type policy: :ref:`Elm_Policy`

    :return: policy value. Will be 0 if policy identifier is invalid.
    :rtype: :ref:`Elm_Policy_Quit`

    """
    return elm_policy_get(policy)

def process_state_get():
    """Get the process state as a while.

    The process may logically be some runnable state. a "foreground" application
    runs as normal and may be user-visible or "active" in some way. A
    background application is not user-visible or otherwise important and
    likely should release resources and not wake up often or process much.

    :return: The current process state
    :rtype: :ref:`Elm_Process_State`

    .. versionadded:: 1.12

    """
    return elm_process_state_get()

def coords_finger_size_adjust(int times_w, int w, int times_h, int h):
    """Adjust size of an element for finger usage.

    :param times_w: How many fingers should fit horizontally
    :type times_w: int
    :param w: Width size to adjust
    :type w: int
    :param times_h: How many fingers should fit vertically
    :type times_h: int
    :param h: Height size to adjust
    :type h: int

    :return: The adjusted width and height
    :rtype: (int **w**, int **h**)

    This takes width and height sizes (in pixels) as input and a
    size multiple (which is how many fingers you want to place
    within the area, being "finger" the size set by
    elm_config_finger_size_set()), and adjusts the size to be large enough
    to accommodate the resulting size -- if it doesn't already
    accommodate it.

    .. note:: This is kind of low level Elementary call, most useful
        on size evaluation times for widgets. An external user wouldn't
        be calling, most of the time.

    """
    cdef Evas_Coord width = w, height = h
    elm_coords_finger_size_adjust(times_w, &width, times_h, &height)
    return (width, height)

def language_set(lang not None):
    """Change the language of the current application

    The ``lang`` passed must be the full name of the locale to use, for
    example ``en_US.utf8`` or ``es_ES@euro``.

    Changing language with this function will make Elementary run through
    all its widgets, translating strings set with
    elm_object_domain_translatable_part_text_set(). This way, an entire
    UI can have its language changed without having to restart the program.

    For more complex cases, like having formatted strings that need
    translation, widgets will also emit a "language,changed" signal that
    the user can listen to and manually translate the text.

    :param lang: Language to set, must be the full name of the locale

    """
    if isinstance(lang, unicode): lang = PyUnicode_AsUTF8String(lang)
    elm_language_set(<const char *>lang)

def cache_all_flush():
    """Frees all data that was in cache and is not currently being used to reduce
    memory usage. This frees Edje's, Evas' and Eet's cache.

    .. note:: Evas caches are flushed for every canvas associated with a window.

    .. versionadded:: 1.8

    """
    elm_cache_all_flush()

def font_properties_get(font not None):
    """Translate a font (family) name string in fontconfig's font names
    syntax into a FontProperties object.

    :param font: The font name and styles string
    :return: the font properties object

    .. note:: The reverse translation can be achieved with
        :py:func:`font_fontconfig_name_get`, for one style only (single font
        instance, not family).

    .. versionadded:: 1.8

    """
    if isinstance(font, unicode): font = PyUnicode_AsUTF8String(font)
    cdef FontProperties ret = FontProperties.__new__()

    ret.efp = elm_font_properties_get(<const char *>font)

    return ret

def font_properties_free(FontProperties fp):
    """Free font properties return by font_properties_get().

    :param fp: the font properties struct

    .. versionadded:: 1.8

    """
    elm_font_properties_free(fp.efp)
    Py_DECREF(fp)

def font_fontconfig_name_get(font_name, style = None):
    """Translate a font name, bound to a style, into fontconfig's font names
    syntax.

    :param font_name: The font (family) name
    :param style: The given style (may be None)

    :return: the font name and style string

    .. note:: The reverse translation can be achieved with
        :py:func:`font_properties_get`, for one style only (single font
        instance, not family).

    .. versionadded:: 1.8

    """
    cdef:
        unicode ret
        char *fc_name
    if isinstance(font_name, unicode): font_name = PyUnicode_AsUTF8String(font_name)
    if isinstance(style, unicode): style = PyUnicode_AsUTF8String(style)
    fc_name = elm_font_fontconfig_name_get(
        <const char *>font_name,
        <const char *>style if style is not None else NULL
        )

    ret = _touni(fc_name)
    elm_font_fontconfig_name_free(fc_name)
    return ret

# TODO: Create an Eina_Hash -> dict conversion function for this
# def font_available_hash_add(list):
#     """Create a font hash table of available system fonts.

#     One must call it with ``list`` being the return value of
#     evas_font_available_list(). The hash will be indexed by font
#     (family) names, being its values ``Elm_Font_Properties`` blobs.

#     :param list: The list of available system fonts, as returned by
#     evas_font_available_list().
#     :return: the font hash.

#     .. note:: The user is supposed to get it populated at least with 3
#     default font families (Sans, Serif, Monospace), which should be
#     present on most systems.

#     """
#     EAPI Eina_Hash *elm_font_available_hash_add(Eina_List *list)


#     """Free the hash returned by elm_font_available_hash_add().

#     :param hash: the hash to be freed.

#     """
#     elm_font_available_hash_del(Eina_Hash *hash)

def object_tree_dump(evasObject top):
    """Print Tree object hierarchy in stdout

    :param top: The root object

    .. versionadded:: 1.8

    """
    elm_object_tree_dump(top.obj)

def object_tree_dot_dump(evasObject top, path):
    """Print Elm Objects tree hierarchy in file as dot(graphviz) syntax.

    :param top: The root object
    :param path: The path of output file

    .. versionadded:: 1.8

    """
    if isinstance(path, unicode): path = PyUnicode_AsUTF8String(path)
    elm_object_tree_dot_dump(top.obj, <const char *>path)

def sys_notify_close(unsigned int id):
    """Causes a notification to be forcefully closed and removed from the user's
    view. It can be used, for example, in the event that what the notification
    pertains to is no longer relevant, or to cancel a notification * with no
    expiration time.

    :param id: Notification id

    .. note:: If the notification no longer exists,
        an empty D-BUS Error message is sent back.

    .. versionadded:: 1.10

    """
    elm_sys_notify_close(id)

def sys_notify_send(
    unsigned int replaces_id=0,
    icon=None, summary=None, body=None,
    Elm_Sys_Notify_Urgency urgency=ELM_SYS_NOTIFY_URGENCY_NORMAL,
    int timeout=-1, cb=None, cb_data=None
    ):
    """Sends a notification to the notification server.

    :param replaces_id: Notification ID that this notification replaces.
        The value 0 means a new notification.
    :param icon: The optional program icon of the calling application.
    :param summary: The summary text briefly describing the notification.
    :param body: The optional detailed body text. Can be empty.
    :param urgency: The urgency level.
    :param timeout: Timeout display in milliseconds.
    :param cb: Callback used to retrieve the notification id
        return by the Notification Server.
    :param cb_data: Optional context data

    .. versionadded:: 1.10

    """
    if cb is not None:
        if not callable(cb):
            raise TypeError("cb must be callable")
        py_cb_data = (cb, cb_data)
        Py_INCREF(py_cb_data)

    if isinstance(icon, unicode): icon = PyUnicode_AsUTF8String(icon)
    if isinstance(summary, unicode): summary = PyUnicode_AsUTF8String(summary)
    if isinstance(body, unicode): body = PyUnicode_AsUTF8String(body)
    elm_sys_notify_send(
        replaces_id,
        <const char *>icon if icon is not None else NULL,
        <const char *>summary if summary is not None else NULL,
        <const char *>body if body is not None else NULL,
        urgency,
        timeout,
        <Elm_Sys_Notify_Send_Cb>py_elm_sys_notify_send_cb if cb is not None else NULL,
        <const void *>py_cb_data if cb is not None else NULL
        )

