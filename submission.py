from mars_planner import*
from search_algorithms import*
from routefinder import*
import antenna_frequencies

#Question 2
print("Running DFS for Move to Sample:")
s = RoverState()  # Initial state for the problem
dfs_move_to_sample = depth_first_search(s, action_list, move_to_sample_goal)
s.loc = "sample"
# 2: Remove sample
print("Running DFS for Remove sample:")
dfs_remove_sample = depth_first_search(s, action_list, remove_sample_goal)
s.sample_extracted = True
# 3: Return to charger
print("Running DFS for Return to charger:")
dfs_return_charger = depth_first_search(s, action_list, return_to_charger_goal)

print("Running DLS for Move to Sample:")
s2 = RoverState()  # Initial state for the problem
dls_move_to_sample = depth_first_search(s2, action_list, move_to_sample_goal, limit=1)
s2.loc = "sample"
# 2: Remove sample
print("Running DLS for Remove sample:")
dls_remove_sample = depth_first_search(s2, action_list, remove_sample_goal, limit=2)
s2.sample_extracted = True
# 3: Return to charger
print("Running DLS for Return to charger:")
dls_return_charger = depth_first_search(s2, action_list, return_to_charger_goal, limit=2)

print("Running BFS for Move to Sample:")
s3 = RoverState()  # Initial state for the problem
bfs_move_to_sample = breadth_first_search(s3, action_list, move_to_sample_goal)
s3.loc = "sample"
# 2: Remove sample
print("Running BFS for Remove sample:")
bfs_remove_sample = breadth_first_search(s3, action_list, remove_sample_goal)
s3.sample_extracted = True
# 3: Return to charger
print("Running BFS for Return to charger:")
bfs_return_charger = breadth_first_search(s3, action_list, return_to_charger_goal)

#Question 3
#Run a* for the origin location "8,8"
map1 = map_state(location="8,8", g=0, h=sld("8,8"))
a_star_result = a_star(map1, sld, goal)
print(a_star_result)

#Run UCS for the origin location "8,8"
map2 = map_state(location="8,8", g=0, h=0)
ucs_result = a_star(map2, h1, goal)
print(ucs_result)

#Question 4
#Run antenna_frequency problem
antenna_frequencies.main()
