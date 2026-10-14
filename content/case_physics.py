"""Simplified physics for a liquid-cooled cold plate under a battery module.

Stands in for a finite-element (FE) thermal simulation. All constants are
illustrative: plausible, but invented for demonstration, not engineering spec.
"""
import numpy as np

CP_COOLANT = 4186.0          # J/(kg K), water coolant
BATTERY_TEMP_LIMIT_C = 60.0  # max safe cell temperature, deg C

# Input ranges: heat load, coolant flow, inlet temperature, geometry, conductivity.
RANGES = {
    "Q_W":      (50.0, 500.0),   # heat load into the plate
    "mdot_kgs": (0.01, 0.10),    # coolant mass flow rate
    "Tin_C":    (15.0, 40.0),    # coolant inlet temperature
    "w_mm":     (1.0, 3.0),      # cooling-channel width
    "k_WmK":    (100.0, 400.0),  # plate thermal conductivity
}
INPUT_COLS = list(RANGES)
OUTPUT_COLS = ["Tout_C", "Tmax_C"]

# Thermal-resistance constants:
#   conduction resistance  R_cond = _C_COND / k
#   convection resistance  R_conv = _C_CONV * w^0.2 / mdot^0.8
_C_COND = 4.0
_C_CONV = 0.004


def truth(Q, mdot, Tin, w, k):
    """Noise-free reference simulation. Returns (Tout_C, Tmax_C).

    Energy balance (first law): Tout = Tin + Q / (mdot * cp)
    Tmax = mean coolant temperature + Q * (R_cond + R_conv)
    """
    Q, mdot, Tin, w, k = map(np.asarray, (Q, mdot, Tin, w, k))
    Tout = Tin + Q / (mdot * CP_COOLANT)
    Tavg = 0.5 * (Tin + Tout)
    R = _C_COND / k + _C_CONV * w**0.2 / mdot**0.8
    Tmax = Tavg + Q * R
    return Tout, Tmax


def energy_balance_Tout(Q, mdot, Tin):
    """The first-law outlet temperature: the PINN's energy-balance target."""
    return np.asarray(Tin) + np.asarray(Q) / (np.asarray(mdot) * CP_COOLANT)
