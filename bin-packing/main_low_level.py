from bin import Bin
from item import Item
from heuristics import BestFit, FirstFit, NextFit, WorstFit
from random import shuffle
from datetime import datetime
import json


def log(message, end=None):
    print(message, flush=True, end=end)


if __name__ == '__main__':
    datasets = [
        {"name": "N1C1W1_A.BPP", "results": {}},
        {"name": "N2C2W1_B.BPP", "results": {}},
        {"name": "N3C3W1_C.BPP", "results": {}},
        {"name": "N4C1W1_D.BPP", "results": {}},
        {"name": "N4C3W1_E.BPP", "results": {}}
    ]
    heuristic_list = [FirstFit, NextFit, WorstFit, BestFit]

    # Loop through each data set.
    for dataset in datasets:
        # Read the data into memory
        with open('datasets/{}'.format(dataset["name"]), 'r') as file:
            data = file.read().splitlines()
            num_items, capacity, items = int(data[0]), int(data[1]), data[2:]
            log("\n\nDATASET {}: num_items {} capacity {} items_read {}".format(dataset["name"], num_items, capacity, len(items)))
        items = [Item(size=int(i)) for i in items]
        log("  Iteration", end=" ")
        # Perform 30 independent iterations.
        for iteration in range(30):
            log(iteration+1, end=" ")
            # Randomize the order of the items in the item list.
            shuffle(items)
            # Apply each heuristic to the list.
            for h in heuristic_list:
                start_time = datetime.now()
                # There is always at least one bin.
                bins = [Bin(capacity=capacity)]
                for item in items:
                    bins = h.apply(item, bins)
                execution_time = datetime.now() - start_time
                # Record the relevant data for analysis
                summary = {
                    "execution_time": str(execution_time),
                    "num_bins": len(bins),
                    "fitness": sum(b.fitness() for b in bins) / len(bins),
                }
                dataset["results"].setdefault(h.__name__, []).append(summary)
    # Write the captured data to disk.
    with open("results_low_level.json", "w") as file:
        file.write(json.dumps(datasets, indent=2))
