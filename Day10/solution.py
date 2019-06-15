class InvalidQueryException(Exception):
    pass


class WordSearchTree:
    """n-ary (max 26) tree for efficient word-search queries"""

    class LetterNode:
        def __init__(self, letter_value):
            self.value = letter_value
            self.children = {}

        def append_child(self, child_letter):
            self.children[child_letter] = self.__class__(child_letter)

        def has_child_with_letter(self, letter):
            return letter in self.children.keys()

        def get_child_from_letter(self, letter):
            return self.children[letter]

        def has_children(self):
            return self.children != {}

    def __init__(self, root_letter, possible_queries):
        self.root = self.LetterNode(root_letter)
        for query in possible_queries:
            if query[0] == root_letter:
                self.append_possible_query(query)

    def append_possible_query(self, possible_query):
        current_node = self.root
        if possible_query[0] != self.root.value:
            raise InvalidQueryException(
                "Cannot add query starting with {} to search tree with root {}".format(
                    possible_query[0], self.root.value
                )
            )
        else:
            for letter in possible_query:
                if current_node.has_child_with_letter(letter):
                    current_node = current_node.get_child_from_letter(letter)
                else:
                    current_node.append_child(letter)
                    current_node = current_node.get_child_from_letter(letter)

    @staticmethod
    def get_traversals_from_node(search_node, word_prefix=None):
        traversal_words = []

        def inner_recursion(node, traversal_word):
            if not node.has_children():
                traversal_words.append(traversal_word + node.value)
            else:
                for child in node.children.values():
                    inner_recursion(child, traversal_word + node.value)

        inner_recursion(search_node, word_prefix if word_prefix else "")
        return traversal_words

    def get_possible_traversals_from_query(self, query):
        search_root = self.root
        for letter in query:
            if search_root.has_child_with_letter(letter):
                search_root = search_root.get_child_from_letter(letter)
            else:
                return []
        return self.get_traversals_from_node(search_root, word_prefix=query[:-1])


def suggest_completions(query_str, possible_completions):
    completion_tree = WordSearchTree(query_str[0], possible_completions)
    return completion_tree.get_possible_traversals_from_query(query_str)
