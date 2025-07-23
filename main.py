from skyfield.api import load, EarthSatellite
from debris_predictor import predict_future_position
from collision_avoidance import suggest_maneuver
import matplotlib.pyplot as plt

# Load TLE data
ts = load.timescale()
line1 = "1 25544U 98067A   21275.51041667  .00002182  00000-0  46434-4 0  9993"
line2 = "2 25544  51.6441 130.5360 0002697  56.3225  36.2573 15.48815336303669"
satellite = EarthSatellite(line1, line2, 'ISS', ts)

# Simulated debris position (random for now)
debris_pos = [(0.1 * i, 0.2 * i, 0.3 * i) for i in range(10)]

# Predict future positions (basic)
sat_pos = []
times = []
for i in range(10):
    t = ts.utc(2021, 10, 2, i)
    sat_pos.append(satellite.at(t).position.km)
    times.append(t.utc_datetime())

# Predict debris (AI-based in future)
predicted_debris = predict_future_position(debris_pos)

# Check for collision and suggest avoidance
for i in range(len(predicted_debris)):
    if abs(sat_pos[i][0] - predicted_debris[i][0]) < 20:  # distance threshold
        print(f"Collision risk at {times[i]}! Suggesting maneuver...")
        new_position = suggest_maneuver(sat_pos[i])
        print(f"New position: {new_position}")

# Plot satellite vs debris
sat_x = [pos[0] for pos in sat_pos]
deb_x = [pos[0] for pos in predicted_debris]

plt.plot(sat_x, label="Satellite Path")
plt.plot(deb_x, label="Predicted Debris Path")
plt.legend()
plt.title("Satellite vs Debris Position Over Time")
plt.xlabel("Time Index")
plt.ylabel("X Position (km)")
plt.grid(True)
plt.show()
