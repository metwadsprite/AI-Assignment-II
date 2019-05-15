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

        empty_pos = new_state.index(0)
        move_pos = empty_pos

        if action == 'UP':
            move_pos -= self.board_size
        elif action == 'DOWN':
            move_pos += self.board_size
        elif action == 'LEFT':
            move_pos -= 1
        elif action == 'RIGHT':
            move_pos += 1

        new_state[empty_pos] = new_state[move_pos]
        new_state[move_pos] = 0

        return tuple(new_state)

    
    # TODO: Heurisitics