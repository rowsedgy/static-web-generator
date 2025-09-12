from enum import Enum
from textnode import TextType, TextNode
from extract_markdown_links import extract_markdown_images, extract_markdown_links



def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != Text.TEXT:
            new_nodes.append(node)
            continue

        split_text = node.text.split(delimiter)
        
        if len(split_text) % 2 == 0:
            raise Exception("That's invalid markdown syntax")
        
        for i in range(len(split_text)):
            nodes = []
            if i % 2 == 0:
                if split_text[i]:
                    nodes.append(TextNode(split_text[i], TextType.TEXT))
            else:
                nodes.append(TextNode(split_text[i], text_type))
            new_nodes.extend(nodes)
    return new_nodes

def split_nodes_image(old_nodes):
    new_nodes = []

    for node in old_nodes:
        image_links = extract_markdown_images(node.text)
        text = node.text
        for list in image_links:
            for link in list:
                text = text.replace(link, '')
    text = text.split('[]()')

def split_nodes_link(old_nodes):
    pass
