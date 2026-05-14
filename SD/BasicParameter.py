import numpy as np
'''
Basic parameters for a single-degree-of-freedom system.
This code defines a class `basic_parameters` that encapsulates the fundamental parameters of a single-degree-of-freedom (SDOF) system, such as mass, stiffness, damping, initial displacement, initial velocity, and gravitational acceleration. The class also includes methods to calculate the natural frequency, damping ratio, period, and angular frequency of the system based on these parameters.
基本參數調用函數庫
可以輸入基本參數m,c,k v0 x0 gav 是 英制單位，輸出自然頻率、阻尼比、週期、角頻率等參數

'''

class basic_parameters:

    def __init__(self):
        self.m = 0.001295 # mass
        self.k = 10.0 # stiffness
        self.c = 0 # damping
        self.x0 = 1.0 # initial displacement
        self.v0 = 0.0 # initial velocity
        self.gav = 386.1 # gravity acceleration
    def natural_frequency(self):
        return np.sqrt(self.k/self.m)
    def damping_ratio(self):
        return self.c/(2*np.sqrt(self.m*self.k))
    def period(self):
        return 2*np.pi/self.natural_frequency()
    def angular_frequency(self):
        return self.natural_frequency() * np.sqrt(1 - self.damping_ratio()**2)  
    def Tr(self, r):
        zeta = self.damping_ratio()
        num = np.sqrt(1.0 + (2.0 * r * zeta)**2)
        den = np.sqrt((1.0 - r**2)**2 + (2.0 * r * zeta)**2)
        return num / den

def parameters():

    parameters = basic_parameters()
    print("'"*40)
    print(f"Mass m: {parameters.m:.6f} kg")
    print(f"Stiffness k: {parameters.k:.2f} N/m")
    print(f"Damping c: {parameters.c:.2f} Ns/m")
    print(f"Natural Frequency: {parameters.natural_frequency():.4f} rad/s")
    print(f"Damping Ratio: {parameters.damping_ratio():.4f}")
    print(f"Period: {parameters.period():.4f} s")
    print(f"Angular Frequency: {parameters.angular_frequency():.4f} rad/s")
    print("'"*40)
    return parameters

if __name__ == "__main__":
    parameters()
    
parameters()