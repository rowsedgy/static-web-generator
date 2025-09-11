from enum import Enum
from textnode import TextType, TextNode



def split_nodes_delimiter(old_nodes, delimiter, text_type):
    # delimiters = ('`', '**', '_')
    new_nodes = []

    for node in old_nodes:
        split_text = node.text.split(delimiter)
        if len(split_text) % 2 == 0:
            raise Exception("That's invalid markdown syntax")
        
        for i in range(len(split_text)):
            nodes = []
            if i % 2 == 0:
                nodes.append(TextNode(split_text[i], TextType.TEXT))
            else:
                nodes.append(TextNode(split_text[i], text_type))
    new_nodes.extend(nodes)
    return new_nodes

    

node = TextNode("This is text with a `code block` word", TextType.TEXT)
node2 = TextNode('`bold` text `code text`', TextType.TEXT)
new_nodes = split_nodes_delimiter([node, node2], "`", TextType.CODE)

print(new_nodes)