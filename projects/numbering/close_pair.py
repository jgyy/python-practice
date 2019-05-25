"""
Given an input array finds the closest pair.
Achieves matching using scipy's cKDTree, very quick even for
millions of points.  Speed ups may be achieved using pyflann:
https://github.com/mariusmuja/flann/tree/master/src/python/pyflann
User must input number of points to generate and the number of dimensions to use.
For 2D and 3D plots are generated.
"""
import sys
import numpy
import matplotlib.pyplot as plt
import scipy.spatial as spatial


def show_2d(r_pts, closest):
    """
    :param r_pts:
    :param closest: recolour closest points
    """
    if closest is None:
        plt.plot(r_pts[:, 1], r_pts[:, 0], 'b.')
        plt.show()
    else:
        plt.plot(r_pts[:, 1], r_pts[:, 0], 'b.')
        plt.plot([r_pts[closest[0], 1], r_pts[closest[1], 1]],
                 [r_pts[closest[0], 0], r_pts[closest[1], 0]],
                 'ro')
        plt.show()
    plt.close()


def show_3d(r_pts, closest):
    """
    :param r_pts: x,y,z
    :param closest: x,y,z
    """
    fig = plt.figure()
    a_x = fig.add_subplot(111, projection='3d')
    if closest is None:
        a_x.scatter(r_pts[:, 0], r_pts[:, 1], r_pts[:, 2], s=5, marker='.')
        plt.show()
    else:
        a_x.scatter(r_pts[:, 0], r_pts[:, 1], r_pts[:, 2], s=5, marker='.')
        a_x.scatter(r_pts[closest[0], 0], r_pts[closest[0], 1], r_pts[closest[0], 2], s=50, c='r')
        a_x.scatter(r_pts[closest[1], 0], r_pts[closest[1], 1], r_pts[closest[1], 2], s=50, c='r')
        plt.show()
    plt.close()


def get_closest_pair(r_pts):
    """
    make kd tree and self compare.
    compute the distances (take the 2 closest as the
    first distance is a self-comparison.
    :param r_pts: find minimum non self-reference distance
    :return: return the two indexes associated with the minimum distance
    """
    # noinspection Pylint
    tree = spatial.cKDTree(r_pts)

    distances, indexes = tree.query(r_pts, 2)

    min_dist_pos = numpy.argmin(distances[:, 1])
    print('L2-norm distance', distances[min_dist_pos, 1])
    print('pt1 coords', r_pts[min_dist_pos])
    print('pt2 coords', r_pts[indexes[min_dist_pos, 1]])

    return min_dist_pos, indexes[min_dist_pos, 1]


def main():
    """
    get grid size, make random x and y values,
    find the closest point pair and re plot
    """
    n_points = int(input('please enter number of random points: '))
    dims = int(input('please enter the number (e.g. 2,3,4,...) '
                     'of dimensions (2D or 3D will plot): '))

    random_points = numpy.random.rand(n_points, dims)

    closest_index = get_closest_pair(random_points)

    if dims == 2:
        show_2d(random_points, closest_index)
    if dims == 3:
        show_3d(random_points, closest_index)


if __name__ == '__main__':
    sys.exit(main())
