class TrieNode:
    def __init__(self, is_end:bool = False):
        self.children = {}
        self.is_end = is_end


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()


    def addWord(self, word: str) -> None:
        # initialize root node
        cur = self.root

        # loop through char of word
        for char in word:
            cur_node = cur.children.get(char)

            if not cur_node:
                # make node
                new_node = TrieNode()
                cur.children[char] = new_node

            # iterate to next node
            cur = cur.children[char]

        # set the is_end flag for the last node
        cur.is_end = True
        

    def search(self, word: str) -> bool:

        def dfs(node, index):
            # base case:
            if index == len(word):
                return node.is_end

            char = word[index]
            # wildcard node
            if char == ".":
                # loop through the children
                for child_node in node.children.values():
                    child_check = dfs(child_node, index + 1)
                    if child_check == True:
                        return True

            # iterative cases
            # normal node
            next_node = node.children.get(char)
            if not next_node:
                return False

            return dfs(next_node, index + 1)

        return dfs(self.root, 0)



    









        
