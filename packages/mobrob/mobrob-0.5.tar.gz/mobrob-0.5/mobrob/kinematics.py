#!/usr/bin/python3

import numpy as np


### in use start ###

def pose_update(x, u, dt = 0.1):
    """Pose update from input velocity (kinematic forward model).
    Returns a pose of shape (n, 3) containing [x, y, phi] position and orientation.

    Keyword arguments
    x -- current pose of shape (3,)
    u -- input velocity of shape (2,)
    DT -- optional: time delta for simulation step (default value: 0.1)"""
    A = np.identity(3)
    B = np.array([[dt * np.cos(x[2]), 0.0],
                  [dt * np.sin(x[2]), 0.0],
                  [0.0                , dt]])
    x = A.dot(x) + B.dot(u)
    return x


def forward_simulation(vomega, dt = 0.1):
    """Sample a trajectory starting from zero.
    Returns a trajectory of shape (n, 3) containing [x, y, phi] position and orientation.

    Keyword arguments
    vomega -- a numpy array of shape (n, 2)"""
    xyphi = np.zeros((0,3))
    update = np.zeros((3,))
    for u in vomega:
        update = pose_update(update, u, dt)
        xyphi = np.vstack((xyphi, update))
    return xyphi


from scipy.spatial import Delaunay
# https://stackoverflow.com/questions/16750618/whats-an-efficient-way-to-find-if-a-point-lies-in-the-convex-hull-of-a-point-cl/16898636#16898636
def in_hull(p, hull):
    """
    Test if points in `p` are in `hull`

    `p` should be a `NxK` coordinates of `N` points in `K` dimensions
    `hull` is either a scipy.spatial.Delaunay object or the `MxK` array of the 
    coordinates of `M` points in `K`dimensions for which Delaunay triangulation
    will be computed
    """
    from scipy.spatial import Delaunay
    if not isinstance(hull,Delaunay):
        hull = Delaunay(hull)

    return hull.find_simplex(p)>=0


def get_footprint(a,b,c,d):
    footprint = np.array([[-b, +c], [+a, +c], [+a, -d], [-b, -d]]).T
    return footprint

def get_footprint_for_pose(footprint, pose):
    x = pose[0]
    y = pose[1]
    phi = pose[2]
    
    # rotation
    Rot1 = np.array([[np.cos(phi), np.sin(phi)],
                     [-np.sin(phi), np.cos(phi)]])
    xy = (footprint.T.dot(Rot1)).T 

    # tranlation
    xy[0,:] += x
    xy[1,:] += y
    return xy


def create_all_trajectories(n_trajectories, trajectory_length, omegas, v_max):
    all_trajectories = np.zeros((trajectory_length,5,0))
    for i in range(n_trajectories):   

        omega = np.full((trajectory_length,), omegas[i])
        #v_max = v_from_omega(omegas[i]) # limit linear velocity 
        v = np.full((trajectory_length,), v_max)
        vomega_trajectory = np.vstack((v, omega)).T

        xyphi_trajectory = forward_simulation(vomega_trajectory, dt = 0.5) # x y phi
        full_trajectory = np.hstack((xyphi_trajectory, vomega_trajectory)) 

        all_trajectories = np.dstack((all_trajectories, full_trajectory))
    return all_trajectories


from scipy.spatial import distance

def get_dwa_vomega(all_trajectories, xy_scan, footprint):

    # get the indexes of max length trajectories
    collision_index = np.zeros(all_trajectories.shape[2]) # one index for every trajectory
    for i in range(all_trajectories.shape[2]):
        trajectory = all_trajectories[:, :, i]
        for j in range(trajectory.shape[0]):
            xyphi = trajectory[j, :]
            new_footprint = get_footprint_for_pose(footprint, xyphi)
            new_collision = np.any(in_hull(xy_scan.T, new_footprint.T))
            if new_collision:
                collision_index[i] = j
                break
    min_value_index = collision_index.min() # zero if no collision for trajectory
    all_min_indexes = np.argwhere(collision_index==min_value_index).flatten()

    if min_value_index > 0: # if none of the trajectories has full length, use default behavior
        v = 0.1
        omega = 0.4 # default: turn left
        return (v, omega)

    # get the trajectory of maximum distance to laserscan
    min_distance = 0.0
    best_index = all_min_indexes[0]
    for index in all_min_indexes: # iterate over all full length trajectories
        trajectory=all_trajectories[:, :, index]
        xy_trajectory = trajectory[:, 0:2]
        new_min_distance = distance.cdist(xy_trajectory, xy_scan.T, 'euclidean').min()

        if new_min_distance > min_distance:
            min_distance = new_min_distance
            best_index = index

    omega = all_trajectories[0,4,best_index]
    v = all_trajectories[0,3,best_index] # take v from trajectory sim

    return (v, omega)


### in use end ###


def sample_trajectories(vomegas, dt=0.1):
    trajectories = []
    for vomega in vomegas:
        xyphi = forward_simulation(vomega, dt)
        trajectories.append(xyphi)
    return trajectories


# laserscan kinematics

def update_scan(ranges, angles, v, omega, delta_t): # delta_t in ms
    steps = int(delta_t / 100) # update in 100 ms steps -> one time-step is 0.1 seconds
    for i in range(steps):
        ranges = ranges - np.cos(angles) * v * 0.1
        angles = angles + np.sin(angles) * v * 0.1 / ranges - omega * 0.1
    return (ranges, angles)


def update_scan_trajectory(ranges, angles, v, omega, delta_t): # delta_t in ms
    steps = int(delta_t / 100) # update in 100 ms steps -> one time-step is 0.1 seconds
    for i in range(steps):
        ranges = ranges - np.cos(angles) * v[i] * 0.1
        angles = angles + np.sin(angles) * v[i] * 0.1 / ranges - omega[i] * 0.1
    return (ranges, angles)
