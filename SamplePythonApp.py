from math import radians
import numpy as np     # installed with matplotlib
import matplotlib.pyplot as plt

def show_shape(patch):
	ax=plt.gca()
	ax.add_patch(patch)
	plt.axis('scaled')
	plt.show()

def main():
    x = np.arange(0, radians(1800), radians(12))
    plt.plot(x, np.sin(x), 'b')
    plt.show()
    c=plt.Circle((0,0), radius=5)
    show_shape(c)
    r = plt.Rectangle((0,0), 5, 3)
    show_shape(r)

main()