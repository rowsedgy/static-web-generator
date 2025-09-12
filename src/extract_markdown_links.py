import re

def extract_markdown_images(text):
    list = []
    alt_text = re.findall(r'!\[(.*?)\]', text)
    url = re.findall(r'\((.*?)\)', text)
    if len(alt_text) == len(url):
        for i in range(len(alt_text)):
            list.append((alt_text[i], url[i]))
    
    return list


def extract_markdown_links(text):
    list = []
    anchor_text = re.findall(r'\[(.*?)\]', text)
    url = re.findall(r'\((.*?)\)', text)
    if len(anchor_text) == len(url):
        for i in range(len(anchor_text)):
            list.append((anchor_text[i], url[i]))
    
    return list

    