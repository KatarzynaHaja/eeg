import os.path as op
import numpy as np

import mne

data_path = op.join(mne.datasets.sample.data_path(), 'MEG', 'sample')

def basic_chart_time():
    raw = mne.io.read_raw_fif(op.join(data_path, 'sample_audvis_raw.fif'),
                              preload=True)
    raw.set_eeg_reference('average', projection=True)  # set EEG average reference
    raw.plot(block=True, lowpass=40)

def events_chart():
    raw = mne.io.read_raw_fif(op.join(data_path, 'sample_audvis_raw.fif'),
                                  preload=True)
    events = mne.read_events(op.join(data_path, 'sample_audvis_raw-eve.fif'))
    event_id = {'A/L': 1, 'A/R': 2, 'V/L': 3, 'V/R': 4, 'S': 5, 'B': 32}
    raw.plot(butterfly=True, block=True, events=events, event_id=event_id)

def draw_head():
    raw = mne.io.read_raw_fif(op.join(data_path, 'sample_audvis_raw.fif'), preload=True)
    raw.plot(butterfly=True, group_by='position',block=True)

def sensor_position():
    raw = mne.io.read_raw_fif(op.join(data_path, 'sample_audvis_raw.fif'), preload=True)
    raw.plot_sensors(kind='3d', ch_type='mag', ch_groups='position',block=True)

def topographic_map():
    raw = mne.io.read_raw_fif(op.join(data_path, 'sample_audvis_raw.fif'), preload=True)
    projs = mne.read_proj(op.join(data_path, 'sample_audvis_eog-proj.fif'))
    raw.add_proj(projs)
    raw.plot_projs_topomap()

def magnetomers():
    raw = mne.io.read_raw_fif(op.join(data_path, 'sample_audvis_raw.fif'), preload=True)
    layout = mne.channels.read_layout('Vectorview-mag')
    layout.plot()
    raw.plot_psd_topo(tmax=30., fmin=5., fmax=60., n_fft=1024, layout=layout)


# basic_chart_time()
# draw_head()
#sensor_position()
#topographic_map()
magnetomers()


