%%%%%%%%%%%%%%%%%%%%%%%%%%%
% MATLAB SCRIPT
% This code will set up the parameters and intial conditions,
% use the model_Epo1 function to run the simulation
% and plot the results
%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Settings
options = odeset('InitialStep',0.1,'MaxStep',0.1);
t_range= [0 70];
x_ini= [0.5 0 0 0];
k1= 0.005;  %     Rate of EpoR phosphorylation
k2 = 0.01;
k3 = 10;
k4 = 0.1;
k5 = 0.01;
Epo= 50;
p = [k1 k2 k3 k4 k5 Epo];

% Simulation
[t,x]=ode45(@model_Epo2,t_range,x_ini,options,p);
% Plot time series of pEpoR
figure();
p1 = plot(t,x(:,2));
l1 = 'k1=0.005 k2=0.01 k3=10 k4=0.1 k5=0.01'
xlabel('time');
ylabel('phosphorylated Epo receptor');
ylim([-0.05,1]);
xlim([-1,70])
title('Four Component Model')
legend(p1, l1);