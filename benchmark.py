import os, runpy, time
from prettytable import PrettyTable
from aocd import models

curr_year = 2021
table = PrettyTable(['Folder', 'Day', 'Title', 'Solved', 'Time[μs]'])
folders = [filename for filename in os.listdir() if os.path.isdir(os.path.join(filename)) if filename[0] != "."]
folders = sorted(folders, key=lambda name: int(name[4:]))

times = [time.perf_counter()]

for folder in folders:
    runpy.run_path(f"{folder}/main.py")
    times.append(time.perf_counter())
    
for i, folder in enumerate(folders):    
    stat_info = os.stat(folder)
    modified = time.ctime(stat_info.st_mtime)
    title = models.Puzzle(curr_year, i + 1).title
    t = '{:.4f}'.format(round(times[i+1]-times[i], 8) * 1000)

    table.add_row([folder, i + 1, title, modified, t])

print(table)
print(f"Total time: {round(times[-1]-times[0], 4)}s")
