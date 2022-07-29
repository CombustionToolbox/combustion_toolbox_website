function pressure = eos_vanderwaals(self, moles, temperature, volume)
    % Compute non ideal contribution of the chemical potential assuming 
    % Van der Waal's Equation of States [J/mol]
    %
    % Args:
    %     self (struct): Data of the mixture, conditions, and databases
    %     moles (float): number of moles of the mixture in gaseous phase [mol]
    %     temperature (float): temperature of the mixture [K]
    %     volume (float): volume of the mixture [m3]
    % 
    % Returns:
    %     pressure (float): pressure of the mixture [Pa]
    
    % Definitions
    Nmoles = length(moles);
    molesGas = sum(moles);
    % Compute mixture coefficients
    a = compute_cofficient(moles, molesGas, Nmoles, self.PD.EOS.a);
    b = compute_cofficient(moles, molesGas, Nmoles, self.PD.EOS.b);
    % Compute specific molar volume
    volume_molar = volume / molesGas;
    % Compute pressure
    pressure = self.C.R0 * temperature / (volume_molar - b) - a / volume_molar^2;
end

% SUB-PASS FUNCTIONS
function value = compute_cofficient(moles, molesGas, coefficients, Nmoles)
    % Comptue mixture coefficient
    value = 0;
    for i = 1:Nmoles
        value = value + sum(moles(i) .* moles .* sqrt(coefficients(i) .* coefficients));
    end
    value = value / molesGas^2;
end