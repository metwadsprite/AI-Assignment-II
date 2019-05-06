import search
import utils
import copy

class WaterJugProblem(search.Problem):
    
    def __init__(self, init_state, final_state, max_caps):
        self.initial = init_state
        self.goal = final_state
        self.max_caps = max_caps


    def actions(self, state):
        return_actions = []

        for i in range(len(state)):
            if state[i] != self.max_caps[i]:
                new_action = dict()
                new_action[i] = self.max_caps[i] - state[i]

                return_actions.append(new_action)

            if state[i] != 0:
                new_action = dict()
                new_action[i] = -state[i]

                return_actions.append(new_action)

        for i in range(len(state) - 1):
            for j in range(i, len(state)):
                move_quant = min(self.max_caps[j] - state[j], state[i])
                
                if move_quant == 0:
                    continue
                
                new_action = dict()
                
                new_action[j] = move_quant
                new_action[i] = -move_quant

                return_actions.append(new_action)
        
        for i in range(len(state) - 1, 1):
            for j in range(i, 0):
                move_quant = min(self.max_caps[j] - state[j], state[i])
                
                if not move_quant:
                    continue

                new_action = dict()
                
                new_action[j] = move_quant
                new_action[i] = -move_quant
                return_actions.append(new_action)

        print(return_actions)
        return return_actions

    
    def result(self, state, action):
        for key, quant in action.items():
            state[key] += quant
            
        print(state)
        return state