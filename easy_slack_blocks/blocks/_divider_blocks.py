class Divider(dict):
    """Generate a Divider Block.

    See Slack documentation for the Divider Block here:
    https://api.slack.com/reference/block-kit/blocks#divider
    """
    def __init__(
        self, 
        *,
        block_id: str=None,
    ):  
        # Start the base block
        block = {'type': 'divider'}

        # Add all block_id to the block, if it was given
        if block_id:
            block['block_id'] = block_id

        # Validate block elements
        if len(block.get('block_id', [])) > 255:
            raise ValueError(
                'the maximum length of a block_id is 255 characters\n'
                'See https://api.slack.com/reference/block-kit/blocks '
                'for more information.'
            )

        super(Divider, self).__init__(block)
