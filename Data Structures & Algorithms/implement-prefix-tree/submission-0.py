class TrieNode:
    def __init__(self, is_end = False):
        self.children = {}
        self.is_end = is_end

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        # iterate through the word
        cur = self.root

        for char in word:
            # check if char in children
            cur_node = cur.children.get(char)

            if not cur_node:
                # create note
                new_node = TrieNode()
                cur.children[char] = new_node

            # update cur
            cur = cur.children[char]
    
        # signal last node
        cur.is_end = True


    def search(self, word: str) -> bool:
        cur = self.root

        # iterate through word
        for char in word:
            # if char now in the children return False
            if not cur.children.get(char):
                return False

            cur = cur.children[char]

        # need to return true or false
        return cur.is_end


    def startsWith(self, prefix: str) -> bool:
        cur = self.root

        # iterate through word
        for char in prefix:
            if not cur.children.get(char):
                return False

            cur = cur.children[char]

        # no check for is_end bc its asking if a word starts with this "prefix"
        return True














        