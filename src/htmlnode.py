class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        return_text = ""
        if self.props is not None:
            for k, v in self.props.items():
                return_text += f' {k}="{v}"'
        return return_text
    def __repr__(self):
        return (f'HTMLNode({self.tag, self.value, self.children, self.props})')

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None,  props)
        
    def to_html(self):
        if not self.value:
            raise ValueError("All leaf nodes must have a value")
        if not self.tag:
            return str(self.value)
        return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        if not self.tag:
            raise ValueError("All parent nodes must have a tag")
        if not self.children:
            raise ValueError("All parent nodes must have children nodes")
        
        children_to_html_content = ""
        
        for child in self.children:
            children_to_html_content += child.to_html()
        
        children_to_html_base = f"<{self.tag}{self.props_to_html()}>{children_to_html_content}</{self.tag}>"
        
        return children_to_html_base


