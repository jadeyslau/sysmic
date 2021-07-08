tmpenv <- new.env()
load("cell_fluorescence.RData", envir=tmpenv)
cell_fluo <- tmpenv$cell_population
# print(cell_fluo)

print(length(cell_fluo[cell_population])) # 10000

cell_samps = cell_fluo[cell_sample]
print(length(cell_samps)) # 6

cell_samp_mean <- mean(cell_samps)
print(cell_samp_mean) # 1183.859

cell_samp2<-sample(cell_fluo[cell_population],6)
cell_samp2_mean <- mean(cell_samp2)
print(cell_samp2_mean)

# Sample 50 with means

cell_samp50_1 <- sample(cell_fluo[cell_population],50)
cell_samp50_1_mean <- mean(cell_samp50_1)
print(cell_samp50_1_mean)

cell_samp50_2 <- sample(cell_fluo[cell_population],50)
cell_samp50_2_mean <- mean(cell_samp50_2)
print(cell_samp50_2_mean)

cell_samp50_3 <- sample(cell_fluo[cell_population],50)
cell_samp50_3_mean <- mean(cell_samp50_3)
print(cell_samp50_3_mean)

# Sample 500 with means

cell_samp500_1 <- sample(cell_fluo[cell_population],500)
cell_samp500_1_mean <- mean(cell_samp500_1)
print(cell_samp50_1_mean)

cell_samp500_2 <- sample(cell_fluo[cell_population],500)
cell_samp500_2_mean <- mean(cell_samp500_2)
print(cell_samp500_2_mean)

cell_samp500_3 <- sample(cell_fluo[cell_population],500)
cell_samp500_3_mean <- mean(cell_samp500_3)
print(cell_samp500_3_mean)

# The means from the larger sample are closer to one another compared to sample 50. This means that sample 500 is a closer approximation of the population mean.
