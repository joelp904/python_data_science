def get_distance(list1, list2):
    assert len(list1) == len(list2), "List lengths unequal"
    point_pairs = zip(list1, list2)
    distances = [(pair[0] - pair[1]) for pair in point_pairs]
    return distances

if __name__ == "__main__":
    a = [1, 2, 3, 4, 5]
    b = [1, 2, 4, 5, 8]

    distances = get_distance(a, b)
    print("Euclidean distances: " + str(distances))
