p_vector <- vector(mode="numeric")

for(i in c(1:1000) ){
  sample <- rnorm(n=20,mean=0,sd=1)
  p_val  <- t.test( sample )$p.value
  p_vector[i] <- p_val
}

# print(p_vector)
ninety <- which(p_vector < 0.1)
ninety_five <- which(p_vector < 0.05)
ninety_nine <- which(p_vector < 0.01)

fract_ninety <- length(ninety)/1000
fract_ninety_five <- length(ninety_five)/1000
fract_ninety_nine <- length(ninety_nine)/1000

print(fract_ninety)
print(fract_ninety_five)
print(fract_ninety_nine)
