x = 1:20;
fib = fibonacci(21);
ratios = zeros(1,20);
gr = 1.61803398875;
for i=1:20
    ratios(i) = fib(i+1)/fib(i);
end

figure();
plot(x, ratios);
hold on;
plot( [0,20],[ gr,gr],'r')
ylabel('fib ratio');
xlabel('i');
legend('fib', 'gr')