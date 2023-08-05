# -*- encoding: utf-8 -*-
__author__ = 'faide'

import asyncio
import json
import aiozmq
from aiozmq import rpc

from sqlalchemy.sql import select
from sqlalchemy.sql import and_
from sqlalchemy import func

from xbus.broker.model import validate_password
from xbus.broker.model import emitter
from xbus.broker.model import envelope
from xbus.broker.model import event
from xbus.broker.model import event_type
from xbus.broker.model import emitter_profile_event_type_rel
from xbus.broker.model import item

from xbus.broker.core.base import XbusBrokerBase


class XbusBrokerFront(XbusBrokerBase):
    """the XbusBrokerFront is in charge of handling emitters on a specific 0mq
    socket. It implements login/logout & new_envelop, new_event

    Before you can call any useful methods on the XbusBrokerFront you'll need
    to obtain a token through the login() call. Once you have a token you will
    need to give it to all subsequent calls.

    If you have finished your session you SHOULD call the logout() method.
    This is important in order to protect yourself. Calling logout will
    invalidate the token and make sure no one can reuse it ever.

    Internally the front server will wait for a backend to come register
    itself.
    As long as the backend is not ready the front will just store the
    envelopes, events and data and acknowledge them to the clients.
    The corresponding envelopes will be marked as waiting as long as no
    backend is present.
    """

    def __init__(self, dbengine, loop=None):
        # at the beginning the backend is None. Then the Front2Back will set
        # a backend in place when one comes to register itself.
        self.backend = None
        self.envelopes = {}
        super(XbusBrokerFront, self).__init__(dbengine, loop=loop)

    @rpc.method
    @asyncio.coroutine
    def login(self, login: str, password: str) -> str:
        """Before doing anything useful you'll need to login into the broker
        we a login/password. If the authentication phase is ok you'll get a
        token that must be provided during other method calls.

        :param login:
         the login you want to authenticate against

        :param password:
         the password that must match your login

        :return:
         Byte token that can be used during the session, or an empty string if
         the token could not be verified (it is the responsibility of the
         caller to ensure the token is correct).
        """

        emitter_row = yield from self.find_emitter_by_login(login)
        emitter_id, emitter_pwd, emitter_profile_id = emitter_row
        if emitter_id and validate_password(password, emitter_pwd):
            token = self.new_token()
            info = {'id': emitter_id, 'login': login,
                    'profile_id': emitter_profile_id}
            info_json = json.dumps(info)
            yield from self.save_key(token, info_json)

        else:
            token = ""

        return token

    @rpc.method
    @asyncio.coroutine
    def logout(self, token: str) -> bool:
        """When you are done using the broker you should call this method to
        make sure your token is destroyed and no one can reuse it

        :param token:
         the token you want to invalidate

        :return:
         True if successful, False otherwise
        """
        res = yield from self.destroy_key(token)
        return res

    @rpc.method
    @asyncio.coroutine
    def start_envelope(self, token: str) -> str:
        """Start a new envelope.

        :param token:
         the emitter's connection token, obtained from the
         :meth:`.XbusBrokerFront.login` method which is exposed on the same
         0mq socket.

        :return:
         The UUID of the new envelope if successful, an empty string otherwise
        """
        emitter_json = yield from self.get_key_info(token)
        if emitter_json is None:
            return ""

        try:
            # lookup the emitters table and find a matching "login"
            emitter_info = json.loads(emitter_json)
            emitter_id = emitter_info['id']
        except KeyError:
            return ""

        envelope_id = self.new_envelope()
        info = {
            'emitter_id': emitter_id,
            'events': {},
            'trigger': asyncio.Future(loop=self.loop)
        }
        self.envelopes[envelope_id] = info

        yield from self.log_new_envelope(envelope_id, emitter_id)

        asyncio.async(
            self.backend_start_envelope(envelope_id),
            loop=self.loop
        )

        return envelope_id

    @rpc.method
    @asyncio.coroutine
    def start_event(self, token: str, envelope_id: str,
                    event_name: str, estimate: int) -> str:
        """Start a new event inside an envelop. Conceptually an event is the
        container of items (which are emitted using :meth:`.XbusBrokerFront
        .login` method on the same 0mq socket. An event is also contained
        inside an envelope with other events potentially of different types.

        :param token:
         the emitter's connection token, obtained from the
         :meth:`.XbusBrokerFront.login` method which is exposed on the same
         0mq socket.

        :param envelope_id:
         the UUID of an envelope previously opened by the emitter using the
         :meth:`.XbusBrokerFront.start_envelope` method which is exposed on
         the same 0mq socket.

        :param event_name:
         the name of the event's type

        :return:
         The UUID of the new event if successful, an empty string otherwise
        """
        emitter_json = yield from self.get_key_info(token)
        if emitter_json is None:
            return ""

        try:
            emitter_info = json.loads(emitter_json)
            emitter_id = emitter_info['id']
            profile_id = emitter_info['profile_id']

        except (ValueError, SyntaxError, KeyError):
            return ""

        try:
            envelope_info = self.envelopes[envelope_id]
            envelope_emitter_id = envelope_info['emitter_id']
            envelope_closed = envelope_info.get('closed', False)
            envelope_forward = envelope_info['forward']

        except KeyError:
            return ""

        if emitter_id != envelope_emitter_id:
            return ""

        if envelope_closed:
            return ""

        type_id, immediate_reply = (
            yield from self.find_event_type_by_name(event_name)
        )

        access = yield from self.check_event_access(profile_id, type_id)
        if access is False:
            # TODO Do something better than print...
            print(
                'Access denied. Emitter profile: %s. Event type: %s - %s.' %
                (profile_id, event_name, type_id)
            )
            return ""

        event_id = self.new_event()
        info = {
            'envelope_id': envelope_id,
            'immediate_reply': immediate_reply,
            'type_id': type_id,
            'recv': 0,
            'sent': 0,
            'trigger': asyncio.Future(loop=self.loop)
        }

        envelope_info['events'][event_id] = info

        yield from self.log_new_event(
            event_id, envelope_id, emitter_id, type_id, estimate
        )

        if envelope_forward:
            asyncio.async(
                self.backend_start_event(
                    envelope_id, event_id, type_id, event_name
                ),
                loop=self.loop
            )

        return event_id

    @rpc.method
    @asyncio.coroutine
    def send_item(self, token: str, envelope_id: str, event_id: str,
                  data: bytes) -> bool:
        """Send an item through XBUS.

        :param token:
         the emitter's connection token, obtained from the
         :meth:`.XbusBrokerFront.login` method which is exposed on the same
         0mq socket.

        :param envelope_id:
         the UUID of an envelope previously opened by the emitter using the
         :meth:`.XbusBrokerFront.start_envelope` method which is exposed on
         the same 0mq socket.

        :param event_id:
         the UUID of the event

        :param data:
         the item data

        :return:
         True if successful, False otherwise
        """
        emitter_json = yield from self.get_key_info(token)
        if emitter_json is None:
            return False

        try:
            emitter_info = json.loads(emitter_json)
            emitter_id = emitter_info['id']
        except (ValueError, SyntaxError, KeyError):
            return False

        try:
            envelope_info = self.envelopes[envelope_id]
            envelope_events = envelope_info['events']
            envelope_emitter_id = envelope_info['emitter_id']
            envelope_forward = envelope_info['forward']
        except KeyError:
            return False

        if emitter_id != envelope_emitter_id:
            return False

        try:
            event_info = envelope_events[event_id]
            index = event_info['recv']
            event_closed = event_info.get('closed', False)
        except KeyError:
            return False

        if event_closed:
            return False

        yield from self.log_sent_item(event_id, index, data)
        event_info['recv'] = index + 1

        if envelope_forward:
            asyncio.async(
                self.backend_send_item(envelope_id, event_id, index, data),
                loop=self.loop
            )

        return True

    @rpc.method
    @asyncio.coroutine
    def end_event(self, token: str, envelope_id: str, event_id: str) -> tuple:
        """Signal that all items have been sent for a given event.

        :param token:
         the emitter's connection token, obtained from the
         :meth:`.XbusBrokerFront.login` method which is exposed on the same
         0mq socket.

        :param envelope_id:
         the UUID of an envelope previously opened by the emitter using the
         :meth:`.XbusBrokerFront.start_envelope` method which is exposed on
         the same 0mq socket.

        :param event_id:
         the UUID of the event

        :return: 2-element tuple:
        - Boolean indicating success (True when succesful).
        - Data sent back by the consumer, when using the "immediate reply"
        feature; None otherwise.
        """

        emitter_json = yield from self.get_key_info(token)
        if emitter_json is None:
            return False, None

        try:
            emitter_info = json.loads(emitter_json)
            emitter_id = emitter_info['id']
        except (ValueError, SyntaxError, KeyError):
            return False, None

        try:
            envelope_info = self.envelopes[envelope_id]
            envelope_emitter_id = envelope_info['emitter_id']
            envelope_events = envelope_info['events']
            envelope_forward = envelope_info['forward']
        except KeyError:
            return False, None

        if emitter_id != envelope_emitter_id:
            return False, None

        try:
            event_info = envelope_events[event_id]
            event_closed = event_info.get('closed', False)
            immediate_reply = event_info['immediate_reply']
        except KeyError:
            return False, None

        if event_closed:
            return False, None
        event_info['closed'] = True

        result = True, None

        if envelope_forward:
            nb_items = event_info['recv']
            result = yield from asyncio.async(
                self.backend_end_event(
                    envelope_id, event_id, nb_items, immediate_reply,
                ),
                loop=self.loop
            )

        return result

    @rpc.method
    @asyncio.coroutine
    def end_envelope(self, token: str, envelope_id: str) -> bool:
        """Closes an envelope. Each event started for this envelope must have
        been closed beforehand, using :meth:`.XbusBrokerFront.end_event`.

        :param token:
         the emitter's connection token, obtained from the
         :meth:`.XbusBrokerFront.login` method which is exposed on the same
         0mq socket.

        :param envelope_id:
         the UUID of an envelope previously opened by the emitter using the
         :meth:`.XbusBrokerFront.start_envelope` method which is exposed on
         the same 0mq socket.

        :return:
         True if successful, False otherwise
        """

        emitter_json = yield from self.get_key_info(token)
        if emitter_json is None:
            return False

        try:
            emitter_info = json.loads(emitter_json)
            emitter_id = emitter_info['id']
        except (ValueError, SyntaxError, KeyError):
            return False

        try:
            envelope_info = self.envelopes[envelope_id]
            envelope_events = envelope_info['events']
            envelope_closed = envelope_info.get('closed', False)
            envelope_emitter_id = envelope_info['emitter_id']
            envelope_forward = envelope_info['forward']
        except KeyError:
            return False

        if emitter_id != envelope_emitter_id:
            return False
        if envelope_closed:
            return False

        for event_info in envelope_events.values():
            if not event_info.get('closed', False):
                return False

        envelope_info['closed'] = True

        if envelope_forward:
            asyncio.async(
                self.backend_end_envelope(envelope_id),
                loop=self.loop
            )
            pass
        else:
            yield from self.update_envelope_state_wait(envelope_id)

        # Do nothing else for now.
        return True

    @rpc.method
    @asyncio.coroutine
    def cancel_envelope(self, token: str, envelope_id: str) -> bool:
        """Cancel the emission of an opened envelope.

        :param token:
         the emitter's connection token, obtained from the
         :meth:`.XbusBrokerFront.login` method which is exposed on the same
         0mq socket.

        :param envelope_id:
         the UUID of an envelope previously opened by the emitter using the
         :meth:`.XbusBrokerFront.start_envelope` method which is exposed on
         the same 0mq socket.

        :return:
         True if successful, False otherwise
        """

        emitter_json = yield from self.get_key_info(token)
        if emitter_json is None:
            return False

        try:
            emitter_info = json.loads(emitter_json)
            emitter_id = emitter_info['id']
        except (ValueError, SyntaxError, KeyError):
            return False

        try:
            envelope_info = self.envelopes[envelope_id]
            envelope_events = envelope_info['events']
            envelope_closed = envelope_info.get('closed')
            envelope_emitter_id = envelope_info['emitter_id']
            envelope_forward = envelope_info['forward']
        except KeyError:
            return False

        if emitter_id != envelope_emitter_id:
            return False
        if envelope_closed:
            return False

        envelope_info['closed'] = True
        for event_info in envelope_events.values():
            event_info['closed'] = True

        yield from self.update_envelope_state_cancel(envelope_id)

        if envelope_forward:
            asyncio.async(
                self.backend_cancel_envelope(envelope_id),
                loop=self.loop
            )

        # Do nothing else for now.
        return True

    @rpc.method
    @asyncio.coroutine
    def get_consumers(self, token: str) -> list:
        """Retrieve the list of consumers that have registered into the Xbus
        back-end, including their metadata and the features they support.

        :param token: The emitter's connection token, obtained from the
        :meth:`.XbusBrokerFront.login` method which is exposed on the same 0mq
        socket.

        :return: List of 2-element tuples (metadata dict, feature dict).
        """

        # Check the token.
        if (yield from self.get_key_info(token)) is None:
            return []

        consumers = yield from self.backend.call.get_consumers()
        return consumers

    @asyncio.coroutine
    def backend_start_envelope(self, envelope_id: str) -> bool:
        """Forward the new envelope to the backend.

        :param envelope_id:
         the generated envelope UUID

        :return:
         True if successful, False otherwise
        """
        envelope_info = self.envelopes[envelope_id]
        res = yield from self.backend.call.start_envelope(envelope_id)
        if res:
            envelope_info['forward'] = True
            if envelope_info['trigger']._callbacks:
                envelope_info['trigger'].set_result(True)
                envelope_info['trigger'] = asyncio.Future(loop=self.loop)
            return True
        else:
            envelope_info['forward'] = False
            envelope_info['trigger'].set_result(False)
            return False

    @asyncio.coroutine
    def backend_start_event(self, envelope_id: str, event_id: str,
                            type_id: str, type_name: str) -> bool:
        """Forward the new event to the backend.

        :param envelope_id:
         the UUID of the envelope which contains the event

        :param event_id:
         the generated UUID of the event

        :param type_id:
         the internal UUID that corresponds to the type of the event

        :param type_name:
         the name of the type of the started event

        :return:
         True if successful, False otherwise
        """
        envelope_info = self.envelopes[envelope_id]
        event_info = envelope_info['events'][event_id]
        forward = envelope_info.get('forward')
        if forward is None:
            forward = yield from envelope_info['trigger']

        if forward is False:
            event_info['trigger'].set_result(False)
            return False

        code, msg = yield from self.backend.call.start_event(
            envelope_id, event_id, type_id, type_name
        )
        if code == 0:
            if event_info['trigger']._callbacks:
                event_info['trigger'].set_result(True)
                event_info['trigger'] = asyncio.Future(loop=self.loop)
            return True
        else:
            yield from self.disable_backend_forward(envelope_id)
            return False

    @asyncio.coroutine
    def backend_send_item(
            self, envelope_id: str, event_id: str, index: int, data: bytes
    ):
        """Forward the item to the backend.

        :param envelope_id:
         the UUID of the envelope which contains the event

        :param event_id:
         The UUID of the event

        :param index:
         the item index

        :param data:
         the item data

        :return:
         True if successful, False otherwise
        """
        event_info = self.envelopes[envelope_id]['events'][event_id]
        while event_info['sent'] < index:
            trigger_res = yield from event_info['trigger']
            if trigger_res is False:
                return False

        code, msg = yield from self.backend.call.send_item(
            envelope_id, event_id, index, data
        )
        if code == 0:
            event_info['sent'] += 1
            if event_info['trigger']._callbacks:
                event_info['trigger'].set_result(True)
                event_info['trigger'] = asyncio.Future(loop=self.loop)
            return True
        else:
            yield from self.disable_backend_forward(envelope_id)
            return False

    @asyncio.coroutine
    def backend_end_event(
        self, envelope_id: str, event_id: str, nb_items: int,
        immediate_reply: bool
    ) -> tuple:
        """Forward the end of the event to the backend.

        :param envelope_id:
         the UUID of the envelope which contains the event

        :param event_id:
         the UUID of the event

        :param event_id:
         the number of items sent for this event.

        :param immediate_reply: Whether an immediate reply is expected; refer
        to the "Immediate reply" section of the Xbus documentation for details.

        :return: 2-element tuple:
        - Boolean indicating success (True when succesful).
        - Data sent back by the consumer, when using the "immediate reply"
        feature; None otherwise.
        """

        envelope_info = self.envelopes[envelope_id]
        event_info = envelope_info['events'][event_id]
        while event_info['sent'] < nb_items:
            trigger_res = yield from event_info['trigger']
            if trigger_res is False:
                return False, None

        call_data = yield from self.backend.call.end_event(
            envelope_id, event_id, nb_items, immediate_reply,
        )

        if not call_data['success']:
            # TODO Do something with errors.
            yield from self.disable_backend_forward(envelope_id)
            return False, None

        if envelope_info['trigger']._callbacks:
            envelope_info['trigger'].set_result(True)
            envelope_info['trigger'] = asyncio.Future(loop=self.loop)

        return True, call_data.get('reply_data') if immediate_reply else None

    @asyncio.coroutine
    def backend_end_envelope(self, envelope_id: str):
        """Forward the end of the envelope to the backend.

        :param envelope_id:
         the UUID of the envelope

        :return:
         True if successful, False otherwise
        """
        envelope_info = self.envelopes[envelope_id]
        events = envelope_info['events'].values()
        while not all(evt.get('closed', False) for evt in events):
            trigger_res = yield from envelope_info['trigger']
            if trigger_res is False:
                return False

        res = yield from self.backend.call.end_envelope(envelope_id)
        if res['success'] is True:
            yield from self.update_envelope_state_exec(envelope_id)
        else:
            yield from self.update_envelope_state_wait(envelope_id)
            yield from self.disable_backend_forward(envelope_id)

        del self.envelopes[envelope_id]
        return bool(res == 0)

    @asyncio.coroutine
    def backend_cancel_envelope(self, envelope_id):
        """Forward the cancellation of the envelope to the backend.

        :param envelope_id:
         the UUID of the envelope

        :return:
         True if successful, False otherwise
        """
        yield from self.disable_backend_forward(envelope_id)
        yield from self.update_envelope_state_cancel(envelope_id)
        res = yield from self.backend.call.cancel_envelope(envelope_id)
        del self.envelopes[envelope_id]
        if res.get('success'):
            return True
        else:
            return False

    @asyncio.coroutine
    def disable_backend_forward(self, envelope_id: str) -> bool:
        """Internal helper that adds a flag to the envelope's cached info,
        in order to prevent its content from being forwarded to the backend.

        :param envelope_id:
         the UUID of the envelope

        :return:
         True in case of success and False in case of error
        """
        try:
            envelope_info = self.envelopes[envelope_id]
            envelope_info['forward'] = False
            envelope_info['trigger'].set_result(False)
            for event_info in envelope_info['events'].values():
                event_info['trigger'].set_result(False)

        except KeyError:
            return False

        return True

    @asyncio.coroutine
    def find_emitter_by_login(self, login: str) -> tuple:
        """Internal helper method used to find an emitter
        (id, password, profile_id) by looking up in the database its login

        :param login:
         the login that identifies the emitter you are searching for

        :return:
         a 3-tuple containing (id, password, profile_id), if nothing is found
         the tuple will contain (None, None, None)
        """
        with (yield from self.dbengine) as conn:
            query = select((emitter.c.id, emitter.c.password,
                            emitter.c.profile_id))
            query = query.where(emitter.c.login == login).limit(1)

            cr = yield from conn.execute(query)
            row = yield from cr.first()
            if row:
                return row.as_tuple()
            else:
                return None, None, None

    @asyncio.coroutine
    def find_event_type_by_name(self, name: str) -> tuple:
        """Internal helper method used to find an event type's id
        by looking up in the database its login

        :param name:
         the name that identifies the event type you are searching for

        :return: 2-element tuple, with:
        - The internal ID of the event type object (or None if not found).
        - Whether the event type has the "immediate reply" flag set.
        """
        with (yield from self.dbengine) as conn:
            query = select((event_type.c.id, event_type.c.immediate_reply))
            query = query.where(event_type.c.name == name)
            query = query.limit(1)

            cr = yield from conn.execute(query)
            row = yield from cr.first()
            if row:
                return row.as_tuple()
            else:
                return None, None

    @asyncio.coroutine
    def check_event_access(self, profile_id: str, type_id: str) -> bool:
        """Internal helper method used to determine whether an emitter, by
        its profile, has the right to start an event of the given type.
        (id, password, profile_id) by looking up in the database its login

        :param profile_id:
         the internal UUID of the emitter's profile. This can be obtained
         using the method :meth:`.XbusBrokerFront.find_emitter_by_login`.

        :param type_id:
         the internal UUID of the event type. This can be obtained using the
         method :meth:`.XbusBrokerFront.find_event_type_by_name`.

        :return:
         True if the emitter has the right to start an event of this type,
         False otherwise
        """
        with (yield from self.dbengine) as conn:
            query = select((func.count(),))
            query = query.select_from(emitter_profile_event_type_rel)
            query = query.where(
                and_(
                    emitter_profile_event_type_rel.c.profile_id == profile_id,
                    emitter_profile_event_type_rel.c.event_id == type_id
                )
            )

            cr = yield from conn.execute(query)
            res = yield from cr.first()
            return True if res[0] > 0 else False

    @asyncio.coroutine
    def log_new_envelope(self, envelope_id: str, emitter_id: str):
        """Internal helper method used to log the creation of a new envelope.

        :param envelope_id:
         the UUID of the new envelope

        :param emitter_id:
         the internal UUID of the emitter of the new envelope
        """
        with (yield from self.dbengine) as conn:
            insert = envelope.insert()
            insert = insert.values(
                id=envelope_id, state='emit', emitter_id=emitter_id,
                posted_date=func.localtimestamp()
            )
            yield from conn.execute(insert)

    @asyncio.coroutine
    def update_envelope_state_exec(self, envelope_id: str):
        """Internal helper method used to log the fact that an envelope has
        been successfully received from its emitter, and is currently being
        treated by the back-end.

        :param envelope_id:
         the UUID of the envelope
        """
        with (yield from self.dbengine) as conn:
            update = envelope.update()
            update = update.where(envelope.c.id == envelope_id)
            update = update.values(state='exec')
            yield from conn.execute(update)

    @asyncio.coroutine
    def update_envelope_state_wait(self, envelope_id: str):
        """Internal helper method used to log the fact that an envelope has
        been successfully received from its emitter, and is now waiting for
        treatment by the back-end.

        :param envelope_id:
         the UUID of the envelope
        """
        with (yield from self.dbengine) as conn:
            update = envelope.update()
            update = update.where(envelope.c.id == envelope_id)
            update = update.values(state='wait')
            yield from conn.execute(update)

    @asyncio.coroutine
    def update_envelope_state_cancel(self, envelope_id: str):
        """Internal helper method used to log the cancellation of an
        envelope before its emission was completed.

        :param envelope_id:
         the UUID of the envelope.
        """
        with (yield from self.dbengine) as conn:
            update = envelope.update()
            update = update.where(envelope.c.id == envelope_id)
            update = update.values(state='canc')
            yield from conn.execute(update)

    @asyncio.coroutine
    def log_new_event(self, event_id: str, envelope_id: str, emitter_id: str,
                      type_id: str, estimate: int):
        """Internal helper method used to log the creation of a new event.

        :param event_id:
         the UUID of the new event

        :param envelope_id:
         the UUID of the envelope which contains the event

        :param emitter_id:
         the internal UUID of the emitter of the new event

        :param type_id:
         the internal UUID of the event type. This can be obtained using the
         method :meth:`.XbusBrokerFront.find_event_type_by_name`

        :param estimate:
         an estimation, by the emitter, of the number of items that will be
         sent for this event.
        """
        with (yield from self.dbengine) as conn:
            insert = event.insert()
            insert = insert.values(
                id=event_id, envelope_id=envelope_id, emitter_id=emitter_id,
                type_id=type_id, estimated_items=estimate, state='unprocessed'
            )
            yield from conn.execute(insert)

    @asyncio.coroutine
    def update_event_sent_items_count(self, event_id: str, sent_items: int):
        """Internal helper method used to log the number of items that was
        finally sent by the emitter for a given event.

        :param event_id:
         the UUID of the event

        :param sent_items:
         the number of items that were emitted
        """
        with (yield from self.dbengine) as conn:
            update = event.update()
            update = update.where(event.c.id == event_id)
            update = update.values(sent_items=sent_items)
            yield from conn.execute(update)

    @asyncio.coroutine
    def log_sent_item(self, event_id: str, index: int, data: bytes):
        """Internal helper method used to preserve the data of each item
        received from the emitter.

        :param event_id:
         the UUID of the event

        :param index:
         the position of the item in the event

        :param data:
         the item's data payload.
        """
        with (yield from self.dbengine) as conn:
            insert = item.insert()
            insert = insert.values(event_id=event_id, index=index, data=data)
            yield from conn.execute(insert)


class XbusBrokerFront2Back(rpc.AttrHandler):

    def __init__(self, broker, *args, **kwargs):
        self.backend = None
        self.broker = broker
        super(XbusBrokerFront2Back, self).__init__(*args, **kwargs)

    @rpc.method
    @asyncio.coroutine
    def register_backend(self, uri):
        """Register a backend on the frontend by giving its URI. If the
        operation goes well returns True. Else return False

        :param uri:
         the URI where the backend is exposing his own 0mq socket configured as
         a router.

        :return:
           - True: if your backend is correctly registered
           - False: if your backend is not properly registered (ie: another
             backend is already registered on this frontend...)
        """
        if self.broker.backend is not None:
            return False

        else:
            # set the backend client on the broker
            self.broker.backend = True
            self.broker.backend = yield from aiozmq.rpc.connect_rpc(
                connect=uri
            )
            return True


@asyncio.coroutine
def get_frontserver(engine_callback, config, socket, b2fsocket, loop=None):
    """A helper function that is used internally to create a running server for
    the front part of Xbus

    :param engine_callback:
     the engine constructor we will "yield from" to get a real dbengine

    :param config:
     the application configuration instance
     :class:`configparser.ConfigParser` it MUST contain a `redis` section and
     two keys: 'host' and 'port'

    :param socket:
     a string representing the socket address on which we will spawn our 0mq
     listener

    :param b2fsocket:
     a string representing the socket address on which the front server will
     listen so that the backend will be able to register itself

    :param loop:
     the event loop this server must use

    :return:
     a future that is waiting for a wait_closed() call before being
     fired back.
    """
    dbengine = yield from engine_callback(config)
    broker = XbusBrokerFront(dbengine, loop=loop)

    redis_host = config.get('redis', 'host')
    redis_port = config.getint('redis', 'port')
    yield from broker.prepare_redis(redis_host, redis_port)

    frontzmqserver = yield from rpc.serve_rpc(
        broker,
        bind=socket,
        loop=loop
    )

    # prepare the socket we use to communicate between front and backend
    front2back = XbusBrokerFront2Back(broker)
    front_from_back_zqm = yield from rpc.serve_rpc(
        front2back,
        bind=b2fsocket,
        loop=loop,
    )

    coroutines = [
        frontzmqserver.wait_closed(),
        front_from_back_zqm.wait_closed()
    ]

    # wait for all coroutines to complete
    yield from asyncio.gather(*coroutines)


# we don't want our imports to be visible to others...
__all__ = ["XbusBrokerFront", "get_frontserver"]
