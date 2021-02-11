import json
from webbrowser import open as open_browser

from components.text import Text
from components.actions import Action, Button

class BlockBuilder(list):
    """Simple Class for generating Slack Blocks.

    This class allows for a simplified way to generate Slack blocks to 
    use in a standard Slack API request.

    This class extends the standard list, so that it can be passed to 
    any function that is expecting a list of dict objects (EX: 
    request.post, slack_bolt.App.say, json.dumps, etc...) directly.
    
    See https://api.slack.com/reference/block-kit/blocks for information 
    on the availible Slack Block types.
    """
    def __init__(self, *args, **kwargs):
        super(BlockBuilder, self).__init__(*args, **kwargs)

    def add_actions(
        self,
        actions: list,
        block_id: str=None):
        """Add an action block.

        Parameters:
         - actions: 
            A list of Slack Action object definitions, these include 
            Buttons, Select Menues, Overflow Menus, and Date Pickers.
            Each Actions block may have no more that 5 Actions.
         - block_id (optional): 
            A unique identifier for a block
        """

        if len(actions) > 5:
            raise ValueError(
                'The \'actions\' parameter must be a list with no more than '
                '5 elements'
            )

        block = {
            'type': 'actions',
            'elements': [],
        }
        for element in actions:
            if element['type'] != 'action':
                raise ValueError(
                    'The \'actions\' parameter must be a list of \'Action\' '
                    'object definitions'
                )
            block['elements'].append(element)

        if block_id:
            block['block_id'] = block_id

        self.append(block)

    def add_context(
        self,
        context: list=None,
        *,
        block_id=None,
    ):
        """Add a context block."""
        if context is None:
            raise ValueError(
                'The \'context\' parameter must be a list of \'Text\' or '
                '\'Image\' object definitions'
            )
        elif isinstance(context, str):
            context = [Text(context)]
        elif not isinstance(context, list):
            context = [context]

        if len(context) > 10:
            raise ValueError(
                'The \'context\' parameter must be a list of no more than '
                '10 \'Text\' or \'Image\' object definitions'
            )

        block = {
            'type': 'context',
            'elements': context,
        }

        for element in context:
            element_type = element['type']
            if (element_type != 'mrkdwn' and 
                element_type != 'plain_text' and 
                element_type != 'image'
            ):
                raise ValueError(
                    'The \'context\' parameter must be a list of \'Text\' or '
                    '\'Image\' object definitions'
                )

        if block_id:
            block['block_id'] = block_id

        self.append(block)

    def add_divider(self, *, block_id=None):
        """Add a divider block"""
        block = {
            'type': 'divider',
        }

        if block_id:
            block['block_id'] = block_id

        self.append(block)

    def add_file(
        self,
        external_id: str,
        *,
        source: str='remote',
        block_id: str=None
    ):
        """Add a file block.
        
        Note that this currently does not support uploading a file, but
        simply creates a block that can display an existing uploaded 
        file by referancing the 'extenal_id.

        source is another field required by Slack, but currently, the 
        only valid value is 'remote'

        WARNING: File Blocks are only valid for Messages, you cannot use
        this type of blocks in Modals or the Home Tab. see more info
        here: https://api.slack.com/reference/block-kit/blocks#file
        """

        block = {
            'type': 'file',
            'external_id': external_id,
            'source': source,
        }

        if block_id:
            block['block_id'] = block_id

        self.append(block)

    def add_header(self, text, *, emoji=True, block_id=None):
        """Add a header block."""

        if not isinstance(text, Text):
            text = Text(text, 'plain_text', emoji=emoji)

        if text['type'] != 'plain_text':
            raise ValueError(
                'header blocks can only accept text components with a '
                '\'text_type\' of \'plain_text\'\n'
                'See https://api.slack.com/reference/block-kit/blocks#header '
                'for more information.'
            )

        block = {
            'type': 'header',
            'text': text,
        }

        if block_id:
            block['block_id'] = block_id
        
        self.append(block)

    def add_image(
        self, 
        image=None, 
        *, 
        image_url=None, 
        text_description=None, 
        title_text=None, 
        block_id=None
    ):
        """Add an image block."""
        
        #TODO add parameter validation

        if image:
            image_url = image.get('image_url')
            text_description = image.get('alt_text')
        
        block = {
            'type': 'image',
            'image_url': image_url,
            'alt_text': text_description
        }

        if title_text:
            block['title'] = {
                'type': 'plain_text',
                'text': title_text,
            }

        if block_id:
            block['block_id'] = block_id

        self.append(block)

    def add_input(self, *, block_id=None):
        """Add an input block."""

        # TODO add this block definition
        ...

    def add_section(self, text=None, *, fields=None, accessory=None, block_id=None):
        """Add a section block."""

        # TODO add parameter validation
        block = {'type': 'section'}

        if text:
            if isinstance(text, str):
                text = Text(text)
            block['text'] = text
            
            if fields:
                block['fields'] = fields

        elif fields:
            block['fields'] = fields
        else:
            raise ValueError(
                'section blocks need either a text or fields parameter'
            )

        # TODO implement accessory object additions
        
        if block_id:
            block['block_id'] = block_id

        self.append(block)

    def add_text(self, text, *, block_id=None):
        """Simplified alias for adding a text only section block."""
        self.add_section(text=text, block_id=block_id)
    
    def add_raw_block(self, block_type, **kwargs):
        """Add a 'raw' block.
        
        The purpose of this method is to allow for any new Slack Blocks
        that are not currently implemented in the current version of
        the BlockBuilder to still be added if needed. 

        This method should not be used in place of the other specialized
        BlockBuilder methods, as it will do no type checking for you. Use
        with caution.
        """
        self.append(dict(type=block_type, **kwargs))

    def get_url_string(self):
        """Get a URL to view the current blocks in the BlockBuilder."""
        json_string = json.dumps(self)
        return (
            'https://app.slack.com/block-kit-builder/#{"blocks":'
            f'{json_string}' '}'
            )

    def open_preview_in_browser(self):
        """Opens a preview of the current Blocks in the BlockBuilder.
        
        Preview opens in a new tab in the default browser.

        This method is recomended for testing/prototyping Slack Block 
        formatting only. 
        """
        open_browser(self.get_url_string())
