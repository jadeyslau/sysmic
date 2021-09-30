% MATLAB FUNCTION
% This can be placed as a local function at the end of the script file
% or saved as MATLAB function file model_Epo1.m
%
function dxdt=model_Epo1(t,x,p)
% Initialize model vector with zeroes,
dxdt=zeros(2,1);
% Load parameter values from vector p
k1 = p(1);  % Rate of EpoR phosphorylation
k2 = p(2);  % Rate of EpoR dephosphorylation
Epo = p(3); % Epo concentration

%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Differential Equation:
%
% unphosphorylated EpoR
dxdt(1)= - k1*x(1)*Epo + k2*x(2);
% phosphorylated EpoR
dxdt(2)=   k1*x(1)*Epo - k2*x(2);
