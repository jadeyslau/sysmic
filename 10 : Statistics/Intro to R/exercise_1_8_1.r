cw <- ChickWeight
# Question 1
chick_1_data <- subset(cw, Chick == 1)
png("chick_1_weight_over_time.png")
plot( chick_1_data$Time, chick_1_data$weight, main="Weight of Chick 1 over time", xlab="Time (day)", ylab="Weight" )
dev.off()

# Question 2
# ii) Compare the weight of Chick 1 on day 21 and when it was born. How many times heavier is it?

comp_weight <- function(single_chick, t0, t1 ){
  w0 <- single_chick$weight[ which(cw$Time == t0) ]
  w1 <- single_chick$weight[ which(cw$Time == t1) ]
  gain <- ceiling(na.omit(w1)/na.omit(w0))
  return(gain)
}

chick_1_gain <- comp_weight(chick_1_data, 0, 21)
message( sprintf("Weight of Chick 1 at 21 days is %s times more than its weight on day 1", chick_1_gain))

# Question 3
# iii) Which of the chicks has the largest weight at 21 days?
# Hint: Look at the documentation for which.max
chicks_at_21 <- subset(cw, Time == 21)
heaviest_21  <- chicks_at_21[ which.max(chicks_at_21$weight), ]

message( sprintf("Heaviest chick is chick %s", heaviest_21$Chick))

# Question 4
# iv) Make histograms for the weights of the chicks on the four different diets after 21 days. Save them as PNG files.

# Question 5
# v) Calculate the mean and standard deviations of the chicks on the four different diets after 21 days. On which diet do the chicks appear to be heavier at 21 days

for(i in c(1,2,3,4) ){
  diet <- subset(cw, Diet == i & Time == 21)
  mean <- format(round(mean(diet$weight), 2), nsmall = 2)
  sd   <- format(round(sd(diet$weight), 2), nsmall = 2)
  subt <- paste("Mean: ", mean, " SD: ", sd, sep="")

  filename <- paste("diet_", i, "_weight_over_time.png", sep="")
  png(filename)
  hist(diet$weight, main=paste("Histogram of the weight of chicks on Diet ", i, " after 21 days",sep=""), xlab="Weight", sub = subt)
  dev.off()
}
