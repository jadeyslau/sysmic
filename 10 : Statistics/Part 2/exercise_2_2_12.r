makeqq <- function(d1){
  md1 <- mean(d1)
  sd1 <- sd(d1)
  standardized <- (d1-md1)/sd1
  qqnorm( standardized )
  abline(0,1,col='red')
}

library(GEOquery)
gds <- getGEO("GDS3420")

geData <- Table(gds)

control_rows=which(grepl("--", geData$IDENTIFIER)==TRUE)

gene_rows=which(grepl("--", geData$IDENTIFIER)!=TRUE)

geData2=geData[gene_rows, ]

hrs4 <- unlist( strsplit( Meta(gds)$sample_id[1], ',' ) )
hrs24 <- unlist( strsplit( Meta(gds)$sample_id[2], ',' ) )

geData_hrs24 <- data.matrix(geData2[,names(geData2) %in% hrs24])
genes <- geData2[,"IDENTIFIER"]

funNA <- function(x){
  n <- sum(is.na(x))
  return( n )
}
numNA <- apply(geData_hrs24, MARGIN=1, funNA )
indices <- which(numNA <= 5)
geData_hrs24 <- geData_hrs24[indices, ]
genes <- genes[indices]

print(length(indices))

funFoldChange <- function(x){
  fc <- median( exp(as.numeric(x)), na.rm=T)
  return( fc )
}
foldchange <- apply(geData_hrs24, MARGIN=1, funFoldChange )

funtTest <- function(x){
  tp <- t.test(as.numeric(x))$p.value
  return( tp )
}
tresults <- apply(geData_hrs24, MARGIN=1, funtTest )
hist(tresults, nclass=500, main="t-test pvalues", xlab="p value")

symbols <- geData2$IDENTIFIER[indices]
results_hrs24 <- data.frame( pvalue=tresults, FC=foldchange, id=genes )

hits24 <- results_hrs24[ which( results_hrs24$pvalue < 5.13e-7 & results_hrs24$FC > 2 ), ]
hits24 <- hits24[order(hits24$FC, decreasing=T),]
print(hits24)
print(nrow(hits24))

down24 <- results_hrs24[ which( results_hrs24$pvalue < 5.13e-7 & results_hrs24$FC < 0.5 ), ]
down24 <- down24[order(down24$FC, decreasing=T),]
print(down24)
print(nrow(down24))

print(length(indices))
