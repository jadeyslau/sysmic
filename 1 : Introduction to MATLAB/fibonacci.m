function result = fibonacci(n)

    result = zeros(1,n);
    result (1) = 1;
    result (2) = 1;
    for i=3:n
        result(i) = result(i-1) + result(i-2);
    end
end
