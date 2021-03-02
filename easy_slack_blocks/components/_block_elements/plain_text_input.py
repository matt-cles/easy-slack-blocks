class PlainTextInput(dict):
    """Generate a PlainTextInput element.

    See Slack documentation for the PlainTextInput Block Element here:
    https://api.slack.com/reference/block-kit/block-elements#input
    """

    def __init__(
        self, 
        action_id,
        *,
        placeholder=None,
        initial_value=None,
        multiline=False,
        min_length=None,
        max_length=None,
        dispatch_action_config=None,
    ):

        plain_text_input = {
            'type': 'plain_text_input',
            'action_id': action_id,
            'multiline': multiline,
        }
        
        if placeholder:
            if isinstance(placeholder, str):
                placeholder = Text(
                    text=placeholder, 
                    text_type=Text.PLAIN_TEXT, 
                    emoji=False,
                )
            plain_text_input['placeholder'] = placeholder

        if initial_value:
            plain_text_input['initial_value'] = initial_value

        if min_length:
            plain_text_input['min_length'] = min_length

        if max_length:
            plain_text_input['max_length'] = max_length

        if dispatch_action_config:
            plain_text_input['dispatch_action_config'] = (
                dispatch_action_config
            )

        ### TODO:
        ### add element validation

        super(PlainTextInput, self).__init__(plain_text_input)
        