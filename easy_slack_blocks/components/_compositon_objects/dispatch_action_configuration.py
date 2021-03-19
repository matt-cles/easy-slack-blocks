ON_ENTER_PRESSED = 'on_enter_pressed'
ON_CHARACTER_ENTERED = 'on_character_entered'

ALL_DISPATCH_ACTION_CONFIGURATIONS = [
    ON_ENTER_PRESSED,
    ON_CHARACTER_ENTERED,
]

class DispatchActionConfiguration(dict):
    """Slack Dispatch Action Configuration composition object builder.

    For more information, see the following URL:
    https://api.slack.com/reference/block-kit/composition-objects#
    dispatch_action_config
    """

    def __init__(self, trigger_actions_on, *, validate=True):
        if not isinstance(trigger_actions_on, list):
            trigger_actions_on = [trigger_actions_on]
        
        super(DispatchActionConfiguration, self).__init__(
            trigger_actions_on=trigger_actions_on,
        )
        
        if validate:
            self.validate()

    def validate(self):    
        max_len = len(ALL_DISPATCH_ACTION_CONFIGURATIONS)

        trigger_actions_on = self.get('trigger_actions_on')
        if (
            not isinstance(trigger_actions_on, list) or
            len(trigger_actions_on) < 1 or 
            len(trigger_actions_on) > max_len
        ):
            raise ValueError(
                'The \'trigger_actions_on\' parameter must be a list '
                'containing one or both of the values: '
                f'\'{ON_ENTER_PRESSED}\', \'{ON_CHARACTER_ENTERED}\'\nSee '
                'https://api.slack.com/reference/block-kit/composition-'
                'objects#dispatch_action_config__fields for more information.'
            )

        for action in trigger_actions_on:
            if action not in ALL_DISPATCH_ACTION_CONFIGURATIONS:
                raise ValueError(
                    'The \'trigger_actions_on\' parameter must be a list '
                    'containing one or both of the values: '
                    f'\'{ON_ENTER_PRESSED}\', \'{ON_CHARACTER_ENTERED}\'\n'
                    'See https://api.slack.com/reference/block-kit/'
                    'composition-objects#dispatch_action_config__fields for '
                    'more information.'
                )

