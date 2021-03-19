class Filter(dict):
    """Slack Filter composition object builder.

    For more information, see the following URL:
    https://api.slack.com/reference/block-kit/composition-objects#
    filter_conversations
    """

    PUBLIC = 'public'
    PRIVATE = 'private'
    IM = 'im'
    MPIM = 'mpim'

    def __init__(
        self, 
        include=None,
        exclude_external_shared_channels=False,
        exclude_bot_users=False,
        *,
        validate=True,
    ):
        if include is None:
            include = [
                PUBLIC,
                PRIVATE,
                IM,
                MPIM,
            ]

        if not isinstance(include, list):
            include = [include]

        super(Filter, self).__init__(
            include=include,
            exclude_external_shared_channels=exclude_external_shared_channels,
            exclude_bot_users=exclude_bot_users,
        )

        if validate:
            self.validate()
        
    def validate(self):
        for element in self.get('include'):
            if element not in [PUBLIC, PRIVATE, IM, MPIM]:
                raise ValueError(
                    '\'include\' must be an array of strings from the '
                    'following options: im, mpim, private, and public\n'
                    'see https://api.slack.com/reference/block-kit/'
                    'composition-objects#filter_conversations__fields for more '
                    'information'
                )

        if not isinstance(exclude_external_shared_channels, bool):
            raise ValueError(
                '\'exclude_external_shared_channels\' must be a Boolean.\n'
                'see https://api.slack.com/reference/block-kit/composition-'
                'objects#filter_conversations__fields for more information'
            )

        if not isinstance(exclude_bot_users, bool):
            raise ValueError(
                '\'exclude_bot_users\' must be a Boolean.\nsee https://api.'
                'slack.com/reference/block-kit/composition-objects#'
                'filter_conversations__fields for more information'
            )
