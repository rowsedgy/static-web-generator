from enum import Enum
from htmlnode import LeafNode, ParentNode, HTMLNode

class TextType(Enum):
    BOLD = 'bold_text'
    ITALIC = 'italic_text'
    CODE = 'code_text'
    LINK = 'link'
    IMAGE = 'image'
    TEXT = 'text'

class TextNode():
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url
    
    def __eq__(self, textnode):
        if not isinstance(textnode, TextNode):
            return False
        return (self.text == textnode.text and
                self.text_type == textnode.text_type and
                self.url == textnode.url)
    
    def __repr__(self):
        return f'TextNode({self.text}, {self.text_type.value}, {self.url})'

def text_node_to_html(text_node):
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(None, text_node.text)
        case TextType.BOLD:
            return LeafNode('b', text_node.text)
        case TextType.ITALIC:
            return LeafNode('i', text_node.text)
        case TextType.CODE:
            return LeafNode('code', text_node.text)
        case TextType.LINK:
            return LeafNode('a', text_node.text, {'href': text_node.url})
        case TextType.IMAGE:
            return LeafNode('img', None, {'src': text_node.url, 'alt': text_node.text})
        case _:
            raise Exception('TextType not found')
