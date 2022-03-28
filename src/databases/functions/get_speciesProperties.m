function [txFormula, mm, Cp0, Cv0, Hf0, H0, Ef0, E0, S0, DfG0] = get_speciesProperties(DB, species, T, MassOrMolar, echo)

if nargin < 5, echo = 0; end

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%
% Calculates the thermodynamic properties of any species included in the 
% NASA database
%
% Uses functions:
%
% - none
%
% Sample application
%
% >> [txFormula, mm, Cp0, Cv0, Hf0, H0, Ef0, E0, S0] = SpeciesThermProp(strDB,'CO',1000,'molar')
% -------------------------------
% Possible phases of this species
% - CO
% -------------------------------
% 
% txFormula =
%     'C   1.00O   1.00    0.00    0.00    0.00'
% mm  = 28.0101
% Cp0 = 33.1788
% Cv0 = 24.8643
% Hf0 = -1.1054e+05
% H0  = -8.8848e+04
% Ef0 = -1.1177e+05
% E0  = -9.7162e+04
% S0  = 234.5409
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% Change lowercase 'l' to uppercase 'L'
species(strfind(species,'Al')+1)='L';
species(strfind(species,'Cl')+1)='L';
species(strfind(species,'Tl')+1)='L';
species(strfind(species,'Fl')+1)='L';

% Store species name with parenthesis (i.e., the name appearing in NASA's
% document tables)
Species_with_parenthesis = species;

% Substitute opening and closing parenthesis and other reserved characters 
% by 'b' in order to format the species name as in the thermo.inp
% electronic database 
name = species;
if name(end)=='+'
    name=[name(1:end-1) 'plus'];
elseif name(end)=='-'
    name=[name(1:end-1) 'minus'];
end
ind=regexp(name,'[()]');
name(ind)='b';
ind=regexp(name,'\W');
name(ind)='_';
if regexp(name(1),'[0-9]')
    name=['num_' name];
end

species = name;

% If the given species does not exist in strDB, abort the program
if ~isfield(DB, species)
    if echo==1
        disp( '-------------------------------')
        disp(['Species ''',species,''' does not exist as a field in strDB structure'])
        disp('Program aborted!')
        disp('-------------------------------')
    end
    txFormula = [];
    mm = [];
    Cp0  = [];
    Cv0  = [];
    Hf0  = [];
    H0   = [];
    Ef0  = [];
    E0   = [];
    S0   = [];
    DfG0 = [];
    return
end

% Detect the position of the phase specifier
n_open_parenthesis = detect_location_of_phase_specifier(Species_with_parenthesis);

% If it does exist, look for other possible states of aggregation of the 
% same species in DB
if echo==1    
    % Look for other possible states of aggregation of the same species in
    % strDB
    names = fieldnames(DB);
    any_other_phase = strfind(names,species(1:n_open_parenthesis-1));
    any_other_phase_index = find(~cellfun(@isempty,any_other_phase));

    if ~isempty(any_other_phase_index)
        disp('-------------------------------')
        disp('Possible phases of this species')
        for i = 1:length(any_other_phase_index)
            name_other_phase_with_parenthesis = name_with_parenthesis(names{any_other_phase_index(i)});
            n_open_parenthesis_other_phase = detect_location_of_phase_specifier(name_other_phase_with_parenthesis); 
            if strcmp(name_other_phase_with_parenthesis(1:n_open_parenthesis_other_phase-1),species(1:n_open_parenthesis-1))
                name_other_phase = name_other_phase_with_parenthesis;
                name_other_phase(name_other_phase(:)=='(') = 'b';
                name_other_phase(name_other_phase(:)==')') = 'b';
                if ~iscell(DB.(name_other_phase).tRange)
                    disp(['> ',name_other_phase_with_parenthesis,' [',num2str(DB.(name_other_phase).tRange(1)),' K]'])
                else
                    disp(['> ',name_other_phase_with_parenthesis,' [',num2str(DB.(name_other_phase).tRange{1}(1)),' - ',num2str(DB.(name_other_phase).tRange{DB.(name_other_phase).ctTInt}(2)),' K]'])
                end
            end
        end
        disp('-------------------------------')
    end
end

% If it does exist, read the corresponding field and store it in the
% following variables

ctTInt       = DB.(species).ctTInt;
txFormula    = DB.(species).txFormula;
swtCondensed = sign(DB.(species).swtCondensed);
mm           = DB.(species).mm;
Hf0          = DB.(species).Hf0;
tRange       = DB.(species).tRange;
tExponents   = DB.(species).tExponents;

% set Elements and Reference_form_of_elements_with_T_intervals lists
[Elements, ~] = set_elements(); % sets Elements list
Element_matrix = set_element_matrix(txFormula,Elements); % sets Element_matrix matrix
set_reference_form_of_elements_with_T_intervals; % sets Reference_form_of_elements_with_T_intervals list

% In order to compute the internal energy of formation from the enthalpy of
% formation of a given species, we must determine the change in moles of
% gases during the formation reaction of a mole of that species starting
% from the elements in their reference state. The only elements that are
% stable as diatomic gases are elements 1 (H), 8 (N), 9 (O), 10 (F), and 18
% (Cl). The remaining elements that are stable as (monoatomic) gases are
% the noble gases He (3), Ne (11), Ar (19), Kr (37), Xe (55), and Rn (87),
% which do not form any compound.
Delta_n_per_mole = sum(Element_matrix(1,:)==[1, 8, 9, 10, 18]')/2 ... 
                 + sum(Element_matrix(1,:)==[3, 11, 19, 37, 55, 87]');
Delta_n = 1 - swtCondensed - dot(Delta_n_per_mole,Element_matrix(2,:));

R0 = 8.3144598; % [J/(K-mol)]. Universal gas constant
% Check if there is at least one temperature interval and, in that case,
% check that the specified temperature is within limits. If it is not, then
% abort, otherwise keep on running
if ctTInt > 0
    a = DB.(species).a;
    b = DB.(species).b;

    Tref = 298.15;

    if (T < tRange{1}(1)) || (T > tRange{ctTInt}(2)) && (echo==1)
        disp(['T - out of range [',num2str(tRange{1}(1)),' - ',num2str(tRange{ctTInt}(2)),' K] for ',name_with_parenthesis(species)])
        Cp0  = [];
        Cv0  = [];
        H0   = [];
        Ef0  = [];
        E0   = [];
        S0   = [];
        DfG0 = [];
        return
    end

    % Get temperature interval
    tInterval = get_interval(species, T, DB);
    % Compute the thermochemical data at the specified temperature using
    % the polynomial coefficients in the selected temperature interval. All
    % magnitudes are computed in a per mole basis  
    Cp0 = R0 *      sum(a{tInterval} .* T.^tExponents{tInterval});
    Cv0 = Cp0 - R0;
    H0  = R0 * T * (sum(a{tInterval} .* T.^tExponents{tInterval} .* [-1   log(T) 1      1/2 1/3 1/4 1/5 0]) + b{tInterval}(1)/T);
    Ef0 = Hf0 - Delta_n * R0 * Tref;
    E0  = Ef0 + (H0 - Hf0) - (1 - swtCondensed) * R0 * (T - Tref);
    S0  = R0 *     (sum(a{tInterval} .* T.^tExponents{tInterval} .* [-1/2 -1     log(T) 1   1/2 1/3 1/4 0]) + b{tInterval}(2)  );
    
    % Compute the standar gibbs free energy of formation at the specified
    % temperature. This enforces us to consider explicitely the formation
    % reaction from the elements in their reference states at room
    % temperature, unless the species is precisely an element in its
    % reference state, in which case the standard gibbs free energy of
    % formation is identically zero.
    
    % disp(['Species = ',Species])
    % name_with_parenthesis(Species)
    
    [iRE, REname] = isRefElm(Reference_form_of_elements_with_T_intervals,species(1:n_open_parenthesis-1),T);
    if (~iRE)
        if echo==1
            disp([species,' is not Ref-Elm.'])
        end
        DfG0 = H0 - T.*S0;
    else
        if echo==1
            disp([REname,' is Ref-Elm.'])
        end
        DfG0 = 0;
    end

    if strcmpi(MassOrMolar,'mass')
        Cp0  = Cp0/(mm/1000);
        Cv0  = Cv0/(mm/1000);
        Hf0  = Hf0/(mm/1000);
        Ef0  = Ef0/(mm/1000);
        H0   =  H0/(mm/1000);
        S0   =  S0/(mm/1000);
        if swtCondensed == 0
            DfG0 = DfG0/(mm/1000);
        else
            DfG0 = [];
        end
    end

% If the species is only a reactant determine it's reference temperature
% Tref. For noncryogenic reactants, assigned enthalpies are given at 298.15
% K. For cryogenic liquids, assigned enthalpies are given at their boiling
% points instead of 298.15 K

else
    if T ~= tRange(1)
        disp(['T - out of range for ',name_with_parenthesis(species),' [',num2str(tRange(1)),' K]'])
        Cp0  = [];
        Cv0  = [];
        H0   = [];
        Ef0  = Hf0 - Delta_n * R0 * tRange(1);
        E0   = [];
        S0   = [];
        DfG0 = [];
        
        if strcmpi(MassOrMolar,'mass')
            Hf0 = Hf0/(mm/1000);
            Ef0 = Ef0/(mm/1000);
        end
        
        return
    end
    
    Tref = tRange(1);
        
    Cp0  = 0;
    Cv0  = 0;
    H0   = Hf0;
    Ef0  = Hf0 - Delta_n * R0 * Tref;
    E0   = Ef0;
    S0   = 0;
    DfG0 = Hf0;
    
    if strcmpi(MassOrMolar,'mass')
        Hf0 = Hf0/(mm/1000);
        Ef0 = Ef0/(mm/1000);
    end
end

end