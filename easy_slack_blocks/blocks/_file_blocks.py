class File(dict):
    """Generate a File Block.

    See Slack documentation for the File Block here:
    https://api.slack.com/reference/block-kit/blocks#file
    """
    def __init__(
        self, 
        external_id: str,
        *,
        source: str='remote',
        block_id: str=None,
    ):  
        # Start the base block
        block = {
            'type': 'file',
            'external_id': external_id,
            'source': source,
        }

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

        super(File, self).__init__(block)
