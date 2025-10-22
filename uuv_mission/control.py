import numpy as np
import matplotlib.pyplot as plt


class Controller:
    def __init__(self, gain: float = 1, gain_p: float = 0.15, gain_d: float = 0.6):
        self.gain = gain
        self.gain_p = gain_p
        self.gain_d = gain_d
        #print("Controller initialized with gain:", gain, "gain_p:", gain_p, "gain_d:", gain_d)  
        
    def get_action(self, error, prev_error) -> float:
        action = self.gain * (self.gain_p * error + self.gain_d * (error - prev_error))
        return action