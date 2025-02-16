from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.sentences = defaultdict(int)  # Maps sentence to its frequency

class AutoCompleteSystem:
    def __init__(self, sentences, times):
        self.root = TrieNode()
        self.current_input = ""
        self.current_node = self.root

        for sentence, time in zip(sentences, times):
            self.add_sentence(sentence, time)

    def add_sentence(self, sentence, time):
        node = self.root
        for char in sentence:
            node = node.children[char]
            node.sentences[sentence] += time
        
    def input(self, c):
        if c == '#':
            self.add_sentence(self.current_input, 1)
            self.current_input = ""
            self.current_node = self.root
            return []

        self.current_input += c

        if self.current_node:
            self.current_node = self.current_node.children.get(c)
        
        if not self.current_node:
            return []

        # Retrieve and sort sentences by frequency and ASCII order
        sorted_sentences = sorted(
            self.current_node.sentences.items(),
            key=lambda x: (-x[1], x[0])
        )

        return [sentence for sentence, _ in sorted_sentences[:3]]
#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    while t > 0:
        n = int(input())
        sentences = []
        times = []
        for _ in range(n):
            sentence = input()
            sentences.append(sentence)
            time = int(input())
            times.append(time)

        obj = AutoCompleteSystem(sentences, times)

        q = int(input())
        for _ in range(q):
            query = input()
            qq = ""
            for x in query:
                qq += x
                suggestions = obj.input(x)
                if x == '#':
                    continue
                print('Typed : "' + qq + '" , Suggestions:')
                for y in suggestions:
                    print(y)

        t -= 1

# } Driver Code Ends