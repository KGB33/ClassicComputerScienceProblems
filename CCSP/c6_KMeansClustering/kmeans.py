from copy import deepcopy
from functools import partial
from random import uniform
from statistics import mean, pstdev
from dataclasses import dataclass
from math import sqrt


def zscores(original):
    avg = mean(original)
    std = pstdev(original)
    if std == 0:
        return [0] * len(original)
    return [(x - avg) / std for x in original]


class DataPoint:
    def __init__(self, initial):
        self._originals = tuple(initial)
        self.dimensions = tuple(initial)

    @property
    def num_dimensions(self):
        return len(self.dimensions)

    def distance(self, other):
        return sqrt(
            sum([pow(a - b, 2) for a, b in zip(self.dimensions, other.dimensions)])
        )

    def __eq__(self, other):
        if not isinstance(other, DataPoint):
            return NotImplemented
        return self.dimensions == other.dimensions

    def __repr__(self):
        return self._originals.__repr__()


class KMeans:
    @dataclass
    class Cluster:
        points: list
        centroid: DataPoint

    def __init__(self, k, points):
        if k < 1:
            raise ValueError("k must be greater than zero")

        self._points = points
        self._zscore_normalize()
        self._clusters = [KMeans.Cluster([], self._random_point()) for _ in range(k)]

    @property
    def _centroids(self):
        return [x.centroid for x in self._clusters]

    def _dimension_slice(self, dimention):
        return [x.dimensions[dimention] for x in self._points]

    def _zscore_normalize(self):
        zscored = [[] for _ in range(len(self._points))]
        for dimention in range(self._points[0].num_dimensions):
            dimention_slice = self._dimension_slice(dimention)
            for index, zscore in enumerate(zscores(dimention_slice)):
                zscored[index].append(zscore)
        for i in range(len(self._points)):
            self._points[i].dimensions = tuple(zscored[i])

    def _random_point(self):
        rand_dims = []
        for dim in range(self._points[0].num_dimensions):
            values = self._dimension_slice(dim)
            rand_value = uniform(min(values), max(values))
            rand_dims.append(rand_value)

        return DataPoint(rand_dims)

    def _assign_clusters(self):
        for point in self._points:
            closest = min(self._centroids, key=partial(DataPoint.distance, point))
            idx = self._centroids.index(closest)
            cluster = self._clusters[idx]
            cluster.points.append(point)

    def _generate_centroids(self):
        for cluster in self._clusters:
            if len(cluster.points) == 0:
                continue
            means = []
            for dim in range(cluster.points[0].num_dimensions):
                dim_slice = [p.dimensions[dim] for p in cluster.points]
                means.append(mean(dim_slice))
                cluster.centroid = DataPoint(means)

    def run(self, max_iterations=100):
        for iteration in range(max_iterations):
            for cluster in self._clusters:
                cluster.points.clear()
            self._assign_clusters()
            old_centroids = deepcopy(self._centroids)
            self._generate_centroids()
            if old_centroids == self._centroids:
                print(f"Converged after {iteration} iterations")
                return self._clusters
        return self._clusters


if __name__ == "__main__":
    p1 = DataPoint([2, 1, 1])
    p2 = DataPoint([2, 2, 5])
    p3 = DataPoint([3, 1.5, 2.5])
    kmeans_test = KMeans(2, [p1, p2, p3])
    test_clusters = kmeans_test.run()
    for index, cluster in enumerate(test_clusters):
        print(f"Cluster {index}: {cluster.points}")

