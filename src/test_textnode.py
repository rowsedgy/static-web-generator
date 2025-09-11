import unittest

from textnode import TextNode, TextType, text_node_to_html

# class TestTextNode(unittest.TestCase):
    # def test_eq(self):
    #     node = TextNode("This is a text node", TextType.BOLD)
    #     node2 = TextNode("This is a text node", TextType.BOLD)
    #     self.assertEqual(node, node2)

    # def test_not_eq(self):
    #     node3 = TextNode("This is a text node", TextType.ITALIC)
    #     node4 = TextNode("This is a text node", TextType.BOLD)
    #     self.assertNotEqual(node3, node4)
    
    # def test_eq_again(self):
    #     node3 = TextNode("This is a text node", TextType.ITALIC)
    #     node4 = TextNode("This is a text node", TextType.BOLD)
    #     self.assertNotEqual(node3, node4)
    
    # def test_text(self):
    #     node = TextNode('This is a text node', TextType.TEXT)
    #     html_node = text_node_to_html(node)
    #     self.assertEqual(html_node.tag, None)
    #     self.assertEqual(html_node.value, 'This is a text node')
    
    # def test_bold(self):
    #     node = TextNode('This is a bold node', TextType.BOLD)
    #     html_node = text_node_to_html(node)
    #     self.assertEqual(html_node.tag, 'b')
    #     self.assertEqual(html_node.value, 'This is a bold node')

    # def test_italic(self):
    #     node = TextNode('This is an italic node', TextType.ITALIC)
    #     html_node = text_node_to_html(node)
    #     self.assertEqual(html_node.tag, 'i')
    #     self.assertEqual(html_node.value, 'This is an italic node')
    
    # def test_code(self):
    #     node = TextNode('This is a code node', TextType.CODE)
    #     html_node = text_node_to_html(node)
    #     self.assertEqual(html_node.tag, 'code')
    #     self.assertEqual(html_node.value, 'This is a code node')

    # def test_link(self):
    #     node = TextNode('This is a code node', TextType.LINK, 'www.google.com')
    #     html_node = text_node_to_html(node)
    #     self.assertEqual(html_node.tag, 'a')
    #     self.assertEqual(html_node.value, 'This is a code node')
    #     self.assertEqual(html_node.props, {'href': 'www.google.com'})
    
    # def test_image(self):
    #     node = TextNode('This is an image node', TextType.IMAGE, 'image.jpg')
    #     html_node = text_node_to_html(node)
    #     self.assertEqual(html_node.tag, 'img')
    #     # self.assertEqual(html_node.value, 'This is an image node')
    #     self.assertEqual(html_node.props, {'src': 'image.jpg', 'alt': 'This is an image node'})

    

if __name__ == "__main__":
    unittest.main()