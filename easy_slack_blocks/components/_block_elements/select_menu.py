"""Several classes that generate the different types of Slack's Select Menus.

See Slack documentation for Select Menus here:
https://api.slack.com/reference/block-kit/block-elements#select
"""

from .. import Text

class StaticSelectMenu(dict):
    """Generate a StaticSelectMenu element.

    See Slack documentation for the StaticSelectMenu Block Element here:
    https://api.slack.com/reference/block-kit/block-elements#static_select
    """
    def __init__(
        self, 
        action_id,
        placeholder,
        *,
        options=None,
        option_groups=None,
        initial_option=None,
        confirm=None,
    ):
        if isinstance(placeholder, str):
            placeholder = Text(
                text=placeholder, 
                text_type=Text.PLAIN_TEXT, 
                emoji=False,
            )

        select_menu = {
            'type': 'static_select',
            'action_id': action_id,
            'placeholder': placeholder,
        }

        if options:
            if not isinstance(options, list):
                options = [options]
            select_menu['options'] = options

        if option_groups:
            if not isinstance(option_groups, list):
                option_groups = [option_groups]
            select_menu['option_groups'] = option_groups
        
        if initial_option:
            select_menu['initial_option'] = initial_option

        if confirm:
            select_menu['confirm'] = confirm

        ### TODO:
        ### add element validation

        super(StaticSelectMenu, self).__init__(select_menu)


class ExternalSelectMenu(dict):
    """Generate a ExternalSelectMenu element.

    See Slack documentation for the ExternalSelectMenu Block Element here:
    https://api.slack.com/reference/block-kit/block-elements#external_select
    """
    def __init__(
        self, 
        action_id,
        placeholder,
        *,
        min_query_length=3,
        initial_option=None,
        confirm=None,
    ):
        if isinstance(placeholder, str):
            placeholder = Text(
                text=placeholder, 
                text_type=Text.PLAIN_TEXT, 
                emoji=False,
            )

        select_menu = {
            'type': 'external_select',
            'action_id': action_id,
            'placeholder': placeholder,
            'min_query_length': min_query_length,
        }
        
        if initial_option:
            select_menu['initial_option'] = initial_option

        if confirm:
            select_menu['confirm'] = confirm

        ### TODO:
        ### add element validation

        super(ExternalSelectMenu, self).__init__(select_menu)


class UserSelectMenu(dict):
    """Generate a UserSelectMenu element.

    See Slack documentation for the UserSelectMenu Block Element here:
    https://api.slack.com/reference/block-kit/block-elements#users_select
    """
    def __init__(
        self, 
        action_id,
        placeholder,
        *,
        initial_user=None,
        confirm=None,
    ):
        if isinstance(placeholder, str):
            placeholder = Text(
                text=placeholder, 
                text_type=Text.PLAIN_TEXT, 
                emoji=False,
            )

        select_menu = {
            'type': 'users_select',
            'action_id': action_id,
            'placeholder': placeholder,
        }
        
        if initial_user:
            select_menu['initial_user'] = initial_user

        if confirm:
            select_menu['confirm'] = confirm

        ### TODO:
        ### add element validation

        super(UserSelectMenu, self).__init__(select_menu)


class ConversationSelectMenu(dict):
    """Generate a ConversationSelectMenu element.

    See Slack documentation for the ConversationSelectMenu Block Element here:
    https://api.slack.com/reference/block-kit/block-elements#conversation_select
    """
    def __init__(
        self, 
        action_id,
        placeholder,
        *,
        initial_conversation=None,
        default_to_current_conversation=False,
        confirm=None,
        response_url_enabled=None,
        filter=None,
    ):
        if isinstance(placeholder, str):
            placeholder = Text(
                text=placeholder, 
                text_type=Text.PLAIN_TEXT, 
                emoji=False,
            )

        select_menu = {
            'type': 'conversations_select',
            'action_id': action_id,
            'placeholder': placeholder,
            'default_to_current_conversation': (
                default_to_current_conversation
            ),
        }
        
        if initial_conversation:
            select_menu['initial_conversation'] = initial_conversation

        if confirm:
            select_menu['confirm'] = confirm

        if response_url_enabled:
            select_menu['response_url_enabled'] = response_url_enabled

        if filter:
            select_menu['filter'] = filter

        ### TODO:
        ### add element validation

        super(ConversationSelectMenu, self).__init__(select_menu)


class PublicChannelSelectMenu(dict):
    """Generate a PublicChannelSelectMenu element.

    See Slack documentation for the PublicChannelSelectMenu Block Element here:
    https://api.slack.com/reference/block-kit/block-elements#channel_select
    """
    def __init__(
        self, 
        action_id,
        placeholder,
        *,
        initial_channel=None,
        confirm=None,
        response_url_enabled=None,
    ):
        if isinstance(placeholder, str):
            placeholder = Text(
                text=placeholder, 
                text_type=Text.PLAIN_TEXT, 
                emoji=False,
            )

        select_menu = {
            'type': 'multi_channels_select',
            'action_id': action_id,
            'placeholder': placeholder,
        }
        
        if initial_channel:
            select_menu['initial_channel'] = initial_channel

        if confirm:
            select_menu['confirm'] = confirm

        if response_url_enabled:
            select_menu['response_url_enabled'] = response_url_enabled

        ### TODO:
        ### add element validation

        super(PublicChannelSelectMenu, self).__init__(select_menu)
        