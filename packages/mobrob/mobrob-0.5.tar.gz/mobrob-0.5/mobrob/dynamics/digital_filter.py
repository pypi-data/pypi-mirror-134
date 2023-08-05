# code taken from https://github.com/5i0770/wheelchair_gazebo

class Memory(object):
    def __init__(self, ValueType, size):
        self.ValueType = ValueType
        self.memories = [self.ValueType(0) for _ in range(size)]

    def update(self, value):
        self.memories[0] = value
        for k in reversed(range(1, len(self.memories))):
            self.memories[k] = self.memories[k - 1]
        self.memories[0] = self.ValueType(0)


class DirectForm1Structure(object):
    def __init__(self, ValueType, a_coefficients, b_coefficients):
        self.ValueType = ValueType
        self.a_coefficients = a_coefficients
        self.b_coefficients = b_coefficients
        self.input_memory = Memory(ValueType, len(b_coefficients))
        self.output_memory = Memory(ValueType, len(a_coefficients))

    def filter(self, input_signal):
        output_signal = self.b_coefficients[0]*input_signal
        for k in range(1, len(self.b_coefficients)):
            output_signal = output_signal + self.b_coefficients[k]*self.input_memory.memories[k]
        
        for k in range(1, len(self.a_coefficients)):
            output_signal = output_signal - self.a_coefficients[k]*self.output_memory.memories[k]            

        self.input_memory.update(input_signal)
        self.output_memory.update(output_signal)

        return output_signal
        
