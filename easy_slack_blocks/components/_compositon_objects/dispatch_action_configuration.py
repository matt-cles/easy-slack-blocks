class DispatchActionConfiguration(object):
    """Slack Dispatch Action Configuration composition object builder.

    For more information, see the following URL:
    https://api.slack.com/reference/block-kit/composition-objects#dispatch_action_config"""

    ON_ENTER_PRESSED = 'on_enter_pressed'
    ON_CHARACTER_ENTERED = 'on_character_entered'

    ALL_DISPATCH_ACTION_CONFIGURATIONS = [
        ON_ENTER_PRESSED,
        ON_CHARACTER_ENTERED,
    ]

    def __init__(self, trigger_actions_on, *, validate=True):
        if not isinstance(trigger_actions_on, list):
            trigger_actions_on = [trigger_actions_on]
        

        if validate:
            max_len = len(ALL_DISPATCH_ACTION_CONFIGURATIONS)
            if (
                len(trigger_actions_on) < 1 or 
                len(trigger_actions_on) > max_len
            ):
                raise ValueError(
                    'trigger_actions_on should be one or both of: '
                    f'{ON_ENTER_PRESSED}, {ON_CHARACTER_ENTERED}'
                )

            for action in trigger_actions_on:
                if action not in ALL_DISPATCH_ACTION_CONFIGURATIONS:
                    raise ValueError(
                        'trigger_actions_on should be one or both of: '
                        f'{ON_ENTER_PRESSED}, {ON_CHARACTER_ENTERED}'
                    )

        super(DispatchActionConfiguration, self).__init__(
            trigger_actions_on=trigger_actions_on,
        )
