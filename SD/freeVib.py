import numpy as np


def free_vibration(self, time):
    omega_n = self.parameters.natural_frequency()
    zeta = self.parameters.damping_ratio()
    x0 = self.parameters.x0
    v0 = self.parameters.v0
    #print (f"zeta={zeta:.4f}, omega_n={omega_n:.4f}")
    if zeta == 0: # undamped
        #print(f"Undamped response: A={x0:.4f}, phi=0.0000")
        return x0 * np.cos(omega_n*time) + (v0/omega_n)*np.sin(omega_n*time) 
    if zeta < 1: # underdamped
        omega_d = omega_n * np.sqrt(1-zeta**2)
        A = np.sqrt(x0**2 + ((v0 + zeta*omega_n*x0)/omega_d)**2)
        phi = np.arctan((v0 + zeta*omega_n*x0)/(omega_d*x0))
        #print(f"Underdamped response: A={A:.4f}, phi={phi:.4f}")
        return A * np.exp(-zeta*omega_n*time)*(np.cos(omega_d*time - phi))
    elif zeta == 1: # critically damped
        A1 = x0
        A2 = v0 + omega_n*x0
        #print(f"Critically damped response: A1={A1:.4f}, A2={A2:.4f}")
        return (A1 + A2*time) * np.exp(-omega_n*time)
    else: # overdamped
        r1 = -omega_n*(zeta - np.sqrt(zeta**2 - 1))
        r2 = -omega_n*(zeta + np.sqrt(zeta**2 - 1))
        A1 = (v0 - r2*x0)/(r1 - r2)
        A2 = (r1*x0 - v0)/(r1 - r2)
        #print(f"Overdamped response: A1={A1:.4f}, A2={A2:.4f}, r1={r1:.4f}, r2={r2:.4f}")
        return A1*np.exp(r1*time) + A2*np.exp(r2*time)
