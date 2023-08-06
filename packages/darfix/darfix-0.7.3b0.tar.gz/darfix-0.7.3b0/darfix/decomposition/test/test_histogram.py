import numpy as np
import time


def linear_hist(values, bins):
	min_val = bins[0]
	max_val = bins[-1]
	bin_size = bins[1] - min_val

	hist = (len(bins) - 1) * [0]

	for i, v in enumerate(values):
		idx = int((v - min_val) / bin_size)
		if idx == len(bins):
			idx -= 1

		hist[idx] += 1

	return hist


min_val = -10.9
bin_size = 0.2
num_bins = 100

bins = [min_val + i * bin_size for i in range(num_bins + 1)]

max_val = max(bins)
values = min_val + (max_val - min_val) * np.random.rand(4000000)

hist_np, _ = np.histogram(values, bins)
hist = linear_hist(values, bins)

np.testing.assert_array_almost_equal(hist, hist_np)

t0 = time.time()
for i in range(10):
	np.histogram(values, bins)
print(time.time() - t0)

t0 = time.time()
for i in range(10):
	linear_hist(values, bins)
print(time.time() - t0)