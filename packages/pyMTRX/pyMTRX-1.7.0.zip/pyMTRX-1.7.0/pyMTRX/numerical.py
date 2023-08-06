# -*- encoding: UTF-8 -*-
'''Spectroscopy Package Numerical Methods Module
	Author: Alex Pronschinske
	Version: 1 (developmental)
	
	List of Classes: -none-
	List of Functions: 
		norm_deriv
		sgSm
	Module dependencies: 
		matplotlib.pyplot
		numpy
'''

import numpy as np

#===============================================================================
def norm_deriv(X, Y, x_window, poly_order):
	''' Calculate the normalized dI/dV (i.e. (V/I)*dI/dV)
		
		Args:
			---
		Returns:
			(SpecBundle)
		Example:
			---
	'''
	
	dx = X[1] - X[0]
	i_window = int(x_window/dx) + 1 - int(x_window/dx)%2
	sY = sgSm(Y, i_window, poly_order, 0)
	i0 = int(-X[0]/dx)
	dy = sY[i0+1]-sY[i0]
	y0 = sY[i0] - (dy/dx)*X[i0]
	sY = sY - y0
	
	dY = sgSm(Y, i_window, poly_order, 1) / dx
	ndY = X*dY/sY
	
	return ndY
# END norm_deriv

#===============================================================================
def sgSm(y, window_size, order, deriv=0):
	'''Savitzky-Golay Smoothing & Differentiating Function
	
	Args:
		Y (list): Objective data array.
		window_size (int): Number of points to use in the local regressions.
						Should be an odd integer.
		order (int): Order of the polynomial used in the local regressions.
					Must be less than window_size - 1.
		deriv = 0 (int): The order of the derivative to take.
	Returns:
		(ndarray)  The resulting smoothed curve data. (or it's n-th derivative)
	Test:
		t = np.linspace(-4, 4, 500)
		y = np.exp( -t**2 ) + np.random.normal(0, 0.05, t.shape)
		ysg = sg_smooth(y, window_size=31, order=4)
		import matplotlib.pyplot as plt
		plt.plot(t, y, label='Noisy signal')
		plt.plot(t, np.exp(-t**2), 'k', lw=1.5, label='Original signal')
		plt.plot(t, ysg, 'r', label='Filtered signal')
		plt.legend()
		plt.show()
	'''
	
	try:
		window_size = np.abs(np.int(window_size))
		order = np.abs(np.int(order))
	except ValueError:
		raise ValueError("window_size and order have to be of type int")
	# END try
	if window_size % 2 != 1 or window_size < 1:
		raise TypeError("window_size size must be a positive odd number")
	if window_size < order + 2:
		raise TypeError("window_size is too small for the polynomials order")
	
	order_range = range(order+1)
	half_window = (window_size -1) / 2
	
	# precompute coefficients
	b = np.mat(
		[
			[k**i for i in order_range] for k in range(
				-half_window, half_window+1
			)
		]
	)
	m = np.linalg.pinv(b).A[deriv]
	# END if
	
	# pad the function at the ends with reflections
	left_pad = y[0] - np.abs( y[1:half_window+1][::-1] - y[0] )
	right_pad = y[-1] + np.abs(y[-half_window-1:-1][::-1] - y[-1])
	y = np.concatenate((left_pad, y, right_pad))
	
	return np.power(-1, deriv) * np.convolve( m, y, mode='valid')
# END sgSm