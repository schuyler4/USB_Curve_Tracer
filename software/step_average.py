class Step_Average:
    def __init__(self, currents, voltages, adc_bit_resolution, dac_bit_resolution):
        self._currents = currents
        self._voltages = voltages
        self._adc_bit_resolution = adc_bit_resolution
        self._dac_bit_resolution = dac_bit_resolution
        self._averaged_currents = None
        self._averaged_voltages = None


    def is_close(self, num1, num2):
        if(num1 > 0 and num2 > 0):
            return ((num1*0.05 + num1) > num2) and (num2 > (num1 - num1*0.05))
        if(num1 < 0 and num2 < 0):
            return ((num1*0.05 + num1) < num2) and (num2 < (num1 - num1*0.05))
        return False


    def find_steps(self):
        currents = self._currents.tolist()
        step_level = currents[0]
        starting_index = 0
        steps = []
        step = [] 
        for i, current in enumerate(currents):
            if(self.is_close(step_level, current)):
                step.append(current)            
            else:
                steps.append(tuple(step))
                step.clear()
                step_level = current
                step.append(current)
        return steps


    def averager(self, the_list):
        average = []
        total = 0
        for i, number in enumerate(the_list):
            total += number
            if(i % self.length == 0):
                average.append(total/self.length)
                total = 0
        return average


    def __call__(self):
        self._averaged_currents = self.averager(self._currents)
        self._averaged_voltages = self.averager(self._voltages) 


    @property 
    def length(self):
        adc_resolution = 2**self._adc_bit_resolution
        dac_resolution = 2**self._dac_bit_resolution
        return adc_resolution/dac_resolution


    @property
    def averaged_currents(self):
        return self._averaged_currents

    
    @property
    def averaged_voltages(self):
        return self._averaged_voltages
