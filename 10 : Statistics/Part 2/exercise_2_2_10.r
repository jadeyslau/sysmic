funNA <- function(x){
  n <- sum(is.na(x))
  return( n )
}
numNA <- apply(geData_hrs4, MARGIN=1, funNA )
