import QuantLib as ql
import matplotlib.pyplot as plt
import numpy as np

# Source: http://gouthamanbalaraman.com/blog/hull-white-simulation-quantlib-python.html

sims=[]
for i in [(1.819042624, 0.391),(2.256855553, 0.414),(1.874569041, 0.184),(2.789210094, 0.461),(2.7810183, 0.558),(2.768875954, 0.684),(2.642328524, 0.335),(2.627745729, 0.393),(2.722157491, 0.982),(2.60204227, 0.511),(2.592376553, 0.558),(2.585349708, 0.601),(2.576048335, 0.646),(2.566138286, 0.694),(2.65910457, 0.794)]:
	# Setting Parameters
	sigma = i[0] # COMPUTE IN EXCEL
	a = 1 # USE HO LEE MODEL
	timestep = 12 # GIVES MONTHLY INTEREST RATES
	length = 1 # in years
	forward_rate = i[1] # FIGURE OUT
	day_count = ql.Thirty360()
	todays_date = ql.Date(15, 1, 2015)
	ql.Settings.instance().evaluationDate = todays_date
	spot_curve = ql.FlatForward(todays_date, ql.QuoteHandle(ql.SimpleQuote(forward_rate)), day_count)
	spot_curve_handle = ql.YieldTermStructureHandle(spot_curve)
	hw_process = ql.HullWhiteProcess(spot_curve_handle, a, sigma)
	rng = ql.GaussianRandomSequenceGenerator(ql.UniformRandomSequenceGenerator(timestep, ql.UniformRandomGenerator()))
	seq = ql.GaussianPathGenerator(hw_process, length, timestep, rng, False)

	# A function to generate paths:
	def generate_paths(num_paths, timestep):
	    arr = np.zeros((num_paths, timestep+1))
	    for i in range(num_paths):
	        sample_path = seq.next()
	        path = sample_path.value()
	        time = [path.time(j) for j in range(len(path))]
	        value = [path[j] for j in range(len(path))]
	        arr[i, :] = np.array(value)
	    return np.array(time), arr

	# Simulate and plot paths
	num_paths = 1
	[time, paths] = generate_paths(num_paths, timestep)
	sims.append([time, paths])

# Concatenate rows into a matrix.  Rows are tenor, columns are times, values at (i,j)
listtoappend=[]
for j in sims:
	listtoappend.append(j[0])
 	for i in range(1):
 	    plt.plot(j[0], j[1][i, :], lw=0.8, alpha=0.6)
plt.title("Hull-White Short Rate Simulation")
plt.show()
rates=np.array(listtoappend)
b=np.zeros((15,1))
np.concatenate((b,rates),axis=1)
print rates.shape

# Define node Class.  Note, principal is $100,000
class Node:
	def __init__(self,rate,location):
		self.rate = rate
		self.location = location
		self.hbenefit = 100000*(1+self.rate*self.location[0])
	def move_cost(self,other):
		return 0 if self.value == '.' else 1

# Convert i,j in rates to a node at i,j with the value from i,j
# Also give principal=$1000000
biggestlisttoappend=[]
for i in range(0,rates.shape[0]):
	listtoappend=[]
	for j in range(0,rates.shape[1]):
		n=Node(rates[i,j],(i,j))
		listtoappend.append(n)
	biggestlisttoappend.append(listtoappend)
	listtoappend=[]
rates=np.array(biggestlisttoappend)
