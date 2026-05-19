import numpy as np
import BasicParameter 


#to calculate to impute funtion with Duhamel integral
def duhamel_integral(time,force,parameters = BasicParameter.parameters()):
    omega_n = parameters.natural_frequency()
    zeta = parameters.damping_ratio()
    dt = time[1] - time[0]  # time step
    response = np.zeros_like(time)
    
    for i in range(len(time)):
        t = time[i]
        integral_sum = 0.0
        
        for j in range(i):
            tau = time[j]
            f_tau = force[j]
            h_tau = np.exp(-zeta*omega_n*(t-tau)) * np.sin(omega_n*np.sqrt(1-zeta**2)*(t-tau))
            integral_sum += f_tau * h_tau * dt
        
        response[i] = integral_sum
    
    return response

def main():
    time = np.linspace(0, 5, 500)
    force = np.sin(2 * np.pi * 1 * time)  # Example force input (1 Hz sine wave)
    response = duhamel_integral(time, force)
    #print(f"Duhamel integral response: {response}")
    return response

if __name__ == "__main__":
    main()
    print(main())