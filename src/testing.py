import re
from extract_markdown_links import extract_markdown_images, extract_markdown_links
from textnode import TextNode, TextType

node = TextNode(
    "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
    TextType.TEXT,
)

links = extract_markdown_links(node.text)



new_nodes = []

# for link in links:
#     # print(f'Links {link[0], link[1]}')
#     sections = node.text.split(f'[{link[0]}]({links[1]})')
#     print(sections)
#     new_nodes.append(TextNode(sections[0], TextType.TEXT))
# print(new_nodes)

sections = node.text.split(f'[{links[0][0]}]({links[0][1]})')