"""Several classes that generate the different types of Slack's Multi 
Select Menus.

See Slack documentation for Multi Select Menus here:
https://api.slack.com/reference/block-kit/block-elements#multi_select
"""

from .. import Text

class StaticMultiSelectMenu(dict):
    """Generate a StaticMultiSelectMenu element.

    See Slack documentation for the StaticMultiSelectMenu Block Element here:
    https://api.slack.com/reference/block-kit/block-elements#static_multi_select
    """
    def __init__(
        self, 
        action_id,
        placeholder,
        *,
        options=None,
        option_groups=None,
        initial_options=None,
        confirm=None,
        max_selected_items=None,
    ):
        if isinstance(placeholder, str):
            placeholder = Text(
                text=placeholder, 
                text_type=Text.PLAIN_TEXT, 
                emoji=False,
            )

        multi_select_menu = {
            'type': 'multi_static_select',
            'action_id': action_id,
            'placeholder': placeholder,
        }

        if options:
            if not isinstance(options, list):
                options = [options]
            multi_select_menu['options'] = options

        if option_groups:
            if not isinstance(option_groups, list):
                option_groups = [option_groups]
            multi_select_menu['option_groups'] = option_groups
        
        if initial_options:
            if not isinstance(initial_options, list):
                initial_options = [initial_options]
            multi_select_menu['initial_options'] = initial_options

        if confirm:
            multi_select_menu['confirm'] = confirm

        if max_selected_items:
            multi_select_menu['max_selected_items'] = max_selected_items

        ### TODO:
        ### add element validation

        super(StaticMultiSelectMenu, self).__init__(multi_select_menu)


class ExternalMultiSelectMenu(dict):
    """Generate a ExternalMultiSelectMenu element.

    See Slack documentation for the ExternalMultiSelectMenu Block Element here:
    https://api.slack.com/reference/block-kit/block-elements#external_multi_select
    """
    def __init__(
        self, 
        action_id,
        placeholder,
        *,
        min_query_length=3,
        initial_options=None,
        confirm=None,
        max_selected_items=None,
    ):
        if isinstance(placeholder, str):
            placeholder = Text(
                text=placeholder, 
                text_type=Text.PLAIN_TEXT, 
                emoji=False,
            )

        multi_select_menu = {
            'type': 'multi_external_select',
            'action_id': action_id,
            'placeholder': placeholder,
            'min_query_length': min_query_length,
        }
        
        if initial_options:
            if not isinstance(initial_options, list):
                initial_options = [initial_options]
            multi_select_menu['initial_options'] = initial_options

        if confirm:
            multi_select_menu['confirm'] = confirm

        if max_selected_items:
            multi_select_menu['max_selected_items'] = max_selected_items

        ### TODO:
        ### add element validation

        super(ExternalMultiSelectMenu, self).__init__(multi_select_menu)


class UserMultiSelectMenu(dict):
    """Generate a UserMultiSelectMenu element.

    See Slack documentation for the UserMultiSelectMenu Block Element here:
    https://api.slack.com/reference/block-kit/block-elements#users_multi_select
    """
    def __init__(
        self, 
        action_id,
        placeholder,
        *,
        initial_users=None,
        confirm=None,
        max_selected_items=None,
    ):
        if isinstance(placeholder, str):
            placeholder = Text(
                text=placeholder, 
                text_type=Text.PLAIN_TEXT, 
                emoji=False,
            )

        multi_select_menu = {
            'type': 'multi_users_select',
            'action_id': action_id,
            'placeholder': placeholder,
        }
        
        if initial_users:
            if not isinstance(initial_users, list):
                initial_users = [initial_users]
            multi_select_menu['initial_users'] = initial_users

        if confirm:
            multi_select_menu['confirm'] = confirm

        if max_selected_items:
            multi_select_menu['max_selected_items'] = max_selected_items

        ### TODO:
        ### add element validation

        super(UserMultiSelectMenu, self).__init__(multi_select_menu)


class ConversationMultiSelectMenu(dict):
    """Generate a ConversationMultiSelectMenu element.

    See Slack documentation for the ConversationMultiSelectMenu Block Element here:
    https://api.slack.com/reference/block-kit/block-elements#conversation_multi_select
    """
    def __init__(
        self, 
        action_id,
        placeholder,
        *,
        initial_conversations=None,
        default_to_current_conversation=False,
        confirm=None,
        max_selected_items=None,
        filter=None,
    ):
        if isinstance(placeholder, str):
            placeholder = Text(
                text=placeholder, 
                text_type=Text.PLAIN_TEXT, 
                emoji=False,
            )

        multi_select_menu = {
            'type': 'multi_conversations_select',
            'action_id': action_id,
            'placeholder': placeholder,
            'default_to_current_conversation': (
                default_to_current_conversation
            ),
        }
        
        if initial_conversations:
            if not isinstance(initial_conversations, list):
                initial_conversations = [initial_conversations]
            multi_select_menu['initial_conversations'] = initial_conversations

        if confirm:
            multi_select_menu['confirm'] = confirm

        if max_selected_items:
            multi_select_menu['max_selected_items'] = max_selected_items

        if filter:
            multi_select_menu['filter'] = filter

        ### TODO:
        ### add element validation

        super(ConversationMultiSelectMenu, self).__init__(multi_select_menu)


class PublicChannelMultiSelectMenu(dict):
    """Generate a PublicChannelMultiSelectMenu element.

    See Slack documentation for the PublicChannelMultiSelectMenu Block Element here:
    https://api.slack.com/reference/block-kit/block-elements#channel_multi_select
    """
    def __init__(
        self, 
        action_id,
        placeholder,
        *,
        initial_channels=None,
        confirm=None,
        max_selected_items=None,
    ):
        if isinstance(placeholder, str):
            placeholder = Text(
                text=placeholder, 
                text_type=Text.PLAIN_TEXT, 
                emoji=False,
            )

        multi_select_menu = {
            'type': 'multi_channels_select',
            'action_id': action_id,
            'placeholder': placeholder,
        }
        
        if initial_channels:
            if not isinstance(initial_channels, list):
                initial_channels = [initial_channels]
            multi_select_menu['initial_channels'] = initial_channels

        if confirm:
            multi_select_menu['confirm'] = confirm

        if max_selected_items:
            multi_select_menu['max_selected_items'] = max_selected_items

        ### TODO:
        ### add element validation

        super(PublicChannelMultiSelectMenu, self).__init__(multi_select_menu)
        