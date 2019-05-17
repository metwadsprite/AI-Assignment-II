from search import Problem
from copy import deepcopy

class NPuzzleProblem(Problem):
    def __init__(self, init_state, final_state, board_size):
        Problem.__init__(self, init_state, final_state)
        self.board_size = board_size
    
    
    def actions(self, state):
        ret_actions = ['UP', 'DOWN', 'LEFT', 'RIGHT']

        empty_pos = state.index(0)
        
        if empty_pos < self.board_size:
            ret_actions.remove('UP')

        if empty_pos >= self.board_size * (self.board_size - 1):
            ret_actions.remove('DOWN')

        if empty_pos % self.board_size == 0:
            ret_actions.remove('LEFT')

        if empty_pos % self.board_size == self.board_size - 1:
            ret_actions.remove('RIGHT')

        return ret_actions
    
    
    def result(self, state, action):
        new_state = list(deepcopy(state))
        direction = {"UP" : -self.board_size, "DOWN" : +self.board_size, "LEFT" : -1, "RIGHT" : +1}

        empty_pos = new_state.index(0)
        move_pos = empty_pos + direction[action]

        new_state[empty_pos], new_state[move_pos] = new_state[move_pos], new_state[empty_pos]

        return tuple(new_state)

    
    def h1(self, node):
        tile_sum = 0

        for i in range(len(node.state)):
            j = self.goal.index(node.state[i])

            if i // self.board_size != j // self.board_size:
                tile_sum += 1
            if i % self.board_size != j % self.board_size:
                tile_sum += 1

        return tile_sum


    def h2(self, node):
        manhat_dist = 0
        seq_score = 1

        for i in range(len(node.state)):
            j = self.goal.index(node.state[i])
            manhat_dist += abs((i // self.board_size) - (j // self.board_size)) + \
                abs((i % self.board_size) - (j % self.board_size))

        for i in range(len(node.state) - 1):
            goal_pos = self.goal.index(node.state[i])
            if goal_pos + 1 == self.board_size**2:
                continue
            elif node.state[i + 1] != self.goal[goal_pos + 1]:
                seq_score += 2

        return manhat_dist + self.board_size * seq_score
