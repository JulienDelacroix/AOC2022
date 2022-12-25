import sys
import re
import functools

dict = {}

@functools.lru_cache()
def dfs(time, ore, clay, obsidian, geode, ore_robots, clay_robots, obsidian_robots, geode_robots):
    key = (ore, clay, obsidian, geode, ore_robots, clay_robots, obsidian_robots, geode_robots)
    
    if key in dict and time >= dict[key]:
        return 0
    if key not in dict or time < dict[key]:
        dict[key] = time

    if time == 33: 
        return geode

    best = 0
    if ore >= geode_ore and obsidian >= geode_obsidian:
        return dfs(
            time+1,
            ore + ore_robots - geode_ore, clay + clay_robots, obsidian + obsidian_robots - geode_obsidian, geode + geode_robots,
            ore_robots, clay_robots, obsidian_robots, geode_robots + 1)

    if ore >= obsidian_ore and clay >= obsidian_clay:
        return dfs(
            time+1,
            ore + ore_robots - obsidian_ore , clay + clay_robots - obsidian_clay, obsidian + obsidian_robots, geode + geode_robots,
            ore_robots, clay_robots, obsidian_robots + 1, geode_robots)

    if ore >= clay_ore:
        best = max(best, dfs(
            time+1,
            ore + ore_robots - clay_ore , clay + clay_robots, obsidian + obsidian_robots, geode + geode_robots,
            ore_robots, clay_robots + 1, obsidian_robots, geode_robots))

    if ore >= ore_ore:
        best = max(best, dfs(
            time+1,
            ore + ore_robots - ore_ore , clay + clay_robots, obsidian + obsidian_robots, geode + geode_robots,
            ore_robots + 1, clay_robots, obsidian_robots, geode_robots))

    best = max(best, dfs(
            time+1,
            ore + ore_robots, clay + clay_robots, obsidian + obsidian_robots, geode + geode_robots,
            ore_robots, clay_robots, obsidian_robots, geode_robots))

    return best

pattern = "Blueprint (\d+): Each ore robot costs (\d+) ore. Each clay robot costs (\d+) ore. Each obsidian robot costs (\d+) ore and (\d+) clay. Each geode robot costs (\d+) ore and (\d+) obsidian."

R = 1
for line in sys.stdin.read().splitlines()[:3]:
    id, ore_ore, clay_ore, obsidian_ore, obsidian_clay, geode_ore, geode_obsidian  = map(int, re.findall(pattern, line)[0])
    R *= dfs(1, 0, 0, 0, 0, 1, 0, 0, 0)
    dfs.cache_clear()
    dict = {}
print(R)
