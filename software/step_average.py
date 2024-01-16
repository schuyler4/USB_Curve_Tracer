class Step_Average:

    STEP_VARIANCE = 0.05

    def __init__(self, currents, voltages, adc_bit_resolution, dac_bit_resolution):
        self._currents = currents
        self._voltages = voltages
        self._adc_bit_resolution = adc_bit_resolution
        self._dac_bit_resolution = dac_bit_resolution
        self._step_currents = []
        self._step_voltages = []
        self._averaged_currents = []
        self._averaged_voltages = []


    def is_close(self, num1, num2):
        if(num1 > 0 and num2 > 0):
            positive_bound = (num1*self.STEP_VARIANCE + num1) > num2
            negative_bound = num2 > (num1 - num1*self.STEP_VARIANCE)
            return positive_bound and negative_bound 
        if(num1 < 0 and num2 < 0):
            positive_bound = ((num1*self.STEP_VARIANCE + num1) < num2) 
            negative_bound = (num2 < (num1 - num1*self.STEP_VARIANCE))
            return positive_bound and negative_bound 
        return False


    def find_steps(self):
        currents = self._currents.tolist()
        voltages = self._voltages.tolist()
        step_level = currents[0]
        starting_index = 0
        voltage_step = [] 
        current_step = []
        for i, current in enumerate(currents):
            voltage = voltages[i]
            if(self.is_close(step_level, current)):
                current_step.append(current)            
                voltage_step.append(voltage)
            else:
                match_found = False
                
                for i, previos_step_current in enumerate(self._step_currents):
                    if(self.is_close(current, previos_step_current[0])):
                        self._step_currents[i].append(current)
                        self._step_voltages[i].append(voltage)
                        match_found = True
                if(not match_found):
                    self._step_currents.append(list(current_step))
                    self._step_voltages.append(list(voltage_step)) 
                    voltage_step.clear()
                    current_step.clear()
                    step_level = current
                    voltage_step.append(voltage)
                    current_step.append(current)


    def averager(self, points):
        total = 0
        for point in points:
            total += point 
        return total/len(points)
             

    def __call__(self):
        self.find_steps()
        for i, voltage_step in enumerate(self._step_voltages):
            current_step = self._step_currents[i]
            self._averaged_voltages.append(self.averager(voltage_step))
            self._averaged_currents.append(self.averager(current_step))


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


    @property
    def step_voltages(self):
        return self._step_voltages


    @property
    def step_currents(self):
        return self._step_currents
