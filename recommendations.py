import operator
from math import sqrt

NAMES = ['Lisa Rose', 'Gene Seymour', 'Michael Phillips', 'Claudia Puig',
         'Mick LaSalle', 'Jack Matthews', 'Toby']
MOVIES = ['Lady in the Water', 'Snakes on a Plane', 'Just My Luck',
          'Superman Returns', 'The Night Listener', 'You, Me and Dupree']

def dict_maker():
    return {n: {} for n in NAMES}

def assign_scores():
    critics = dict_maker()
    critics['Lisa Rose']['Lady in the Water'] = 2.5
    critics['Lisa Rose']['Snakes on a Plane'] = 3.5
    critics['Lisa Rose']['Just My Luck'] = 3.0
    critics['Lisa Rose']['Superman Returns'] = 3.5
    critics['Lisa Rose']['The Night Listener'] = 2.5
    critics['Lisa Rose']['You, Me and Dupree'] = 3.0

    critics['Gene Seymour']['Lady in the Water'] = 3.0
    critics['Gene Seymour']['Snakes on a Plane'] = 3.5
    critics['Gene Seymour']['Just My Luck'] = 1.5
    critics['Gene Seymour']['Superman Returns'] = 5.0
    critics['Gene Seymour']['The Night Listener'] = 3.0
    critics['Gene Seymour']['You, Me and Dupree'] = 3.5

    critics['Michael Phillips']['Lady in the Water'] = 2.5
    critics['Michael Phillips']['Snakes on a Plane'] = 3.0
    critics['Michael Phillips']['Superman Returns'] = 3.5
    critics['Michael Phillips']['The Night Listener'] = 4.0

    critics['Claudia Puig']['Snakes on a Plane'] = 3.5
    critics['Claudia Puig']['Just My Luck'] = 3.0
    critics['Claudia Puig']['Superman Returns'] = 4.0
    critics['Claudia Puig']['The Night Listener'] = 4.5
    critics['Claudia Puig']['You, Me and Dupree'] = 2.5

    critics['Mick LaSalle']['Lady in the Water'] = 3.0
    critics['Mick LaSalle']['Snakes on a Plane'] = 4.0
    critics['Mick LaSalle']['Just My Luck'] = 2.0
    critics['Mick LaSalle']['Superman Returns'] = 3.0
    critics['Mick LaSalle']['The Night Listener'] = 3.0
    critics['Mick LaSalle']['You, Me and Dupree'] = 2.0

    critics['Jack Matthews']['Lady in the Water'] = 3.0
    critics['Jack Matthews']['Snakes on a Plane'] = 4.0
    critics['Jack Matthews']['Superman Returns'] = 5.0
    critics['Jack Matthews']['The Night Listener'] = 3.0
    critics['Jack Matthews']['You, Me and Dupree'] = 3.5

    critics['Toby']['Snakes on a Plane'] = 4.5
    critics['Toby']['Superman Returns'] = 4.0
    critics['Toby']['You, Me and Dupree'] = 1.0

    return critics

def euclidean_distance(critic_list):
    """
    Calculate Euclidean distance between k critics for the set of movies
    which they have each reviewed.
    
    """
    critics = assign_scores()
    movie_sets = []
    
    for critic in critic_list:
        movie_sets.append(set(critics[critic]))

    # Set intersection
    common_movies = list(reduce(operator.and_, movie_sets))
    num_shared = len(common_movies)

    if not num_shared:
        return 0

    critic_sums = []
    
    for critic in critic_list:
        c = [critics[critic][movie] for movie in common_movies]
        critic_sums.append(c)

def sim_pearson(prefs, p1, p2):
    si = {}
    for item in prefs[p1]:
        if item in prefs[p2]:
            si[item] = 1

    n = len(si)

    if n == 0:
        return 0

    # Get the sum of each critic's reviews for all common movies
    sum1 = sum([prefs[p1][it] for it in si])
    sum2 = sum([prefs[p2][it] for it in si])

    # Calculate the sum of the squares of each critic's reviews for all
    # common movies.
    sum1_square = sum([pow(prefs[p1][it], 2) for it in si])
    sum2_square = sum([pow(prefs[p2][it], 2) for it in si])

    # Calculate the sum of the product of the review of each movie from
    # each critic.
    sum_of_products = sum([prefs[p1][it] * prefs[p2][it] for it in si])
    num = sum_of_products - (sum1 * sum2 / n)
    den = sqrt((sum1_square - pow(sum1, 2) / n) * (sum2_square - pow(sum2, 2) / n))

    if den == 0:
        return 0

    r = num/den

    return r
        

def getRecommendations(prefs, person, similarity=sim_pearson):
    totals = {}
    simSums = {}
    for other in prefs:
        if other == person:
            continue
        sim = similarity(prefs, person, other)

        # Ignore scores of zero or less.
        if sim <= 0:
            continue

        for item in prefs[other]:
            if item not in prefs[person] or prefs[person][item] == 0:
                totals.setdefault(item, 0)
                totals[item] += prefs[other][item] * sim
                simSums.setdefault(item, 0)
                simSums[item] += sim

    rankings = [(total/simSums[item], item) for item, total in totals.items()]
    return sorted(rankings, reverse=True)
    
        
            
    
    
    
    
    
