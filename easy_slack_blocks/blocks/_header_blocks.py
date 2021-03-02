from ..components import Text

class Header(dict):
    """Generate a Header Block.

    See Slack documentation for the Header Block here:
    https://api.slack.com/reference/block-kit/blocks#header
    """
    def __init__(
        self, 
        text,
        *,
        emoji=None,
        block_id=None,
    ):  
        # Start the base block
        block = {'type': 'header'}

        # Start by adding all parameters to the block
        if isinstance(text, str):
            text = Text(
                text=text,
                text_type=Text.PLAIN_TEXT,
                emoji=emoji,
            )
        block['text'] = text

        if block_id:
            block['block_id'] = block_id

        # Validate the block elements
        if block.get('text').get('type') != Text.PLAIN_TEXT:
            raise ValueError(
                'header blocks can only accept text components with a '
                '\'text_type\' of \'plain_text\'\n'
                'See https://api.slack.com/reference/block-kit/blocks#header '
                'for more information.'
            )
        if len(block.get('text').get('text')) > 150:
            raise ValueError(
                'header blocks can only accept text components with a '
                'maximum length of 150 characters\n'
                'See https://api.slack.com/reference/block-kit/blocks#header '
                'for more information.'
            )
        if len(block.get('block_id', [])) > 255:
            raise ValueError(
                'the maximum length of a block_id is 255 characters\n'
                'See https://api.slack.com/reference/block-kit/blocks '
                'for more information.'
            )

        # initilize the class dict after the validated input
        super(Header, self).__init__(block)
