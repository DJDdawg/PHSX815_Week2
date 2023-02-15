#! /usr/bin/env python

# imports of external packages to use in our code
import sys
import math
import numpy as np
import matplotlib.pyplot as plt

# import our Random class from python/Random.py file
sys.path.append(".")
import MySort as mys

# main function for our CookieAnalysis Python code
if __name__ == "__main__":
   
    haveInput = False

    for i in range(1,len(sys.argv)):
        if sys.argv[i] == '-h' or sys.argv[i] == '--help':
            continue

        InputFile = sys.argv[i]
        haveInput = True
    
    if '-h' in sys.argv or '--help' in sys.argv or not haveInput:
        print ("Usage: %s [options] [input file]" % sys.argv[0])
        print ("  options:")
        print ("   --help(-h)          print options")
        print
        sys.exit(1)
    
    #initialize 
    Nmeas = 1 #just place a bullshit value bc will redefine later.
    Nexp = 0 #will count 1 by 1
    times = []
    times_avg = []

    need_rate = True
    
    with open(InputFile) as ifile:
        for line in ifile: #Each line is a new experiment. 
            if need_rate:
                need_rate = False
                rate = float(line)
                continue
            
            lineVals = line.split() #Each experiment.
            Nmeas = len(lineVals) #Each experiment has N measurements.
            t_avg = 0 #initialize the avg for each experiment.
            for v in lineVals: #each measurement in one experiment.
                t_avg += float(v) #sum of all measurements
                times.append(float(v)) #array of times for all measurements. 

            t_avg /= Nmeas #average time for each experiment.
            times_avg.append(t_avg) #add average time for each experiment to an array.
            Nexp += 1 

    #Sorting time
    Sorter = mys.MySort()

    times = Sorter.DefaultSort(times) #sort all times in ascending order. 1D array of len = Nmeas * Nexp.
    times_avg = Sorter.DefaultSort(times_avg) #sort avg. times of each experiment in ascending order. 1D array of len = Nexp.

    # try some other sorting methods! see how long they take
    # times_avg = Sorter.BubbleSort(times_avg)
    # times_avg = Sorter.InsertionSort(times_avg)
    # times_avg = Sorter.QuickSort(times_avg)

    # ADD YOUR CODE TO PLOT times AND times_avg HERE

    #testing to see if shit works....
    #print(times)
    #print(len(times))
    #print(Nexp)
    #print(times_avg)
    #print(len(times_avg)) #should match Nexp
    
    #find the mean of times_avg array and get a singular value so code works w/ Nexp > 1.
    
    for t in range(Nexp): 
    	#print(times_avg[t]) #each t is the average of an experiment w/ N measurements
    	t_avg += float(times_avg[t]) #sum of the averages
    	#print(t_avg) #make sure this is doing what I actually intend it to
    	
    t_avg = t_avg/Nexp #the average/mean of all experiments
    
    #print(t_avg) #make sure correct


    #Neema's Code. See if works. ###only works for Nexp = 1, but Nmeas = any.
    times1 = np.array(times) #need np array of sorted times
       

    # calculate quantiles of data
    q68 = np.quantile(times1, 0.68) # 68th percentile
    q95 = np.quantile(times1, 0.95) # 95th percentile
    q997 = np.quantile(times1, 0.997) #99.7th percentile
    q10 = np.quantile (times1, 0.1) # 10th percentile

    # create histogram of our data
    n, bins, patches = plt.hist(times, 16,edgecolor = 'black', linewidth = 3, density=True, facecolor='orange', alpha=0.75)
    plt.yticks(fontsize = 13)
    
    # plot line at mean
    plt.axvline(t_avg, color='blue', linestyle = 'dashed', linewidth = 3, label = 'Mean')
  
    # plot line at quantiles
    plt.axvline(q10, color='red', linestyle = 'dashed', linewidth = 3, label = 'Quartile: 0.10') #10 percentile line
     
    plt.axvline(q68, color='green', linestyle = 'dashed', linewidth = 3, label = 'Quartile: 0.68') #68 percentile line
     
    plt.axvline(q95, color='cyan', linestyle = 'dashed', linewidth = 3, label = 'Quartile: 0.95') #95 percentile line
    
    plt.axvline(q997, color='m', linestyle = 'dashed', linewidth = 3, label = 'Quartile: 0.997') #99.7 percentile line
    

    # plot formating options
    plt.xlabel('Time to Next Missing Cookie (days)', fontsize = 15)
    plt.ylabel('Probability', fontsize = 15)
    plt.title('Probability of Missing Cookie Time Intervals', fontsize = 20)
    plt.legend(fontsize = 15)

# show figure (program only ends once closed
    plt.show()
