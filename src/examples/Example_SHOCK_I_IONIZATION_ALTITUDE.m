% -------------------------------------------------------------------------
% EXAMPLE: SHOCK_I_IONIZATION_ALTITUDE
%
% Compute pre-shock and post-shock state for a planar incident shock wave
% at standard conditions, a set of 51 species considered and a set of
% initial shock front velocities (u1) contained in (360, 13000) [m/s]
%    
% Air_ions == {'eminus', 'Ar', 'Arplus', 'C', 'Cplus', 'Cminus', ...
%              'CN', 'CNplus', 'CNminus', 'CNN', 'CO', 'COplus', ...
%              'CO2', 'CO2plus', 'C2', 'C2plus', 'C2minus', 'CCN', ...
%              'CNC', 'OCCN', 'C2N2', 'C2O', 'C3', 'C3O2', 'N', ...
%              'Nplus', 'Nminus', 'NCO', 'NO', 'NOplus', 'NO2', ...
%              'NO2minus', 'NO3', 'NO3minus', 'N2', 'N2plus', ...
%              'N2minus', 'NCN', 'N2O', 'N2Oplus', 'N2O3', 'N2O4', ...
%              'N2O5', 'N3', 'O', 'Oplus', 'Ominus', 'O2', 'O2plus', ...
%              'O2minus', 'O3'}
%   
% See wiki or list_species() for more predefined sets of species
%
% @author: Alberto Cuadra Lara
%          PhD Candidate - Group Fluid Mechanics
%          Universidad Carlos III de Madrid
%                 
% Last update Jan 10 2023
% -------------------------------------------------------------------------
clear;
%% INITIALIZE
self = App('Air_ions');
% self.Misc.FLAG_RESULTS = false;

z = [0, 2000, 5000, 10000, 20000, 30000];

Mach = logspace(0, 2, 1e3);
% Mach(Mach < 1.2) = [];
% Mach(Mach > 40) = [];

z = 30000;
Mach = 1.001;

for i = length(z):-1:1
    % Get temperature-pressure profile
    [~, ~, TR, pR] = atmos(z(i));
    % Change pressure units
    pR = convert_Pa_to_bar(pR);
    % INITIAL CONDITIONS
    self = set_prop(self, 'TR', TR, 'pR', pR);
    self.PD.S_Oxidizer = {'N2', 'O2', 'Ar', 'CO2'};
    self.PD.N_Oxidizer = [78.084, 20.9476, 0.9365, 0.0319] ./ 20.9476;
    % Compute sound velocity
    sound_pre = compute_sound(TR, pR, self.PD.S_Oxidizer, self.PD.N_Oxidizer, 'self', self);
    % ADDITIONAL INPUTS (DEPENDS OF THE PROBLEM SELECTED)
    self = set_prop(self, 'u1', sound_pre * Mach);
    % SOLVE PROBLEM
    self = solve_problem(self, 'SHOCK_I');
    % Get results
    R = cell2vector(self.PS.strP, 'rho') ./ cell2vector(self.PS.strR, 'rho');
    P = cell2vector(self.PS.strP, 'p') ./ cell2vector(self.PS.strR, 'p');
    T = cell2vector(self.PS.strP, 'T') ./ cell2vector(self.PS.strR, 'T');
    M1 = cell2vector(self.PS.strR, 'u') ./ cell2vector(self.PS.strR, 'sound');
    M2 = cell2vector(self.PS.strP, 'v_shock') ./ cell2vector(self.PS.strP, 'sound');
    Gammas = compute_Gammas(cell2vector(self.PS.strP, 'v_shock'), cell2vector(self.PS.strP, 'rho'), cell2vector(self.PS.strP, 'p'));
    % Remove last point to get same number of points
    R = R(1:end-1);
    P = P(1:end-1);
    T = T(1:end-1);
    M1 = M1(1:end-1);
    M2 = M2(1:end-1);
    % Get filename
    filename = sprintf('thermo_num_air_%dkm.mat', z(i)*1e-3);
    save(filename, 'R', 'P', 'T', 'M1', 'M2', 'Gammas');
    % Save results
    results.R(:, i) =  R;
    results.P(:, i) =  P;
    results.T(:, i) =  T;
    results.M1(:, i) =  M1;
    results.M2(:, i) =  M2;
    results.Gammas(:, i) =  Gammas;
end

config = self.Misc.config;
config.xscale = 'log';
config.yscale = 'log';

ax = set_figure(config);

for i = length(z):-1:1
    plot_figure('$R^{-1}$', 1./results.R(:, i), 'P', results.P(:, i), 'color', 'auto', 'ax', ax);
    leg{i} = sprintf('z = %d m', z(i));
end
legend(ax, flip(leg), 'Interpreter', 'latex');