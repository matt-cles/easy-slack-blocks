class Checkbox(dict):
    """Generate a Checkbox element.

    See Slack documentation for the Checkbox Block Element here:
    https://api.slack.com/reference/block-kit/block-elements#checkboxes
    """

    def __init__(
        self, 
        action_id,
        options,
        *,
        initial_options=None,
        confirm=None,
    ):
        if not isinstance(options, list):
            options = [options]


        checkbox = {
            'type': 'checkboxes',
            'action_id': action_id,
            'options': options
        }

        if initial_options:
            if not isinstance(initial_options, list):
                initial_options = [initial_options]
            checkbox['initial_options'] = initial_options

        if confirm:
            checkbox['confirm'] = confirm

        ### TODO:
        ### add element validation

        super(Checkbox, self).__init__(checkbox)
        