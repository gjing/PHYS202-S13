clear all; close all;
experiment = importdata('radioactivedecay.dat')
t = experiment.data(:,1);
N = experiment.data(:,2);
figure(42)

xlabel('t') 
ylabel('N') 
axis equal

fun = @(a,b,c,x) -sqrt(a^2-(x-b).^2)+c;

guess = fun(15,0,15,t); 

hold on
plot(t,guess,'r:')
hold off

fittedmodel = fit(t,N,fun,'StartPoint',[15 0 15]);

hold on
plot(fittedmodel,'r-');
hold off
