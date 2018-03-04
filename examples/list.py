#!/usr/bin/env python
"""List items in slack."""

# https://github.com/os/slacker
# https://api.slack.com/methods

import os
import asyncio
from slacker import Slacker


async def list_slack():
    """List channels & users in slack."""
    try:
        token = os.environ['SLACK_TOKEN']
        slack = Slacker(token)

        # Get channel list
        response = await slack.channels.list()
        channels = response.body['channels']
        for channel in channels:
            print(channel['id'], channel['name'])
            # if not channel['is_archived']:
            # slack.channels.join(channel['name'])
        print()

        # # Get users list
        # response = await slack.users.list()
        # users = response.body['members']
        # for user in users:
        #     if not user['deleted']:
        #         print(user['id'], user['name'], user['is_admin'], user[
        #             'is_owner'])
        # print()
        await slack.close()
    except KeyError as ex:
        print('Environment variable %s not set.' % str(ex))


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(list_slack())
