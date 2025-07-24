# Orbital Debris Detection and Collision Avoidance System

#  Orbital Collision Prediction System

A Python-based simulation to track satellite positions using real TLE data and predict potential collisions with space debris. The system visualizes the paths and suggests basic avoidance maneuvers when risks are detected.

## Features

- **Satellite Tracking**: Uses [Skyfield](https://rhodesmill.org/skyfield/) and real Two-Line Element (TLE) data to compute the orbital path of the International Space Station (ISS).
- **Debris Simulation**: Simulates future positions of orbital debris (placeholder for AI-based prediction).
- **Collision Detection**: Identifies potential collision risks based on proximity threshold.
- **Avoidance Maneuver**: Suggests simple maneuver positions to avoid predicted collisions.
- **Visualization**: Plots satellite and debris trajectories using Matplotlib.

## 🛠️ Tech Stack

- **Python**
- **Skyfield** for orbital mechanics
- **Matplotlib** for plotting
- Custom modules:
  - `debris_predictor.py` – Predicts future debris positions
  - `collision_avoidance.py` – Provides basic maneuver logic
