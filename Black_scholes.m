P = 208.80; % Current stock price
X = 200; % Strike price of the option
t = 178/365; % Time to maturity (1 year)
r = 0.0558; % Risk-free interest rate
C = 34.45; % Current price of the option
option_type = 'call'; % Type of option

implied_volatility = inverse_BS(P, X, t, r, C, option_type);
disp(['Implied volatility: ', num2str(implied_volatility)]);