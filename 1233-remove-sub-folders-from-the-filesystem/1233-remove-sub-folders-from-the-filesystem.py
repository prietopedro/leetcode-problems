class TrieNode:
    def __init__(self):
        self.children = {}
        self.isFolder = False

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        root = TrieNode()
        output = []
        for directory in folder:
            path = directory.split('/')[1:]
            curr = root
            for subdirectory in path:
                if subdirectory not in curr.children:
                    curr.children[subdirectory] = TrieNode()
                curr = curr.children[subdirectory]
                if curr.isFolder:
                    break
            if not curr.isFolder:
                curr.isFolder = True
                output.append(directory)


        return output
