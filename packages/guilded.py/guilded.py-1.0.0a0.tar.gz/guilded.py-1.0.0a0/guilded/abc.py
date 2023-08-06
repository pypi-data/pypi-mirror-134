"""
MIT License

Copyright (c) 2020-present shay (shayypy)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

------------------------------------------------------------------------------

This project includes code from https://github.com/Rapptz/discord.py, which is
available under the MIT license:

The MIT License (MIT)

Copyright (c) 2015-present Rapptz

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
"""

import abc
import datetime
from typing import List, Optional

from .activity import Activity
from .asset import Asset
from .colour import Colour
from .errors import GuildedException
from .embed import _EmptyEmbed, Embed
from .file import MediaType, FileType, File
from .message import HasContentMixin, ChatMessage
from .presence import Presence
from .utils import ISO8601


__all__ = (
    'Messageable',
    'User',
    'TeamChannel',
    'Reply',
)


class Messageable(metaclass=abc.ABCMeta):
    """An ABC for models that messages can be sent to.

    The following implement this ABC:

        * :class:`.ChatChannel`
        * :class:`.VoiceChannel`
        * :class:`.Thread`
        * :class:`.DMChannel`
        * :class:`.User`
        * :class:`.Member`
        * :class:`.ext.commands.Context`
    """
    def __init__(self, *, state, data):
        self._state = state
        self.id = data.get('id')
        self._channel_id = data.get('id')

    @property
    def _channel(self):
        if isinstance(self, User):
            return self.dm_channel
        elif hasattr(self, 'channel'):
            return self.channel
        else:
            return self

    async def send(self, *content, **kwargs) -> ChatMessage:
        """|coro|

        Send a message to a Guilded channel.

        .. note::

            Guilded supports embeds/attachments/strings in any order, which is
            not practically possible with keyword arguments. For this reason,
            it is recommended that you pass arguments positionally instead.

        .. warning::

            Replying with both ``silent`` and ``private`` set to ``True`` (a
            private reply with no mention) will not send the reply to the
            author of the message(s) until they refresh the channel. This is a
            Guilded bug.

        Parameters
        -----------
        \*content: Union[:class:`str`, :class:`.Embed`, :class:`.File`, :class:`.Emoji`, :class:`.Member`]
            An argument list of the message content, passed in the order that
            each element should display in the message.
        reply_to: List[:class:`.ChatMessage`]
            A list of up to 5 messages to reply to.
        silent: :class:`bool`
            Whether this message should not mention the members mentioned in
            it, including the authors of messages it is in reply to, if any.
            Defaults to ``False``.
        private: :class:`bool`
            Whether this message should only be visible to its author (the
            bot) and the authors of the messages it is replying to. Defaults
            to ``False``. You should not include sensitive data in these
            because private replies can still be visible to server moderators.
        """
        if self._state.userbot:
            content = list(content)
            if kwargs.get('file'):
                file = kwargs.get('file')
                file.set_media_type(MediaType.attachment)
                if file.url is None:
                    await file._upload(self._state)
                content.append(file)
            for file in kwargs.get('files') or []:
                file.set_media_type(MediaType.attachment)
                if file.url is None:
                    await file._upload(self._state)
                content.append(file)

            def embed_attachment_uri(embed):
                # pseudo-support attachment:// URI for use in embeds
                for slot in [('image', 'url'), ('thumbnail', 'url'), ('author', 'icon_url'), ('footer', 'icon_url')]:
                    url = getattr(getattr(embed, slot[0]), slot[1])
                    if isinstance(url, _EmptyEmbed):
                        continue
                    if url.startswith('attachment://'):
                        filename = url.strip('attachment://')
                        for node in content:
                            if isinstance(node, File) and node.filename == filename:
                                getattr(embed, f'_{slot[0]}')[slot[1]] = node.url
                                content.remove(node)
                                break

                return embed

            # upload Files passed positionally
            for node in content:
                if isinstance(node, File) and node.url is None:
                    node.set_media_type(MediaType.attachment)
                    await node._upload(self._state)

            # handle attachment URIs for Embeds passed positionally
            # this is a separate loop to ensure that all files are uploaded first
            for node in content:
                if isinstance(node, Embed):
                    content[content.index(node)] = embed_attachment_uri(node)

            if kwargs.get('embed'):
                content.append(embed_attachment_uri(kwargs.get('embed')))

            for embed in kwargs.get('embeds') or []:
                content.append(embed_attachment_uri(embed))

            message_payload = {
                'isSilent': kwargs.get('silent', not kwargs.get('mention_author', True)),
                'isPrivate': kwargs.get('private', False)
            }

            if kwargs.get('reference') and kwargs.get('reply_to'):
                raise ValueError('Cannot provide both reference and reply_to')

            if kwargs.get('reference'):
                kwargs['reply_to'] = [kwargs['reference']]

            if kwargs.get('reply_to'):
                if not isinstance(kwargs['reply_to'], list):
                    raise TypeError('reply_to must be type list, not %s' % type(kwargs['reply_to']).__name__)

                message_payload['repliesToIds'] = [message.id for message in kwargs['reply_to']]

            share_urls = [message.share_url for message in kwargs.get('share', []) if message.share_url is not None]
            response_coro, payload = self._state.send_message(self._channel_id, content, message_payload, share_urls=share_urls)
            response = await response_coro
            payload['createdAt'] = response.pop('message', response or {}).pop('createdAt', None)
            payload['id'] = payload.pop('messageId')
            try:
                payload['channelId'] = getattr(self, 'id', getattr(self, 'channel', None).id)
            except AttributeError:
                payload['channelId'] = None
            payload['teamId'] = self.team.id if self.team else None
            payload['createdBy'] = self._state.my_id

            author = None
            if payload['teamId'] is not None:
                args = (payload['teamId'], payload['createdBy'])
                try:
                    author = self._state._get_team_member(*args) or await self._state.get_team_member(*args, as_object=True)
                except:
                    author = None

            if author is None or payload['teamId'] is None:
                try:
                    author = self._state._get_user(payload['createdBy']) or await self._state.get_user(payload['createdBy'], as_object=True)
                except:
                    author = None

            return self._state.create_message(channel=self._channel, data=payload, author=author)

        else:
            content = content[0] if content else None

            if kwargs.get('reference'):
                kwargs['reply_to'] = [kwargs['reference']]

            data = await self._state.create_channel_message(self._channel_id,
                content=content,
                private=kwargs.get('private', False),
                reply_to_ids=[message.id for message in (kwargs.get('reply_to') or [])]
            )
            message = self._state.create_message(
                data=data['message'],
                channel=self._channel
            )
            return message

    async def trigger_typing(self):
        """|coro|

        Begin your typing indicator in this channel.
        """
        return await self._state.trigger_typing(self._channel_id)

    async def history(self, *, limit: int = 50) -> List[ChatMessage]:
        """|coro|

        Fetch the message history of this channel.

        Parameters
        -----------
        limit: Optional[:class:`int`]
            The maximum number of messages to fetch. Defaults to 50.

        Returns
        --------
        List[:class:`.ChatMessage`]
        """
        history = await self._state.get_channel_messages(self._channel_id, limit=limit)
        messages = []
        for message in history.get('messages', []):
            try:
                messages.append(self._state.create_message(channel=self._channel, data=message))
            except:
                pass

        return messages

    async def fetch_message(self, id: str) -> ChatMessage:
        """|coro|

        Fetch a message.

        Parameters
        -----------
        id: :class:`str`
            The message's ID to fetch.

        Returns
        --------
        :class:`.ChatMessage`
            The message from the ID.
        """
        message = await self._state.get_channel_message(self._channel_id, id)
        return message

    async def create_thread(self, *content, **kwargs):
        """|coro|

        Create a new thread in this channel.

        Parameters
        ------------
        content: Any
            The content of the message that should be created as the initial
            message of the newly-created thread. Passing either this or
            ``message`` is required.
        name: :class:`str`
            The name to create the thread with.
        message: Optional[:class:`.ChatMessage`]
            The message to create the thread from. Passing either this or
            values for ``content`` is required.
        """
        name = kwargs.get('name')
        message = kwargs.get('message')
        if not name:
            raise TypeError('name is a required argument that is missing.')
        if not message and not content:
            raise TypeError('Must include message, an argument list of content, or both.')

        data = await self._state.create_thread(self._channel_id, content, name=name, initial_message=message)
        thread = self._state.create_channel(data=data.get('thread', data), group=self.group, team=self.team)
        return thread

    async def pins(self):
        """|coro|

        Fetch the pinned messages in this channel.

        Returns
        --------
        List[:class:`.ChatMessage`]
        """
        messages = []
        data = await self._state.get_pinned_messages(self._channel_id)
        for message_data in data['messages']:
            message = self._state.create_message(data=message_data, channel=self._channel)
            messages.append(message)

        return messages

    async def seen(self, clear_all_badges: bool = False) -> None:
        """|coro|

        |onlyuserbot|

        Mark this channel as seen; acknowledge all unread messages within it.

        Parameters
        -----------
        clear_all_badges: :class:`bool`
            Whether to clear all badges.

        Raises
        -------
        GuildedException
            The messageable has no channel attached.
        """
        if not self._channel:
            if isinstance(self, User):
                await self.create_dm()
            else:
                raise GuildedException('The messageable has no channel attached.')
        await self._state.mark_channel_seen(self._channel.id, clear_all_badges=clear_all_badges)


class User(metaclass=abc.ABCMeta):
    """An ABC for user-type models.

    The following implement this ABC:

        * :class:`guilded.User`
        * :class:`.Member`
        * :class:`.ClientUser`

    Attributes
    -----------
    id: :class:`str`
        The user's id.
    name: :class:`str`
        The user's name.
    subdomain: Optional[:class:`str`]
        The user's "subdomain", or vanity code. Referred to as a "URL" in the
        client.
    email: Optional[:class:`str`]
        The user's email address. This value should only be present when
        accessing this on your own :class:`.ClientUser`\.
    service_email: Optional[:class:`str`]
        The user's "service email".
    bio: :class:`str`
        The user's bio. This is referred to as "About" in the client.
    tagline: :class:`str`
        The user's tagline. This is the text under the user's name on their
        profile page in the client.
    avatar: Optional[:class:`.Asset`]
        The user's set avatar, if any.
    banner: Optional[:class:`.Asset`]
        The user's profile banner, if any.
    presence: Optional[:class:`Presence`]
        The user's presence.
    dm_channel: Optional[:class:`DMChannel`]
        The user's DM channel with you, if fetched/created and/or cached
        during this session.
    online_at: :class:`datetime.datetime`
        When the user was last online.
    created_at: Optional[:class:`datetime.datetime`]
        When the user's account was created.

        .. warning::

            Due to API ambiguities, this may erroneously be the same as
            :attr:`.joined_at` if this is a :class:`.Member`\.

    blocked_at: Optional[:class:`datetime.datetime`]
        When you blocked the user.
    bot: :class:`bool`
        Whether this user is a bot (webhook or flow bot).
    moderation_status: Optional[Any]
        The user's moderation status.
    badges: List[:class:`str`]
        The user's badges.
    stonks: Optional[:class:`int`]
        How many "stonks" the user has.
    """
    def __init__(self, *, state, data, **extra):
        self._state = state
        data = data.get('user', data)

        self.type = None
        self.id: str = data.get('id')
        self.dm_channel = None
        self.name: str = data.get('name') or ''
        self.colour: Colour = Colour(0)
        self.subdomain: Optional[str] = data.get('subdomain')
        self.email: Optional[str] = data.get('email')
        self.service_email: Optional[str] = data.get('serviceEmail')
        self.games: List = data.get('aliases', [])
        self.bio: str = (data.get('aboutInfo') or {}).get('bio') or ''
        self.tagline: str = (data.get('aboutInfo') or {}).get('tagLine') or ''
        self.presence: Presence = Presence.from_value(data.get('userPresenceStatus')) or None
        status = data.get('userStatus') or {}
        if status.get('content'):
            self.status: Optional[Activity] = Activity.build(status['content'])
        else:
            self.status: Optional[Activity] = None

        self.blocked_at: Optional[datetime.datetime] = ISO8601(data.get('blockedDate'))
        self.online_at: Optional[datetime.datetime] = ISO8601(data.get('lastOnline'))
        self.created_at: datetime.datetime = ISO8601(data.get('createdAt') or data.get('joinDate'))
        # in profilev3, createdAt is returned instead of joinDate

        self.default_avatar: Asset = Asset._from_default_user_avatar(self._state, 1)

        avatar = None
        _avatar_url = data.get('profilePicture') or data.get('profilePictureLg') or data.get('profilePictureSm') or data.get('profilePictureBlur')
        if _avatar_url:
            avatar = Asset._from_user_avatar(self._state, _avatar_url)
        self.avatar: Optional[Asset] = avatar

        banner = None
        _banner_url = data.get('profileBannerLg') or data.get('profileBannerSm') or data.get('profileBannerBlur')
        if _banner_url:
            banner = Asset._from_user_banner(self._state, _banner_url)
        self.banner: Optional[Asset] = banner

        self.moderation_status: Optional[str] = data.get('moderationStatus')
        self.badges: List = data.get('badges') or []
        self.stonks: Optional[int] = data.get('stonks')

        self._bot: bool = data.get('bot', extra.get('bot', False))

        self.friend_status = extra.get('friend_status')
        self.friend_requested_at: Optional[datetime.datetime] = ISO8601(extra.get('friend_created_at'))

    def __str__(self):
        return self.display_name or ''

    def __eq__(self, other):
        return isinstance(other, User) and self.id == other.id

    def __repr__(self):
        return f'<{self.__class__.__name__} id={self.id!r} name={self.name!r} bot={self.bot!r}>'

    @property
    def slug(self) -> Optional[str]:
        return self.subdomain

    @property
    def url(self) -> Optional[str]:
        return self.subdomain

    @property
    def profile_url(self) -> str:
        return f'https://guilded.gg/profile/{self.id}'

    @property
    def vanity_url(self) -> Optional[str]:
        if self.subdomain:
            return f'https://guilded.gg/{self.subdomain}'
        else:
            return None

    @property
    def mention(self) -> str:
        return f'<@{self.id}>'

    @property
    def display_name(self) -> str:
        return self.name

    @property
    def color(self) -> Colour:
        return self.colour

    @property
    def _channel_id(self):
        return self.dm_channel.id if self.dm_channel else None

    @property
    def bot(self) -> bool:
        return self._bot

    @property
    def display_avatar(self) -> Asset:
        """:class:`.Asset`: The "top-most" avatar for this user, or, the avatar
        that the client will display in the member list and in chat."""
        return self.avatar or self.default_avatar

    async def create_dm(self) -> Messageable:
        """|coro|

        Create a DM channel with this user.

        Returns
        --------
        :class:`.DMChannel`
            The DM channel you created.
        """
        data = await self._state.create_dm_channel([self.id])
        channel = self._state.create_channel(data=data)
        self.dm_channel = channel
        self._state.add_to_dm_channel_cache(channel)
        return channel

    async def hide_dm(self):
        """|coro|

        Visually hide your DM channel with this user in the client.

        Equivalent to :meth:`.DMChannel.hide`.

        Raises
        -------
        ValueError
            Your DM channel with this user is not available or does not exist.
        """
        if self.dm_channel is None:
            raise ValueError('No DM channel is cached for this user. You may want to first run the create_dm coroutine.')

        await self.dm_channel.hide()

    async def send(self, *content, **kwargs) -> ChatMessage:
        if self.dm_channel is None:
            await self.create_dm()

        return await super().send(*content, **kwargs)


class TeamChannel(metaclass=abc.ABCMeta):
    """An ABC for the various types of team channels.

    The following implement this ABC:

        * :class:`.AnnouncementChannel`
        * :class:`.ChatChannel`
        * :class:`.DocsChannel`
        * :class:`.ForumChannel`
        * :class:`.ListChannel`
        * :class:`.MediaChannel`
        * :class:`.Thread`
        * :class:`.VoiceChannel`
    """
    def __init__(self, *, state, group, data, **extra):
        self._state = state
        self.type = None
        if 'metadata' in data:
            data = data['metadata']
        data = data.get('channel') or data.get('thread') or data
        self._group = group
        self.group_id = data.get('groupId') or (self._group.id if self._group else None)

        self._team = extra.get('team') or (self._group.team if self._group else None)
        self.team_id = data.get('teamId') or (self._team.id if self._team else None)

        self.id: str = data['id']
        self.name: str = data.get('name') or ''
        self.description: str = data.get('description') or ''

        self.position: int = data.get('priority')
        self.slug: Optional[str] = data.get('slug')
        self.roles_synced: Optional[bool] = data.get('isRoleSynced')
        self.public: bool = data.get('isPublic', False)
        self._settings: dict = data.get('settings') or {}

        self.created_at: datetime.datetime = ISO8601(data.get('createdAt'))
        self.updated_at: Optional[datetime.datetime] = ISO8601(data.get('updatedAt'))
        self.added_at: Optional[datetime.datetime] = ISO8601(data.get('addedAt'))  # i have no idea what this is
        self.archived_at: Optional[datetime.datetime] = ISO8601(data.get('archivedAt'))
        self.auto_archive_at: Optional[datetime.datetime] = ISO8601(data.get('autoArchiveAt'))
        self.created_by_id: Optional[str] = extra.get('createdBy')
        if data.get('createdByInfo'):
            self._created_by = self._state.create_member(data=data.get('createdByInfo'), team=self.team)
        else:
            self._created_by = None
        self.archived_by = extra.get('archived_by') or self._state._get_team_member(self.team_id, extra.get('archivedBy'))
        self.created_by_webhook_id: Optional[str] = data.get('createdByWebhookId')
        self.archived_by_webhook_id: Optional[str] = data.get('archivedByWebhookId')

        self.parent_id: Optional[str] = data.get('parentChannelId') or data.get('originatingChannelId')

    @property
    def topic(self) -> str:
        return self.description

    @property
    def vanity_url(self) -> str:
        if self.slug and self.team.vanity_url:
            return f'{self.team.vanity_url}/blog/{self.slug}'
        return None

    @property
    def share_url(self) -> str:
        # For channel links, any real type will work in the client, but
        # linking to individual content requires the proper type string
        if hasattr(self, '_shareable_content_type'):
            type_ = self._shareable_content_type
        elif self.type is not None:
            type_ = self.type.value
        else:
            type_ = 'chat'

        return f'https://guilded.gg//groups/{self.group_id}/channels/{self.id}/{type_}'

    @property
    def mention(self) -> str:
        return f'<#{self.id}>'

    @property
    def group(self):
        group = self._group
        if not group and self.team:
            group = self.team.get_group(self.group_id)

        return group

    @property
    def team(self):
        return self._team or self._state._get_team(self.team_id)

    @property
    def guild(self):
        return self.team

    @property
    def parent(self):
        return self.team.get_channel_or_thread(self.parent_id)

    @property
    def created_by(self):
        return self._created_by or self.team.get_member(self.created_by_id)

    @property
    def slowmode(self) -> int:
        """:class:`int`: The number of seconds that members will be restricted
        before they can send another piece of content in the channel."""
        return self._settings.get('slowMode', 0)

    @property
    def slowmode_delay(self) -> int:
        """|dpyattr|

        This is an alias of :attr:`.slowmode`.

        Returns
        --------
        :class:`int`
        """
        return self.slowmode

    def __str__(self):
        return self.name

    def __repr__(self):
        return f'<{self.__class__.__name__} id={self.id!r} name={self.name!r} team={self.team!r}>'

    def __eq__(self, other):
        try:
            return self.id == other.id
        except:
            return False

    async def edit(self, **options):
        """|coro|

        |onlyuserbot|

        Edit this channel.

        Parameters
        -----------
        name: :class:`str`
            The channel's name.
        description: :class:`str`
            The channel's description (topic).
        public: :class:`bool`
            Whether the channel should be public (visible to users not in the
            team).
        slowmode: :class:`int`
            The number of seconds that members should be restricted before they
            can send another piece of content in the channel. Must be one of
            ``0``, ``5``, ``10``, ``15``, ``30``, ``60``, ``120``, ``300``, ``600``, or ``3600``.
            Set to ``0`` or ``None`` to disable slowmode.

        Returns
        --------
        :class:`.TeamChannel`
            The newly-edited channel. If ``slowmode`` was specified, this is a
            new channel object from Guilded, else it is the current object
            modified in-place.
        """
        edited_channel = self
        info_payload = {}
        try:
            name = options.pop('name')
        except KeyError:
            pass
        else:
            info_payload['name'] = name

        if 'description' in options or 'topic' in options:
            description = options.get('description', options.get('topic'))
            info_payload['description'] = description

        try:
            public = options.pop('public')
        except KeyError:
            pass
        else:
            info_payload['isPublic'] = public

        if info_payload:
            if self.name and 'name' not in info_payload:
                # While you aren't required to provide this, not doing so will
                # cause an unusual-looking "user renamed this channel from name to ."
                # system message to be sent.
                info_payload['name'] = self.name
            await self._state.update_team_channel_info(self.team_id, self.group_id, self.id, info_payload)
            # We have to edit in-place here because PUT /info does not return the new channel object
            try: edited_channel.name: str = name
            except NameError: pass
            try: edited_channel.description: str = description
            except NameError: pass
            try: edited_channel.public: bool = public
            except NameError: pass

        settings_payload = {}
        if 'slowmode' in options or 'slowmode_delay' in options:
            slowmode = options.get('slowmode', options.get('slowmode_delay'))
            settings_payload['slowMode'] = slowmode

        if settings_payload:
            data = await self._state.update_team_channel_settings(self.team_id, self.group_id, self.id, {'channelSettings': settings_payload})
            edited_channel = self._state.create_channel(data=data, team=self.team)
            self.team._channels[self.id] = edited_channel

        return edited_channel

    async def delete(self):
        """|coro|

        |onlyuserbot|

        Delete this channel.
        """
        return await self._state.delete_team_channel(self.team_id, self.group_id, self.id)

    async def seen(self, clear_all_badges: bool = False) -> None:
        """|coro|

        |onlyuserbot|

        Mark this channel as seen; acknowledge all unread items within it.

        Parameters
        -----------
        clear_all_badges: :class:`bool`
            Whether to clear all badges.
        """
        await self._state.mark_channel_seen(self.id, clear_all_badges=clear_all_badges)


class Reply(HasContentMixin, metaclass=abc.ABCMeta):
    """An ABC for replies to posts.

    The following implement this ABC:

        * :class:`.AnnouncementReply`
        * :class:`.DocReply`
        * :class:`.ForumReply`

    .. container:: operations

        .. describe:: x == y

            Checks if two replies are equal.

        .. describe:: x != y

            Checks if two replies are not equal.

    Attributes
    -----------
    id: :class:`int`
        The reply's ID.
    content: :class:`str`
        The reply's content.
    parent: Union[:class:`.Announcement`, :class:`.Doc`, :class:`.ForumTopic`, :class:`.Media`]
        The content that the reply is a child of.
    created_at: :class:`datetime.datetime`
        When the reply was created.
    edited_at: Optional[:class:`datetime.datetime`]
        When the reply was last edited.
    deleted_by: Optional[:class:`.Member`]
        Who deleted this reply. This will only be present through a delete
        event, e.g. :func:`on_forum_reply_delete`.
    """
    def __init__(self, *, state, data, parent):
        super().__init__()
        self._state = state
        self.parent = parent

        self.id: int = int(data['id'])
        self.content: str = self._get_full_content(data['message'])

        self.author_id: str = data.get('createdBy')
        self.created_by_bot_id: Optional[str] = data.get('createdByBotId')
        self.created_at: datetime.datetime = ISO8601(data.get('createdAt'))
        self.edited_by_id: Optional[str] = data.get('updatedBy')
        self.edited_at: Optional[datetime.datetime] = ISO8601(data.get('editedAt'))
        self.deleted_by: Optional[User] = None

        self.replied_to_id: Optional[int] = None
        self.replied_to_author_id: Optional[str] = None

    def __repr__(self):
        return f'<{self.__class__.__name__} id={self.id!r} author={self.author!r} parent={self.parent!r}>'

    def __eq__(self, other):
        return isinstance(other, Reply) and other.id == self.id and other.parent == self.parent

    @property
    def _content_type(self):
        return getattr(self.channel, 'content_type', self.channel.type.value)

    @property
    def author(self) -> Optional[User]:
        """Optional[:class:`.Member`]: The :class:`.Member` that created the
        reply, if they are cached."""
        return self.team.get_member(self.author_id)

    @property
    def edited_by(self) -> Optional[User]:
        """Optional[:class:`.Member`]: The :class:`.Member` that last modified
        the reply, if they exist and are cached."""
        return self.team.get_member(self.edited_by_id)

    @property
    def replied_to(self):
        if self.replied_to_id:
            return self.parent.get_reply(self.replied_to_id)
        return None

    @property
    def channel(self) -> TeamChannel:
        """:class:`~.abc.TeamChannel`: The channel that the reply is in."""
        return self.parent.channel

    @property
    def group(self):
        """:class:`.Group`: The group that the reply is in."""
        return self.parent.group

    @property
    def team(self):
        """:class:`.Team`: The team that the reply is in."""
        return self.parent.team

    @classmethod
    def _copy(cls, reply):
        self = cls.__new__(cls)

        self.parent = reply.parent
        self.id: int = reply.id
        self.content: str = reply.content
        self.author_id: str = reply.author_id
        self.created_by_bot_id: Optional[str] = reply.created_by_bot_id
        self.created_at: datetime.datetime = reply.created_at
        self.edited_by_id: Optional[str] = reply.edited_by_id
        self.edited_at: Optional[datetime.datetime] = reply.edited_at
        self.deleted_by: Optional[User] = reply.deleted_by
        self.replied_to_id: Optional[int] = reply.replied_to_id
        self.replied_to_author_id: Optional[str] = reply.replied_to_author_id

        return self

    def _update(self, data):
        try:
            self.content = self._get_full_content(data['message'])
        except KeyError:
            pass

        try:
            self.edited_at = ISO8601(data['editedAt'])
        except KeyError:
            pass

        try:
            self.edited_by_id = data['updatedBy']
        except KeyError:
            pass

    async def add_reaction(self, emoji):
        """|coro|

        Add a reaction to this reply.

        Parameters
        -----------
        emoji: :class:`.Emoji`
            The emoji to add.
        """
        await self._state.add_content_reaction(self._content_type, self.id, emoji.id, reply=True)

    async def remove_self_reaction(self, emoji):
        """|coro|

        Remove your reaction from this reply.

        Parameters
        -----------
        emoji: :class:`.Emoji`
            The emoji to remove.
        """
        await self._state.remove_self_content_reaction(self._content_type, self.id, emoji.id, reply=True)

    async def delete(self):
        """|coro|

        Delete this reply.
        """
        await self._state.delete_content_reply(self._content_type, self.team.id, self.parent.id, self.id)

    async def reply(self, *content, **kwargs):
        """|coro|

        Reply to this reply.

        This method is identical to the reply method of its parent.
        """
        kwargs['reply_to'] = self
        return await self.parent.reply(*content, **kwargs)

    async def edit(self, *content):
        """|coro|

        Edit this reply.

        Parameters
        -----------
        \*content: Any
            The content of the reply.
        """
        await self._state.update_content_reply(self._content_type, self.parent.id, self.id, content=content)
