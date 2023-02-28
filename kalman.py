import numpy as np
from filterpy.kalman import KalmanFilter
from scipy.linalg import block_diag
from filterpy.common import Q_discrete_white_noise


def tracker_1st_order(R=4**2, P=10**2, Q=0.05**2, X0=np.array([[-60,0]])):
    tracker = KalmanFilter(dim_x=2, dim_z=1)
    dt = 0.2  # time step

    tracker.F = np.array([
        [1, dt],
        [0,  1],
    ])
    tracker.u = 0.
    tracker.H = np.array([[1, 0]])
    tracker.R = np.eye(1) * R
    if Q != 0:
        tracker.Q = Q_discrete_white_noise(dim=2, dt=dt, var=Q)
    else:
        tracker.Q = np.eye(2) * Q
    tracker.x = X0.T
    # tracker.P = np.eye(2) * P
    tracker.P = np.array([
        [P,  0],
        [0,  2**2],
    ])
    return tracker


def tracker_2nd_order(R=0.1, P=20**2, Q=0.0001, X0=np.array([[1, 0]])):
    tracker = KalmanFilter(dim_x=1, dim_z=1)
    # dt = 1  # time step

    # tracker.F = np.array([
    #     [1]
    # ])
    # tracker.u = 0.
    # tracker.H = np.array([[1]])
    # tracker.R = np.eye(1) * R
    # tracker.Q = np.eye(1) * Q
    # tracker.x = X0.T
    # tracker.P = np.eye(1) * P
    return tracker


def predict_rssi(single_channel, tracker=None):
    xs = np.array(range(single_channel.size))
    ys = single_channel

    ys_filtered, ps_rssi = [], []
    print('\tx0\tv0\tvar0\t\tz\t\tx\tv\tvar')
    for idx, rssi_raw in enumerate(single_channel):
        # predict
        tracker.predict()
        prior = np.array([tracker.x[0][0], tracker.x[1][0], tracker.P[0][0]])
        tracker.update(rssi_raw)
        poster = np.array([tracker.x[0][0], tracker.x[1][0], tracker.P[0][0]])
        # print_gh
        print(f'{prior[0]:10.1f}{prior[1]:10.1f}{prior[2]:10.3f}\t{rssi_raw:10.1f}\t{poster[0]:10.1f}{poster[1]:10.1}{poster[2]:10.6f}')

        # collect data to estimate model
        ys_filtered.append(tracker.x)
        ps_rssi.append(tracker.P.diagonal())  # just save variances

    ys_filtered = np.asarray(ys_filtered)
    ps_rssi = np.asarray(ps_rssi)
    return ys_filtered[:, 0].reshape(1, -1)[0], ps_rssi