import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

# class TestHTMLNode(unittest.TestCase):
#     def test_to_html(self):
#         node = HTMLNode()
#         self.assertRaises(NotImplementedError, node.to_html)
    
#     def test_props_to_html(self):
#         node = HTMLNode(props={'href': 'google.com', 'id': 'main'})
#         expected = ' href="google.com" id="main"'
#         self.assertEqual(node.props_to_html(), expected)
    
#     def test_props_to_html_empty(self):
#         node = HTMLNode()
#         expected = ''
#         self.assertEqual(node.props_to_html(), expected)

# class TestLeafNode(unittest.TestCase):
#     def test_to_html(self):
#         leaf = LeafNode('p', 'Hello, world!')
#         self.assertEqual(leaf.to_html(), '<p>Hello, world!</p>')

# class TestParentNode(unittest.TestCase):
#     def test_to_html_with_children(self):
#         child_node = LeafNode('span', 'child')
#         parent_node = ParentNode('div', [child_node])
#         self.assertEqual(parent_node.to_html(), '<div><span>child</span></div>')

#     def test_to_html_with_grandchildren(self):
#         grandchild_node = LeafNode('b', 'grandchild')
#         child_node = ParentNode('span', [grandchild_node])
#         parent_node = ParentNode('div', [child_node])
#         self.assertEqual(
#             parent_node.to_html(),
#             "<div><span><b>grandchild</b></span></div>",
#         )

#     def test_parent_no_tag(self):
#         child_node = LeafNode('span', 'child')
#         parent_node = ParentNode(None, [child_node])
#         with self.assertRaises(ValueError) as cm:
#             parent_node.to_html()
#         exception = cm.exception
#         self.assertEqual(str(exception), "All parent nodes must have a tag")
    
#     def test_parent_valueerror_messages(self):
#         child_node = LeafNode('span', 'child')
#         parent_nochild_node = ParentNode('b', None)
#         parent_notag_node = ParentNode(None, [child_node])

#         with self.assertRaises(ValueError) as nochild_cm:
#             parent_nochild_node.to_html()
#         nochild_exception = str(nochild_cm.exception)

#         with self.assertRaises(ValueError) as notag_cm:
#             parent_notag_node.to_html()
#         notag_exception = str(notag_cm.exception)

#         self.assertNotEqual(nochild_exception, notag_exception)

if __name__ == "__main__":
    unittest.main()
