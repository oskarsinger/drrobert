# TODO: implement find all
class SuffixTree:

    def __init__(self, vocabulary=None):

        self.tree = {}

        if vocabulary is not None:
            self._populate(vocabulary)

    def _populate(self, vocabulary):

        for word in vocabulary:
            self.insert(word)

    def insert(self, word, value=None):

        self._recursive_insert(self.tree, word, value)
        
    def _recursive_insert(self, subtree, subword, value):

        letter = subword[0]
        is_terminal = len(subword) == 1

        if letter in subtree:
            if is_terminal:
                subtree[letter].is_terminal = True
                subtree[letter].value = value
            else:
                self._recursive_insert(
                    subtree[letter].children, 
                    subword[1:],
                    value)
        else:
            subtree[letter] = Node(
                is_terminal, 
                value=value)

            if not is_terminal:
                self._recursive_insert(
                    subtree[letter].children, 
                    subword[1:],
                    value)

    def has(self, word):
        
        return self._recursive_has_word(self.tree, word)
    
    def _recursive_has_word(self, subtree, subword):

        letter = subword[0]
        has_word = False
        value = None

        if letter in subtree:
            if len(subword) == 1:
                if subtree[letter].is_terminal:
                    has_word = True
                    value = subtree[letter].value
            else:
                (has_word, value) = self._recursive_has_word(
                    subtree[letter].children,
                    subword[1:])

        return (has_word, value)

class Node:

    def __init__(self, is_terminal, value=None):

        self.is_terminal = is_terminal
        self.children = {}
        self.value = value
