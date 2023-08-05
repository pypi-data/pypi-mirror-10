import json
from random import shuffle

from sklearn.metrics import adjusted_rand_score
import matplotlib.pyplot as plt

from concept_formation.trestle import TrestleTree
from concept_formation.cluster import cluster
from concept_formation.datasets import load_rb_wb_03

def run_demo():
    ############### LOAD THE DATA ################

    towers = load_rb_wb_03()
    shuffle(towers)
    towers = towers[:30]

    ############## CLUSTER THE DATA ##############

    tree = TrestleTree()
    clusters = cluster(tree, towers, maxsplit=10)

    ############# PLOT THE RESULTS ###############

    human_labels = [tower['_human_cluster_label'] for tower in towers]

    x = [num_splits for num_splits in range(1,len(clusters)+1)]
    y = [adjusted_rand_score(human_labels, split) for split in clusters]
    plt.plot(x, y, label="TRESTLE")

    plt.title("TRESTLE Clustering Accuracy (Given Human Ground Truth)")
    plt.ylabel("Adjusted Rand Index (Agreement Correcting for Chance)")
    plt.xlabel("# of Splits of Trestle Tree")
    plt.legend(loc=4)
    plt.show()

if __name__ == "__main__":
    run_demo()
