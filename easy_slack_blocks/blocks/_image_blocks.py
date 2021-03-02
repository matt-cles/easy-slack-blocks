from ..components import Image as ImageComponent

class Image(dict):
    """Generate an Image Block.

    See Slack documentation for the Input Block here:
    https://api.slack.com/reference/block-kit/blocks#image
    """
    def __init__(
        self,
        *,
        image=None,
        image_url=None,
        text_description=None,
        title_text=None,
        block_id=None,
    ):

        # Start the base block
        block = {'type': 'image'}

        # Start by adding all parameters to the block
        if image:
            if isinstance(text, dict):
                block['image_url'] = image.get('image_url')
                block['alt_text'] = image.get('alt_text')
        
        if image_url:
            block['image_url'] = image_url

        if text_description:
            block['alt_text'] = text_description

        if title_text:
            block['title'] = title_text

        if block_id:
            block['block_id'] = block_id

        ### TODO: ###
        ###   validate block elements

        super(Image, self).__init__(block)
