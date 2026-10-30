# CMOS Inverter Simulation

## 1. Overview

This project explores the behavior of a CMOS inverter using Synopsys HSPICE.

The goal is to understand how output load capacitance affects propagation delay and average power consumption.

## 2. Tools

- Synopsys HSPICE
- Synopsys WaveView
- Linux

## 3. Simulation Setup

A CMOS inverter was simulated using 7nm transistor models.

- Supply voltage (VDD): 0.7 V
- Input signal: Pulse waveform
- Load capacitance: 5 fF and 10 fF
- Transient simulation time: 10 ns

## 4. Experiment

Two simulations were performed with different load capacitances.

Propagation delay was measured in WaveView using the 50% voltage crossing points (0.35 V), from a falling input to a rising output.

Average power was measured over 0–10 ns.

## 5. Results

| Load Capacitance | Propagation Delay | Average Power |
|---|---|---|
| 5 fF | ~29 ps | 617.7 nW |
| 10 fF | ~48.1 ps | 1277.4 nW |

When the load capacitance was doubled:

- Propagation delay increased by approximately 65.9%.
- Average power increased by approximately 106.8%.

## 6. Conclusion

Increasing the output load capacitance increased both propagation delay and average power consumption in this simulation.

This experiment helped me understand the relationship between capacitive loading, circuit speed, and power consumption.

## 7. Future Work

- Test additional capacitance values
- Automate HSPICE simulations using Python
- Compare simulation results using graphs

## Acknowledgment

This is an introductory learning exercise based on HSPICE training provided at San Francisco State University.
