from ..components import Text

class Section(dict):
    """docstring for Section"""
    def __init__(
        self, 
        *,
        text=None,
        text_type=None,
        emoji=None,
        verbatim=None,
        fields=None,
        accessory=None,
        block_id=None,
    ):  
        # Start the base block
        block = {'type': 'section'}

        # Start by adding all parameters to the block
        if text:
            if isinstance(text, str):
                text = Text(
                    text=text,
                    text_type=text_type,
                    emoji=emoji,
                    verbatim=verbatim,
                )
            block['text'] = text

        if fields:
            block['fields'] = fields

        if accessory:
            block['accessory'] = accessory

        if block_id:
            block['block_id'] = block_id

        ### TODO: ###
        ###   validate block elements

        super(Section, self).__init__(block)
