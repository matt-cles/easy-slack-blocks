from .. import Text

class DatePicker(dict):
    """Generate a DatePicker element.

    See Slack documentation for the DatePicker Block Element here:
    https://api.slack.com/reference/block-kit/block-elements#datepicker
    """
    def __init__(
        self, 
        action_id,
        *,
        placeholder=None,
        initial_date=None,
        confirm=None,
    ):
        datepicker = {
            'type': 'datepicker',
            'action_id': action_id,
        }

        if placeholder:
            if isinstance(placeholder, str):
                placeholder = Text(
                    text=placeholder, 
                    text_type=Text.PLAIN_TEXT, 
                    emoji=False,
                )
            datepicker['placeholder'] = placeholder

        if initial_date:
            datepicker['initial_date'] = initial_date

        if confirm:
            datepicker['confirm'] = confirm

        ### TODO:
        ### add element validation

        super(DatePicker, self).__init__(datepicker)
        