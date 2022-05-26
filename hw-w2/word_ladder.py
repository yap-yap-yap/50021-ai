from search_py3.search import *

WORDS = set(i.lower().strip() for i in open('words2.txt'))
def is_valid_word(word):
    return word in WORDS

def str_to_list(word):
    out = []
    for char in word:
        out.append(char)
    return out

def list_to_str(lst):
    out = ''
    for char in lst:
        out += char
    return out

class WordLadder(Problem):
    # actions are in the form of the index of the letter that is to be changed
    def actions(self, state):
        # print(state)
        action_list = []
        for index, (current_letter, goal_letter) in enumerate(zip(state, self.goal)):
            if current_letter == goal_letter:
                continue
            new_state = self.result(state, index)
            if not is_valid_word(new_state):
                continue
            action_list.append(index)
        return action_list
            
    def result(self, state, action):
        new_word = str_to_list(state)
        new_word[action] = self.goal[action]
        new_word = list_to_str(new_word)
        return new_word


def main():
    ladder = WordLadder('best', 'math') # input the initial and goal word
    goal_node = breadth_first_search(ladder) # change the search strategy here
    if goal_node is None:
        print('there is no solution')
        return None
    node_path = goal_node.path()
    solution = []
    for node in node_path:
        solution.append(node.state)
    print(solution)

if __name__ == "__main__":
    main()