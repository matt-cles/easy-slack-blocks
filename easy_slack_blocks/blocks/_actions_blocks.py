from ..components import Text

class Actions(dict):
    """Generate an Actions Block.

    See Slack documentation for the Actions Block here:
    https://api.slack.com/reference/block-kit/blocks#actions
    """
    def __init__(
        self, 
        elements,
        *,
        block_id: str=None,
    ):  
        # Add ensure elements is a list
        if not isinstance(elements, list):
            # If the elements are not a list, put them into a list
            elements = [elements]

        # Start the base block
        block = {
            'type': 'actions',
            'elements': elements,
        }

        # Add block_id, if given
        if block_id:
            block['block_id'] = block_id

        # Validate and normalize block elements
        if len(elements) > 5:
            raise ValueError(
                'the maximum number of objects allowed in the actions'
                'elements is 5\n '
                'See https://api.slack.com/reference/block-kit/blocks#actions'
                'for more information.'
            )

        if len(block.get('block_id', [])) > 255:
            raise ValueError(
                'the maximum length of a block_id is 255 characters\n'
                'See https://api.slack.com/reference/block-kit/blocks '
                'for more information.'
            )

        for element in elements:
            element_type = element.get('type') 
            if not element_type in [
                'button', 
                'static_select', 
                'external_select', 
                'users_select', 
                'conversations_select', 
                'channels_select', 
                'overflow',
                'datepicker',
            ]:
                raise ValueError(
                    'context elements must be Slack buttons, select menus, '
                    'overflow menus, or date pickers\nSee '
                    'https://api.slack.com/reference/block-kit/blocks#actions'
                    'for more information.'
                )

        super(Actions, self).__init__(block)
