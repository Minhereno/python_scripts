# -*- coding: utf-8 -*-

import os
import imagehash
import numpy as np

# folder containing the images
folder = 'path/to/folder'

# hamming distance threshold
threshold = 5

def group_duplicates(folder, threshold):
    # list all files in folder
    files = [os.path.join(folder, f) for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]

    # number of files
    n = len(files)

    # list to store pHash values
    pHashes = [imagehash.phash(file) for file in files]

    # matrix to store hamming distances
    distances = np.zeros((n, n))

    # fill distance matrix
    for i in range(n):
        for j in range(i, n):
            distances[i, j] = imagehash.hash.hamming(pHashes[i], pHashes[j])
            distances[j, i] = distances[i, j]

    # list to store clusters
    clusters = []

    # list to store indices of unassigned files
    unassigned = list(range(n))

    # iterate over unassigned files
    for i in unassigned:
        # flag to indicate if file has been added to a cluster
        added = False

        # iterate over existing clusters
        for j, cluster in enumerate(clusters):
            # if any file in cluster is within threshold distance, add file to cluster
            if np.min(distances[i, cluster]) <= threshold:
                clusters[j].append(i)
                unassigned.remove(i)
                added = True
                break

        # if file was not added to any cluster, create new cluster
        if not added:
            clusters.append([i])

    # create set for images with duplicates
    duplicates = set()
    for cluster in clusters:
        # only add files to duplicates set if there are duplicates
        if len(cluster) > 1:
            # sort cluster by filename
            filenames = [files[i] for i in cluster]
            filenames.sort()
            # add all but the first file in the cluster to duplicates set
            for filename in filenames[1:]:
                duplicates.add(filename)

    # remove all but one image in each duplicate cluster
    for cluster in clusters:
        if len(cluster) > 1:
            # sort cluster by filename
            filenames = [files[i] for i in cluster]
            filenames.sort()
            # keep only the first file in the cluster
            for filename in filenames[1:]:
                os.remove(filename)

if __name__ == '__main__':
    group_duplicates(folder, threshold)