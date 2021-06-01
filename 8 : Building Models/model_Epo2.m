% MATLAB FUNCTION
% This can be placed as a local function at the end of the script file
% or saved as MATLAB function file model_Epo1.m
%
function dxdt=model_Epo2(t,x,p)
% Initialize model vector with zeroes,
dxdt=zeros(4,1);
% Load parameter values from vector p
k1 = p(1);  % Rate of EpoR phosphorylation
k2 = p(2);  % Rate of EpoR dephosphorylation
k3 = p(3);
k4 = p(4);
k5 = p(5);
Epo= p(6);
%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Differential Equation:
%
% unphosphorylated EpoR
dxdt(1)=-k1*x(1)*Epo+k2*x(2)*x(4);
% phosphorylated EpoR
dxdt(2)=k1*x(1)*Epo-k2*x(2)*x(4);
% Unknown 1
dxdt(3)=k3*x(2)-k4*x(3);
% Unknown 2
dxdt(4)=k4*x(3)-k5*x(4);