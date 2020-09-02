def greedySetCover(states_needed, stations):
  final_stations = set()

  while states_needed:
    best_station = None
    states_covered = set()
    for station, states in stations.items():
      covered = states_needed & states
      if len(covered) > len(states_covered):
        best_station = station
        states_covered = covered
    final_stations.add(best_station)
    states_needed -= states_covered
#    print(best_station, states_covered)
  return final_stations
