draw_histogram<-function(dataset){
	dist_mean=mean(dataset)
	dist_sd=sd(dataset)

	# draw a histogram with x axis ranging from +/- 4 standard deviations from the mean
	# and title annotated with the mean and standard deviation of the distribution

	H <- hist(dataset, freq=TRUE,
	xlim=range(dataset,dist_mean+4*dist_sd,dist_mean-4*dist_sd),
	main=paste("Histogram","mean:",round(dist_mean,2),"sd:",signif(dist_sd,2)))

	# Overlay a normal distribution curve. This first requires us to find the histogram
	# bin width and number of measurements in total so that the curve can be normalised to
	# the correct height.

	bin_width <- min(diff(H$breaks))
	# H$breaks contains a vector of the breaks used to bin the histogram
	N<-length(dataset)
	curve(N*bin_width*dnorm(x,mean=dist_mean,sd=dist_sd), add=TRUE, col="blue")
}

simulate_cell_measurement <- function( cell_intensity, noise_sd, n_pixels ){
	pixel_readings<-rep(0,n_pixels)
	for (i in 1:n_pixels) {
		pixel_readings[i]<-cell_intensity+rnorm(1, mean=0, sd=noise_sd)
		}
	return (mean(pixel_readings))
}

measurements_40pixels<-rep(0,5000)
for (i in 1:5000){
	measurements_40pixels[i]<-simulate_cell_measurement(1200,400,40)
}
# or alternatively
# measurements_40pixels<-replicate(5000,simulate_cell_measurement(1200,400,40))

draw_histogram(measurements_40pixels)
print(mean(measurements_40pixels))
print(sd(measurements_40pixels))
