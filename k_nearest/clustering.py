"""
Excersise in k-nearest neighbours, it is quite slow, so there is room for improvement
"""
import random
import matplotlib.pyplot as plt
import math

# Point class
class Point:
    def __init__(self, x, y, centroid = False):
        self._x = x
        self._y = y
        self._centroid = centroid
    
    def get_x(self):
        return self._x
    
    def set_x(self, x):
        self._x = x
    
    def get_y(self):
        return self._y
    
    def set_y(self, y):
        self._y = y

    def is_origin(self):
        return self._x == 0 and self._y == 0

    def is_centroid(self):
        return self._centroid
    
    def distance_to(self, other_point):
        x_dist = math.sqrt((self.get_x() - other_point.get_x())**2)
        y_dist = math.sqrt((self.get_y() - other_point.get_y())**2) 
        return x_dist + y_dist
    
    def __repr__(self):
        return(f"POINT (X {self.get_x()}, Y: {self.get_y()})")

def random_points(width, height, n):
    rand_points = []
    for i in range(n):
        x_coord = random.randint(0,width)
        y_coord = random.randint(0,height)
        p = Point(x_coord, y_coord)
        rand_points.append(p)
    return rand_points

def show_clusters(clusters):    
        i = 0
        for cluster in clusters:
            # Get centroid of cluster (used for annotation)
            centroid = ""
            for p in cluster: 
                if p.is_centroid():
                    centroid = p
            # Get all x and y coords
            x_coords = [p.get_x() for p in cluster]
            y_coords = [p.get_y() for p in cluster]
            # Create plot
            plt.scatter(x_coords, y_coords, label = i)
            plt.text(centroid.get_x(), centroid.get_y(), f"Centroid: {i}")
            i += 1
        # Show plot
        plt.legend(title="Cluster number")
        plt.show()

    
def k_mean(data, k):
    # Assign all entries to the cluster with the closest centroid
    def create_clusters(centroids):
        clusters =  [[centroid] for centroid in centroids] 
        for p in data:
            distances = []
            for centroid in centroids:
                distances.append(centroid.distance_to(p))
            clusters[distances.index(min(distances))].append(p)
        return clusters

    def nearest_n(clusters, centroids):
        # Check which point in each cluster is closest to the center
        i = 0 # For getting the centroid
        for cluster in clusters:
            x_coords = [p.get_x() for p in cluster]
            y_coords = [p.get_y() for p in cluster]
            
            # Get center coordinates
            center_x = int(math.sqrt((max(x_coords) - min(x_coords))**2) / 2) + min(x_coords)
            center_y = int(math.sqrt((max(y_coords) - min(y_coords))**2) / 2) + min(y_coords)
            center_point = Point(center_x, center_y)
            # Test and change centroid
            for p in cluster:
                if p.distance_to(center_point) < centroids[i].distance_to(center_point):
                    centroids[i]._centroid = False
                    p._centroid = True
                    centroids[i] = p
                    clusters = create_clusters(centroids)
                    nearest_n(clusters, centroids)
            i += 1
            return clusters
    # Select k random entries of the data to be centroids
    centroids = random.sample(data, k)
    # Set points to be centroids and create list of clusters
    for centroid in centroids:
        centroid._centroid = True
    # Create clusters 
    clusters = create_clusters(centroids)
    nearest_n(clusters, centroids)
    show_clusters(clusters)


if __name__ == "__main__":
    data = random_points(100,100,600)
    k_mean(data,5)

