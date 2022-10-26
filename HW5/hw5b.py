from math import sin, cos
from scipy.integrate import odeint
import numpy as np
from matplotlib import pyplot as plt

def solve_pendulum(z,t,g,l1,l2,m1,m2):

    def ode_functions(x,t):

        theta1ddot = ((-1 * g * ((2 * m1) + m2) * sin(x[0])) - (m2 * g * sin(x[0] - (2 * x[1])))) - (2 * sin(x[0] - x[1]) * m2 * ((x[3] ** 2) * l2 + (x[2] ** 2) * l1 * cos(x[0] - x[1]))) / (l1 * ((2 * m1) + m2 - (m2 * cos((2 * x[0]) - (2 * x[1])))))
        theta1dot = x[2]
        theta2ddot = (2 * sin(x[0] - x[1]) * ((x[3] ** 2) * l2 * m2 * cos(x[0] - x[1])) + ((x[2] ** 2) * l1 * (m1 + m2)) + (g * (m1 + m2) * cos(x[0]))) / (l2 * ((2 * m1) + m2 - (m2 * cos((2 * x[0]) - (2 * x[1])))))
        theta2dot = x[3]
        
        return(theta1dot,theta1ddot,theta2dot,theta2ddot)

    theta1, theta1dot, theta2, theta2dot = odeint(func=(ode_functions), y0=[z[0],z[1],z[2],z[3]], t=t, full_output=True)
    return theta1, theta2
def main():

    t = np.arange(0,10,0.1)

    theta1 = 0
    theta2 = 0.1
    theta1dot = 0
    theta2dot = 0
    initial_conditions = [theta1,theta2,theta1dot,theta2dot]
    solutions = solve_pendulum(initial_conditions,t,9.8,1,1,1,1)

    plt.plot(t,solutions[0],label="theta1")
    plt.plot(t,solutions[1],label="theta2")
    plt.xlabel("Time (s)")
    plt.ylabel("Theta (radians)")
    plt.legend()
    plt.show()

    # theta1 = 0.1
    # theta2 = 0
    # theta1dot = 0
    # theta2dot = 0
    # initial_conditions = [theta1,theta2,theta1dot,theta2dot]
    # solutions = solve_pendulum(initial_conditions,t,9.8,1,2,1,1)

    # plt.plot(t,solutions[0],label="theta1")
    # plt.plot(t,solutions[1],label="theta2")
    # plt.xlabel("Time (s)")
    # plt.ylabel("Theta (radians)")
    # plt.legend()
    # plt.show()

    # theta1 = 0.1
    # theta2 = 0.1
    # theta1dot = 0
    # theta2dot = 0
    # initial_conditions = [theta1,theta2,theta1dot,theta2dot]
    # solutions = solve_pendulum(initial_conditions,t,1.62,1,1,1,1)

    # plt.plot(t,solutions[0],label="theta1")
    # plt.plot(t,solutions[1],label="theta2")
    # plt.xlabel("Time (s)")
    # plt.ylabel("Theta (radians)")
    # plt.legend()
    # plt.show()

main()