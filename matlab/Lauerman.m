%Goal is to plot a single graph of probability of a two state system, then later multiple graphs.
%Probality equals the multiplicity of the macrostate over the muliplicty of the entire system, which is in line 21
%N is the total amount of chances of the system and n being the secondary amount.(ex. total amount of coins flipped is 100(N), with 20 head and 80(n) tails.)
% multiplicity of the entire system is calculated use 2^N, 2 being there because its a two state system and N being the total amount of coins flipped.
% multiplicty of a macrostate is calculated using Omega=N!/n!*(N-n)!
%-later comment
% N (10:10:100):
N = 100
n = (0:1:N)


for i = N;
    for j = n;
        probability = calculate_probability(N,n)
        plot(n, probability)

    end
end

function probability = calculate_probability(N,n)
    probability = (1/2.^N) .* factorial(N) ./ (factorial(n) .* factorial(N-n));

end
