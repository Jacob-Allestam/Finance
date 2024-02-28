function price = black_scholes_formula(S, K, T, r, sigma, option_type)
    % Function to calculate the Black-Scholes option price
    % Inputs:
    %   S: Current stock price
    %   K: Strike price of the option
    %   T: Time to maturity (in years)
    %   r: Risk-free interest rate (annualized)
    %   sigma: Volatility of the stock
    %   option_type: 'call' or 'put'
    % Output:
    %   price: Price of the option according to Black-Scholes formula

    d1 = (log(S/K) + (r + 0.5 * sigma^2) * T) / (sigma * sqrt(T));
    d2 = d1 - sigma * sqrt(T);

    if strcmpi(option_type, 'call')
        price = S * normcdf(d1) - K * exp(-r * T) * normcdf(d2);
    elseif strcmpi(option_type, 'put')
        price = K * exp(-r * T) * normcdf(-d2) - S * normcdf(-d1);
    else
        error('Invalid option type. Use ''call'' or ''put''.');
    end
end