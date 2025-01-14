"""
Title: Implement Trie
URL: https://leetcode.com/problems/implement-trie-prefix-tree/description/
Difficulty: Medium
Tags: NeetCode 150, Grind, Blind 75

Approach:
- need to make a separate TrieNode class with a dictionary and end_of_word as the class variables
- init just defines root to be an empty TrieNode
- for all functions, make a copy of the root and use that to iterate like in linked lists
                  also make sure to actually go to the next child with node = node.children[c]
- insert: iterate through word, if the current character is not in the children of the 
          current TrieNode, we can set an empty TrieNode 
          make sure to set end_of_word as True
- search: same as insert, just make sure to return false if character is not in children or at the very end,
          if the last-checked TrieNode is NOT an end of a word
- startsWith: same code as search, just we return true at the end no matter what once we iterate through the prefix
- delete: not part of original question but might be asked



Time Complexity: O(m) -> m is the key length
Space Complexity: O(m) -> same

this is for insert. search and startsWith have O(1) time complexity



Solution:
"""
from template import *

class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        
        node.end_of_word = True

    def search(self, word: str) -> bool:
        node = self.root
        for c in word:
            if c not in node.children:
                return False
            node = node.children[c]
        
        return node.end_of_word

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for c in prefix:
            if c not in node.children:
                return False
            node = node.children[c]
        
        return True
    
    def deleteWord(self, word: str) -> None:
        def dfs(node, word, i):
            if i == len(word):
                if not node.end_of_word: # word is not in Trie
                    return False
                
                node.end_of_word = False # delete word by marking end_of_word to be false
                return len(node.children) == 0 # still might be more words (ex deleting app but having apple in Trie)

            if word[i] not in node.children:
                return False # word is not in Trie
            
            need_delete = dfs(node.children[word[i]], word, i + 1)
            # checks if we can safely delete a node -ie no children.
            # for example, if we only had app, we could delete the last p since it has no children
            # then we could delete the first p since it now has no children, etc
            # but if we want to delete app but have apple in the tree, the second p
            # will still have children (l) so we can't delete it. we just have to mark 
            # end_of_word as False to effectively delete it
            if need_delete:
                node.children.pop(word[i])
                return len(node.children) == 0
            
            return False
        
        dfs(self.root, word, 0)
    



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)



"""
Question:

A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

Implement the Trie class:

Trie() Initializes the trie object.
void insert(String word) Inserts the string word into the trie.
boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.
 

Example 1:

Input
["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
Output
[null, null, true, false, true, null, true]

Explanation
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // return True
trie.search("app");     // return False
trie.startsWith("app"); // return True
trie.insert("app");
trie.search("app");     // return True
 

Constraints:

1 <= word.length, prefix.length <= 2000
word and prefix consist only of lowercase English letters.
At most 3 * 104 calls in total will be made to insert, search, and startsWith.
"""