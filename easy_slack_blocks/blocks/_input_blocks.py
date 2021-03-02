from ..components import Text

class Input(dict):
    """Generate an Input Block.

    See Slack documentation for the Input Block here:
    https://api.slack.com/reference/block-kit/blocks#input
    """
    def __init__(
        self, 
        label, 
        element, 
        *, 
        dispatch_action=None, 
        hint=None, 
        optional=None, 
        block_id=None,
    ):  
        # Start the base block
        block = {'type': 'input'}

        # Start by adding all parameters to the block
        if isinstance(label, str):
            label = Text(
                text=label,
                text_type=Text.PLAIN_TEXT,
            )
        block['label'] = label
        block['element'] = element

        if dispatch_action:
            block['dispatch_action'] = dispatch_action

        if hint:
            block['hint'] = hint

        if optional:
            block['optional'] = optional

        if block_id:
            block['block_id'] = block_id

        ### TODO: ###
        ###   validate block elements

        super(Input, self).__init__(block)
