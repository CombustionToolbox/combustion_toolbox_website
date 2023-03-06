% -------------------------------------------------------------------------
% EXAMPLE: TP
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
% See wiki or list_species() for more predefined sets of species
%
% @author: Alberto Cuadra Lara
%          PhD Candidate - Group Fluid Mechanics
%          Universidad Carlos III de Madrid
%                  
% Last update July 22 2022
% -------------------------------------------------------------------------

Air_ions = {'eminus', 'Ar', 'Arplus', 'C', 'Cplus', 'Cminus', ...
            'CN', 'CNplus', 'CNminus', 'CNN', 'CO', 'COplus', ...
            'CO2', 'CO2plus', 'C2', 'C2plus', 'C2minus', 'CCN', ...
            'CNC', 'OCCN', 'C2N2', 'C2O', 'C3', 'C3O2', 'N', ...
            'Nplus', 'Nminus', 'NCO', 'NO', 'NOplus', 'NO2', ...
            'NO2minus', 'NO3', 'NO3minus', 'N2', 'N2plus', ...
            'N2minus', 'NCN', 'N2O', 'N2Oplus', 'N2O3', 'N2O4', ...
            'N2O5', 'N3', 'O', 'Oplus', 'Ominus', 'O2', 'O2plus', ...
            'O2minus', 'O3'};

% profile on
%% INITIALIZE
self = App('Air_ions');
self.TN.FLAG_TCHEM_FROZEN = false;
%% INITIAL CONDITIONS
self = set_prop(self, 'TR', 300, 'pR', 1 * 1.01325);
self.PD.S_Oxidizer = {'N2', 'O2', 'Ar', 'CO2'};
self.PD.ratio_oxidizers_O2 = [78.084, 20.9476, 0.9365, 0.0319] ./ 20.9476;
%% ADDITIONAL INPUTS (DEPENDS OF THE PROBLEM SELECTED)
self = set_prop(self, 'pP', self.PD.pR.value, 'TP', 300); 
%% SOLVE PROBLEM
self = solve_problem(self, 'TP');
%% DISPLAY RESULTS (PLOTS)
% post_results(self);
% profile viewer
% profile off



%%
Air_ions = {'eminus', 'Ar', 'Arplus', 'C', 'Cplus', 'Cminus', ...
            'CN', 'CNplus', 'CNminus', 'CNN', 'CO', 'COplus', ...
            'CO2', 'CO2plus', 'C2', 'C2plus', 'C2minus', 'CCN', ...
            'CNC', 'OCCN', 'C2N2', 'C2O', 'C3', 'C3O2', 'N', ...
            'Nplus', 'Nminus', 'NCO', 'NO', 'NOplus', 'NO2', ...
            'NO2minus', 'NO3', 'NO3minus', 'N2', 'N2plus', ...
            'N2minus', 'NCN', 'N2O', 'N2Oplus', 'N2O3', 'N2O4', ...
            'N2O5', 'N3', 'O', 'Oplus', 'Ominus', 'O2', 'O2plus', ...
            'O2minus', 'O3'};
%% INITIALIZE
self = App('Air_ions');
self.TN.FLAG_TCHEM_FROZEN = false;
%% INITIAL CONDITIONS
self = set_prop(self, 'TR', 300, 'pR', 1 * 1.01325);
self.PD.S_Oxidizer = {'N2', 'O2', 'Ar', 'CO2'};
self.PD.ratio_oxidizers_O2 = [78.084, 20.9476, 0.9365, 0.0319] ./ 20.9476;
%% ADDITIONAL INPUTS (DEPENDS OF THE PROBLEM SELECTED)
self = set_prop(self, 'pP', self.PD.pR.value, 'TP', 300:1:305); 
%% SOLVE PROBLEM
self = solve_problem(self, 'TP');