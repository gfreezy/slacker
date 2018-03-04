#!/usr/bin/env python
"""Post slack message."""

# https://github.com/os/slacker
# https://api.slack.com/methods

import os
import asyncio
from slacker import Slacker


async def post_slack():
    """Post slack message."""
    try:
        token = os.environ['SLACK_TOKEN']
        slack = Slacker(token)

        obj = await slack.chat.post_message(
            channel='#general',
            text='',
            as_user=True,
            attachments=[{"pretext": "Subject",
                          "text": "Body"}])
        print(obj.successful, obj.__dict__['body']['channel'], obj.__dict__[
            'body']['ts'])
        slack.close()
    except KeyError as ex:
        print('Environment variable %s not set.' % str(ex))


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(post_slack())
