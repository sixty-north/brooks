"""This program constructs a one-off chart for use in the accompanying presentation.

Execute it from the parent directory to produce a chart at plots/communication.pdf"

"""

import seaborn  # Although apparently unused, this import has side-effects.

import matplotlib.pyplot as plt

from brooks.communication import *

def main():
    qo = []
    qr = range(31)
    for i in qr:
        try:
            overhead = quadratic_overhead_proportion(i)
        except ValueError:
            overhead = 0
        qo.append(overhead)

    go = []
    gr = range(61)
    for i in gr:
        go.append(gompertz_overhead_proportion(i))


    plt.figure(figsize=(8, 4.5), dpi=144)
    qp, = plt.plot(qr, qo, label='Abdel-Hamid (Quadratic)')
    gp, = plt.plot(gr, go, label='Smallshire (Gompertz)')
    plt.xlabel('Number of personnel')
    plt.ylabel('Communication overhead')
    plt.legend(handles=[qp, gp], loc=4)
    plt.gcf().savefig("plots/communication.pdf", dpi=144)


if __name__ == '__main__':
    main()

