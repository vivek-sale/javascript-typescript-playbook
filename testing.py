store_distance_tat = dict()

stores = ["1", "2", "3", "4"]

distance = {"1":1, "2":3, "3":2, "4":4}

tat = {"1":6, "2":2, "3":2, "4":1}

for store in stores:
    store_distance_tat[store] = {
                "distance": distance[store],
                "tat": tat[store]
            }

print(sorted(store_distance_tat,
                      key=lambda x: (store_distance_tat[x]['tat'], store_distance_tat[x]['distance'])))