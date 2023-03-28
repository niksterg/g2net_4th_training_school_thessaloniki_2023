from gwpy.timeseries import TimeSeries
from gwpy.signal import filter_design

t0 = 1126259462.4
hdata = TimeSeries.fetch_open_data('H1', t0-0.4,t0+0.4)

bp = filter_design.bandpass(50, 250, hdata.sample_rate)
notches = [filter_design.notch(line, hdata.sample_rate) for line in (60, 120, 180)]
zpk = filter_design.concatenate_zpks(bp, *notches)
hfilt = hdata.filter(zpk, filtfilt=True)
hfilt = hfilt.crop(t0-0.2,t0+0.2)
plot = hfilt.plot()
ax = plot.gca()
ax.set_title('LIGO-Hanford strain data around GW150914')
ax.set_ylabel('Amplitude [strain]')
plot.show()
