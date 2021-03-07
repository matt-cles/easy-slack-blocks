import json
from webbrowser import open as open_browser

from ..components import Text
from ..blocks import (
    Actions, 
    Context, 
    Divider,
    File, 
    Header, 
    Image, 
    Input, 
    Section,
)


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

    MESSAGE = 'message',
    MODAL = 'modal',
    ATTACHMENT = 'attachment'
    APP_HOME = HOME = 'home'


    def __init__(self, *args, block_type=None, **kwargs):
        super(BlockBuilder, self).__init__(*args, **kwargs)
        if not block_type:
            block_type = BlockBuilder.MESSAGE
        self._block_type = block_type

        if block_type == BlockBuilder.ATTACHMENT:
            self._color = '#3098c8'

        if block_type == BlockBuilder.MODAL:
            self._title = Text('My easy-slack-blocks App', Text.PLAIN_TEXT, emoji=True)


    def add_actions(
        self, 
        value=None, 
        *,
        elements=None,
        block_id=None,
    ):
        """Add an action block."""
        if not isinstance(value, dict) or value.get('type') != 'actions':
            # If no elements, use value as the elements
            if elements is None:
                elements = value

            value = Actions(
                elements=elements,
                block_id=block_id,
            )
        self.append(value)

    def add_context(
        self, 
        value=None, 
        *,
        elements=None,
        block_id=None,
    ):
        """Add a context block."""
        if not isinstance(value, dict) or value.get('type') != 'context':
            # If no elements, use value as the elements
            if elements is None:
                elements = value

            value = Context(
                elements=elements,
                block_id=block_id,
            )
        self.append(value)
        
    def add_divider(self, *, block_id=None):
        """Add a divider block"""
        block = Divider(block_id=block_id)

        self.append(block)

    def add_file(
        self,
        value=None,
        *,
        external_id: str=None,
        source: str='remote',
        block_id: str=None
    ):
        """Add a file block.
        
        Note that this currently does not support uploading a file, but
        simply creates a block that can display an existing uploaded 
        file by referancing the 'external_id.

        source is another field required by Slack, but currently, the 
        only valid value is 'remote'

        WARNING: File Blocks are only valid for Messages, you cannot use
        this type of blocks in Modals or the Home Tab. see more info
        here: https://api.slack.com/reference/block-kit/blocks#file
        """
        if self._block_type != self.MESSAGE:
            raise ValueError(
                'File block can only be used in messages. If you are '
                'building blocks for a Modal or the Home tab, you cannot'
                'add File blocks'
            )

        if not isinstance(value, dict):
            value = File(
                external_id=external_id,
                source=source,
                block_id=block_id,
            )
        self.append(value)

    def add_header(
        self, 
        value=None, 
        *, 
        text=None,
        emoji=True, 
        block_id=None,
    ):
        """Add a header block."""

        if not isinstance(value, dict) or value.get('type') != 'header':
            # If no explict text was passed, try to use the non-dict value 
            # as the text parameter
            if not text:
                text = value

            value = Header(
                text=text,
                emoji=emoji,
                block_id=block_id,
            )
        self.append(value)

    def add_image(
        self, 
        value=None, 
        *, 
        image=None,
        image_url=None, 
        text_description=None, 
        title_text=None, 
        block_id=None
    ):
        """Add an image block."""

        if not isinstance(value, dict):
            value = Image(
                image=image,
                image_url=image_url,
                text_description=text_description,
                title_text=title_text,
                block_id=block_id
            )
        self.append(value)

    def add_input(
        self, 
        value=None,
        *, 
        label=None, 
        element=None, 
        dispatch_action=False, 
        hint=None, 
        optional=False, 
        block_id=None,
    ):
        """Add an input block.

        Warning, this type of block is only valid in Modals and the Home Tab.
        It cannot be used in a message block.
        """
        if self._block_type == self.MESSAGE:
            raise ValueError(
                'Input block cannot be used in messages. If you are building '
                'blocks for a Modal or the Home tab, initialize the '
                'BlockBuilder with \'block_type\' of BlockBuilder.MODAL or '
                'BlockBuilder.HOME'
            )

        if not isinstance(value, dict):
            value = Input(
                label=label,
                element=element,
                dispatch_action=dispatch_action,
                hint=hint,
                optional=optional,
                block_id=block_id,
            )
        self.append(value)

    def add_section(
        self, 
        value=None, 
        *,
        text=None,
        type=Text.MRKDWN, 
        emoji=None, 
        verbatim=None,
        fields=None, 
        accessory=None, 
        block_id=None
    ):
        """Add a section block."""
        if not isinstance(value, dict) or value.get('type') != 'section':
            # If no explict text was passed, try to use the non-dict value 
            # as the text parameter
            if not text:
                text = value

            value = Section(
                text=text, 
                type=type, 
                emoji=emoji, 
                verbatim=verbatim,
                fields=fields,
                accessory=accessory,
                block_id=block_id,
            )
        self.append(value)

    def add_text(
        self, 
        text, 
        *, 
        type=Text.MRKDWN, 
        emoji=None, 
        verbatim=None, 
        block_id=None,
    ):
        """Simplified alias for adding a text only section block."""
        self.add_section(
            text=text, 
            type=type, 
            emoji=emoji, 
            verbatim=verbatim, 
            block_id=block_id,
        )
    
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
        payload = f'"blocks":{json.dumps(self)}'

        if self._block_type == BlockBuilder.ATTACHMENT:
            payload = (
                '"attachments":'
                f'[{{"color":"{self._color}",{payload}}}]'
            )
        elif self._block_type == BlockBuilder.MODAL:
            payload = (
                f'"type":"modal","title":{json.dumps(self._title)},'
                '"submit": {"type": "plain_text","text": "Submit","emoji": true},'
                '"close": {"type": "plain_text","text": "Cancel","emoji": true},'
                f'{payload}'
            )
        elif self._block_type == BlockBuilder.HOME:
            payload = f'"type":"home",{payload}'


        payload = f'https://app.slack.com/block-kit-builder/#{{{payload}}}'

        return payload

    def open_preview_in_browser(self):
        """Opens a preview of the current Blocks in the BlockBuilder.
        
        Preview opens in a new tab in the default browser.

        This method is recomended for testing/prototyping Slack Block 
        formatting only. 
        """
        open_browser(self.get_url_string())
