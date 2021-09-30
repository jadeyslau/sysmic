timespan=[0 15];
figure()
subplot(2,1,1);
y0 = [0.1 1.0];
[t,y] = ode45(@toggle2,timespan,y0); 
plot(t,y)
ylabel('u,v')
xlabel('time')
legend('u','v','Location','SouthEast')
subplot(2,1,2);
y0 = [5.0 4.0];
[t,y] = ode45(@toggle2,timespan,y0);
plot(t,y)
ylabel('u,v')
xlabel('time')
legend('u','v','Location','SouthEast')