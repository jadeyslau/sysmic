%%%%%%%%%%%%%%%%%%%%%%%%%%%
% MATLAB SCRIPT
% This code will set up the parameters and intial conditions,
% use the model_Epo1 function to run the simulation
% and plot the results
%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Settings
options = odeset('InitialStep',0.1,'MaxStep',0.1);
t_range= [0 120];
x_ini= [0.5 0];
k1= 0.005;  %     Rate of EpoR phosphorylation
k2= 0.005;  %     Rate of EpoR dephosphorylation
Epo = 50;   %     Epo concentration

p = [k1 k2 Epo];
% Simulation
[t,x]=ode45(@model_Epo1,t_range,x_ini,options,p);
% Plot time series of all variables
figure(1);
plot(t,x(:,:));
xlabel('Time ');
ylabel('Epo receptor ');
legend('EpoR', 'p-EpoR');
%%%%%%%%%%%%%%%%%%%%%%%%%%%