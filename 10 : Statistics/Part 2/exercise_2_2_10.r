funNA <- function(x){
  n <- sum(is.na(x))
  return( n )
}
numNA <- apply(geData_hrs4, MARGIN=1, funNA )
indices <- which(numNA <= 5)
geData_hrs4 <- geData_hrs4[indices, ]
genes <- genes[indices]

print(length(indices))

funFoldChange <- function(x){
  fc <- median( exp(as.numeric(x)), na.rm=T)
  return( fc )
}
foldchange <- apply(geData_hrs4, MARGIN=1, funFoldChange )

funtTest <- function(x){
  tp <- t.test(as.numeric(x))$p.value
  return( tp )
}
tresults <- apply(geData_hrs4, MARGIN=1, funtTest )
hist(tresults, nclass=500, main="t-test pvalues", xlab="p value")

symbols <- geData2$IDENTIFIER[indices]
results_hrs4 <- data.frame( pvalue=tresults, FC=foldchange, id=genes )

hits4 <- results_hrs4[ which( results_hrs4$pvalue < 2.56e-6 & results_hrs4$FC > 2 ), ]
print(hits4)
