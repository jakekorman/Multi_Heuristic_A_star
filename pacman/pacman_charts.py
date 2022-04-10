import matplotlib.pyplot as plt
import DataOrganizer
import math
TIME,COST,EXPANDED = 0,1,2
ASTAR, WASTAR, IMHASTAR, SMHASTAR = 0, 1, 2, 3
X_VALUES, Y_VALUES = 0, 1




# # RUN TIME
# plt.xlabel("Game Size")
# plt.ylabel("Run Time (seconds)")
# plt.title("Weights w1: root(1.5), w2: root(1.5)")
# plt.plot(sizes[:len(a_star_run_time)],a_star_run_time[:len(a_star_run_time)],  color='green',
#          linestyle='solid',
#          marker='o',markerfacecolor='black', markersize=5, label="A*")
# plt.plot(sizes[:len(wa_star_run_time)],wa_star_run_time[:len(
#     wa_star_run_time)],  color='orange',linestyle='solid',
#          marker='o',markerfacecolor='black', markersize=5, label="WA*")
# plt.plot(sizes[:len(imha_star_run_time)],imha_star_run_time[:len(
#     imha_star_run_time)], color='red',linestyle='solid',
#          marker='o',markerfacecolor='black', markersize=5,label="IMHA*" )
# plt.plot(sizes[:len(smha_star_run_time)],smha_star_run_time[:len(
#     smha_star_run_time)],  color='blue',linestyle='solid',
#          marker='o',markerfacecolor='black', markersize=5,label="SMHA*")
# plt.legend()
# plt.show()
#
# #COST
# plt.xlabel("Game Size")
# plt.ylabel("Cost")
# plt.title("Weights w1: root(1.5), w2: root(1.5)")
# plt.plot(sizes[:len(a_star_cost)],a_star_cost[:len(a_star_cost)],
#          color='green',
#          linestyle='solid',
#          marker='o',markerfacecolor='black', markersize=5, label="A*")
# plt.plot(sizes[:len(wa_star_cost)],wa_star_cost[:len(
#     wa_star_cost)],  color='orange',linestyle='solid',
#          marker='o',markerfacecolor='black', markersize=5, label="WA*")
# plt.plot(sizes[:len(imha_star_cost)],imha_star_cost[:len(
#     imha_star_cost)], color='red',linestyle='solid',
#          marker='o',markerfacecolor='black', markersize=5,label="IMHA*" )
# plt.plot(sizes[:len(smha_star_cost)],smha_star_cost[:len(
#     smha_star_cost)],  color='blue',linestyle='solid',
#          marker='o',markerfacecolor='black', markersize=5,label="SMHA*")
# plt.legend()
# plt.show()

def template_graph(x_label:str, y_label:str, title:str, legend_title:str, plotlines):
    plt.xlabel(x_label,fontweight="bold")
    plt.ylabel(y_label,fontweight="bold")
    plt.title(title,fontweight="bold")
    for line in plotlines:  # ALL INFO IN THE PLOTLINE
        # if line[COLOR]== 'c' or line[COLOR]== 'b':
            plt.plot(line[X_VALUES],line[Y_VALUES],color=line[COLOR],linestyle=line[LINESTYLE],marker=line[MARK],
                     markerfacecolor=line[MARK_COLOR],markersize=line[MARK_SIZE],label=line[LABEL]) # fill in each parameter from the line which is a list
    plt.legend(title=legend_title)
    plt.show()

## Indicies for the following lists: Astar, WAstar, IMHAstar, SMHAstar

board_sizes = [(8,4),(9,5),(10,6),(11,7),(12,8),(13,9),(14,10)]
weight_combos=[(10,10), (1,1), (math.sqrt(2),math.sqrt(2)), (3,3), (1,10),
                (math.sqrt(2),math.sqrt(1.5)) ,(math.sqrt(1.5),math.sqrt(2))]
data_holders = DataOrganizer.initialize_DOs()
sizes = ['8 x 4', '9 x 5', '10 x 6', '11 x 7', '12 x 8', '13 x 9','14 x 10']


#### First set of Graphs (9 total)
#### Solcost, runtime, expnodes of each algo as compared to astar, each weight combo a different line

# Astar Benchmark Plotlines:
Astar_data = data_holders[ASTAR]
A_cost_data = []
A_time_data = []
A_expanded_data = []

for size in board_sizes:
    time, cost, expanded = Astar_data.get_value(size)
    A_time_data.append(time)
    A_cost_data.append(cost)
    A_expanded_data.append(expanded)

astar_time_plotline = [sizes, A_time_data, 'green', 'solid','o','black', 5, "A*"]
astar_cost_plotline = [sizes, A_cost_data, 'green', 'solid','o','black', 5, "A*"]
astar_expanded_plotline = [sizes, A_expanded_data, 'green', 'solid','o','black', 5, "A*"]


def set_up_plot_lst(weight_combos):
    # plotlines_lst is the list of five lists, one for each weightcombo.
    # Each one of those lists has three lists, one for each type of info
    plotlines_lst = []
    for i in range(len(weight_combos)):
        wcombo_list = [[None]*8, [None]*8, [None]*8]
        for sublist in wcombo_list:
            sublist[1] = []
        plotlines_lst.append(wcombo_list)


    return plotlines_lst

def set_x_and_y_vals(plotlines_lst, DO: DataOrganizer, board_sizes, graphics_sizes, weight_combos):
    for idx, wcombo_lst in enumerate(plotlines_lst):
        for plot in wcombo_lst:
            plot[X_VALUES] = graphics_sizes  # x_vals
        for size in board_sizes:
            time, cost, expanded = DO.get_value((weight_combos[idx], size))
            wcombo_lst[TIME][Y_VALUES].append(time)
            wcombo_lst[COST][Y_VALUES].append(cost)
            wcombo_lst[EXPANDED][Y_VALUES].append(expanded)
    return plotlines_lst

COLOR, LINESTYLE, MARK, MARK_COLOR,MARK_SIZE,LABEL = 2,3,4,5,6,7
def set_up_graphics(plotlines_lst, color_lst, label_lst):

    counter = 0
    for w_combo_lst in plotlines_lst:
        for plot_lst in w_combo_lst:
            plot_lst[COLOR] = color_lst[counter]
            plot_lst[LINESTYLE] = '-'
            plot_lst[MARK] = 'o'
            plot_lst[MARK_COLOR] = 'black'
            plot_lst[MARK_SIZE] = 5
            plot_lst[LABEL] = label_lst[counter]
        counter +=1
    return plotlines_lst

# # WAstar
#
# WAstar_plots = set_up_plot_lst(weight_combos[2:-1])
# WAstar_plots = set_x_and_y_vals(WAstar_plots, data_holders[WASTAR],board_sizes[:-2],sizes[:-2],weight_combos[2:-1])
# colors = ['#C68907','#B8B30A','y','#EA8B0B']
# labels = ['w=2','w=9','w=10','w=√3']
# WAstar_plots = set_up_graphics(WAstar_plots,colors, labels)
#
# IMHAstar

IMHAstar_plots = set_up_plot_lst(weight_combos)
IMHAstar_plots = set_x_and_y_vals(IMHAstar_plots, data_holders[IMHASTAR],board_sizes,sizes,weight_combos)
colors = ['b','#F17509','r','c','m','y','k']
labels = ['w1=10,w2=10','w1=1,w2=1','w1=√2,w2=√2','w1=3,w2=3','w1=1,w2=10','w1=√2,w2=√1.5','w1=√1.5,w2=√2']
IMHAstar_plots = set_up_graphics(IMHAstar_plots,colors, labels)

I_time_plots = []
I_cost_plots = []
I_expanded_plots = []
for wcombo_lst in IMHAstar_plots:
    I_time_plots.append(wcombo_lst[TIME])
    I_cost_plots.append(wcombo_lst[COST])
    I_expanded_plots.append(wcombo_lst[EXPANDED])

I_time_plots.insert(0,astar_time_plotline)
I_cost_plots.insert(0,astar_cost_plotline)
I_expanded_plots.insert(0,astar_expanded_plotline)

template_graph("Game Size (spaces)","Runtime (s)", "Runtime IMHA*","Weight Combos", I_time_plots)
template_graph("Game Size (spaces)","Cost (steps)", "Solution Cost IMHA*","Weight Combos", I_cost_plots)
template_graph("Game Size (spaces)","Number of Nodes", "Expanded Nodes IMHA*","Weight Combos", I_expanded_plots)

# SMHAstar :

SMHAstar_plots = set_up_plot_lst(weight_combos)
SMHAstar_plots = set_x_and_y_vals(SMHAstar_plots, data_holders[SMHASTAR],board_sizes,sizes,weight_combos)
colors = ['b','#F17509','r','c','m','y','k']
labels = ['w1=10,w2=10','w1=1,w2=1','w1=√2,w2=√2','w1=3,w2=3','w1=1,w2=10','w1=√2,w2=√1.5','w1=√1.5,w2=√2']
SMHAstar_plots = set_up_graphics(SMHAstar_plots,colors, labels)

S_time_plots = []
S_cost_plots = []
S_expanded_plots = []
for wcombo_lst in SMHAstar_plots:
    S_time_plots.append(wcombo_lst[TIME])
    S_cost_plots.append(wcombo_lst[COST])
    S_expanded_plots.append(wcombo_lst[EXPANDED])

S_time_plots.insert(0,astar_time_plotline)
S_cost_plots.insert(0,astar_cost_plotline)
S_expanded_plots.insert(0,astar_expanded_plotline)

template_graph("Game Size (spaces)","Runtime (s)", "Runtime SMHA*","Weight Combos", S_time_plots)
template_graph("Game Size (spaces)","Cost (steps)", "Solution Cost SMHA*","Weight Combos", S_cost_plots)
template_graph("Game Size (spaces)","Number of Nodes", "Expanded Nodes SMHA*","Weight Combos", S_expanded_plots)

# Solcost, runtime, expnodes vs board size with all 4 algos with specific weights
# Instances solved under 90seconds for (10,10),(1,1),(1,10),(3,3)
# Generate graphs for w1 = root2 and w2 = root1.5 and the opposite



# Generate all graphs, make all their plotlines and call template graph in a for loop.
# Figure out how to save all the graphs to a file to put in report



# #COST
# plt.xlabel("Game Size")
# plt.ylabel("Cost")
# plt.title("Weights w1: root(1.5), w2: root(1.5)")
# plt.plot(sizes[:len(a_star_cost)], a_star_cost[:len(a_star_cost)],
#          color='green',
#          linestyle='solid',
#          marker='o',markerfacecolor='black', markersize=5, label="A*")
# plt.plot(sizes[:len(wa_star_cost)],wa_star_cost[:len(
#     wa_star_cost)],  color='orange',linestyle='solid',
#          marker='o',markerfacecolor='black', markersize=5, label="WA*")
# plt.plot(sizes[:len(imha_star_cost)],imha_star_cost[:len(
#     imha_star_cost)], color='red',linestyle='solid',
#          marker='o',markerfacecolor='black', markersize=5,label="IMHA*" )
# plt.plot(sizes[:len(smha_star_cost)],smha_star_cost[:len(
#     smha_star_cost)],  color='blue',linestyle='solid',
#          marker='o',markerfacecolor='black', markersize=5,label="SMHA*")
# plt.legend()
# plt.show()