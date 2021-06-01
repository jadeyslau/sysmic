% sum_of_squares = 0;
% for i=1:7
%     sum_of_squares = sum_of_squares + i^2;
% end
% disp(sum_of_squares);

% result = zeros(1,17); result (1) = 1;
% result (2) = 1;
% for i=3:17
% result(i) = result(i-1) + result(i-2);
% end
% result

% MATLAB script file to sum square numbers%initialise_variables
n = 20;
sum_of_squares = 0;
% loop to sum the sequence of square numbers
for i = 1:n;
    sum_of_squares = sum_of_squares + i*i;
end
% display result
disp(['The sum of squares up to ', num2str(n),' is: ' num2str(sum_of_squares)])