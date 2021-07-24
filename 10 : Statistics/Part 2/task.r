makeqq <- function(d1){
  md1 <- mean(d1)
  sd1 <- sd(d1)
  standardized <- (d1-md1)/sd1
  qqnorm( standardized )
  abline(0,1,col='red')
}

library(GEOquery)
gds <- getGEO("GDS3420")

# print(gds@header)
print(gds@header$sample_id)

geData <- Table(gds)
print(dim(geData))
print(names(geData))
print(geData[1:10,1:5])


control_rows=which(grepl("--", geData$IDENTIFIER)==TRUE)
length(control_rows)

gene_rows=which(grepl("--", geData$IDENTIFIER)!=TRUE)
length(gene_rows)

geData2=geData[gene_rows, ]

hrs4 <- unlist( strsplit( Meta(gds)$sample_id[1], ',' ) )
hrs24 <- unlist( strsplit( Meta(gds)$sample_id[2], ',' ) )

geData_hrs4 <- data.matrix(geData2[,names(geData2) %in% hrs4])
genes <- geData2[,"IDENTIFIER"]

# hist( geData_hrs4[1,], main=genes[1] )
# plot( density(geData_hrs4[1,]), main=genes[1] )


# makeqq( geData_hrs4[8,] )
# makeqq( geData_hrs4[9,] )
print(t.test( geData_hrs4[1,] ))
