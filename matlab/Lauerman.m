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
