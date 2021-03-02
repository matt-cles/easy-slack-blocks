class RadioButton(dict):
    """Generate a RadioButton element.

    See Slack documentation for the RadioButton Block Element here:
    https://api.slack.com/reference/block-kit/block-elements#radio
    """

    def __init__(
        self, 
        action_id,
        options,
        *,
        initial_option=None,
        confirm=None,
    ):
        if not isinstance(options, list):
            options = [options]


        radio_button = {
            'type': 'radio_buttons',
            'action_id': action_id,
            'options': options
        }

        if initial_option:
            radio_button['initial_option'] = initial_option

        if confirm:
            radio_button['confirm'] = confirm

        ### TODO:
        ### add element validation

        super(RadioButton, self).__init__(radio_button)
        