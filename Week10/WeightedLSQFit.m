function [ m, sig_m, b, sig_b ] = WeightedLSQFit(x,y,w)
%WeightedLSQFit(x,y,w)
%   Take in arrays representing (x,y) values for a set of linearly varying data and an array of weights w.
%    Perform a weighted linear least squares regression. Return the resulting slope and intercept
%    parameters of the best fit line with their uncertainties.
%
%    If the weights are all equal to one, the uncertainties on the parameters are calculated using the 
%    non-weighted least squares equations.

    m = (sum(w)*sum(w.*x.*y) - sum(w.*x)*sum(w.*y))/((sum(w)*sum(w.*x.^2)) - (sum(w.*x))^2);
    b = (sum(w.*x.^2)*sum(w.*y) - sum(w.*x)*sum(w.*x.*y))/(sum(w)*sum(w.*x.^2) - (sum(w.*x)^2));
    
    a = true;
    
    for i=1:size(w)
        if w(i) ~= 1
            a = false; 
        end
    end
    
    if a
        
        n = size(x);
        delta = y-(m.*x + b);
        d2_ = mean(delta.^2);
    
        sig_m = sqrt((1/(n-2))*(d2_/(mean(x.^2) - (mean(x)^2))));
        sig_b = sqrt((1/(n-2))*((d2_*mean(x.^2))/(mean(x.^2) - (mean(x)^2))));
        
    else
        sig_m = sqrt(sum(w)/(sum(w)*sum(w.*x.^2) - (sum(w.*x)^2)));
        sig_b = sqrt(sum(w.*x.^2)/(sum(w)*sum(w.*x.^2) - (sum(w.*x)^2)));
    end
end