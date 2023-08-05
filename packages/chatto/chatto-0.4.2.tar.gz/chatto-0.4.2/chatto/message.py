# Copyright (c) 2021-2022, Ethan Henderson
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice, this
#    list of conditions and the following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.
#
# 3. Neither the name of the copyright holder nor the names of its
#    contributors may be used to endorse or promote products derived from
#    this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

from __future__ import annotations

import datetime as dt
import typing as t
from dataclasses import dataclass

from dateutil.parser import parse as parse_ts

from chatto.channel import Channel
from chatto.stream import Stream


@dataclass(eq=True, frozen=True)
class Message:
    """A dataclass representing a message. All class variables are also
    parameters that should be passed into the constructor."""

    id: str
    """The message's ID."""

    type: str
    """The message's type."""

    stream: Stream
    """The stream instance the """

    channel: Channel
    """The channel in which the message was sent."""

    published_at: dt.datetime
    """The date and time the message was published at."""

    content: str
    """The content of the message."""

    @classmethod
    def from_youtube(cls, resource: dict[str, t.Any], stream: Stream) -> Message:
        """Create a `Message` object from a liveChatMessage resource
        from the YouTube Live Streaming API.

        ## Arguments
        * `resource` -
            The liveChatMessage resource.
        * `stream` -
            The `Stream` instance of the stream the bot is currently
            connected to.

        ## Returns
        * `Message`:
            The newly created message object.
        """
        snippet = resource["snippet"]
        return cls(
            id=resource["id"],
            type=snippet["type"],
            stream=stream,
            channel=Channel.from_author(resource["authorDetails"]),
            published_at=parse_ts(snippet["publishedAt"]),
            content=snippet["displayMessage"],
        )
