% Generate matrix
mymatrix = randi([0,1],1000);
% In degree: column-wise summation        
degree_in = sum(mymatrix);
% Out degree: row-wise summation        
degree_out = sum(mymatrix,2);
% Display network in biograph
% view(biograph(mymatrix))


histogram(degree_in)
