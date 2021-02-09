class Text(dict):
    """docstring for Text"""
    def __init__(self, text, text_type='mrkdwn', *, emoji=None, verbatim=None):
        if text_type == 'mrkdwn':
            if emoji is not None:
                raise ValueError(
                    'The \'emoji\' field is only usable when \'text_type\' '
                    'is \'plain_text\'.'
                )
            # Set default 'verbatim' value if none was passed
            if verbatim is None:
                verbatim = False
            super(Text, self).__init__(
                text=text, 
                type=text_type, 
                verbatim=verbatim,
            )
        elif text_type == 'plain_text':
            if verbatim is not None:
                raise ValueError(
                    'The \'verbatim\' field is only usable when '
                    '\'text_type\' is \'mrkdwn\'.'
                )
            # Set default 'emoji' value if none was passed
            if emoji is None:
                emoji = True
            super(Text, self).__init__(
                text=text,
                type=text_type,
                emoji=emoji,
            )
        else:
            raise ValueError(
                '\'text_type\' must either be \'mrkdwn\' or \'plain_text\''
            )
