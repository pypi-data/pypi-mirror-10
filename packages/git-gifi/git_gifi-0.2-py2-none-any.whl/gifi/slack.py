from slackclient import SlackClient

from command import AggregatedCommand, Command, CommandException
from internal.configuration import Configuration, NOT_SET, configuration_command
from internal.git_utils import get_repo


def _configuration(repo=None):
    repo = get_repo(repo)
    return Configuration(repo, 'slack', {
        'access-token': (NOT_SET, 'Slack access token')
    })


def notify(channel, message):
    config = _configuration()
    if config.access_token is NOT_SET:
        raise missingConfigurationException('access-token')
    client = SlackClient(config.access_token)
    client.api_call('chat.postMessage', channel='#%s' % channel, text=message, as_user=True)


def missingConfigurationException(item):
    return CommandException('No slack %s is set, please do configure.' % item)


command = AggregatedCommand('slack', 'Integration with slack.', [
    Command('notify', 'Post a message on given channel.', notify, '<channel> <message>'),
    configuration_command(_configuration, 'Configure slack settings.')
])
