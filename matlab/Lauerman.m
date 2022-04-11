%Goal is to plot a single graph of probability of a two state system, then later multiple graphs.
%Probality equals the multiplicity of the macrostate over the muliplicty of the entire system, which is in line 43
%N is the total amount of chances of the system and n being the secondary amount.(ex. total amount of coins flipped is 100(N), with 20 head and 80(n) tails.)
% multiplicity of the entire system is calculated use 2^N, 2 being there because its a two state system and N being the total amount of coins flipped.
% multiplicty of a macrostate is calculated using Omega=N!/n!*(N-n)!
%-later comment
% N (10:10:100):
%Previous code below
%N = (10:10:100)
%n = (0:1:N)
%plot(n,P)
%probability(n):
%function probability(n)
%hold on
%plot_probability(n)......
%hold off
%
%function plot_probability(n)
%   plot(n,P)
%end
%-----------------------------------
%N=10
%MA = 2.*N
%MM = factorial(N) ./ (factiorial(n).*factorial(N-n)
%P=MA/MM
%plot(n,P)
%-------------------------------------------------------------------------------------------------
N = 100
n = 0:1:N


for i = n
    probabilities =[]
    for j = 0:1:i
        probability = calculate_probability(i,j)
        probabilities = [probabilities, probability]
        
    end
     plot(0:1:j, probabilities)
end

function probability = calculate_probability(N,n)
    probability = (1/2.^N) .* factorial(N) ./ (factorial(n) .* factorial(N-n));
    
end
