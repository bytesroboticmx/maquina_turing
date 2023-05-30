class TuringMachine:
    def __init__(self, tape, initial_state, final_states, transitions):
        self.tape = tape
        self.head = 0
        self.current_state = initial_state
        self.final_states = final_states
        self.transitions = transitions

    def extend_tape(self):
        self.tape.append(None)  

    def run(self):
        while self.current_state not in self.final_states:
            symbol = self.tape[self.head]

            if (self.current_state, symbol) not in self.transitions:
                raise RuntimeError("No transition found for the current state and symbol")

            new_state, new_symbol, move = self.transitions[(self.current_state, symbol)]
            self.tape[self.head] = new_symbol
            self.current_state = new_state

            if self.head == len(self.tape) - 1 and move == 1:
                self.extend_tape()  
            elif self.head == 0 and move == -1:
                self.tape.insert(0, None)  

            self.head += move

    def __str__(self):
        return f"Cinta: {self.tape}\nEstado actual: {self.current_state}\n"

# Ejemplo de uso

tape = ['1', '1', '0', '1', '0', '1', '1']
initial_state = 'q0'
final_states = ['qf']
transitions = {
    ('q0', '0'): ('q0', '0', 1),
    ('q0', '1'): ('q0', '1', 1),
    ('q0', None): ('qf', None, 0)
}

tm = TuringMachine(tape, initial_state, final_states, transitions)
tm.run()
print(tm)
