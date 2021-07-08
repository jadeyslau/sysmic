tmpenv <- new.env()
load("cell_fluorescence.RData", envir=tmpenv)
cell_population <- tmpenv$cell_population_b

# hist(cell_population)


# To investigate the prediction of the Central Limit Theorem write a function repeat_measurements which repeats many measurements on an input population dataset, then plots the distribution of sample means. Its input arguments should be:
# dataset the input dataset
# sample_size the number of sampled cells that make one measurement
# n_repeats the number of sample means to calculate
# Its output should be a histogram of the resulting distribution of sample means. (Hint. Make use of the draw_histogram function to plot the distribution.)
# e.g. repeat_measurements<-function(dataset, sample_size, n_repeats )

draw_histogram<-function(dataset, sample_size){
	dist_mean=mean(dataset)
	dist_sd=sd(dataset)

	# draw a histogram with x axis ranging from +/- 4 standard deviations from the mean
	# and title annotated with the mean and standard deviation of the distribution

	H <- hist(dataset, freq=TRUE,
	xlim=range(dataset,dist_mean+4*dist_sd,dist_mean-4*dist_sd),
	main=paste("Histogram","mean:",round(dist_mean,2),"sd:",signif(dist_sd,2),"n:",sample_size))

	# Overlay a normal distribution curve. This first requires us to find the histogram
	# bin width and number of measurements in total so that the curve can be normalised to
	# the correct height.

	bin_width <- min(diff(H$breaks))
	# H$breaks contains a vector of the breaks used to bin the histogram
	N<-length(dataset)
	curve(N*bin_width*dnorm(x,mean=dist_mean,sd=dist_sd), add=TRUE, col="blue")
}

repeat_measurements<-function(dataset, sample_size, n_repeats){
  measurements<-rep(0,n_repeats)
  for (i in 1:n_repeats){
  		measurements[i]<-mean(sample(dataset,sample_size))
  	}
  head(measurements)
  print(length(measurements))
  draw_histogram(measurements, sample_size)
}

sample_size<-1250
n_repeats<-10000
# repeat_measurements(cell_population, sample_size, n_repeats)

draw_histogram(cell_population, 1)
