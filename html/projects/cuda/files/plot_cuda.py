import matplotlib.pyplot as plt
import matplotlib
import numpy as np

mat_dim = [10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000, 20000]

cuda_10 = np.array([ 0.200874667, 0.355701333, 0.825088, 1.690432, 3.307168,
8.166197333, 17.14825567, 32.63356933, 111.283745, 484.6938273, 2846.308431])
cuda_10 /= 1000

mkl_10 = np.array([ 33.91566667, 33.97633333, 37.76466667, 45.224, 47.59066667,
39.62233333, 45.55233333, 113.8413333, 446.626, 1228.294667, 5292.633])
mkl_10 /= 1000


cuda_50 = np.array([ 0.200096, 0.367925333, 0.857098667, 1.661514667, 3.430613333,
8.038730667, 21.216544, 91.01067833, 970.1171467, 7377.11556])
cuda_50 /= 1000

mkl_50 = np.array([ 40.231, 37.823, 39.38833333, 36.63533333, 43.89133333, 60.934,
255.7156667, 407.8676667, 1616.073, 9350.764333])
mkl_50 /= 1000

cuda_90 = np.array([ 0.201301333, 0.364021333, 0.847733333, 1.685066667, 3.446464,
9.327872, 37.00229367, 204.1055347, 2753.997721, 21860.26823])
cuda_90 /= 1000

mkl_90 = np.array([ 34, 37.97666667, 37.71, 35.79066667, 66.924, 242.3616667,
280.5513333, 500.4723333, 3453.995333, 22564.02533])
mkl_90 /= 1000


plt.plot(mat_dim, cuda_10, color="red", linestyle="-", label="CUDA, k/n = 0.1")
plt.plot(mat_dim, mkl_10, color="red", linestyle="--", label="MKL, k/n = 0.1")
plt.plot(mat_dim[:-1], cuda_50, color="blue", linestyle="-", label="CUDA, k/n = 0.5")
plt.plot(mat_dim[:-1], mkl_50, color="blue", linestyle="--", label="MKL, k/n = 0.5")
plt.plot(mat_dim[:-1], cuda_90, color="green", linestyle="-", label="CUDA, k/n = 0.9")
plt.plot(mat_dim[:-1], mkl_90, color="green", linestyle="--", label="MKL, k/n = 0.9")

plt.ylabel("execution time (s)")
plt.xlabel("n")

plt.xscale("linear")
plt.yscale("linear")
plt.xlim([1E3, 1E4])

plt.legend(loc=2)


font = {'family' : 'normal',
        'size'   : 14}

matplotlib.rc('font', **font)

#plt.ticklabel_format(style='sci', axis='x', scilimits=(0,0))
plt.savefig("cuda_results.png")
