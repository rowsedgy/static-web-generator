import unittest
from textnode import TextNode, TextType
from split_nodes_delimiter import split_nodes_delimiter

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_not_text(self):
        node = TextNode("`code block`", TextType.CODE)
        new_node = split_nodes_delimiter([node], '`', TextType.CODE)
        self.assertEqual(str(new_node), '[TextNode(code block, code_text, None)]')

    def test_bad_markdown(self):
        node = TextNode('this is bad *bold', TextType.TEXT)
        with self.assertRaises(Exception) as cm:
            split_nodes_delimiter([node], '*', TextType.BOLD)
        exception = str(cm.exception)
        self.assertEqual(exception, "That's invalid markdown syntax")

    def test_mutiple_words(self):
        node1 = TextNode('This is *bold1* and *bold text* too', TextType.TEXT)
        node2 = TextNode('This is only *one bold*', TextType.TEXT)
        new_nodes = split_nodes_delimiter([node1, node2], '*', TextType.BOLD)
        self.assertEqual(len(new_nodes), 7)

    

if __name__ == "__main__":
    unittest.main()