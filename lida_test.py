from lida import Manager
from lida.utils import plot_raster 

lida = Manager()
summary = lida.summarize("model/data/Loan payments data.xlsx") # generate data summary

print(summary)


goals = lida.goals(summary, n=5) # generate goals

print(goals)


# generate charts (generate and execute visualization code)
charts = lida.visualize(summary=summary, goal=goals[0], library="matplotlib") # seaborn, ggplot ..

# plot raster image of chart
plot_raster(charts[0].raster)