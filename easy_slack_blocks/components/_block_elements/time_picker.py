from .. import Text

class TimePicker(dict):
    """Generate a TimePicker element.

    See Slack documentation for the TimePicker Block Element here:
    https://api.slack.com/reference/block-kit/block-elements#timepicker
    """
    def __init__(
        self, 
        action_id,
        *,
        placeholder=None,
        initial_time=None,
        confirm=None,
    ):
        timepicker = {
            'type': 'timepicker',
            'action_id': action_id,
        }

        if placeholder:
            if isinstance(placeholder, str):
                placeholder = Text(
                    text=placeholder, 
                    text_type=Text.PLAIN_TEXT, 
                    emoji=False,
                )
            timepicker['placeholder'] = placeholder

        if initial_time:
            timepicker['initial_time'] = initial_time

        if confirm:
            timepicker['confirm'] = confirm

        ### TODO:
        ### add element validation

        super(TimePicker, self).__init__(timepicker)
        