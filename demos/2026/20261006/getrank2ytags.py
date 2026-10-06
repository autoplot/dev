import autoplot as ap
import jpype
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime, timezone


# Start Autoplot / JVM.
ap.init()

QDataSet = jpype.JClass("org.das2.qds.QDataSet")


# Load the HAPI dataset through Autoplot.
uri = (
    "vap+hapi:https://jfaden.net/HapiServerDemo/hapi"
    "?id=SpectrumTimeVaryingChannels"
    "&parameters=Time,Spectra"
    "&timerange=2016-01-01"
)

apds = ap.APDataSet()
apds.setDataSetURI(uri)

# Ask Autoplot to return time coordinates as seconds since 1970.
apds.setPreferredUnits("t1970")

apds.doGetDataSet()


# Extract the QDataSet and its coordinate dependencies as numpy arrays.
z = ap.to_ndarray(apds)

time = ap.to_ndarray(
    apds,
    apds.property(QDataSet.DEPEND_0)
)

ytags = ap.to_ndarray(
    apds,
    apds.property(QDataSet.DEPEND_1)
)

print("z:    ", z.shape)
print("time: ", time.shape)
print("ytags:", ytags.shape)

x= time

# pcolormesh allows X and Y to both be two-dimensional.
#
# ytags is already (ntime, ny), because DEPEND_1 varies with time.
# Repeat the time coordinate along the second dimension to give X
# the same shape.
X = np.repeat(x[:, np.newaxis], z.shape[1], axis=1)


# Plot.
fig, ax = plt.subplots(figsize=(11, 6))

mesh = ax.pcolormesh(
    X,
    ytags,
    z,
    shading="auto"
)

ax.xaxis_date()
ax.xaxis.set_major_formatter(
    mdates.DateFormatter("%H:%M", tz=timezone.utc)
)

ax.set_xlabel("Time (UTC)")
ax.set_ylabel("Energy")

fig.colorbar(mesh, ax=ax, label="Spectra")

fig.autofmt_xdate()
plt.tight_layout()
plt.show()
