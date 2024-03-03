import itertools
import collections

##############################################################################
# Three provided containers
corpus = [
    ["i", "did", "not", "like", "the", "service"],
    ["the", "service", "was", "ok"],
    ["i", "was", "ignored", "when", "i", "asked", "for", "service"]
]

tags = ["a", "b", "c"]

dct_keys = {
    "a" : 1,
    "b" : 2,
    "c" : 3
}

##############################################################################
def get_score(id_alpha, id_beta):
    """
    Returns score of two reviews (id_alpha, id_beta)
    """
    # Get set(review)
    corpus_0 = set(corpus[id_alpha-1])
    corpus_1 = set(corpus[id_beta-1])

    # Calculate Score
    score = 0.0
    union = len(corpus_0|corpus_1)
    intersection = len(corpus_0&corpus_1)
    score = intersection / union
    return score

def get_value(key):
    """
    Return 'value' (embedded_dict) of particular key (tuple)
    """
    # Create Skeleton embedded dictionary
    embedded_dict = {
        "id_alpha" : None,
        "id_beta" : None,
        "score" : 0.0
    }
    # Define id_alpha/id_beta
    for idx, item in enumerate(key):
        if idx == 0:
            id_alpha = dct_keys[item]
            embedded_dict["id_alpha"] = id_alpha
        if idx == 1:
            id_beta= dct_keys[item]
            embedded_dict["id_beta"] = id_beta
    # Define score
    embedded_dict["score"] = get_score(id_alpha, id_beta)
    return embedded_dict

def create_keys(tags):
    """
    Returns 3! 'key' (tuple) values from list tags
    """
    products = tuple(itertools.product(tags,tags))
    combinations = tuple(itertools.combinations(tags,2))
    keys = tuple([x for x in products if x not in combinations])
    return keys

##############################################################################

if __name__ == "__main__":
    keys = create_keys(tags)
    final_dict = {}
    for key in keys:
        value = get_value(key)
        print(str(key) + " : " + str(value))
