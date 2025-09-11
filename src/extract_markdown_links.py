import re

def extract_markdown_images(text):
    list = []
    alt_text = re.findall(r'!\[(.*?)\]', text)
    url = re.findall(r'\((.*?)\)', text)
    if len(alt_text) == len(url):
        for i in range(len(alt_text)):
            list.append((alt_text[i], url[i]))
    
    return list


text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"

print(extract_markdown_images(text))

def extract_markdown_links(text):
    list = []
    anchor_text = re.findall(r'\[(.*?)\]', text)
    url = re.findall(r'\((.*?)\)', text)
    if len(anchor_text) == len(url):
        for i in range(len(anchor_text)):
            list.append((anchor_text[i], url[i]))
    
    return list

text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
print(extract_markdown_links(text))

    