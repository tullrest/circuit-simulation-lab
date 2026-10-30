# Circuit Simulation Lab

A collection of hands-on circuit simulation experiments focused on CMOS circuits, semiconductor fundamentals, and Python-based automation.

## About This Repository

I am an Electrical Engineering student at San Francisco State University interested in digital hardware design and semiconductor engineering.

This repository documents my learning process, simulation experiments, and future automation projects.

## Tools & Technologies

- Synopsys HSPICE — Circuit simulation
- Synopsys WaveView — Waveform analysis
- Linux — Simulation environment
- Python — Simulation automation (planned)

## Projects

### 01. CMOS Inverter Simulation

**Objective:** Investigate how output load capacitance affects propagation delay and average power consumption.

**Experiment Results**

| Load Capacitance | Propagation Delay | Average Power |
|---|---|---|
| 5 fF | ~29 ps | 617.7 nW |
| 10 fF | ~48.1 ps | 1,277.4 nW |

**Key Findings:**
- Increasing load capacitance increased propagation delay.
- Average power consumption also increased.
- Propagation delay was measured using the 50% voltage crossing points.

*These results are from an introductory HSPICE simulation exercise.*

### 02. Python Simulation Automation

Planned: Automating HSPICE simulations and collecting measurement results using Python.

## Learning Goals

- Understand transistor-level circuit simulation
- Analyze timing and power characteristics
- Automate repetitive simulations using Python
- Develop practical semiconductor engineering skills

## Project Status

Ongoing — New experiments and scripts will be added as I continue learning.
