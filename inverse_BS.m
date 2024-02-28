function implied_volatility = inverse_BS(S, K, T, r, C, option_type)
    % Function to calculate implied volatility using the Black-Scholes formula
    % Inputs:
    %   S: Current stock price
    %   K: Strike price of the option
    %   T: Time to maturity (in years)
    %   r: Risk-free interest rate (annualized)
    %   C: Current price of the option
    %   option_type: 'call' or 'put'
    % Output:
    %   implied_volatility: Implied volatility of the option

    % Define constants
    tol = 1e-6; % Tolerance for the solver
    max_iter = 100; % Maximum number of iterations for the solver

    % Define the Black-Scholes formula
    black_scholes = @(sigma) black_scholes_formula(S, K, T, r, sigma, option_type) - C;

    % Use a solver to find the implied volatility
    implied_volatility = fzero(black_scholes, 0.3, optimset('TolX', tol, 'MaxIter', max_iter));
end