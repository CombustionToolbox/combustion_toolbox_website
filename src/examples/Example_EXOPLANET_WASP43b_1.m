% -------------------------------------------------------------------------
% EXAMPLE: EXOPLANET WASP-43b - METALLICITY 1
%
% Compute equilibrium composition at defined temperature (e.g., 3000 K) and
% pressure (e.g., 1.01325 bar) for lean to rich CH4-air mixtures at
% standard conditions, a set of 26 species considered and a set of
% equivalence ratios phi contained in (0.5, 5) [-]
%   
% Soot formation == {'CO2','CO','H2O','H2','O2','N2','He','Ar','Cbgrb',...
%                    'C2','C2H4','CH','CH','CH3','CH4','CN','H',...
%                    'HCN','HCO','N','NH','NH2','NH3','NO','O','OH'}
%   
% See wiki or ListSpecies() for more predefined sets of species
%
% @author: Alberto Cuadra Lara
%          PhD Candidate - Group Fluid Mechanics
%          Universidad Carlos III de Madrid
%                  
% Last update July 22 2022
% -------------------------------------------------------------------------

LS = {'C2H2_acetylene', 'C2H4', 'C', 'CH4', 'CO2', 'CO', 'H2', 'H2O', 'H2S', 'H', 'HCN', 'He', 'HS_M', 'N2', 'N', 'NH3', 'O', 'S'};

%% INITIALIZE
self = App(LS);
%% INITIAL CONDITIONS
Fuel = {'H', 'He', 'C', 'N', 'O', 'S'};
Ni_abundances = abundances2moles(Fuel, 'abundances_WASP43b_1xsolar.txt')';
T = linspace(100, 4000, 300);
p = logspace(-5, 2, 300);

self.PD.S_Fuel = Fuel;
self.PD.N_Fuel = Ni_abundances;
self = set_prop(self, 'TR', 300, 'pR', 1);
self = set_prop(self, 'TP', T, 'pP', p);
%% SOLVE PROBLEM
self = SolveProblem(self, 'TP');
%% DISPLAY RESULTS (PLOTS)
postResults(self);