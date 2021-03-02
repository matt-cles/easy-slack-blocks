class OverflowMenu(dict):
    """Generate a OverflowMenu element.

    See Slack documentation for the OverflowMenu Block Element here:
    https://api.slack.com/reference/block-kit/block-elements#overflow
    """

    def __init__(
        self, 
        action_id,
        options,
        *,
        confirm=None,
    ):
        if not isinstance(options, list):
            options = [options]


        overflow = {
            'type': 'overflow',
            'action_id': action_id,
            'options': options
        }
        
        if confirm:
            overflow['confirm'] = confirm

        ### TODO:
        ### add element validation

        super(OverflowMenu, self).__init__(overflow)
        