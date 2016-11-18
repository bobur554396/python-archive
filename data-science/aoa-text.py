import numpy as np
import jinja2
import matplotlib.pyplot as plt


import csv
data_file = "Maine_Median_Household_Income.csv"
with open(data_file, 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    data = list(reader)

print reader.fieldnames

len(reader.fieldnames)

def dataset(path):
    with open(path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            yield row

print set([row["Place"] for row in dataset(data_file)])
print min(set([int (row["Date"]) for row in dataset(data_file)]))
print max(set([int (row["Date"]) for row in dataset(data_file)]))
print {row["Place"] for row in dataset(data_file)}


def main(path):
    data = [(row["Date"], int(row["Median Income"][1:]))
            for row in dataset(path)]
    width = 0.35
    ind = np.arange(len(data))
    fig = plt.figure()
    ax = plt.subplot(111)
    ax.bar(ind, list(d[1] for d in data))
    ax.set_xticks(np.arange(0, len(data), 4))
    ax.set_xticklabels(list(d[0] for d in data),
                       rotation=45)
    ax.set_ylabel("Income in USD")
    plt.title("U.S. Average Income 1913-2008")

    plt.show()


if __name__ == "__main__":
    main("Maine_Median_Household_Income.csv")