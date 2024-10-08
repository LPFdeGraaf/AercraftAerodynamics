import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
plt.close('all')

path = '/home/zbook/Desktop/MSc/Q1/AercraftAerodynamics/Report2/'
part1 = 'Part 1/'
part2 = 'Part 2/'
part3 = 'Part 3/'


newairfoil = np.loadtxt(path + part2 + 'naca_polars.txt', skiprows=12)
print(path )


#    alpha    CL        CD       CDp       CM     Top_Xtr  Bot_Xtr  Top_Itr  Bot_Itr
polar_6 = np.loadtxt(path +part1+ '6_polar.txt', skiprows=12)

def part6():
    fig6 = plt.figure(figsize=(8, 6))
    ax6 = fig6.add_subplot(111)

    # Use a color palette for the lines
    colors = plt.get_cmap('tab20')(np.linspace(0, 1, 2))

    ax6.plot(polar_6[:,0], polar_6[:,2], color=colors[0], label='Polar 6')
    # ax6.plot(newairfoil[:,0], newairfoil[:,1], color=colors[1], label='New Airfoil')
    ax6.grid(which='both', linestyle='--', linewidth=0.5)

    # Set the limits of the x and y axes
    ax6.set_xlim([-2, 8])
    # ax6.set_ylim([0, 1.3])

    # Add labels for the x and y axes
    ax6.set_xlabel(r'$\alpha$ [deg]', fontsize=20)
    ax6.set_ylabel(r'$C_D$', fontsize=20)

    # Use a larger font size for the title and the labels
    # plt.suptitle('Figure Title', fontsize=16, fontweight='bold')
    # ax6.set_title('Axes Title', loc='left', fontsize=14, fontstyle='oblique')

    # Use tight_layout() to automatically adjust the padding around the plot
    plt.tight_layout()

    # Use rcParams to customize the appearance of the plot
    plt.rcParams['font.family'] = 'sans-serif'
    plt.rcParams['font.size'] = 12
    plt.rcParams['lines.linewidth'] = 1

    #plt.legend(loc='best')
    fig6.savefig('Part1_6_CD.png')
    plt.show()

# part6()



# Cl - C
def part7():
    fig7 = plt.figure(figsize=(8, 6))
    ax7 = fig7.add_subplot(111)
    # Transition points vs angle of attack
    colors = plt.get_cmap('tab20')(np.linspace(0, 1, 2))

    ax7.plot(polar_6[:, 0], polar_6[:, 5], label='Upper Surface')
    ax7.plot(polar_6[:, 0], polar_6[:, 6], label='Lower Surface')
    # plt.plot(newairfoil[:, 0], newairfoil[:, 5], label='upper new')
    # plt.plot(newairfoil[:, 0], newairfoil[:, 6], label='lower new')

    ax7.grid(which='both', linestyle='--', linewidth=0.5)
    ax7.set_xlim([-2, 8])
    ax7.set_ylim([0, 1.])
    # Add labels for the x and y axes

    ax7.set_xlabel(r'$\alpha$ [deg]', fontsize=20)
    ax7.set_ylabel(r'$x_{tr}$', fontsize=20)

    # Use a larger font size for the title and the labels
    # plt.suptitle('Figure Title', fontsize=16, fontweight='bold')
    # ax7.set_title('Axes Title', loc='left', fontsize=14, fontstyle='oblique')

    # Use tight_layout() to automatically adjust the padding around the plot
    plt.tight_layout()

    # Use rcParams to customize the appearance of the plot
    plt.rcParams['font.family'] = 'sans-serif'
    plt.rcParams['font.size'] = 12
    plt.rcParams['lines.linewidth'] = 1

    plt.legend(loc='best')
    plt.show()
    fig7.savefig('Part1_7.png')
# part7()

def part8():
    xtr90 = np.loadtxt('xtr90_forced.txt', skiprows=12)
    xtr88 = np.loadtxt('xtr88_forced.txt', skiprows=12)
    xtr85 = np.loadtxt('xtr85_forced.txt', skiprows=12)
    xtr83 = np.loadtxt('xtr83_forced.txt', skiprows=12)
    xtr80 = np.loadtxt('xtr80_forced.txt', skiprows=12)
    xtr70 = np.loadtxt('xtr70_forced.txt', skiprows=12)
    xtr60 = np.loadtxt('xtr60_forced.txt', skiprows=12)
    xtr50 = np.loadtxt('xtr50_forced.txt', skiprows=12)
    xtr40 = np.loadtxt('xtr40_forced.txt', skiprows=12)
    xtr30 = np.loadtxt('xtr30_forced.txt', skiprows=12)
    xtr20 = np.loadtxt('xtr20_forced.txt', skiprows=12)
    xtr10 = np.loadtxt('xtr10_forced.txt', skiprows=12)

    CD_list = [xtr10[2], xtr20[2], xtr30[2],xtr40[2], xtr50[2], xtr60[2],xtr70[2], xtr80[2],xtr83[2],  xtr85[2],  xtr88[2], xtr90[2], polar_6[7,2]]
    xtr = [xtr10[5], xtr20[5], xtr30[5],xtr40[5], xtr50[5], xtr60[5],xtr70[5], xtr80[5],xtr83[5], xtr85[5], xtr88[5], xtr90[5],  polar_6[7,5]]

    fig8 = plt.figure(figsize=(8, 6))
    ax8 = fig8.add_subplot(111)
    # Transition points vs angle of attack
    colors = plt.get_cmap('tab20')(np.linspace(0, 1, 2))

    ax8.plot(xtr, CD_list, label= r'Forced Trans: $\alpha$ = 0')
    ax8.scatter(xtr[-1], CD_list[-1], label= 'Natural Transition', marker='x', color='r')

    ax8.grid(which='both', linestyle='--', linewidth=0.5)
    # ax8.set_ylim([0.006, 0.0105])
    ax8.set_xlim([0, 1.])
    # Add labels for the x and y axes

    ax8.set_ylabel(r'$C_d$', fontsize=20)
    ax8.set_xlabel(r'$x_{tr}$', fontsize=20)

    # Use a larger font size for the title and the labels
    # plt.suptitle('Figure Title', fontsize=16, fontweight='bold')
    # ax8.set_title('Axes Title', loc='left', fontsize=14, fontstyle='oblique')

    # Use tight_layout() to automatically adjust the padding around the plot
    plt.tight_layout()

    # Use rcParams to customize the appearance of the plot
    plt.rcParams['font.family'] = 'sans-serif'
    plt.rcParams['font.size'] = 12
    plt.rcParams['lines.linewidth'] = 1

    legend = plt.legend(loc="upper right", edgecolor="black")

    plt.show()
    fig8.savefig('Part1_8.png')
# part8()


def part9():
    cf_a0 = np.loadtxt(path + part1 + 'cf_alfa0.txt', skiprows=7)
    cf_a4 = np.loadtxt(path + part1 + 'cf_alfa4.txt', skiprows=7)

    fig9 = plt.figure(figsize=(8, 6))
    ax9 = fig9.add_subplot(111)
    colors = plt.get_cmap('tab20')(np.linspace(0, 8, 8))

    ax9.plot(cf_a0[:82,0], cf_a0[:82,1], color=colors[0], label=r'$\alpha$ = 0')
    ax9.plot(cf_a4[:88, 0], cf_a4[:88, 1], color='g', label=r'$\alpha$ = 4')

    ax9.grid(which='both', linestyle='--', linewidth=0.5)
    ax9.set_xlim([0, 1.])
    # ax9.set_ylim([0, 0.02])

    ax9.set_xlabel(r'$x/c$', fontsize=20)
    ax9.set_ylabel(r'$C_f$', fontsize=20)

    plt.suptitle('Friction coefficient along the upper surface', fontsize=16, fontweight='bold')
    # ax9.set_title('Axes Title', loc='left', fontsize=14, fontstyle='oblique')

    # Use tight_layout() to automatically adjust the padding around the plot
    plt.tight_layout()

    # Use rcParams to customize the appearance of the plot
    plt.rcParams['font.family'] = 'sans-serif'
    plt.rcParams['font.size'] = 12
    plt.rcParams['lines.linewidth'] = 1

    plt.legend(loc='best')
    plt.show()
    fig9.savefig('Part1_9.png')

# part9()


"""  Part 2:  Airfoil improved Design  """

def part2_1():
    index = 8
    print(polar_6[index,1])
    print('Cl/ Cd for Cl = 0.4 is roughly', polar_6[index,1]/polar_6[index,2])

# part2_1()

def part2_3():
    myairfoil = np.loadtxt(path + part1 + 'myairfoil.txt', skiprows=1)
    gdes_airfoil = np.loadtxt(path + part2 + 'Usefull/' + 'gdes_test2.txt', skiprows=1)
    inv_airfoil  = np.loadtxt(path + part2 + 'Usefull/' + 'inv_test7.txt', skiprows=1)

    fig23 = plt.figure(figsize=(8, 6))

    # Create two subplots
    ax23_1 = fig23.add_subplot(121)
    ax23_2 = fig23.add_subplot(122)

    colors = ['b', 'g', 'r']  # Define colors for each airfoil
    linestyles = ['-', '--', ':']  # Define line styles for each airfoil

    # Plot the first subplot
    ax23_1.plot(myairfoil[:,0] , myairfoil[:,1], label='NACA 2814', color=colors[0], linestyle=linestyles[1])
    ax23_1.plot(gdes_airfoil[:,0], gdes_airfoil[:,1], label='Design 1', color=colors[1], linestyle=linestyles[0])
    ax23_1.legend(loc='best')
    ax23_1.set_title('Subplot 1')
    ax23_1.grid(which='both', linestyle='--', linewidth=0.5)
    # ax23_1.set_xlim([0, 1.])
    ax23_1.set_ylim([-0.3, 0.3])
    ax23_1.set_xlabel(r'$x/c$', fontsize=20)
    ax23_1.set_ylabel(r'$y/c$', fontsize=20)

    # Plot the second subplot
    ax23_2.plot(myairfoil[:,0] , myairfoil[:,1], label='NACA 2814', color=colors[0], linestyle=linestyles[1])
    ax23_2.plot(inv_airfoil[:,0], inv_airfoil[:,1], label='Design 2', color=colors[2], linestyle=linestyles[1])
    ax23_2.set_title('Subplot 2')
    ax23_2.grid(which='both', linestyle='--', linewidth=0.5)
    # ax23_2.set_xlim([0, 1.])
    ax23_2.set_ylim([-0.3, 0.3])
    ax23_2.set_xlabel(r'$x/c$', fontsize=20)

    # plt.suptitle('Figure Title', fontsize=16, fontweight='bold')
    plt.tight_layout()

    # Use rcParams to customize the appearance of the plot
    plt.rcParams['font.family'] = 'sans-serif'
    plt.rcParams['font.size'] = 12
    plt.rcParams['lines.linewidth'] = 1

    plt.legend(loc='best')
    plt.show()
    fig23.savefig('Part2_3.png')

# part2_3()


def part2_4():
    my = np.loadtxt(path +part2 + 'Usefull/' + 'my_polar.txt', skiprows=12)
    gdes = np.loadtxt(path+ part2 + 'Usefull/' + 'gdes_polar.txt', skiprows=12)
    inv = np.loadtxt(path+ part2 + 'Usefull/' + 'inv_polar.txt', skiprows=12)

    print(my[1]/my[2])
    print(gdes[1]/gdes[2])
    print(inv[1]/inv[2])



    my_pres = np.loadtxt(path + part2 + 'Usefull/' + 'cp_myairfoil.txt', skiprows=1)
    gdes_pres = np.loadtxt(path  + part2 + 'Usefull/' + 'gdes_test2_cp.txt', skiprows=1)
    inv_pres = np.loadtxt(path + part2 + 'Usefull/' + 'inv_test7_cp.txt', skiprows = 1)

    fig241 = plt.figure(figsize=(8, 6))
    #fig242 = plt.figure(figsize=(8, 6))
    ax24_1 = fig241.add_subplot(121)
    ax24_2 = fig241.add_subplot(122)
    colors = ['b', 'g', 'r']
    linestyles = ['-', '--', ':']

    ax24_1.plot(my_pres[:,0], my_pres[:,1], label='NACA 2814', color=colors[0], linestyle=linestyles[1])
    ax24_1.plot(gdes_pres[:,0], gdes_pres[:,1], label='Design 1', color=colors[1], linestyle=linestyles[2])
    ax24_1.legend(loc='best')
    # ax24_1.set_title('Subplot 1')
    ax24_1.grid(which='both', linestyle='--', linewidth=0.5)
    # ax24_1.set_ylim([-0.3, 0.3])
    ax24_1.invert_yaxis()

    ax24_1.grid(which='both', linestyle='--', linewidth=0.5)
    ax24_1.set_xlabel(r'$x/c$', fontsize=20)
    ax24_1.set_ylabel(r'$C_p$', fontsize=20)
    plt.legend(loc='best')
    # plt.show()

    ax24_2.plot(my_pres[:,0], my_pres[:,1], label='NACA 2814', color=colors[0], linestyle=linestyles[1])
    ax24_2.plot(inv_pres[:,0], inv_pres[:,1], label='Design 2', color=colors[2], linestyle=linestyles[2])
    # ax24_2.set_title('Subplot 2')
    ax24_2.invert_yaxis()
    ax24_2.grid(which='both', linestyle='--', linewidth=0.5)
    # ax24_2.set_ylim([-0.3, 0.3])
    ax24_2.set_xlabel(r'$x/c$', fontsize=20)
    ax24_2.set_ylabel(r'$C_p$', fontsize=20)
    # plt.suptitle('Figure Title', fontsize=16, fontweight='bold')
    plt.tight_layout()
    plt.rcParams['font.family'] = 'sans-serif'
    plt.rcParams['font.size'] = 12
    plt.rcParams['lines.linewidth'] = 1
    plt.legend(loc='best')
    plt.show()
    fig241.savefig('part2_4.png')
# part2_4()

""" Part 3: Laminar Separation Bubble"""

def part3_2():

    my_cp_lamsepbub = np.loadtxt(path + part3 + 'cp_nattrans.txt', skiprows=1)
    # Value for which the bubble is removed: TBF
    cp_71trans = np.loadtxt(path + part3 + 'cp_71trans.txt', skiprows=1)

    # Create the first figure
    fig1 = plt.figure(figsize=(8, 6))
    ax1 = fig1.add_subplot(111)

    colors = ['b', 'g', 'r']  # Define colors for each airfoil
    linestyles = ['-', '--', ':']  # Define line styles for each airfoil

    # Plot the data for the first figure
    ax1.set_xlabel(r'$x/c$', fontsize=20)
    ax1.set_ylabel(r'$C_p}$', fontsize=20)
    ax1.plot(my_cp_lamsepbub[:, 0], my_cp_lamsepbub[:, 1], label='Natural transition', color=colors[0], linestyle='--')
    ax1.plot(cp_71trans[:, 0], cp_71trans[:, 1], label='Forced transition at x/c = 0.71', color=colors[1])
    ax1.tick_params(axis='y', colors='k')
    ax1.invert_yaxis()
    ax1.legend(loc='best')
    ax1.grid(which='both', linestyle='--', linewidth=0.5)

    # Create the second figure
    fig2 = plt.figure(figsize=(8, 6))
    ax2 = fig2.add_subplot(111)

    # Load the data for the second figure
    my_cf_lamsepbub = np.loadtxt(path + part3 + 'cf_nattrans.txt', skiprows=7)
    cf_71trans = np.loadtxt(path + part3 + 'cf_71trans.txt', skiprows=7)

    # Plot the data for the second figure
    ax2.set_xlabel(r'$x/c$', fontsize=20)
    ax2.set_ylabel(r'$C_f$', fontsize=20)
    ax2.plot(my_cf_lamsepbub[:84, 0], my_cf_lamsepbub[:84, 1], label='Natural transition', color=colors[0], linestyle='--')
    ax2.plot(cf_71trans[:84,0], cf_71trans[:84,1], label='Forced transition at x/c = 0.71', color=colors[1])
    ax2.tick_params(axis='y', colors='b')
    ax2.grid(which='both', linestyle='--', linewidth=0.5)
    ax2.legend(loc='best')
    # Use rcParams to customize the appearance of the plots
    plt.rcParams['font.family'] = 'sans-serif'
    plt.rcParams['font.size'] = 12
    plt.rcParams['lines.linewidth'] = 1

    # Add legends and tighten the layout for both figures
    #plt.legend(loc='best')
    fig1.tight_layout()
    fig2.tight_layout()

    fig1.savefig('part3_2_cp.png')
    fig2.savefig('part3_2_cf.png')


    # Show both figures
    plt.show()

# part3_2()


def part3_mindrag():

    xtr_val = []
    Cd_values = []

    for i in [58, 64, 67, 70, 71 , 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85]:
        data = np.loadtxt(path + part3 + f'{i}trans.txt', skiprows=12)
        val = data[2]
        print(val)
        xtr_val.append(i/100)
        Cd_values.append(val)

    # natural transition
    nat_trans = np.loadtxt(path + part3 + 'nattrans.txt', skiprows=12)


    # Minimum drag
    print(np.min(Cd_values), Cd_values.index(min(Cd_values)))
    print(Cd_values)

    figcd = plt.figure(figsize=(8, 6))
    axcd = figcd.add_subplot(111)
    colors = plt.get_cmap('tab20')(np.linspace(0, 8, 8))

    axcd.plot(xtr_val, Cd_values, color=colors[0], label=r'$\alpha$ = 0')
    axcd.scatter(nat_trans[5], nat_trans[2], label='Natural Transition', marker='x', color='r')

    axcd.grid(which='both', linestyle='--', linewidth=0.5)
    axcd.set_xlim([0, 1.])
    # axcd.set_ylim([0, 0.02])

    axcd.set_xlabel(r'$x/c$', fontsize=20)
    axcd.set_ylabel(r'$C_d$', fontsize=20)

    plt.suptitle('Figure Title', fontsize=16, fontweight='bold')
    axcd.set_title('Axes Title', loc='left', fontsize=14, fontstyle='oblique')

    # Use tight_layout() to automatically adjust the padding around the plot
    plt.tight_layout()

    # Use rcParams to customize the appearance of the plot
    plt.rcParams['font.family'] = 'sans-serif'
    plt.rcParams['font.size'] = 12
    plt.rcParams['lines.linewidth'] = 1

    plt.legend(loc='best')
    # axcd.show()
    axcd.savefig('part3_cd_transition.pdf')

part3_mindrag()

