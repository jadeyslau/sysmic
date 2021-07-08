simulate_cell_measurement <- function( cell_intensity, noise_sd, n_pixels ){
	pixel_readings<-rep(0,n_pixels)
	for (i in 1:n_pixels) {
		pixel_readings[i]<-cell_intensity+rnorm(1, mean=0, sd=noise_sd)
		}
	return (mean(pixel_readings))
}

repeat_measurements_inc_noise<-function(dataset,sample_size,n_pixels, n_repeats=500,noise_sd=60){

	measurements<-rep(0, n_repeats)
	measured_intensity<-rep(0, sample_size)

		for (i in 1:length(measurements)){
			for (k in 1: sample_size){
				cell_intensity<-sample(dataset,1)
				measured_intensity[k]<-simulate_cell_measurement(cell_intensity, noise_sd,n_pixels)
			}
			if (i%%100 == 0 ) {
				# print(paste('completed ',i,' of ', n_repeats,' repeats'))
				}
		measurements[i]<-mean(measured_intensity)
	}
	draw_histogram(measurements)
	print(paste('sampled cells: ', sample_size ,', pixels per cell: ', n_pixels,', mean: ', mean(measurements),', sd: ',sd(measurements)))
# 	uncomment the following line if you want to return the measurement vector
#	return(measurements)
}

tmpenv <- new.env()
load("cell_fluorescence.RData", envir=tmpenv)
cell_population <- tmpenv$cell_population

repeat_measurements_inc_noise(cell_population,16,1024,500,7.5)
repeat_measurements_inc_noise(cell_population,32,512,500,15)
repeat_measurements_inc_noise(cell_population,64,256,500,30)
repeat_measurements_inc_noise(cell_population,128,128,500,60)
repeat_measurements_inc_noise(cell_population,256,64,500,120)
repeat_measurements_inc_noise(cell_population,512,32,500,240)
repeat_measurements_inc_noise(cell_population,1024,16,500,480)
repeat_measurements_inc_noise(cell_population,2048,8,500,960)
repeat_measurements_inc_noise(cell_population,4096,4,500,1920)
