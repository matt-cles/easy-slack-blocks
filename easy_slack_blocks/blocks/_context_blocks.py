from ..components import Text

class Context(dict):
    """Generate a Context Block.

    See Slack documentation for the Context Block here:
    https://api.slack.com/reference/block-kit/blocks#context
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
            'type': 'context',
            'elements': elements,
        }

        # Add block_id, if given
        if block_id:
            block['block_id'] = block_id

        # Validate and normalize block elements
        if len(elements) > 10:
            raise ValueError(
                'the maximum number of objects allowed in the context'
                'elements is 10\n '
                'See https://api.slack.com/reference/block-kit/blocks#context'
                'for more information.'
            )

        if len(block.get('block_id', [])) > 255:
            raise ValueError(
                'the maximum length of a block_id is 255 characters\n'
                'See https://api.slack.com/reference/block-kit/blocks '
                'for more information.'
            )

        for i, element in enumerate(elements):
            if isinstance(element, str):
                element = Text(element)
                elements[i] = element

            element_type = element.get('type') 
            if not element_type in ['mrkdwn', 'plain_text', 'image']:
                raise ValueError(
                    'context elements must be Slack text objects or image '
                    'elements\nSee '
                    'https://api.slack.com/reference/block-kit/blocks#context'
                    'for more information.'
                )

        super(Context, self).__init__(block)
