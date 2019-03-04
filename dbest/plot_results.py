import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import numpy as np
import matplotlib.pyplot as plt
import matplotlib._color_data as mcd
import matplotlib.patches as mpatch

overlap = {name for name in mcd.CSS4_COLORS
           if "xkcd:" + name in mcd.XKCD_COLORS}

font_size = 14  # 14
colors = {
    "DBEst_1k": mcd.XKCD_COLORS['xkcd:coral'],
    "DBEst_10k": mcd.XKCD_COLORS['xkcd:orange'],  # blue
    "DBEst_100k": mcd.XKCD_COLORS['xkcd:orangered'],  # green
    "DBEst_1m": mcd.XKCD_COLORS['xkcd:red'],  # yellow
    "BlinkDB_1k": mcd.XKCD_COLORS['xkcd:lightblue'],  # red
    "BlinkDB_10k": mcd.XKCD_COLORS['xkcd:turquoise'],  # red
    "BlinkDB_100k": mcd.XKCD_COLORS['xkcd:teal'],  # cyan
    "BlinkDB_1m": mcd.XKCD_COLORS['xkcd:azure'],  # magenta
    "BlinkDB_5m": mcd.XKCD_COLORS['xkcd:blue'],  # red
    "BlinkDB_26m": mcd.XKCD_COLORS['xkcd:darkblue'],  # red
    "lightgreen": mcd.XKCD_COLORS['xkcd:lightgreen'],
    "green": mcd.XKCD_COLORS['xkcd:green'],
    "orange": mcd.XKCD_COLORS['xkcd:orange'],
    "orangered": mcd.XKCD_COLORS['xkcd:orangered'],
    "red": mcd.XKCD_COLORS['xkcd:red'],
}
alpha = {
    "1": 0.1,
    "2": 0.3,
    "3": 0.5,
    "4": 0.7,
    "5": 0.9,
    '6': 1.0
}

# colors = {
#     "DBEst_1k": mcd.XKCD_COLORS['xkcd:lime'],
#     "DBEst_10k": mcd.XKCD_COLORS['xkcd:lightgreen'],  # blue
#     "DBEst_100k": mcd.XKCD_COLORS['xkcd:green'],  # green
#     "DBEst_1m": mcd.XKCD_COLORS['xkcd:darkgreen'],  # yellow
#     "BlinkDB_1k": mcd.XKCD_COLORS['xkcd:lightblue'],  # red
#     "BlinkDB_10k": mcd.XKCD_COLORS['xkcd:turquoise'],  # red
#     "BlinkDB_100k": mcd.XKCD_COLORS['xkcd:teal'],  # cyan
#     "BlinkDB_1m": mcd.XKCD_COLORS['xkcd:azure'],  # magenta
#     "BlinkDB_5m": mcd.XKCD_COLORS['xkcd:blue'],  # red
# }


def model_training_time_ensemble():
    x = [200, 2000, 20000, 200000, 2000000]
    X = [0.00523, 0.0144, 0.12209, 1.09748, 13.21596]
    G = [0.00834, 0.01452, 0.0636, 0.58815, 7.70868]
    C = [0.074486, 0.322717, 2.94475, 31.227796, 306.769922]
    plt.loglog(x, X, "x-", label="XGboost")
    plt.loglog(x, G, "o-", label="GBoost")
    plt.loglog(x, C, "v-", label="Qreg")
    plt.legend()
    plt.xlabel("Number of training points", fontsize=font_size)
    plt.ylabel("Training time (s)", fontsize=font_size)
    plt.tick_params(labelsize=font_size)

    plt.show()


def model_training_time_base_models():
    x = [100, 1000, 10000, 100000, 1000000]
    LR = [0.00056,    0.00061,  0.00073,   0.00221,    0.02457]
    PR = [0.00260,   0.00613,  0.02261,   0.57020,   8.13341]
    DTR = [0.00019,    0.00042,    0.00291,   0.02642,   0.26859]
    KNN = [0.00028,  0.00041,   0.00178,   0.01814,   0.56045]
    SVR = [0.00032,   0.01614,   1.21145,   1078.83512]
    Gaussian = [0.13289,  2.15688,   780.21678]
    plt.loglog(x, LR, "x-", label="LR")
    plt.loglog(x, PR, "o-", label="PR")
    plt.loglog(x, DTR, "v-", label="DTR")
    plt.loglog(x, KNN, "*-", label="KNN")
    plt.loglog(x[:-1], SVR, ".-", label="SVR")
    plt.loglog(x[:-2], Gaussian, "h-", label="Gaussian")
    plt.legend()
    plt.xlabel("Number of training points", fontsize=font_size)
    plt.ylabel("Training time (s)", fontsize=font_size)
    plt.tick_params(labelsize=font_size)

    plt.show()


def draw_tpcds_bars():
    def to_percent(y, pos):
        return '%.1f%%' % (y * 100)
    x = [1, 3]
    x1 = [0.8, 2.8]
    x2 = [1.2, 3.2]
    y1 = [0.0531, 0.0137]
    y2 = [0.436, 2.592]

    fig, ax1 = plt.subplots()

    ax2 = ax1.twinx()
    p1 = ax1.bar(x1, y1, color='g', width=0.3)

    formatter = FuncFormatter(to_percent)
    ax1.yaxis.set_major_formatter(formatter)
    p2 = ax2.bar(x2, y2, color='r', width=0.3)
    #ax1.set_xlabel('X data')
    plt.xticks(x, ("Relative Error (%)", 'Response Time (s)'))
    plt.legend((p1[0], p2[0]), ('10k', '100k'), loc='center')
    ax1.set_ylabel("Relative Error (%)")
    ax2.set_ylabel('Response Time (s)')

    plt.show()


def to_percent(y, pos):
    return '%.1f%%' % (y * 100)

#-----------------------------------------------------------------------------------------------

def plt_tpcds_multi_cp_relative_error():
    plt.rcParams.update({'font.size': 12})
    width = 0.20
    data = [
        [0.0650,  0.0279,  0.0393, 0.0441],  # , 0.0486],
        [0.0727,  0.0596,  0.0155, 0.0493],  # , 0.0335],
        [0.0317,  0.0220,  0.0104, 0.0214],  # , 0.0182],
        [0.0628,  0.0707,  0.0069, 0.0468]  # , 0.0212]
    ]

    X = np.arange(4)

    fig, ax = plt.subplots()

    p1 = plt.bar(
        X + 0.00, data[0], color=colors["DBEst_10k"], width=width, alpha=alpha['2'])
    p2 = plt.bar(
        X + 0.20, data[1], color=colors["BlinkDB_10k"], width=width, alpha=alpha['3'])
    p3 = plt.bar(
        X + 0.40, data[2], color=colors["DBEst_100k"], width=width, alpha=alpha['4'])
    p4 = plt.bar(
        X + 0.60, data[3], color=colors["BlinkDB_100k"], width=width, alpha=alpha['6'])

    plt.legend((p1[0], p2[0], p3[0], p4[0]),
               ('DBEst_10k', 'BlinkDB_10k', 'DBEst_100k', 'BlinkDB_100k'), loc='1')

    plt.xticks(X + 1.5 * width, ("COUNT", 'SUM', 'AVG', 'OVERALL'))
    ax.set_ylabel("Relative Error (%)")
    # ax.set_yscale('log')
    formatter = FuncFormatter(to_percent)
    ax.yaxis.set_major_formatter(formatter)
    plt.subplots_adjust(bottom=0.07)
    # plt.subplots_adjust(left=0.23)

    plt.show()


def plt_tpcds_multi_cp_response_time():
    plt.rcParams.update({'font.size': 12})
    width = 0.20
    data = [
        [0.015,  0.588, 0.436],  # , 0.0486],
        [91.32,  64.290, 56.140],  # , 0.0335],
        [0.085,  2.551, 2.592],  # , 0.0182],
        [187.05,  143.99, 171.57]  # , 0.0212]
    ]

    X = np.arange(3)

    fig, ax = plt.subplots()

    p1 = plt.bar(
        X + 0.00, data[0], color=colors["DBEst_10k"], width=width, alpha=alpha['2'])
    p2 = plt.bar(
        X + 0.20, data[1], color=colors["BlinkDB_10k"], width=width, alpha=alpha['3'])
    p3 = plt.bar(
        X + 0.40, data[2], color=colors["DBEst_100k"], width=width, alpha=alpha['4'])
    p4 = plt.bar(
        X + 0.60, data[3], color=colors["BlinkDB_100k"], width=width, alpha=alpha['6'])

    plt.legend((p1[0], p2[0], p3[0], p4[0]),
               ('DBEst_10k', 'BlinkDB_10k', 'DBEst_100k', 'BlinkDB_100k'), loc='center left')

    plt.xticks(X + 1.5 * width, ("COUNT", 'SUM', 'AVG', 'OVERALL'))
    ax.set_ylabel("Response Time (s)")
    ax.set_yscale('log')
    formatter = FuncFormatter(to_percent)
    # ax.yaxis.set_major_formatter(formatter)

    plt.show()


def plt_tpcds_multi_cp_training_time():
    plt.rcParams.update({'font.size': 22})
    width = 0.30
    # data = [
    #     [281.5, 286],  # , 0.0486],
    #     [39.8,  278.3],  # , 0.0335],
    #     [2328,  2342]
    # ]
    data = [
        [67.49972558, 68],
        [0.653846154, 4.961538462],
        [108.8538909, 107.7999105] 
    ]

    X = np.arange(2)

    fig, ax = plt.subplots()

    p1 = plt.bar(X + 0.00, data[0], color=colors["orange"], width=width,alpha=0.3)
    p2 = plt.bar(X + 0.00, data[1], color=colors["red"],
                 width=width, bottom=data[0],alpha=0.6)
    p3 = plt.bar(X + 0.30, data[2], color=colors["BlinkDB_10k"], width=width,alpha=0.9)

    plt.legend((p1[0], p2[0], p3[0]),
               ('DBEst Sampling', 'DBEst Training', 'VerdictDB Sampling', 'BlinkDB_100k'), loc='lower center', prop={'size': 18})

    plt.xticks(X + 0.5 * width, ("10k", '100k', 'AVG', 'OVERALL'))
    ax.set_ylabel("Total Training Time (s)")
    ax.set_xlabel("Sample Size")
    # ax.set_yscale('log')
    formatter = FuncFormatter(to_percent)
    # ax.yaxis.set_major_formatter(formatter)
    plt.subplots_adjust(bottom=0.16)
    plt.subplots_adjust(left=0.20)
    plt.ylim([0,120])

    plt.show()


def plt_tpcds_multi_cp_memory_usage():
    plt.rcParams.update({'font.size': 22})
    width = 0.30
    # data = [
    #     [5.9959, 22.195],  # , 0.0486],
    #     [1024,  1340],  # , 0.0335],
    # ]
    data = [
        [0.192,   1.684], 
        [1.7,       9.7], 
    ]



    X = np.arange(2)

    fig, ax = plt.subplots()

    p1 = plt.bar(
        X + 0.00, data[0], color=colors["DBEst_10k"], width=width, alpha=alpha['2'])
    p2 = plt.bar(
        X + width, data[1], color=colors["BlinkDB_10k"], width=width, alpha=alpha['6'])
    # p3 = plt.bar(X + 0.30, data[2], color=colors["BlinkDB_10k"], width=width)

    plt.legend((p1[0], p2[0]),
               ('DBEst', 'VerdictDB', 'BlinkDB Sampling', 'BlinkDB_100k'), loc='center', prop={'size': 18})

    plt.xticks(X + 0.5 * width, ("10k", '100k', 'AVG', 'OVERALL'))
    ax.set_ylabel("Space Overhead (MB)")
    ax.set_xlabel("Sample Size")
    # ax.set_yscale('log')
    formatter = FuncFormatter(to_percent)
    # ax.yaxis.set_major_formatter(formatter)
    plt.subplots_adjust(bottom=0.18)
    plt.subplots_adjust(left=0.18)

    plt.show()




##----------------------------------------------------------------------------------------##

def plt_tpcds_single_cp_sample_size_response_time():
    plt.rcParams.update({'font.size': 12})
    width = 0.20
    # data = [
    #     [0.00829, 0.2673276,  0.03481, 0.0352, 0.04278, 0.05179, 0.07853, 0.07707],
    #     [0.09, 3.1,   0.22,  0.23, 0.22, 0.29, 0.053, 0.053],
    #     [1.13, 41.46232,  3.07, 3.08, 3.01, 4.66, 0.06, 0.06],
    #     [7.07, 200, 21.07,  21.13, 19.07, 26.44, 0.056, 0.056],
    # ]
    # data = [
    #     [0.00829, 0.12,  0.03481, 0.0352, 0.04278, 0.05179, 0.07853, 0.07707],
    #     [0.09, 1.2,   0.22,  0.23, 0.22, 0.29, 0.053, 0.053],
    #     [1.13, 24,  3.07, 3.08, 3.01, 4.66, 0.06, 0.06],
    #     [7.07, 0, 21.07,  21.13, 19.07, 26.44, 0.056, 0.056],
    # ]

    data = [
        [0.00829, 0.12,  0.03481, 0.0352, 0.04278, 0.05179],
        [0.09, 1.2,   0.22,  0.23, 0.22, 0.29             ],
        [1.13, 24,  3.07, 3.08, 3.01, 4.66                ]  ,
        [7.07, 0, 21.07,  21.13, 19.07, 26.44             ],
    ]

    X = np.arange(6)

    fig, ax = plt.subplots()

    p1 = plt.bar(
        X + 0.00, data[0], color=colors["lightgreen"], width=width, alpha=alpha['2'])
    p2 = plt.bar(X + 0.20, data[1], color=colors["green"],
                 width=width, alpha=alpha['3'])
    p3 = plt.bar(
        X + 0.40, data[2], color=colors["BlinkDB_1m"], width=width, alpha=alpha['4'])
    p4 = plt.bar(
        X + 0.60, data[3], color=colors["BlinkDB_5m"], width=width, alpha=alpha['6'])

    plt.legend((p1[0], p2[0], p3[0], p4[0]),
               ('10k', '100k', '1m', '5m'), loc='1')

    plt.xticks(X + 1.5 * width, ("COUNT", 'PERCENTILE',
                                 'VARIANCE', 'STDDEV', 'SUM', 'AVG', 'MIN', 'MAX'))
    ax.set_ylabel("Query Response Time (s)")
    ax.set_yscale('log')
    formatter = FuncFormatter(to_percent)
    # ax.yaxis.set_major_formatter(formatter)

    for item in ax.axes.get_xticklabels():
        item.set_rotation(60)
    plt.subplots_adjust(bottom=0.22)

    plt.show()


def plt_tpcds_single_cp_sample_size_relative_error():
    plt.rcParams.update({'font.size': 12})
    width = 0.20
    # data = [
    #     [0.0607,  0.01, 0.0704,  0.0151,  0.0831,  0.0397,  0.3092,  0.1971],
    #     [0.0259,  0.00607, 0.0103,  0.0045,  0.0248, 0.00620,  0.3021,  0.204],
    #     [0.0099,  0.00360, 0.0092,  0.0039,  0.0103,  0.0021,  0.3139,  0.2088],
    #     [0.0048,  0.0035, 0.009,  0.0038,  0.0051,  0.0015,  0.3163,  0.2104],
    # ]
    data = [
        [0.0607,  0.01, 0.0704,  0.0151,  0.0831,     0.0397],
        [0.0259,  0.00607, 0.0103,  0.0045,  0.0248, 0.00620],
        [0.0099,  0.00360, 0.0092,  0.0039,  0.0103,  0.0021],
        [0.0048,  0.0035, 0.009,  0.0038,  0.0051,    0.0015],
    ]

    X = np.arange(6)

    fig, ax = plt.subplots()

    p1 = plt.bar(
        X + 0.00, data[0], color=colors["lightgreen"], width=width, alpha=alpha['2'])
    p2 = plt.bar(X + 0.20, data[1], color=colors["green"],
                 width=width, alpha=alpha['3'])
    p3 = plt.bar(
        X + 0.40, data[2], color=colors["BlinkDB_1m"], width=width, alpha=alpha['4'])
    p4 = plt.bar(
        X + 0.60, data[3], color=colors["BlinkDB_5m"], width=width, alpha=alpha['6'])

    plt.legend((p1[0], p2[0], p3[0], p4[0]),
               ('10k', '100k', '1m', '5m'), loc='1')

    plt.xticks(X + 1.0 * width, ("COUNT", 'PERCENTILE',
                                 'VARIANCE', 'STDDEV', 'SUM', 'AVG', 'MIN', 'MAX'))
    ax.set_ylabel("Relative Error (%)")
    ax.set_yscale('log')
    formatter = FuncFormatter(to_percent)
    ax.yaxis.set_major_formatter(formatter)

    for item in ax.axes.get_xticklabels():
        item.set_rotation(60)
    plt.subplots_adjust(bottom=0.22)
    plt.subplots_adjust(left=0.15)
    plt.show()


def plt_tpcds_single_cp_sample_size_relative_error_blinkdb():
    plt.rcParams.update({'font.size': 22})
    width = 0.16
    data = [
        [0.31361,     0.31337,     0.10307],
        [0.09527,     0.09525,     0.01158],
        [0.07199,     0.07227,     0.00375],
        [0.06938,     0.06757,     0.00020],
        [0.06760,     0.06760,     0.00020],
    ]

    X = np.arange(3)

    fig, ax = plt.subplots()

    p1 = plt.bar(
        X + 0.00, data[0], color=colors["lightgreen"], width=width, alpha=alpha['2'])
    p2 = plt.bar(
        X + 1 * width, data[1], color=colors["green"], width=width, alpha=alpha['3'])
    p3 = plt.bar(
        X + 2 * width, data[2], color=colors["BlinkDB_1m"], width=width, alpha=alpha['4'])
    p4 = plt.bar(
        X + 3 * width, data[3], color=colors["BlinkDB_5m"], width=width, alpha=alpha['5'])
    p5 = plt.bar(
        X + 4 * width, data[4], color=colors["BlinkDB_26m"], width=width, alpha=alpha['6'])

    plt.legend((p1[0], p2[0], p3[0], p4[0], p5[0]),
               ('1k', '10k', '100k', '1m', '26m'), loc='1', prop={'size': 13})

    plt.xticks(X + 2 * width, ("COUNT", 'SUM', 'AVG',
                               'STDDEV', 'SUM', 'AVG', 'MIN', 'MAX'))
    ax.set_ylabel("Relative Error (%)")
    ax.set_yscale('log')
    formatter = FuncFormatter(to_percent)
    ax.yaxis.set_major_formatter(formatter)

    # for item in ax.axes.get_xticklabels():
    #     item.set_rotation(60)
    plt.subplots_adjust(bottom=0.1)
    plt.subplots_adjust(left=0.23)
    plt.show()


def plt_tpcds_single_cp_sample_size_response_time_blinkdb():
    plt.rcParams.update({'font.size': 22})
    width = 0.16
    data = [
        [1.763, 1.872, 1.871],
        [11.65, 12.52, 12.28],
        [115.36, 131.86, 126.04],
        [174.65, 193.32, 185.24],
        [291.19, 265.98, 558.94],
    ]

    X = np.arange(3)

    fig, ax = plt.subplots()

    p1 = plt.bar(
        X + 0.00, data[0], color=colors["lightgreen"], width=width, alpha=alpha['2'])
    p2 = plt.bar(
        X + 1 * width, data[1], color=colors["green"], width=width, alpha=alpha['3'])
    p3 = plt.bar(
        X + 2 * width, data[2], color=colors["BlinkDB_1m"], width=width, alpha=alpha['4'])
    p4 = plt.bar(
        X + 3 * width, data[3], color=colors["BlinkDB_5m"], width=width, alpha=alpha['5'])
    p5 = plt.bar(
        X + 4 * width, data[4], color=colors["BlinkDB_26m"], width=width, alpha=alpha['6'])

    plt.legend((p1[0], p2[0], p3[0], p4[0], p5[0]),
               ('1k', '10k', '100k', '1m', '26m'), loc='upper left', prop={'size': 11})

    plt.xticks(X + 2 * width, ("COUNT", 'SUM', 'AVG',
                               'STDDEV', 'SUM', 'AVG', 'MIN', 'MAX'))
    ax.set_ylabel("Response Time (s)")
    ax.set_yscale('log')
    # formatter = FuncFormatter(to_percent)
    # ax.yaxis.set_major_formatter(formatter)

    # for item in ax.axes.get_xticklabels():
    #     item.set_rotation(60)
    plt.subplots_adjust(bottom=0.1)
    plt.subplots_adjust(left=0.18)
    plt.show()


def plt_tpcds_single_cp_training_time_comparison():
    plt.rcParams.update({'font.size': 22})
    fig, ax = plt.subplots()
    # y1 = [411, 421.295, 442.629, 779.5,   3847,    17228]
    # y2 = [2321,    2326,    2343,    2342,    2355,    2378]
    # x = [1E3, 1E4, 1E5, 1E6, 5E6, 26E6]

    y1 = [67.1,    68.15357173, 72.96153846, 154]
    y2 = [107, 108.8538909, 110.7999105, 122.7593984]
    x = [1E3, 1E4, 1E5, 1E6]




    p1 = plt.plot(x, y1, 'rx-')
    p2 = plt.plot(x, y2, 'gh-')

    plt.legend((p1[0], p2[0]),
               ('DBEst', 'VerdictDB'), loc='1')

    ax.set_xlabel("Sample Size")
    ax.set_ylabel("Training Time (s)")

    plt.xticks([5E6, 1E6], ('5m', '26m'))
    ax.set_xscale('log')
    # ax.set_yscale('log')

    plt.subplots_adjust(bottom=0.16)
    plt.subplots_adjust(left=0.18)

    plt.show()


def plt_tpcds_single_cp_memory_cost_comparison():
    plt.rcParams.update({'font.size': 22})
    fig, ax = plt.subplots()
    # y2 = [78, 99, 208, 787.6923077, 4096]
    # y1 = [0.486134,   1.995219,   20.265429,  94.901193,  484.876566]
    # x = [1E4, 1E5, 1E6, 5E6, 26E6]

    y1 = [0.486134,   1.995219,   20.265429,  94.901193,  484.876566]
    y2 = [78, 99, 208, 787.6923077, 4096]
    
    x = [1E4, 1E5, 1E6, 5E6, 26E6]
    p1 = plt.plot(x, y1, 'rx-')
    p2 = plt.plot(x, y2, 'gh-')

    plt.legend((p1[0], p2[0]),
               ('DBEst', 'BlinkDB'), loc='1')

    ax.set_xlabel("Sample Size")
    ax.set_ylabel("Memory Overhead (MB)")

    plt.xticks([5E6, 26E6], ('5m', '26m'))
    ax.set_xscale('log')
    ax.set_yscale('log')

    plt.subplots_adjust(bottom=0.16)
    plt.subplots_adjust(left=0.18)

    plt.show()


def plt_tpcds_single_cp_query_range_relative_error():
    plt.rcParams.update({'font.size': 12})
    width = 0.20
    data = [
        [0.0364,  0.0061,  0.0360,  0.0178,  0.0363,  0.0085,  0.2957, 0.1985],
        [0.0260,  0.0061,  0.0107,  0.0047,  0.0248,  0.0062,  0.3021, 0.2040],
        [0.0111,  0.0061,  0.0092,  0.0039,  0.0113,  0.0033,  0.2883, 0.1886],
    ]
    data = [
        [0.0364,  0.0061,  0.0360,  0.0178,  0.0363,  0.0085],
        [0.0260,  0.0061,  0.0107,  0.0047,  0.0248,  0.0062],
        [0.0111,  0.0061,  0.0092,  0.0039,  0.0113,  0.0033],
    ]

    X = np.arange(6)

    fig, ax = plt.subplots()

    p1 = plt.bar(
        X + 0.00, data[0], color=colors["lightgreen"], width=width, alpha=alpha['2'])
    p2 = plt.bar(X + 0.20, data[1], color=colors["green"],
                 width=width, alpha=alpha['4'])
    p3 = plt.bar(
        X + 0.40, data[2], color=colors["BlinkDB_1m"], width=width, alpha=alpha['6'])
    # p4 = plt.bar(X + 0.60, data[3], color=colors["BlinkDB_5m"], width=width)

    plt.legend((p1[0], p2[0], p3[0]),
               ('0.1% query range', '1.0% query range', '10.0% query range', '5m'), loc='1')

    plt.xticks(X + 1.0 * width, ("COUNT", 'PERCENTILE',
                                 'VARIANCE', 'STDDEV', 'SUM', 'AVG', 'MIN', 'MAX'))
    ax.set_ylabel("Relative Error (%)")
    ax.set_yscale('log')
    formatter = FuncFormatter(to_percent)
    ax.yaxis.set_major_formatter(formatter)

    for item in ax.axes.get_xticklabels():
        item.set_rotation(60)
    plt.subplots_adjust(bottom=0.22)
    plt.subplots_adjust(left=0.15)
    plt.show()


def plt_tpcds_single_cp_query_range_response_time():
    plt.rcParams.update({'font.size': 12})
    width = 0.25
    shift=1
    # data = [
    #     [0.0873, 1.2,  0.2465,  0.2480,  0.1449,  0.2223,  0.0532,  0.0530],
    #     [0.0866, 1.2,  0.2200,  0.2300,  0.2184,  0.2885,  0.0530,  0.0530],
    #     [0.1823, 1.2,  0.5837,  0.5800,  0.6567,  0.9072,  0.0568,  0.0573],
    # ]
    data = [
        [0.0873, 1.2,  0.2465,  0.2480,  0.1449,  0.2223],
        [0.0866, 1.2,  0.2200,  0.2300,  0.2184,  0.2885],
        [0.1823, 1.2,  0.5837,  0.5800,  0.6567,  0.9072],
    ]

    X = np.arange(6)

    fig, ax = plt.subplots()

    p1 = plt.bar(
        X + 0.00+shift*width, data[0], color=colors["lightgreen"], width=width, alpha=alpha['2'])
    p2 = plt.bar(X + width+shift*width, data[1], color=colors["green"],
                 width=width, alpha=alpha['4'])
    p3 = plt.bar(
        X + 2*width+shift*width, data[2], color=colors["BlinkDB_1m"], width=width, alpha=alpha['6'])
    # p4 = plt.bar(X + 0.60, data[3], color=colors["BlinkDB_5m"], width=width)

    plt.legend((p1[0], p2[0], p3[0]),
               ('0.1% query range', '1.0% query range', '10.0% query range', '5m'), loc='1')

    plt.xticks(X + 1.5 * width, ("COUNT", 'PERCENTILE',
                                 'VARIANCE', 'STDDEV', 'SUM', 'AVG', 'MIN', 'MAX'))
    ax.set_ylabel("Query Response Time (s)")
    # ax.set_yscale('log')
    formatter = FuncFormatter(to_percent)
    # ax.yaxis.set_major_formatter(formatter)

    for item in ax.axes.get_xticklabels():
        item.set_rotation(60)
    plt.subplots_adjust(bottom=0.22)

    plt.show()


#--------------------------------------------------------------------
# CCPP
#--------------------------------------------------------------------
def plt_ccpp_multi_cp_relative_error():
    plt.rcParams.update({'font.size': 12})
    width = 0.20
    data = [
        [0.0478,  0.0481,  0.0017,  0.0325],  # , 0.0486],
        [0.0534,  0.0548,  0.0020,  0.0367],  # , 0.0335],
        [0.0155,  0.0153,  0.0006,  0.0104],  # , 0.0182],
        [0.0174,  0.0171,  0.0005,  0.0117]  # , 0.0212]
    ]

    X = np.arange(4)

    fig, ax = plt.subplots()

    p1 = plt.bar(
        X + 0.00, data[0], color=colors["DBEst_10k"], width=width, alpha=alpha['2'])
    p2 = plt.bar(
        X + 0.20, data[1], color=colors["BlinkDB_10k"], width=width, alpha=alpha['3'])
    p3 = plt.bar(
        X + 0.40, data[2], color=colors["DBEst_100k"], width=width, alpha=alpha['4'])
    p4 = plt.bar(
        X + 0.60, data[3], color=colors["BlinkDB_100k"], width=width, alpha=alpha['6'])

    plt.legend((p1[0], p2[0], p3[0], p4[0]),
               ('DBEst_10k', 'BlinkDB_10k', 'DBEst_100k', 'BlinkDB_100k'), loc='1')

    plt.xticks(X + 1.5 * width, ("COUNT", 'SUM', 'AVG', 'OVERALL'))
    ax.set_ylabel("Relative Error (%)")
    # ax.set_yscale('log')
    formatter = FuncFormatter(to_percent)
    ax.yaxis.set_major_formatter(formatter)
    plt.subplots_adjust(bottom=0.08)
    # plt.subplots_adjust(left=0.13)

    plt.show()
def plt_ccpp_multi_cp_relative_error_verdict_10k():
    plt.rcParams.update({'font.size': 12})
    width = 0.20
    data = [
        [0.051461925, 0.050878425, 0.00192856 ,0.034756303],
        [0.174683727, 0.177441235, 0.005118666,0.119081209],
        [0.15574034 , 0.156995274, 0.006549603,0.106428406],
        [0.164854974, 0.165270941, 0.005731419,0.111952445] 
    ]
    # no MySQL
    data = [
        [0.051461925, 0.050878425, 0.00192856 ,0.034756303],
        # [0.174683727, 0.177441235, 0.005118666,0.119081209],
        [0.15574034 , 0.156995274, 0.006549603,0.106428406],
        # [0.164854974, 0.165270941, 0.005731419,0.111952445] 
    ]

    X = np.arange(4)

    fig, ax = plt.subplots()

    p1 = plt.bar(
        X + 0.00, data[0], color=colors["DBEst_10k"], width=width, alpha=alpha['2'])
    p2 = plt.bar(
        X + 0.20, data[1], color=colors["BlinkDB_10k"], width=width, alpha=alpha['3'])
    # p3 = plt.bar(
    #     X + 0.40, data[2], color=colors["DBEst_100k"], width=width, alpha=alpha['4'])
    # p4 = plt.bar(
    #     X + 0.40, data[2], color=colors["BlinkDB_100k"], width=width, alpha=alpha['6'])

    plt.legend((p1[0], p2[0]),
               ('DBEst_10k', 'MySQL_10k'), loc='1')

    plt.xticks(X + 1.0 * width, ("COUNT", 'SUM', 'AVG', 'OVERALL'))
    ax.set_ylabel("Relative Error (%)")
    # ax.set_yscale('log')
    formatter = FuncFormatter(to_percent)
    ax.yaxis.set_major_formatter(formatter)
    plt.subplots_adjust(bottom=0.08)
    plt.subplots_adjust(left=0.15)

    plt.show()
def plt_ccpp_multi_cp_response_time_verdict_10k():
    plt.rcParams.update({'font.size': 18})
    width = 0.20
    data = [
        [0.0120  ,0.0181  ,0.0171  ,0.0136 ],
        [13.9600 ,14.1800 ,14.3500 ,14.1633],
        [0.0067  ,0.0067  ,0.0068  ,0.0067 ],
        [0.8652  ,0.6366  ,0.6185  ,0.7068 ] 
    ]

    X = np.arange(4)

    fig, ax = plt.subplots()

    p1 = plt.bar(
        X + 0.00, data[0], color=colors["DBEst_10k"], width=width, alpha=alpha['2'])
    p2 = plt.bar(
        X + 0.20, data[1], color=colors["BlinkDB_10k"], width=width, alpha=alpha['3'])
    p3 = plt.bar(
        X + 0.40, data[2], color=colors["DBEst_100k"], width=width, alpha=alpha['4'])
    p4 = plt.bar(
        X + 0.60, data[3], color=colors["BlinkDB_100k"], width=width, alpha=alpha['6'])

    plt.legend((p1[0], p2[0],p3[0],p4[0]),
               ('DBEst_10k','BlinkDB_10k','MySQL_10k', 'VerdictDB_10k'), loc='upper left')

    plt.xticks(X + 1.5 * width, ("COUNT", 'SUM', 'AVG', 'OVERALL'))
    ax.set_ylabel("Qeury Response Time (s)")
    ax.set_yscale('log')
    formatter = FuncFormatter(to_percent)
    # ax.yaxis.set_major_formatter(formatter)
    plt.subplots_adjust(bottom=0.08)
    plt.subplots_adjust(left=0.17)

    plt.show()

def plt_ccpp_multi_cp_response_time_verdict_100k():
    plt.rcParams.update({'font.size': 18})
    width = 0.20
    data = [
        [0.1695  ,0.272  ,0.2731  ,0.2381 ],
        [18.4900 ,20.1900 ,19.2100 ,19.2967 ],
        [0.0639  ,0.0623  ,0.0628  ,0.0630 ],
        [0.5939  ,0.5915  ,0.5838  ,0.5897 ] 
    ]





    X = np.arange(4)

    fig, ax = plt.subplots()

    p1 = plt.bar(
        X + 0.00, data[0], color=colors["DBEst_10k"], width=width, alpha=alpha['2'])
    p2 = plt.bar(
        X + 0.20, data[1], color=colors["BlinkDB_10k"], width=width, alpha=alpha['3'])
    p3 = plt.bar(
        X + 0.40, data[2], color=colors["DBEst_100k"], width=width, alpha=alpha['4'])
    p4 = plt.bar(
        X + 0.60, data[3], color=colors["BlinkDB_100k"], width=width, alpha=alpha['6'])

    plt.legend((p1[0], p2[0],p3[0],p4[0]),
               ('DBEst_100k','BlinkDB_100k','MySQL_100k', 'VerdictDB_100k'), loc='upper left')

    plt.xticks(X + 1.5 * width, ("COUNT", 'SUM', 'AVG', 'OVERALL'))
    ax.set_ylabel("Qeury Response Time (s)")
    ax.set_yscale('log')
    formatter = FuncFormatter(to_percent)
    # ax.yaxis.set_major_formatter(formatter)
    plt.subplots_adjust(bottom=0.08)
    plt.subplots_adjust(left=0.17)

    plt.show()

def plt_ccpp_multi_cp_relative_error_verdict_100k():
    plt.rcParams.update({'font.size': 12})
    width = 0.20
    data = [
        [0.027136681, 0.027507043, 0.000903558, 0.018515761],
        [0.073711447, 0.074260957, 0.001724737, 0.049899047],
        [0.065931394, 0.064697144, 0.0023057  , 0.044311413],
        [0.050935661, 0.050739747, 0.001832127, 0.034502512] 
    ]

    data = [
        [0.027136681, 0.027507043, 0.000903558, 0.018515761],
        # [0.073711447, 0.074260957, 0.001724737, 0.049899047],
        [0.065931394, 0.064697144, 0.0023057  , 0.044311413],
        # [0.050935661, 0.050739747, 0.001832127, 0.034502512] 
    ]





    X = np.arange(4)

    fig, ax = plt.subplots()

    p1 = plt.bar(
        X + 0.00, data[0], color=colors["DBEst_10k"], width=width, alpha=alpha['2'])
    p2 = plt.bar(
        X + 0.20, data[1], color=colors["BlinkDB_10k"], width=width, alpha=alpha['3'])
    # p3 = plt.bar(
    #     X + 0.40, data[2], color=colors["DBEst_100k"], width=width, alpha=alpha['4'])
    # p4 = plt.bar(
    #     X + 0.40, data[2], color=colors["BlinkDB_100k"], width=width, alpha=alpha['6'])

    plt.legend((p1[0], p2[0]),
               ('DBEst_100k', 'MySQL_100k'), loc='1')

    plt.xticks(X + 1.5 * width, ("COUNT", 'SUM', 'AVG', 'OVERALL'))
    ax.set_ylabel("Relative Error (%)")
    # ax.set_yscale('log')
    formatter = FuncFormatter(to_percent)
    ax.yaxis.set_major_formatter(formatter)
    plt.subplots_adjust(bottom=0.08)
    plt.subplots_adjust(left=0.15)

    plt.show()
def plt_tpcds_multi_cp_relative_error_verdict_combined():
    plt.rcParams.update({'font.size': 12})
    width = 0.20
    data = [
        [0.027136681, 0.027507043, 0.000903558, 0.018515761],
        [0.073711447, 0.074260957, 0.001724737, 0.049899047],
        [0.065931394, 0.064697144, 0.0023057  , 0.044311413],
        [0.050935661, 0.050739747, 0.001832127, 0.034502512] 
    ]

    data=[
    [0.037773051,0.107663034, 0.012524812,0.0527],
    [0.146994078,0.145764373, 0.018608432,0.1038],
    [0.032786002,0.05248726 , 0.011889626,0.0324],
    [0.038593217,0.059797881, 0.012760796,0.0371]
    ]

       











    X = np.arange(4)

    fig, ax = plt.subplots()

    p1 = plt.bar(
        X + 0.00, data[0], color=colors["DBEst_10k"], width=width, alpha=alpha['2'])
    p2 = plt.bar(
        X + 0.20, data[1], color=colors["BlinkDB_10k"], width=width, alpha=alpha['3'])
    p3 = plt.bar(
        X + 0.40, data[2], color=colors["DBEst_100k"], width=width, alpha=alpha['4'])
    p4 = plt.bar(
        X + 0.60, data[3], color=colors["BlinkDB_100k"], width=width, alpha=alpha['6'])

    plt.legend((p1[0], p2[0], p3[0],p4[0]),
               ('DBEst_10k', 'VerdictDB_10k', 'DBEst_100k', 'VerdictDB_100k'), loc='1')

    plt.xticks(X + 1.5 * width, ("COUNT", 'SUM', 'AVG', 'OVERALL'))
    ax.set_ylabel("Relative Error (%)")
    # ax.set_yscale('log')
    formatter = FuncFormatter(to_percent)
    ax.yaxis.set_major_formatter(formatter)
    plt.subplots_adjust(bottom=0.08)
    plt.subplots_adjust(left=0.15)

    plt.show()


def plt_ccpp_multi_cp_response_time():
    plt.rcParams.update({'font.size': 12})
    width = 0.20
    data = [
        [0.0120,   0.1800,  0.1904,   0.1274],  # , 0.0486],
        [48.4600,   50.6000,  49.5600,   49.5400],  # , 0.0335],
        [0.1199,   0.7943,  0.8474,   0.5872],  # , 0.0182],
        [252.1500,   267.4700,  265.5200,   261.7133]  # , 0.0212]
    ]

    X = np.arange(4)

    fig, ax = plt.subplots()

    p1 = plt.bar(
        X + 0.00, data[0], color=colors["DBEst_10k"], width=width, alpha=alpha['2'])
    p2 = plt.bar(
        X + 0.20, data[1], color=colors["BlinkDB_10k"], width=width, alpha=alpha['3'])
    p3 = plt.bar(
        X + 0.40, data[2], color=colors["DBEst_100k"], width=width, alpha=alpha['4'])
    p4 = plt.bar(
        X + 0.60, data[3], color=colors["BlinkDB_100k"], width=width, alpha=alpha['6'])

    plt.legend((p1[0], p2[0], p3[0], p4[0]),
               ('DBEst_10k', 'BlinkDB_10k', 'DBEst_100k', 'BlinkDB_100k'), loc='center left')

    plt.xticks(X + 1.5 * width, ("COUNT", 'SUM', 'AVG', 'OVERALL'))
    ax.set_ylabel("Response Time (s)")
    ax.set_yscale('log')
    formatter = FuncFormatter(to_percent)
    # ax.yaxis.set_major_formatter(formatter)

    plt.show()


def plt_ccpp_multi_cp_training_time():
    plt.rcParams.update({'font.size': 22})
    width = 0.30
    data = [
        [4668.49, 4506],  # , 0.0486],
        [11.9,  70.5],  # , 0.0335],
        [6623.128,  6717.777]
    ]

    X = np.arange(2)

    fig, ax = plt.subplots()

    p1 = plt.bar(
        X + 0.00, data[0], color=colors["orange"], width=width, alpha=alpha['2'])
    p2 = plt.bar(X + 0.00, data[1], color=colors["red"],
                 width=width, bottom=data[0], alpha=alpha['4'])
    p3 = plt.bar(
        X + 0.30, data[2], color=colors["BlinkDB_10k"], width=width, alpha=alpha['6'])

    plt.legend((p1[0], p2[0], p3[0]),
               ('DBEst Sampling', 'DBEst training', 'BlinkDB Sampling', 'BlinkDB_100k'), loc='lower center', prop={'size': 18})

    plt.xticks(X + 0.5 * width, ("10k", '100k', 'AVG', 'OVERALL'))
    ax.set_ylabel("Total Training Time (s)")
    # ax.set_yscale('log')
    formatter = FuncFormatter(to_percent)
    # ax.yaxis.set_major_formatter(formatter)
    plt.subplots_adjust(bottom=0.09)
    plt.subplots_adjust(left=0.23)

    plt.show()


def plt_ccpp_multi_cp_memory_usage():
    plt.rcParams.update({'font.size': 22})
    width = 0.30
    data = [
        [0.333, 2.4156],  # , 0.0486],
        [66.4,  102.4],  # , 0.0335],
    ]

    X = np.arange(2)

    fig, ax = plt.subplots()

    p1 = plt.bar(
        X + 0.00, data[0], color=colors["DBEst_10k"], width=width, alpha=alpha['2'])
    p2 = plt.bar(
        X + width, data[1], color=colors["BlinkDB_10k"], width=width, alpha=alpha['6'])
    # p3 = plt.bar(X + 0.30, data[2], color=colors["BlinkDB_10k"], width=width)

    plt.legend((p1[0], p2[0]),
               ('DBEst', 'BlinkDB', 'BlinkDB Sampling', 'BlinkDB_100k'), loc='center', prop={'size': 18})

    plt.xticks(X + 0.5 * width, ("10k", '100k', 'AVG', 'OVERALL'))
    ax.set_ylabel("Memory Usage (MB)")
    ax.set_xlabel("Sample Size")
    ax.set_yscale('log')
    formatter = FuncFormatter(to_percent)
    # ax.yaxis.set_major_formatter(formatter)
    plt.subplots_adjust(bottom=0.16)
    plt.subplots_adjust(left=0.18)

    plt.show()


def plt_ccpp_multi_cp_relative_error_xgboost():
    plt.rcParams.update({'font.size': 12})
    width = 0.20
    data = [
        [0.0478 , 0.0481 , 0.0017 , 0.0325 ],  # , 0.0486],
        [0.0478 , 0.0410 , 0.0016 , 0.0329 ],  # , 0.0335],
        [0.0155 , 0.0153 , 0.0006 , 0.0104 ],  # , 0.0182],
        [0.0155 , 0.0188 , 0.0006 , 0.0134 ]  # , 0.0212]
    ]





    X = np.arange(4)

    fig, ax = plt.subplots()

    p1 = plt.bar(
        X + 0.00, data[0], color=colors["DBEst_10k"], width=width, alpha=alpha['2'])
    p2 = plt.bar(
        X + 0.20, data[1], color=colors["BlinkDB_10k"], width=width, alpha=alpha['3'])
    p3 = plt.bar(
        X + 0.40, data[2], color=colors["DBEst_100k"], width=width, alpha=alpha['4'])
    p4 = plt.bar(
        X + 0.60, data[3], color=colors["BlinkDB_100k"], width=width, alpha=alpha['6'])

    plt.legend((p1[0], p2[0], p3[0], p4[0]),
               ('DBEst_10k', 'DBEst_10k_XGBoost', 'DBEst_100k', 'DBEst_100k_XGBoost'), loc='1', prop={'size': 16})

    plt.xticks(X + 1.5 * width, ("COUNT", 'SUM', 'AVG', 'OVERALL'))
    ax.set_ylabel("Relative Error (%)")
    # ax.set_yscale('log')
    formatter = FuncFormatter(to_percent)
    ax.yaxis.set_major_formatter(formatter)
    plt.subplots_adjust(bottom=0.08)
    plt.subplots_adjust(left=0.20)

    plt.show()


def plt_ccpp_multi_cp_response_time_xgboost():
    plt.rcParams.update({'font.size': 12})
    width = 0.20
    data = [
        [0.012 ,  0.180,  0.190 , 0.127 ],  # , 0.0486],
        [0.012 ,  0.018,  0.029 , 0.019 ],  # , 0.0335],
        [0.120 ,  0.794,  0.847 , 0.587 ],  # , 0.0182],
        [0.119 ,  0.156,  0.263 , 0.179 ]  # , 0.0212]
    ]





    X = np.arange(4)

    fig, ax = plt.subplots()

    p1 = plt.bar(
        X + 0.00, data[0], color=colors["DBEst_10k"], width=width, alpha=alpha['2'])
    p2 = plt.bar(
        X + 0.20, data[1], color=colors["BlinkDB_10k"], width=width, alpha=alpha['3'])
    p3 = plt.bar(
        X + 0.40, data[2], color=colors["DBEst_100k"], width=width, alpha=alpha['4'])
    p4 = plt.bar(
        X + 0.60, data[3], color=colors["BlinkDB_100k"], width=width, alpha=alpha['6'])

    plt.legend((p1[0], p2[0], p3[0], p4[0]),
               ('DBEst_10k', 'DBEst_10k_XGBoost', 'DBEst_100k', 'DBEst_100k_XGBoost'), loc='uper left', prop={'size': 16})

    plt.xticks(X + 1.5 * width, ("COUNT", 'SUM', 'AVG', 'OVERALL'))
    ax.set_ylabel("Response Time (s)")
    ax.set_yscale('log')
    formatter = FuncFormatter(to_percent)
    # ax.yaxis.set_major_formatter(formatter)
    plt.subplots_adjust(bottom=0.08)
    plt.subplots_adjust(left=0.20)

    plt.show()


def plt_ccpp_multi_cp_training_time_xgboost():
    plt.rcParams.update({'font.size': 12})
    width = 0.30
    data = [
        [4468.49, 4506],  # , 0.0486],
        [11.9,  70.5],  # , 0.0335],
        [2.7,  15.9]
    ]

    X = np.arange(2)

    fig, ax = plt.subplots()

    p1 = plt.bar(
        X + 0.00, data[0], color=colors["orange"], width=width, alpha=alpha['2'])
    p2 = plt.bar(X + 0.00, data[1], color=colors["red"],
                 width=width, bottom=data[0], alpha=alpha['3'])


    p3 = plt.bar(
        X + 0.30, data[0], color=colors["BlinkDB_10k"], width=width, alpha=alpha['4'])
    p4 = plt.bar(
        X + 0.30, data[2], color=colors["BlinkDB_100k"], width=width, bottom=data[0], alpha=alpha['6'])

    plt.legend((p1[0], p2[0], p3[0], p4[0]),
               ('DBEst Sampling', 'DBEst Training', 'DBEst_XGBoost Sampling', 'DBEst_XGBoost Training'), loc='upper left', prop={'size': 16})

    plt.xticks(X + 0.5 * width, ("10k", '100k', 'AVG', 'OVERALL'))
    ax.set_ylabel("Total Training Time (s)")
    # ax.set_yscale('log')
    formatter = FuncFormatter(to_percent)
    # ax.yaxis.set_major_formatter(formatter)
    plt.subplots_adjust(bottom=0.09)
    plt.subplots_adjust(left=0.23)
    plt.ylim(4400, 4700)

    plt.show()


def plt_ccpp_multi_cp_memory_usage_xgboost():
    plt.rcParams.update({'font.size': 12})
    width = 0.30
    data = [
        [0.333, 2.4156],  # , 0.0486],
        [0.2056,  1.956],  # , 0.0335],
    ]

    X = np.arange(2)

    fig, ax = plt.subplots()

    p1 = plt.bar(
        X + 0.00, data[0], color=colors["DBEst_10k"], width=width, alpha=alpha['2'])
    p2 = plt.bar(
        X + width, data[1], color=colors["BlinkDB_10k"], width=width, alpha=alpha['6'])
    # p3 = plt.bar(X + 0.30, data[2], color=colors["BlinkDB_10k"], width=width)

    plt.legend((p1[0], p2[0]),
               ('DBEst', 'DBEst_XGBoost', 'BlinkDB Sampling', 'BlinkDB_100k'), loc='center left', prop={'size': 18})

    plt.xticks(X + 0.5 * width, ("10k", '100k', 'AVG', 'OVERALL'))
    ax.set_ylabel("Space Overhead (MB)")
    ax.set_xlabel("Sample Size")
    # ax.set_yscale('log')
    formatter = FuncFormatter(to_percent)
    # ax.yaxis.set_major_formatter(formatter)
    plt.subplots_adjust(bottom=0.16)
    plt.subplots_adjust(left=0.18)

    plt.show()



#--------------------------------------------------------------------
# Group by  501 groups
#--------------------------------------------------------------------
def plt_group_by_relative_error():
    plt.rcParams.update({'font.size': 22})
    width = 0.20
    data = [
        [0.0670,  0.0672,  0.0161,  0.0501],  # , 0.0486],
        [0.0389,  0.0421,  0.0169,  0.0326],  # , 0.0335],
    ]

    X = np.arange(4)

    fig, ax = plt.subplots()

    p1 = plt.bar(
        X + 0.00, data[1], color=colors["DBEst_10k"], width=width, alpha=alpha['2'])
    p2 = plt.bar(
        X + 0.20, data[0], color=colors["BlinkDB_10k"], width=width, alpha=alpha['6'])
    # p3 = plt.bar(X + 0.40, data[2], color=colors["DBEst_100k"], width=width)
    # p4 = plt.bar(X + 0.60, data[3], color=colors["BlinkDB_100k"], width=width)

    plt.legend((p1[0], p2[0]),
               ('DBEst', 'BlinkDB', 'DBEst_100k', 'BlinkDB_100k'), loc='1')

    plt.xticks(X + 0.5 * width, ("COUNT", 'SUM', 'AVG', 'OVERALL'))
    ax.set_ylabel("Relative Error (%)")
    # ax.set_yscale('log')
    formatter = FuncFormatter(to_percent)
    ax.yaxis.set_major_formatter(formatter)
    plt.subplots_adjust(bottom=0.10)
    plt.subplots_adjust(left=0.21)
    # plt.subplots_adjust(left=0.23)

    plt.show()
def plt_group_by_relative_error_verdict():
    plt.rcParams.update({'font.size': 22})
    width = 0.20
    # data = [
    #     [0.0670,  0.0672,  0.0161,  0.0501],  # , 0.0486],
    #     [0.0389,  0.0421,  0.0169,  0.0326],  # , 0.0335],
    # ]

    data = [
        [0.05,   0.058425871, 0.021159024, 0.044343787], 
        [0.16,   0.163163671, 0.036915332, 0.120475894], 
    ]



    X = np.arange(4)

    fig, ax = plt.subplots()

    p1 = plt.bar(
        X + 0.00, data[0], color=colors["DBEst_10k"], width=width, alpha=alpha['2'])
    p2 = plt.bar(
        X + 0.20, data[1], color=colors["BlinkDB_10k"], width=width, alpha=alpha['6'])
    # p3 = plt.bar(X + 0.40, data[2], color=colors["DBEst_100k"], width=width)
    # p4 = plt.bar(X + 0.60, data[3], color=colors["BlinkDB_100k"], width=width)

    plt.legend((p1[0], p2[0]),
               ('DBEst', 'VerdictDB', 'DBEst_100k', 'BlinkDB_100k'), loc='1')

    plt.xticks(X + 0.5 * width, ("COUNT", 'SUM', 'AVG', 'OVERALL'))
    ax.set_ylabel("Relative Error (%)")
    # ax.set_yscale('log')
    formatter = FuncFormatter(to_percent)
    ax.yaxis.set_major_formatter(formatter)
    plt.subplots_adjust(bottom=0.10)
    plt.subplots_adjust(left=0.24)
    # plt.subplots_adjust(left=0.23)

    plt.show()


def plt_group_by_response_time():
    plt.rcParams.update({'font.size': 22})
    width = 0.30
    data = [
        [205.31, 209.30,  214.89,  209.83],  # , 0.0486],
        [8.90, 23.10,  29.90,  20.63],  # , 0.0335],
    ]

    X = np.arange(4)

    fig, ax = plt.subplots()

    p1 = plt.bar(
        X + 0.00, data[1], color=colors["DBEst_10k"], width=width, alpha=alpha['2'])
    p2 = plt.bar(
        X + width, data[0], color=colors["BlinkDB_10k"], width=width, alpha=alpha['6'])
    # p3 = plt.bar(X + 0.40, data[2], color=colors["DBEst_100k"], width=width)
    # p4 = plt.bar(X + 0.60, data[3], color=colors["BlinkDB_100k"], width=width)

    plt.legend((p1[0], p2[0]),
               ('DBEst', 'BlinkDB', 'DBEst_100k', 'BlinkDB_100k'), loc='center left')

    plt.xticks(X + 0.5 * width, ("COUNT", 'SUM', 'AVG', 'OVERALL'))
    ax.set_ylabel("Response Time (s)")
    ax.set_yscale('log')
    formatter = FuncFormatter(to_percent)
    # ax.yaxis.set_major_formatter(formatter)
    plt.subplots_adjust(bottom=0.10)
    plt.subplots_adjust(left=0.18)

    plt.show()
def plt_group_by_response_time_verdict():
    plt.rcParams.update({'font.size': 22})
    width = 0.30
    data = [
        [205.31, 209.30,  214.89,  209.83],  # , 0.0486],
        [8.90, 23.10,  29.90,  20.63],  # , 0.0335],
    ]

    data = [
        [0.90,    1.32       , 1.5       ,  1.24],  # , 0.0486],
        [1.16,    0.700424022, 0.599106285, 0.820077781],  # , 0.0335],
    ]



    X = np.arange(4)

    fig, ax = plt.subplots()

    p1 = plt.bar(
        X + 0.00, data[0], color=colors["DBEst_10k"], width=width, alpha=alpha['2'])
    p2 = plt.bar(
        X + width, data[1], color=colors["BlinkDB_10k"], width=width, alpha=alpha['6'])
    # p3 = plt.bar(X + 0.40, data[2], color=colors["DBEst_100k"], width=width)
    # p4 = plt.bar(X + 0.60, data[3], color=colors["BlinkDB_100k"], width=width)

    plt.legend((p1[0], p2[0]),
               ('DBEst', 'VerdictDB', 'DBEst_100k', 'BlinkDB_100k'), loc='lower left')

    plt.xticks(X + 0.5 * width, ("COUNT", 'SUM', 'AVG', 'OVERALL'))
    ax.set_ylabel("Response Time (s)")
    # ax.set_yscale('log')
    # formatter = FuncFormatter(to_percent)
    # ax.yaxis.set_major_formatter(formatter)
    plt.subplots_adjust(bottom=0.10)
    plt.subplots_adjust(left=0.18)

    plt.show()


def plt_group_by_training_time():
    plt.rcParams.update({'font.size': 22})
    width = 0.40
    data = [
        [1525.3, 0],  # , 0.0486],
        [502, 0],  # , 0.0335],
        [2405.467, 0]
    ]

    X = np.arange(2)

    fig, ax = plt.subplots()

    p1 = plt.bar(
        X + 0.00, data[0], color=colors["orange"], width=width, alpha=alpha['2'])
    p2 = plt.bar(X + 0, data[1], color=colors["red"],
                 width=width, bottom=data[0], alpha=alpha['4'])
    p3 = plt.bar(X + 1, data[2], color=colors["BlinkDB_10k"],
                 width=width, alpha=alpha['6'])
    p1[1].set_color(colors["BlinkDB_10k"])

    plt.legend((p1[0], p2[0], p3[0]),
               ('DBEst Sampling', 'DBEst training', 'BlinkDB Sampling', 'BlinkDB_100k'), loc='lower center', prop={'size': 18})

    plt.xticks(X, ("DBEst", 'BlinkDB', 'AVG', 'OVERALL'))
    ax.set_ylabel("Total Training Time (s)")
    # ax.set_yscale('log')
    formatter = FuncFormatter(to_percent)
    # ax.yaxis.set_major_formatter(formatter)
    plt.subplots_adjust(bottom=0.09)
    plt.subplots_adjust(left=0.23)
    plt.xlim(-0.5, 1.5)

    plt.show()

def plt_group_by_training_time_verdict():
    plt.rcParams.update({'font.size': 22})
    width = 0.40
    data = [
        [1525.3,   0],  # , 0.0486],
        [502,      0],  # , 0.0335],
        [2405.467, 0]
    ]

    data = [
        [68,   0],  # , 0.0486],
        [43.6,      0],  # , 0.0335],
        [120, 0]
    ]

    X = np.arange(2)

    fig, ax = plt.subplots()

    p1 = plt.bar(
        X + 0.00, data[0], color=colors["orange"], width=width, alpha=alpha['2'])
    p2 = plt.bar(X + 0, data[1], color=colors["red"],
                 width=width, bottom=data[0], alpha=alpha['4'])
    p3 = plt.bar(X + 1, data[2], color=colors["BlinkDB_10k"],
                 width=width, alpha=alpha['6'])
    p1[1].set_color(colors["BlinkDB_10k"])

    plt.legend((p1[0], p2[0], p3[0]),
               ('DBEst Sampling', 'DBEst Training', 'VerdictDB Sampling', 'BlinkDB_100k'), loc='lower center', prop={'size': 18})

    plt.xticks(X, ("DBEst", 'VerdictDB', 'AVG', 'OVERALL'))
    ax.set_ylabel("Total Training Time (s)")
    # ax.set_yscale('log')
    formatter = FuncFormatter(to_percent)
    # ax.yaxis.set_major_formatter(formatter)
    plt.subplots_adjust(bottom=0.09)
    plt.subplots_adjust(left=0.23)
    plt.xlim(-0.5, 1.5)

    plt.show()


def plt_group_by_memory_usage():
    plt.rcParams.update({'font.size': 22})
    width = 0.40
    data = [
        [145, 166.8],  # , 0.0486],
        # [66.4,  102.4 ],#, 0.0335],
    ]

    X = np.arange(2)

    fig, ax = plt.subplots()

    p1 = plt.bar(X, data[0], color=colors["DBEst_10k"], width=width)
    # p2 = plt.bar(X + width, data[1], color=colors["BlinkDB_10k"], width=width)
    # p3 = plt.bar(X + 0.30, data[2], color=colors["BlinkDB_10k"], width=width)

    # plt.legend((p1[0]),
    #     ('DBEst', 'BlinkDB','BlinkDB Sampling','BlinkDB_100k'), loc='center', prop={'size': 18})

    # p1[0].set_color('r')
    p1[1].set_color(colors["BlinkDB_10k"])

    plt.xticks(X, ("DBEst", 'BlinkDB', 'AVG', 'OVERALL'))
    ax.set_ylabel("Memory Usage (MB)")
    # ax.set_xlabel("Sample Size")
    # ax.set_yscale('log')
    formatter = FuncFormatter(to_percent)
    # ax.yaxis.set_major_formatter(formatter)
    plt.subplots_adjust(bottom=0.10)
    plt.subplots_adjust(left=0.18)

    plt.show()
def plt_group_by_memory_usage_verdict():
    plt.rcParams.update({'font.size': 22})
    width = 0.40
    data = [
        [11.15, 67],  # , 0.0486],
        # [66.4,  102.4 ],#, 0.0335],
    ]

    X = np.arange(2)

    fig, ax = plt.subplots()

    p1 = plt.bar(X, data[0], color=colors["DBEst_10k"], width=width)
    # p2 = plt.bar(X + width, data[1], color=colors["BlinkDB_10k"], width=width)
    # p3 = plt.bar(X + 0.30, data[2], color=colors["BlinkDB_10k"], width=width)

    # plt.legend((p1[0]),
    #     ('DBEst', 'BlinkDB','BlinkDB Sampling','BlinkDB_100k'), loc='center', prop={'size': 18})

    # p1[0].set_color('r')
    p1[1].set_color(colors["BlinkDB_10k"])

    plt.xticks(X, ("DBEst", 'VerdictDB', 'AVG', 'OVERALL'))
    ax.set_ylabel("Space Overhead (MB)")
    # ax.set_xlabel("Sample Size")
    # ax.set_yscale('log')
    formatter = FuncFormatter(to_percent)
    # ax.yaxis.set_major_formatter(formatter)
    plt.subplots_adjust(bottom=0.10)
    plt.subplots_adjust(left=0.16)

    plt.show()


#--------------------------------------------------------------------
# Group by  8 groups
#--------------------------------------------------------------------
def plt_group8_by_relative_error():
    plt.rcParams.update({'font.size': 22})
    width = 0.20
    data = [
        [0.0717,  0.0756, 0.0117, 0.0530],  # , 0.0486],
        [0.0377,  0.0354, 0.0195, 0.0309],  # , 0.0335],
        [0.0679,  0.0668, 0.0048, 0.0465],  # , 0.0486],
        [0.0273,  0.0240, 0.0062, 0.0192],  # , 0.0335],
    ]

    X = np.arange(4)

    fig, ax = plt.subplots()

    p1 = plt.bar(
        X + 0.00, data[1], color=colors["DBEst_10k"], width=width, alpha=alpha['2'])
    p2 = plt.bar(
        X + 0.20, data[0], color=colors["BlinkDB_10k"], width=width, alpha=alpha['3'])
    p3 = plt.bar(
        X + 0.40, data[3], color=colors["DBEst_100k"], width=width, alpha=alpha['4'])
    p4 = plt.bar(
        X + 0.60, data[2], color=colors["BlinkDB_100k"], width=width, alpha=alpha['6'])

    plt.legend((p1[0], p2[0], p3[0], p4[0]),
               ('DBEst_100k', 'BlinkDB_100k', 'DBEst_1m', 'BlinkDB_1m'), loc='1', prop={'size': 18})

    plt.xticks(X + 1.5 * width, ("COUNT", 'SUM', 'AVG', 'OVERALL'))
    ax.set_ylabel("Relative Error (%)")
    # ax.set_yscale('log')
    formatter = FuncFormatter(to_percent)
    ax.yaxis.set_major_formatter(formatter)
    plt.subplots_adjust(bottom=0.08)
    plt.subplots_adjust(left=0.20)

    plt.show()
    fig.savefig(
        "/home/u1796377/Desktop/figures/group8_by_reltive_error.pdf", bbox_inches='tight')


def plt_group8_by_response_time():
    plt.rcParams.update({'font.size': 22})
    width = 0.20
    data = [
        [74.9153, 76.2767, 74.4477],  # , 0.0486],
        [0.2283, 0.4939, 0.6485],  # , 0.0335],
        [75.4965, 76.1026, 75.1319],  # , 0.0486],
        [1.7242, 1.9514, 3.5275],  # , 0.0335],
    ]

    X = np.arange(3)

    fig, ax = plt.subplots()

    p1 = plt.bar(
        X + 0.00, data[1], color=colors["DBEst_10k"], width=width, alpha=alpha['2'])
    p2 = plt.bar(
        X + width, data[0], color=colors["BlinkDB_10k"], width=width, alpha=alpha['3'])
    p3 = plt.bar(
        X + 2 * width, data[3], color=colors["DBEst_100k"], width=width, alpha=alpha['4'])
    p4 = plt.bar(
        X + 3 * width, data[2], color=colors["BlinkDB_100k"], width=width, alpha=alpha['6'])

    plt.legend((p1[0], p2[0], p3[0], p4[0]),
               ('DBEst_100k', 'BlinkDB_100k', 'DBEst_1m', 'BlinkDB_1m'), loc='upper center')

    plt.xticks(X + 1.5 * width, ("COUNT", 'SUM', 'AVG', 'OVERALL'))
    ax.set_ylabel("Response Time (s)")
    ax.set_yscale('log')
    formatter = FuncFormatter(to_percent)
    # ax.yaxis.set_major_formatter(formatter)
    plt.subplots_adjust(bottom=0.08)
    plt.subplots_adjust(left=0.16)

    plt.show()
    fig.savefig(
        "/home/u1796377/Desktop/figures/group8_by_response_time.pdf", bbox_inches='tight')


def plt_group8_by_training_time():
    plt.rcParams.update({'font.size': 22})
    width = 0.30
    data = [
        [434.9009142, 434.6685901],  # , 0.0486],
        [27, 192.9],  # , 0.0335],
        [2108, 2152]
    ]

    X = np.arange(2)

    fig, ax = plt.subplots()

    p1 = plt.bar(
        X + 0.00, data[0], color=colors["orange"], width=width, alpha=alpha["1"])
    p2 = plt.bar(X + 0, data[1], color=colors["red"],
                 width=width, bottom=data[0], alpha=alpha["3"])
    p3 = plt.bar(
        X + width, data[2], color=colors["BlinkDB_10k"], width=width, alpha=alpha["5"])
    # p1[1].set_color(colors["BlinkDB_10k"])

    plt.legend((p1[0], p2[0], p3[0]),
               ('DBEst Sampling', 'DBEst training', 'BlinkDB Sampling', 'BlinkDB_100k'), loc='upper left', prop={'size': 18})

    plt.xticks(X + 0.5 * width, ("DBEst", 'BlinkDB', 'AVG', 'OVERALL'))
    ax.set_ylabel("Total Training Time (s)")
    # ax.set_yscale('log')
    formatter = FuncFormatter(to_percent)
    # ax.yaxis.set_major_formatter(formatter)
    plt.subplots_adjust(bottom=0.09)
    plt.subplots_adjust(left=0.21)
    # plt.xlim(-0.5,1.5)

    plt.show()
    fig.savefig(
        "/home/u1796377/Desktop/figures/group8_by_training_time.pdf", bbox_inches='tight')


def plt_group8_by_memory_usage():
    plt.rcParams.update({'font.size': 22})
    width = 0.30
    data = [
        [3.0188, 17.488],  # , 0.0486],
        [13,  27],  # , 0.0335],
    ]

    X = np.arange(2)

    fig, ax = plt.subplots()

    p1 = plt.bar(X, data[0], color=colors["DBEst_10k"],
                 width=width, alpha=alpha["3"])
    p2 = plt.bar(
        X + width, data[1], color=colors["BlinkDB_10k"], width=width, alpha=alpha["6"])
    # p3 = plt.bar(X + 0.30, data[2], color=colors["BlinkDB_10k"], width=width)

    plt.legend((p1[0], p2[0]),
               ('DBEst', 'BlinkDB', 'BlinkDB Sampling', 'BlinkDB_100k'), loc='upper left', prop={'size': 18})

    # p1[0].set_color('r')
    # p1[1].set_color(colors["BlinkDB_10k"])

    plt.xticks(X + 0.5 * width, ("100k", '1m', 'AVG', 'OVERALL'))
    ax.set_ylabel("Memory Usage (MB)")
    # ax.set_xlabel("Sample Size")
    # ax.set_yscale('log')
    formatter = FuncFormatter(to_percent)
    # ax.yaxis.set_major_formatter(formatter)
    plt.subplots_adjust(bottom=0.10)
    plt.subplots_adjust(left=0.15)

    plt.show()
    fig.savefig(
        "/home/u1796377/Desktop/figures/group8_by_memory_usage.pdf", bbox_inches='tight')


def plt_group_by_hist():
    plt.rcParams.update({'font.size': 12})
    x = [
        0.008462985, 0.000649833, 0.010881737, 0.019874081, 0.039346075, 0.003571377, 0.026939946,
        0.021393266, 0.005201863, 0.015298297, 0.018229333, 0.008637057, 0.014436533, 0.027777002,
        0.034631676, 0.012341524, 0.0258706, 0.006000121, 0.003729624, 0.044551047, 0.003648729,
        0.018700766, 0.000783815, 0.020980242, 0.014418494, 0.010292997, 0.00812975, 0.020275727,
        0.028618814, 0.010201438, 0.021742944, 0.009251167, 0.001059743, 0.015501865, 0.022066053,
        0.002559358, 0.013786249, 0.013611123, 0.020307255, 0.007548499, 0.006023911, 0.012341901,
        0.019598433, 0.035337897, 0.015755378, 0.030308311, 0.042099321, 0.035901669, 0.014647428,
        0.002699447, 0.012202254, 0.018638841,
        0.000278544, 0.012019519, 0.030165266, 0.003467017, 0.033242599, 0.04112212, 0.008085862,
        0.016743042, 0.01284619, 0.029190805, 0.007815511, 0.007233848, 0.030781278, 0.003010079,
        0.004480336, 0.015579436, 0.033798304, 0.003046802, 0.008665101, 0.047337198, 0.013837248,
        0.013763259, 0.001069675, 0.004265096, 0.012416027, 0.006200573, 0.008460815, 0.028962004,
        0.011069929, 0.01960857, 0.022572247, 0.036914386, 0.140734388, 0.005041994, 0.000984966,
        0.002316471, 0.004212788, 0.007712929, 0.008466944, 0.022988696, 0.023860911, 0.035828249,
        0.005466769, 0.00567563, 0.01866136, 0.012834972, 0.011048793, 0.015736116, 0.003991098,
        0.022842372, 0.001398384,
        0.031689339, 0.002854207, 0.015328667, 7.19238E-05, 0.023863784, 0.035296671, 0.021433148,
        0.029587743, 0.014869902, 0.00920762, 0.008948738, 0.01442898, 0.019455567, 0.021161534,
        0.00060057, 0.017514734, 0.011161216, 0.048464679, 0.022985382, 0.013120304, 0.014141606,
        0.004482663, 0.012054031, 0.008919319, 0.023385979, 0.00728777, 0.017716817, 0.014284039,
        0.008298422, 0.003414605, 0.017275317, 0.002040174, 0.013601237, 0.013660302, 0.048360068,
        0.001754731, 0.02916015, 0.025669333, 0.010524094, 0.038962487, 0.010386024, 0.009859369,
        0.006291422, 0.017239173, 0.00743845, 0.019254461, 0.027995475, 0.008295051, 0.037301053,
        0.018901212, 0.064678402, 0.002804271,
        0.015545777, 0.009038624, 0.026740564, 0.020596602, 0.031882421, 0.018980904, 0.00440758,
        0.014419872, 0.031117005, 0.021881356, 0.005967287, 0.048905349, 0.012778648, 0.014950126,
        0.002952227, 0.008805702, 0.055245, 0.00063001, 0.009675911, 0.00368954, 0.019531477,
        0.026858709, 0.00709812, 0.00515008, 0.043121636, 0.018709218, 0.002440149, 0.017062117,
        0.041490604, 0.034186104, 0.007607038, 0.017325633, 0.024473606, 0.004843587, 0.001932604,
        0.045011196, 0.010890094, 0.007983287, 0.011281576, 0.012066398, 0.008177211, 0.023393661,
        0.016762132, 0.002815898, 0.000439521, 0.027129103, 0.035638241, 0.017242052, 0.003307042,
        0.043929802, 0.020596882, 0.00400651,
        0.016168377, 0.021507634, 0.024676393, 0.006862053, 0.034160401, 0.025645268, 0.026683376,
        0.005831263, 0.008000727, 0.024394465, 0.01174157, 0.033649857, 0.031705911, 0.005894599,
        0.011419122, 0.015361558, 0.040308435, 0.023248812, 0.00517292, 0.00708495, 0.002055437,
        0.039751895, 0.0244555, 0.020943844, 0.020885427, 0.011524265, 0.005229043, 0.001262883,
        0.002639129, 0.001052436, 0.0246822, 0.012980881, 0.030692436, 0.016786055, 0.020879873,
        0.010571628, 0.007999897, 0.021040711, 0.040436769, 0.015943549, 0.016520651, 0.024286203,
        0.010946921, 0.007354054, 0.015290895, 0.010784894, 0.018106004, 0.021681473, 0.003838333,
        0.013646924, 0.04199949, 0.009302462,
        0.02039623, 0.024030158, 0.020051635, 0.014535193, 0.064783374, 0.000820819, 0.018647539,
        0.016595631, 0.00749719, 0.002655991, 0.025815134, 0.014934251, 0.138437057, 0.014018613,
        0.023951689, 0.000428988, 0.017361018, 0.006963992, 0.001618278, 0.008085414, 0.042242572,
        0.012145611, 0.005279952, 0.01083989, 0.013909057, 0.01490347, 0.040963137, 0.014044257,
        0.007108637, 0.012698641, 0.027197087, 0.021429206, 0.014025829, 0.000499166, 0.006408685,
        0.006684109, 0.024340515, 0.019492902, 0.029473133, 0.007052602, 0.008107923, 0.010432857,
        0.035100458, 0.003525452, 0.017013558, 0.095511724, 0.000140889, 0.010629875, 0.007096889,
        0.015265209, 0.009109113, 0.002062698, 0.022976335, 0.012562032, 0.022386979, 0.000100013,
        0.015094217, 0.045341189,
        0.020319328, 0.009802289, 0.043094066, 0.000139667, 0.012582496, 0.016295296, 0.055495367,
        0.006465074, 0.029799432, 0.036719329, 0.008677339, 0.070524196, 0.019384782, 0.027033504,
        0.003040137, 0.026284848, 0.019005781, 0.022906252, 0.016043265, 0.006526817, 0.008363289,
        0.044456629, 0.010615164, 0.03987122, 0.022463093, 0.015420188, 0.02722384, 0.020813133,
        0.004083479, 0.033416687, 0.058048936, 0.026698091, 0.026213007, 0.003799286, 0.028285901,
        0.028938235, 0.02522193, 0.037802796, 0.000308768, 0.006372713, 0.013302656, 0.001937565,
        0.00269786, 0.026586087, 0.02378528, 0.009720781, 0.014647232, 0.034289353, 0.00494238,
        0.043737264, 0.027960453,
        0.022771529, 0.005836506, 0.038219828, 0.014241725, 0.001559216, 0.001716119, 0.026019934,
        0.024741338, 0.007161639, 0.016916403, 0.020066875, 0.014563596, 0.02735833, 0.038509643,
        0.012168468, 0.012811839, 0.011922682, 0.039554001, 0.05620724, 0.030288062, 0.042515491,
        0.008304207, 0.029185858, 0.002333962, 0.030116382, 0.014067018, 0.008570436, 0.017576213,
        0.020510671, 0.030715175, 0.028348787, 0.034239241, 0.008891356, 0.00673758, 0.028180994,
        0.025906799, 0.003642136, 0.054744327, 0.00464959, 0.015256509, 0.022382895, 0.003317725,
        0.006179115, 0.060658785, 0.015812781, 0.018725003, 0.025708213, 0.001195295, 0.008258188,
        0.01038488, 0.039250142,
        0.020464175, 0.015446059, 0.029179533, 0.002964981, 0.024224873, 0.003144933, 0.009764459,
        0.031880663, 0.003747997, 0.027831028, 0.019627863, 0.000331274, 0.015145269, 0.009575039,
        0.026671031, 0.021321967, 0.004445517, 0.039623535, 0.002268241, 0.012206298, 0.025270309,
        0.027226665, 0.013948173, 0.021159928, 0.003814335, 0.022115669, 0.020186873, 0.010851511,
        0.029447977, 0.04111507, 0.001452279, 0.025236788, 7.30391E-05, 0.025714813, 0.014918101,
        0.019399826, 0.042377721, 0.026432244, 0.014128886, 0.02073962, 0.010547859, 0.025291583,
        0.005898149, 0.004274129,
        0.027498465, 0.006496447, 0.007466645, 0.008691038, 0.037911743, 0.003117525, 0.010598016,
        0.011108073, 0.041004715, 0.008838573, 0.006342802, 0.017424345, 0.008303449, 0.001522786,
        0.035384576, 0.041733229, 0.012235548, 0.037297234, 0.02156264, 0.024660309, 0.001169242,
        0.021732707, 0.048612164, 0.014658683, 0.014144955, 0.036605784, 0.004461146, 0.0022407,
        0.022810741, 0.007734431, 0.00789999, 0.020910912, 0.00386069, 0.00232009, 0.038652552,
        0.027562495, 0.026052591, 0.00354465, ]
    fig, ax = plt.subplots()
    plt.hist(x, 501, normed=1, cumulative=True,
             color=colors["BlinkDB_10k"], alpha=0.8)
    plt.xlim(0, 0.1)
    plt.ylim(0, 1)
    formatter = FuncFormatter(to_percent)
    ax.xaxis.set_major_formatter(formatter)
    ax.yaxis.set_major_formatter(formatter)
    plt.xlabel("Relative Error (%)")
    plt.ylabel("Cumulative Probability")
    plt.subplots_adjust(bottom=0.12)
    plt.subplots_adjust(left=0.16)
    plt.show()
    fig.savefig(
        "/home/u1796377/Desktop/figures/group_by_histgram.pdf", bbox_inches='tight')


def plt_group8_by_detail_error():
    plt.rcParams.update({'font.size': 12})
    width = 0.20
    data = [
        [0.0278,  0.0060,  0.0393,  0.0158,  0.0183,
            0.0167, 0.0269, 0.0075],  # , 0.0486],
        [0.0705,  0.0143,  0.0189,  0.0440,  0.0330,
            0.0518, 0.0414, 0.0449],  # , 0.0335],
    ]

    X = np.arange(8)

    fig, ax = plt.subplots()

    p1 = plt.bar(
        X + 0.00, data[0], color=colors["DBEst_10k"], width=width, alpha=alpha["2"])
    p2 = plt.bar(
        X + 0.20, data[1], color=colors["BlinkDB_10k"], width=width, alpha=alpha["6"])
    # p3 = plt.bar(X + 0.40, data[2], color=colors["DBEst_100k"], width=width)
    # p4 = plt.bar(X + 0.60, data[3], color=colors["BlinkDB_100k"], width=width)

    plt.legend((p1[0], p2[0]),
               ('100k', '1m', 'DBEst_100k', 'BlinkDB_100k'), loc='1')

    plt.xticks(X + 0.5 * width, ("1", '2', '3', '4', "5", '6', '7', '8'))
    ax.set_ylabel("Relative Error (%)")
    ax.set_xlabel("Group By ID")
    # ax.set_yscale('log')
    formatter = FuncFormatter(to_percent)
    ax.yaxis.set_major_formatter(formatter)
    plt.subplots_adjust(bottom=0.10)
    plt.subplots_adjust(left=0.13)

    plt.show()
    fig.savefig(
        "/home/u1796377/Desktop/figures/group8_by_detail_error.pdf", bbox_inches='tight')


def min_max():
    plt.rcParams.update({'font.size': 12})
    width = 0.20
    data = [
        [0.3372,  0.2203],  # , 0.0486],
        [0.3021,  0.2040],  # , 0.0335],
        [0.2952,  0.1972],  # , 0.0486],
        [0.2874,  0.1930],  # , 0.0335],
    ]

    X = np.arange(2)

    fig, ax = plt.subplots()

    p1 = plt.bar(
        X + 0.00, data[0], color=colors["BlinkDB_1k"], width=width, alpha=alpha['2'])
    p2 = plt.bar(
        X + 0.20, data[1], color=colors["BlinkDB_10k"], width=width, alpha=alpha['3'])
    p3 = plt.bar(
        X + 0.40, data[2], color=colors["BlinkDB_100k"], width=width, alpha=alpha['4'])
    p4 = plt.bar(
        X + 0.60, data[3], color=colors["BlinkDB_1m"], width=width, alpha=alpha['6'])

    plt.legend((p1[0], p2[0], p3[0], p4[0]),
               ('no CI', 'CI-95%', 'CI-99%', 'CI-99.9%'), loc='1')

    plt.xticks(X + 1.5 * width, ("MIN", 'MAX', 'AVG', 'OVERALL'))
    ax.set_ylabel("Relative Error (%)")
    # ax.set_yscale('log')
    formatter = FuncFormatter(to_percent)
    ax.yaxis.set_major_formatter(formatter)
    plt.subplots_adjust(bottom=0.06)
    plt.subplots_adjust(left=0.14)

    plt.show()
    fig.savefig("/home/u1796377/Desktop/figures/min_max.pdf",
                bbox_inches='tight')


def plt_tpcds_multi_cp_relative_error_xgboost():
    plt.rcParams.update({'font.size': 12})
    width = 0.12
    data = [
        [0.06496  ,  0.02789 ,   0.03932  ,   0.04406 ],  # , 0.0486],
        [0.06496  ,  0.05114 ,   0.02888  ,   0.04832 ],  # , 0.0335],
        [0.03171  ,  0.02203 ,   0.01043  ,   0.02139 ],  # , 0.0182],
        [0.03171  ,  0.03039 ,   0.00966  ,   0.02392 ],  # , 0.0212]
        [0.03182  ,  0.00333 ,   0.00323  ,   0.01279 ],
        [0.03182  ,  0.00624 ,   0.00324  ,   0.01376 ],
    ]
  

 
 

    X = np.arange(4)

    fig, ax = plt.subplots()

    p1 = plt.bar(
        X + 0.00, data[0], color=colors["DBEst_10k"], width=width, alpha=0.15)
    p2 = plt.bar(
        X + 1*width, data[1], color=colors["BlinkDB_10k"], width=width, alpha=alpha['2'])
    p3 = plt.bar(
        X + 2*width, data[2], color=colors["DBEst_100k"], width=width, alpha=alpha['3'])
    p4 = plt.bar(
        X + 3*width, data[3], color=colors["BlinkDB_100k"], width=width, alpha=alpha['4'])
    p5 = plt.bar(
        X + 4*width, data[4], color=colors["DBEst_1m"], width=width, alpha=alpha['5'])
    p6 = plt.bar(
        X + 5*width, data[5], color=colors["BlinkDB_1m"], width=width, alpha=alpha['6'])

    plt.legend((p1[0], p2[0], p3[0], p4[0], p5[0], p6[0]),
               ('DBEst_10k', 'DBEst_10k_XGBoost', 'DBEst_100k', 'DBEst_100k_XGBoost','DBEst_1m', 'DBEst_1m_XGBoost'), loc='1')

    plt.xticks(X + 2.5 * width, ("COUNT", 'SUM', 'AVG', 'OVERALL'))
    ax.set_ylabel("Relative Error (%)")
    # ax.set_yscale('log')
    formatter = FuncFormatter(to_percent)
    ax.yaxis.set_major_formatter(formatter)
    plt.subplots_adjust(bottom=0.07)
    # plt.subplots_adjust(left=0.23)

    plt.show()


def plt_tpcds_multi_cp_response_time_xgboost():
    plt.rcParams.update({'font.size': 12})
    width = 0.12
    data = [
        [0.01512  ,   0.58804 ,   0.43552  ,   0.34623 ],  # , 0.0486],
        [0.01345  ,   0.03817 ,   0.04465  ,   0.03209 ],  # , 0.0335],
        [0.08485  ,   2.55147 ,   2.59192  ,   1.74275 ],  # , 0.0182],
        [0.09597  ,   0.24926 ,   0.31481  ,   0.22001 ],  # , 0.0212]
        [1.54524  ,   6.14746 ,   4.53269  ,   4.07513 ],
        [1.75875  ,   9.88013 ,   6.56452  ,   6.06780 ],
    ]







    X = np.arange(4)

    fig, ax = plt.subplots()

    p1 = plt.bar(
        X + 0.00, data[0], color=colors["DBEst_10k"], width=width, alpha=0.15)
    p2 = plt.bar(
        X + 1*width, data[1], color=colors["BlinkDB_10k"], width=width, alpha=alpha['2'])
    p3 = plt.bar(
        X + 2*width, data[2], color=colors["DBEst_100k"], width=width, alpha=alpha['3'])
    p4 = plt.bar(
        X + 3*width, data[3], color=colors["BlinkDB_100k"], width=width, alpha=alpha['4'])
    p5 = plt.bar(
        X + 4*width, data[4], color=colors["DBEst_1m"], width=width, alpha=alpha['5'])
    p6 = plt.bar(
        X + 5*width, data[5], color=colors["BlinkDB_1m"], width=width, alpha=alpha['6'])

    plt.legend((p1[0], p2[0], p3[0], p4[0], p5[0], p6[0]),
               ('DBEst_10k', 'DBEst_10k_XGBoost', 'DBEst_100k', 'DBEst_100k_XGBoost','DBEst_1m', 'DBEst_1m_XGBoost'), loc='1')


    plt.xticks(X + 1.5 * width, ("COUNT", 'SUM', 'AVG', 'OVERALL'))
    ax.set_ylabel("Response Time (s)")
    ax.set_yscale('log')
    formatter = FuncFormatter(to_percent)
    # ax.yaxis.set_major_formatter(formatter)
    plt.subplots_adjust(bottom=0.06)
    plt.show()


def plt_tpcds_multi_cp_training_time_xgboost():
    plt.rcParams.update({'font.size': 22})
    width = 0.30
    data = [
        [2328,  2342],  # , 0.0486],
        [39.8,  278.3],  # , 0.0335],
        [10.6,  68.7]
    ]

    X = np.arange(2)

    fig, ax = plt.subplots()

    p1 = plt.bar(
        X + 0.00, data[0], color=colors["orange"], width=width, alpha=alpha['2'])
    p2 = plt.bar(X + 0.00, data[1], color=colors["red"],
                 width=width, bottom=data[0], alpha=alpha['3'])


    p3 = plt.bar(
        X + 0.30, data[0], color=colors["BlinkDB_10k"], width=width, alpha=alpha['4'])
    p4 = plt.bar(
        X + 0.30, data[2], color=colors["BlinkDB_100k"], width=width, bottom=data[0], alpha=alpha['6'])

    plt.legend((p1[0], p2[0], p3[0], p4[0]),
               ('DBEst Sampling', 'DBEst Training', 'DBEst_XGBoost Sampling', 'DBEst_XGBoost Training'), loc='lower center', prop={'size': 16})

    plt.xticks(X + 0.5 * width, ("10k", '100k', 'AVG', 'OVERALL'))
    ax.set_ylabel("Total Training Time (s)")
    # ax.set_yscale('log')
    formatter = FuncFormatter(to_percent)
    # ax.yaxis.set_major_formatter(formatter)
    plt.subplots_adjust(bottom=0.09)
    plt.subplots_adjust(left=0.23)
    plt.ylim(2000, 2700)

    plt.show()


def plt_tpcds_multi_cp_memory_usage_xgboost():
    plt.rcParams.update({'font.size': 22})
    width = 0.30
    data = [
        [1.552, 9.14],  # , 0.0486],
        [0.233,  1.615],  # , 0.0335],
    ]

    X = np.arange(2)

    fig, ax = plt.subplots()

    p1 = plt.bar(
        X + 0.00, data[0], color=colors["DBEst_10k"], width=width, alpha=alpha['2'])
    p2 = plt.bar(
        X + width, data[1], color=colors["BlinkDB_10k"], width=width, alpha=alpha['6'])
    # p3 = plt.bar(X + 0.30, data[2], color=colors["BlinkDB_10k"], width=width)

    plt.legend((p1[0], p2[0]),
               ('DBEst', 'DBEst_XGBoost', 'BlinkDB Sampling', 'BlinkDB_100k'), loc='center left', prop={'size': 18})

    plt.xticks(X + 0.5 * width, ("10k", '100k', 'AVG', 'OVERALL'))
    ax.set_ylabel("Memory Usage (MB)")
    ax.set_xlabel("Sample Size")
    # ax.set_yscale('log')
    formatter = FuncFormatter(to_percent)
    # ax.yaxis.set_major_formatter(formatter)
    plt.subplots_adjust(bottom=0.16)
    plt.subplots_adjust(left=0.18)

    plt.show()



# def plt_tpcds_multi_cp_training_time_xgboost():
#     plt.rcParams.update({'font.size': 22})
#     width = 0.30
#     data = [
#         [281.5, 286],  # , 0.0486],
#         [39.8,  278.3],  # , 0.0335],
#         [2328,  2342]
#     ]

#     X = np.arange(2)

#     fig, ax = plt.subplots()

#     p1 = plt.bar(X + 0.00, data[0], color=colors["orange"], width=width)
#     p2 = plt.bar(X + 0.00, data[1], color=colors["red"],
#                  width=width, bottom=data[0])
#     p3 = plt.bar(X + 0.30, data[2], color=colors["BlinkDB_10k"], width=width)

#     plt.legend((p1[0], p2[0], p3[0], p4[0]),
#                ('DBEst Sampling', 'DBEst Training', 'DBEst_XGBoost Sampling', 'DBEst_XGBoost Training'), loc='upper left', prop={'size': 16})

#     plt.xticks(X + 0.5 * width, ("10k", '100k', 'AVG', 'OVERALL'))
#     ax.set_ylabel("Total Training Time (s)")
#     # ax.set_yscale('log')
#     formatter = FuncFormatter(to_percent)
#     # ax.yaxis.set_major_formatter(formatter)
#     plt.subplots_adjust(bottom=0.09)
#     plt.subplots_adjust(left=0.23)

#     plt.show()


# def plt_tpcds_multi_cp_memory_usage_xgboost():
#     plt.rcParams.update({'font.size': 22})
#     width = 0.30
#     data = [
#         [5.9959, 22.195],  # , 0.0486],
#         [1024,  1340],  # , 0.0335],
#     ]

#     X = np.arange(2)

#     fig, ax = plt.subplots()

#     p1 = plt.bar(
#         X + 0.00, data[0], color=colors["DBEst_10k"], width=width, alpha=alpha['2'])
#     p2 = plt.bar(
#         X + width, data[1], color=colors["BlinkDB_10k"], width=width, alpha=alpha['6'])
#     # p3 = plt.bar(X + 0.30, data[2], color=colors["BlinkDB_10k"], width=width)

#    plt.legend((p1[0], p2[0]),
#                ('DBEst', 'DBEst_XGBoost', 'BlinkDB Sampling', 'BlinkDB_100k'), loc='center left', prop={'size': 18})

#     plt.xticks(X + 0.5 * width, ("10k", '100k', 'AVG', 'OVERALL'))
#     ax.set_ylabel("Memory Usage (MB)")
#     ax.set_yscale('log')
#     formatter = FuncFormatter(to_percent)
#     # ax.yaxis.set_major_formatter(formatter)
#     plt.subplots_adjust(bottom=0.10)
#     plt.subplots_adjust(left=0.18)

#     plt.show()




def plt_blinkdb_query_range():
    plt.rcParams.update({'font.size': 12})
    width = 0.20
    data = [
        [0.11238 ,    0.11502 ,   0.01018],  # , 0.0486],
        [0.07199 ,    0.07227 ,   0.00375],  # , 0.0335],
        [0.07131 ,    0.07097 ,   0.00181],  # , 0.0182],
        #[0.0628,  0.0707,  0.0069, 0.0468]  # , 0.0212]
    ]

 
 
 



    X = np.arange(3)

    fig, ax = plt.subplots()

    p1 = plt.bar(
        X + 0.00, data[0], color=colors["DBEst_10k"], width=width, alpha=alpha['2'])
    p2 = plt.bar(
        X + 0.20, data[1], color=colors["BlinkDB_10k"], width=width, alpha=alpha['3'])
    p3 = plt.bar(
        X + 0.40, data[2], color=colors["DBEst_100k"], width=width, alpha=alpha['4'])
    # p4 = plt.bar(
    #     X + 0.60, data[3], color=colors["BlinkDB_100k"], width=width, alpha=alpha['6'])

    plt.legend((p1[0], p2[0], p3[0]),
               ('0.1% Query Range', '1.0% Query Range', '10.0% Query Range', 'BlinkDB_100k'), loc='1')

    plt.xticks(X + 1.5 * width, ("COUNT", 'SUM', 'AVG', 'OVERALL'))
    ax.set_ylabel("Relative Error (%)")
    # ax.set_yscale('log')
    formatter = FuncFormatter(to_percent)
    ax.yaxis.set_major_formatter(formatter)
    plt.subplots_adjust(bottom=0.07)
    plt.subplots_adjust(left=0.15)

    plt.show()





def plt_group_by_relative_error_xgboost():
    plt.rcParams.update({'font.size': 22})
    width = 0.20
    data = [
        #[0.0670,  0.0672,  0.0161,  0.0501],  # , 0.0486],
        [0.0389,  0.0421,  0.0169],  # , 0.0335],
        [0.0389,  0.0409,  0.0120]
    ]

    X = np.arange(3)

    fig, ax = plt.subplots()

    p1 = plt.bar(
        X + 0.00, data[0], color=colors["DBEst_10k"], width=width, alpha=alpha['2'])
    p2 = plt.bar(
        X + 0.20, data[1], color=colors["BlinkDB_10k"], width=width, alpha=alpha['6'])
    # p3 = plt.bar(X + 0.40, data[2], color=colors["DBEst_100k"], width=width)
    # p4 = plt.bar(X + 0.60, data[3], color=colors["BlinkDB_100k"], width=width)

    plt.legend((p1[0], p2[0]),
               ('DBEst', 'DBEst_XGBoost', 'DBEst_100k', 'BlinkDB_100k'), loc='lower left')

    plt.xticks(X + 0.5 * width, ("COUNT", 'SUM', 'AVG', 'OVERALL'))
    ax.set_ylabel("Relative Error (%)")
    # ax.set_yscale('log')
    formatter = FuncFormatter(to_percent)
    ax.yaxis.set_major_formatter(formatter)
    plt.subplots_adjust(bottom=0.10)
    plt.subplots_adjust(left=0.21)
    # plt.subplots_adjust(left=0.23)

    plt.show()


def plt_group_by_response_time_xgboost():
    plt.rcParams.update({'font.size': 22})
    width = 0.30
    data = [
        # [205.31, 209.30,  214.89,  209.83],  # , 0.0486],
        [8.90, 23.10,  29.90],  # , 0.0335],
        [8.90, 10.9,   17.6],
    ]

    X = np.arange(3)

    fig, ax = plt.subplots()

    p1 = plt.bar(
        X + 0.00, data[0], color=colors["DBEst_10k"], width=width, alpha=alpha['2'])
    p2 = plt.bar(
        X + width, data[1], color=colors["BlinkDB_10k"], width=width, alpha=alpha['6'])
    # p3 = plt.bar(X + 0.40, data[2], color=colors["DBEst_100k"], width=width)
    # p4 = plt.bar(X + 0.60, data[3], color=colors["BlinkDB_100k"], width=width)

    plt.legend((p1[0], p2[0]),
               ('DBEst', 'DBEst_XGBoost', 'DBEst_100k', 'BlinkDB_100k'), loc='lower right')

    plt.xticks(X + 0.5 * width, ("COUNT", 'SUM', 'AVG', 'OVERALL'))
    ax.set_ylabel("Response Time (s)")
    # ax.set_yscale('log')
    formatter = FuncFormatter(to_percent)
    # ax.yaxis.set_major_formatter(formatter)
    plt.subplots_adjust(bottom=0.10)
    plt.subplots_adjust(left=0.18)

    plt.show()


def plt_group_by_training_time_xgboost():
    plt.rcParams.update({'font.size': 22})
    width = 0.40
    data = [
        [1525.3, 1525.3],  # , 0.0486],
        [502, 0],  # , 0.0335],
        [386, 0]
    ]

    X = np.arange(2)

    fig, ax = plt.subplots()

    p1 = plt.bar(
        X + 0.00, data[0], color=colors["DBEst_10k"], width=width, alpha=alpha['2'])
    p2 = plt.bar(X + 0, data[1], color=colors["DBEst_100k"],
                 width=width, bottom=data[0], alpha=alpha['4'])
    # p3 = plt.bar(X + 1, data[0], color=colors["BlinkDB_10k"],
    #              width=width, alpha=alpha['4'])
    p4 = plt.bar(X + 1, data[2], color=colors["BlinkDB_100k"],
                 width=width, alpha=alpha['6'], bottom=data[0])
    #p1[1].set_color(colors["BlinkDB_10k"])

    plt.legend((p1[0], p2[0],p4[0]),
               ('DBEst Sampling', 'DBEst training', 'DBEst_XGBoost training'), loc='lower center', prop={'size': 18})

    plt.xticks(X, ("DBEst", 'DBEst_XGBoost', 'AVG', 'OVERALL'))
    ax.set_ylabel("Total Training Time (s)")
    # ax.set_yscale('log')
    formatter = FuncFormatter(to_percent)
    # ax.yaxis.set_major_formatter(formatter)
    plt.subplots_adjust(bottom=0.09)
    plt.subplots_adjust(left=0.23)
    plt.xlim(-0.5, 1.5)

    plt.show()


def plt_group_by_memory_usage_xgboost():
    plt.rcParams.update({'font.size': 22})
    width = 0.40
    data = [
        [145, 98.73],  # , 0.0486],
        # [66.4,  102.4 ],#, 0.0335],
    ]

    X = np.arange(2)

    fig, ax = plt.subplots()

    p1 = plt.bar(X, data[0], color=colors["DBEst_10k"], width=width)
    # p2 = plt.bar(X + width, data[1], color=colors["BlinkDB_10k"], width=width)
    # p3 = plt.bar(X + 0.30, data[2], color=colors["BlinkDB_10k"], width=width)

    # plt.legend((p1[0]),
    #     ('DBEst', 'BlinkDB','BlinkDB Sampling','BlinkDB_100k'), loc='center', prop={'size': 18})

    # p1[0].set_color('r')
    p1[1].set_color(colors["BlinkDB_10k"])

    plt.xticks(X, ("DBEst", 'DBEst_XGBoost', 'AVG', 'OVERALL'))
    ax.set_ylabel("Memory Usage (MB)")
    # ax.set_xlabel("Sample Size")
    # ax.set_yscale('log')
    formatter = FuncFormatter(to_percent)
    # ax.yaxis.set_major_formatter(formatter)
    plt.subplots_adjust(bottom=0.10)
    plt.subplots_adjust(left=0.18)

    plt.show()

def plt_qreg_5d_all_gboost_win_NRMSE():
    plt.rcParams.update({'font.size': 22})
    width = 0.30
    x = np.arange(1,9)
    y1=[1.258380136,1.15068287,1.268301136,1.733106718,1.304683412,1.047334284,1,1.12319753]
    y2=[1.104369805,1.121203432,1.030391071,1.707040062,1.226973796,1.023649057,1,1.057215493]
    # X = np.arange(2)

    fig, ax = plt.subplots()

    p1 = plt.bar(x, y1, color=colors["DBEst_10k"], width=width, alpha=alpha['2'])
    p2 = plt.bar(x+width, y2, color=colors["BlinkDB_10k"], width=width, alpha=alpha['5'])
    # p2 = plt.bar(X + width, data[1], color=colors["BlinkDB_10k"], width=width)
    # p3 = plt.bar(X + 0.30, data[2], color=colors["BlinkDB_10k"], width=width)

    # plt.legend((p1[0]),
    #     ('DBEst', 'BlinkDB','BlinkDB Sampling','BlinkDB_100k'), loc='center', prop={'size': 18})

    # p1[0].set_color('r')
    # p1[1].set_color(colors["BlinkDB_10k"])
    plt.legend((p1[0], p2[0]),
               ('XGboost', 'QReg',), loc='upper right', prop={'size': 15})

    plt.xticks(x, ("1", '2', '3', '4','5','6','7','8'))
    ax.set_ylabel("NRMSE Ratio")
    ax.set_xlabel("Dataset ID")
    # ax.set_yscale('log')
    formatter = FuncFormatter(to_percent)
    # ax.yaxis.set_major_formatter(formatter)
    plt.subplots_adjust(bottom=0.18)
    plt.subplots_adjust(left=0.18)
    plt.ylim([1,1.8])

    plt.show()
    fig.savefig(
        "/Users/qingzhima/Desktop/NRMSE/5d_all_gboost.pdf", bbox_inches='tight')

def plt_qreg_5d_all_xgboost_win_NRMSE():
    plt.rcParams.update({'font.size': 22})
    width = 0.30
    x = np.arange(1,9)
    y1=[1.33016406,1.203790881,1.226169949,8.725116227,1.398625775,1.046487533,1.000312056,1.145814976]
    y2=[1.094605234,1.031325017,1.201777986,1.011646806,1.036660731,1.022319881,1,1.031595393]
    # X = np.arange(2)

    fig, ax = plt.subplots()

    p1 = plt.bar(x, y1, color=colors["DBEst_10k"], width=width, alpha=alpha['2'])
    p2 = plt.bar(x+width, y2, color=colors["BlinkDB_10k"], width=width, alpha=alpha['5'])
    # p2 = plt.bar(X + width, data[1], color=colors["BlinkDB_10k"], width=width)
    # p3 = plt.bar(X + 0.30, data[2], color=colors["BlinkDB_10k"], width=width)

    # plt.legend((p1[0]),
    #     ('DBEst', 'BlinkDB','BlinkDB Sampling','BlinkDB_100k'), loc='center', prop={'size': 18})

    # p1[0].set_color('r')
    # p1[1].set_color(colors["BlinkDB_10k"])
    plt.legend((p1[0], p2[0]),
               ('GBoost', 'QReg',), loc='upper right', prop={'size': 15})

    plt.xticks(x, ("1", '2', '3', '4','5','6','7','8'))
    ax.set_ylabel("NRMSE Ratio")
    ax.set_xlabel("Dataset ID")
    # ax.set_yscale('log')
    formatter = FuncFormatter(to_percent)
    # ax.yaxis.set_major_formatter(formatter)
    plt.subplots_adjust(bottom=0.18)
    plt.subplots_adjust(left=0.18)
    plt.ylim([1,1.8])

    plt.show()
    fig.savefig(
        "/Users/qingzhima/Desktop/NRMSE/5d_all_xgboost.pdf", bbox_inches='tight')

def plt_qreg_4d_all_gboost_win_NRMSE():
    plt.rcParams.update({'font.size': 22})
    width = 0.30
    x = np.arange(1,9)
    y1=[1.255179409,1.144666109,1.171040158,1.719770663,1.172163909,1.029519354,1.0,1.129121701]
    y2=[1.111063072,1.103036824,1.062702969,1.70154241,1.079607725,1.014047491,1.0,1.057749707]
    # X = np.arange(2)

    fig, ax = plt.subplots()

    p1 = plt.bar(x, y1, color=colors["DBEst_10k"], width=width, alpha=alpha['2'])
    p2 = plt.bar(x+width, y2, color=colors["BlinkDB_10k"], width=width, alpha=alpha['5'])
    # p2 = plt.bar(X + width, data[1], color=colors["BlinkDB_10k"], width=width)
    # p3 = plt.bar(X + 0.30, data[2], color=colors["BlinkDB_10k"], width=width)

    # plt.legend((p1[0]),
    #     ('DBEst', 'BlinkDB','BlinkDB Sampling','BlinkDB_100k'), loc='center', prop={'size': 18})

    # p1[0].set_color('r')
    # p1[1].set_color(colors["BlinkDB_10k"])
    plt.legend((p1[0], p2[0]),
               ('XGboost', 'QReg',), loc='upper right', prop={'size': 15})

    plt.xticks(x, ("1", '2', '3', '4','5','6','7','8'))
    ax.set_ylabel("NRMSE Ratio")
    ax.set_xlabel("Dataset ID")
    # ax.set_yscale('log')
    formatter = FuncFormatter(to_percent)
    # ax.yaxis.set_major_formatter(formatter)
    plt.subplots_adjust(bottom=0.18)
    plt.subplots_adjust(left=0.18)
    plt.ylim([1,1.8])

    plt.show()
    fig.savefig(
        "/Users/qingzhima/Desktop/NRMSE/4d_all_gboost.pdf", bbox_inches='tight')

def plt_qreg_4d_all_xgboost_win_NRMSE():
    plt.rcParams.update({'font.size': 22})
    width = 0.30
    x = np.arange(1,9)
    y1=[1.328834625,1.188130648,1.152159565,8.144936446,1.160754681,1.028199225,1.000312522,1.140370554]
    y2=[1.078060376,1.046809325,1.072493416,1.009619958,1.076673209,1.014322855,1,1.032626243]
    # X = np.arange(2)

    fig, ax = plt.subplots()

    p1 = plt.bar(x, y1, color=colors["DBEst_10k"], width=width, alpha=alpha['2'])
    p2 = plt.bar(x+width, y2, color=colors["BlinkDB_10k"], width=width, alpha=alpha['5'])
    # p2 = plt.bar(X + width, data[1], color=colors["BlinkDB_10k"], width=width)
    # p3 = plt.bar(X + 0.30, data[2], color=colors["BlinkDB_10k"], width=width)

    # plt.legend((p1[0]),
    #     ('DBEst', 'BlinkDB','BlinkDB Sampling','BlinkDB_100k'), loc='center', prop={'size': 18})

    # p1[0].set_color('r')
    # p1[1].set_color(colors["BlinkDB_10k"])
    plt.legend((p1[0], p2[0]),
               ('GBoost', 'QReg',), loc='upper right', prop={'size': 15})

    plt.xticks(x, ("1", '2', '3', '4','5','6','7','8'))
    ax.set_ylabel("NRMSE Ratio")
    ax.set_xlabel("Dataset ID")
    # ax.set_yscale('log')
    formatter = FuncFormatter(to_percent)
    # ax.yaxis.set_major_formatter(formatter)
    plt.subplots_adjust(bottom=0.18)
    plt.subplots_adjust(left=0.18)
    plt.ylim([1,1.8])

    plt.show()
    fig.savefig(
        "/Users/qingzhima/Desktop/NRMSE/4d_all_xgboost.pdf", bbox_inches='tight')

# -----------------------------------------------------------------------------------

def plt_qreg_5d_20_gboost_win_NRMSE():
    plt.rcParams.update({'font.size': 22})
    width = 0.30
    x = np.arange(1,9)
    y1=[6.262674613,1.408869412,2.571591463,1.733106718,2.098165628,1.203151256,1.0,1.240643516]
    y2=[1.018527856,1.299619899,1.045053009,1.707040062,1.809182459,1.095678729,1.0,1.133271403]
    # X = np.arange(2)

    fig, ax = plt.subplots()

    p1 = plt.bar(x, y1, color=colors["DBEst_10k"], width=width, alpha=alpha['2'])
    p2 = plt.bar(x+width, y2, color=colors["BlinkDB_10k"], width=width, alpha=alpha['5'])
    # p2 = plt.bar(X + width, data[1], color=colors["BlinkDB_10k"], width=width)
    # p3 = plt.bar(X + 0.30, data[2], color=colors["BlinkDB_10k"], width=width)

    # plt.legend((p1[0]),
    #     ('DBEst', 'BlinkDB','BlinkDB Sampling','BlinkDB_100k'), loc='center', prop={'size': 18})

    # p1[0].set_color('r')
    # p1[1].set_color(colors["BlinkDB_10k"])
    plt.legend((p1[0], p2[0]),
               ('XGBoost', 'QReg',), loc='upper right', prop={'size': 15})

    plt.xticks(x, ("1", '2', '3', '4','5','6','7','8'))
    ax.set_ylabel("NRMSE Ratio")
    ax.set_xlabel("Dataset ID")
    # ax.set_yscale('log')
    formatter = FuncFormatter(to_percent)
    # ax.yaxis.set_major_formatter(formatter)
    plt.subplots_adjust(bottom=0.18)
    plt.subplots_adjust(left=0.18)
    plt.ylim([1,3])

    plt.show()
    fig.savefig(
        "/Users/qingzhima/Desktop/NRMSE/5d_20_gboost.pdf", bbox_inches='tight')

def plt_qreg_5d_20_xgboost_win_NRMSE():
    plt.rcParams.update({'font.size': 22})
    width = 0.30
    x = np.arange(1,9)
    y1=[1.350480679,1.760293749,1.804700949,15.75397076,2.978374011,1.218450222,1.000399372,1.384219496]
    y2=[1.065880997,1.071900781,1.708882995,1.00589506,1.161744503,1.080354967,1,1.087235847]
    # X = np.arange(2)

    fig, ax = plt.subplots()

    p1 = plt.bar(x, y1, color=colors["DBEst_10k"], width=width, alpha=alpha['2'])
    p2 = plt.bar(x+width, y2, color=colors["BlinkDB_10k"], width=width, alpha=alpha['5'])
    # p2 = plt.bar(X + width, data[1], color=colors["BlinkDB_10k"], width=width)
    # p3 = plt.bar(X + 0.30, data[2], color=colors["BlinkDB_10k"], width=width)

    # plt.legend((p1[0]),
    #     ('DBEst', 'BlinkDB','BlinkDB Sampling','BlinkDB_100k'), loc='center', prop={'size': 18})

    # p1[0].set_color('r')
    # p1[1].set_color(colors["BlinkDB_10k"])
    plt.legend((p1[0], p2[0]),
               ('GBoost', 'QReg',), loc='upper right', prop={'size': 15})

    plt.xticks(x, ("1", '2', '3', '4','5','6','7','8'))
    ax.set_ylabel("NRMSE Ratio")
    ax.set_xlabel("Dataset ID")
    # ax.set_yscale('log')
    formatter = FuncFormatter(to_percent)
    # ax.yaxis.set_major_formatter(formatter)
    plt.subplots_adjust(bottom=0.18)
    plt.subplots_adjust(left=0.18)
    plt.ylim([1,3])

    plt.show()
    fig.savefig(
        "/Users/qingzhima/Desktop/NRMSE/5d_20_xgboost.pdf", bbox_inches='tight')

def plt_qreg_4d_20_gboost_win_NRMSE():
    plt.rcParams.update({'font.size': 22})
    width = 0.30
    x = np.arange(1,9)
    y1=[8.7049404,1.385833011,1.968796846,1.719770663,1.693530178,1.114288095,1.0,1.215151202]
    y2=[1.020434842,1.237549681,1.191694511,1.70154241,1.311740762,1.030646717,1.0,1.124459639]
    # X = np.arange(2)




    fig, ax = plt.subplots()

    p1 = plt.bar(x, y1, color=colors["DBEst_10k"], width=width, alpha=alpha['2'])
    p2 = plt.bar(x+width, y2, color=colors["BlinkDB_10k"], width=width, alpha=alpha['5'])
    # p2 = plt.bar(X + width, data[1], color=colors["BlinkDB_10k"], width=width)
    # p3 = plt.bar(X + 0.30, data[2], color=colors["BlinkDB_10k"], width=width)

    # plt.legend((p1[0]),
    #     ('DBEst', 'BlinkDB','BlinkDB Sampling','BlinkDB_100k'), loc='center', prop={'size': 18})

    # p1[0].set_color('r')
    # p1[1].set_color(colors["BlinkDB_10k"])
    plt.legend((p1[0], p2[0]),
               ('XGBoost', 'QReg',), loc='upper right', prop={'size': 15})

    plt.xticks(x, ("1", '2', '3', '4','5','6','7','8'))
    ax.set_ylabel("NRMSE Ratio")
    ax.set_xlabel("Dataset ID")
    # ax.set_yscale('log')
    formatter = FuncFormatter(to_percent)
    # ax.yaxis.set_major_formatter(formatter)
    plt.subplots_adjust(bottom=0.18)
    plt.subplots_adjust(left=0.18)
    plt.ylim([1,2])

    plt.show()
    fig.savefig(
        "/Users/qingzhima/Desktop/NRMSE/4d_20_gboost.pdf", bbox_inches='tight')

def plt_qreg_4d_20_xgboost_win_NRMSE():
    plt.rcParams.update({'font.size': 22})
    width = 0.30
    x = np.arange(1,9)
    y1=[1.337221096,1.707164074,1.629248301,14.06955886,1.773262497,1.095319195,1.000399552,1.353009814]
    y2=[1.03650826,1.114213952,1.297107356,1.00625691,1.34056072,1.046021968,1,1.073025246]
    # X = np.arange(2)

    fig, ax = plt.subplots()

    p1 = plt.bar(x, y1, color=colors["DBEst_10k"], width=width, alpha=alpha['2'])
    p2 = plt.bar(x+width, y2, color=colors["BlinkDB_10k"], width=width, alpha=alpha['5'])
    # p2 = plt.bar(X + width, data[1], color=colors["BlinkDB_10k"], width=width)
    # p3 = plt.bar(X + 0.30, data[2], color=colors["BlinkDB_10k"], width=width)

    # plt.legend((p1[0]),
    #     ('DBEst', 'BlinkDB','BlinkDB Sampling','BlinkDB_100k'), loc='center', prop={'size': 18})

    # p1[0].set_color('r')
    # p1[1].set_color(colors["BlinkDB_10k"])
    plt.legend((p1[0], p2[0]),
               ('GBoost', 'QReg',), loc='upper right', prop={'size': 15})

    plt.xticks(x, ("1", '2', '3', '4','5','6','7','8'))
    ax.set_ylabel("NRMSE Ratio")
    ax.set_xlabel("Dataset ID")
    # ax.set_yscale('log')
    formatter = FuncFormatter(to_percent)
    # ax.yaxis.set_major_formatter(formatter)
    plt.subplots_adjust(bottom=0.18)
    plt.subplots_adjust(left=0.18)
    plt.ylim([1,2])

    plt.show()
    fig.savefig(
        "/Users/qingzhima/Desktop/NRMSE/4d_20_xgboost.pdf", bbox_inches='tight')





def plt_qreg_5d_all_gboost_win_NRMSE_sample():
    plt.rcParams.update({'font.size': 22})
    width = 0.30
    x = np.arange(1,5)
    y1=[1.0675, 1.1369,  1.1550,  1.3325]
    y2=[1.0386, 1.0765,  1.0835,  1.2175]
    # X = np.arange(2)
 
    fig, ax = plt.subplots()

    p1 = plt.bar(x, y1, color=colors["DBEst_10k"], width=width, alpha=alpha['2'])
    p2 = plt.bar(x+width, y2, color=colors["BlinkDB_10k"], width=width, alpha=alpha['5'])
    # p2 = plt.bar(X + width, data[1], color=colors["BlinkDB_10k"], width=width)
    # p3 = plt.bar(X + 0.30, data[2], color=colors["BlinkDB_10k"], width=width)

    # plt.legend((p1[0]),
    #     ('DBEst', 'BlinkDB','BlinkDB Sampling','BlinkDB_100k'), loc='center', prop={'size': 18})

    # p1[0].set_color('r')
    # p1[1].set_color(colors["BlinkDB_10k"])
    plt.legend((p1[0], p2[0]),
               ('XGboost', 'QReg',), loc='upper left', prop={'size': 15})

    plt.xticks(x+0.5*width, ("6", '7', '8', 'store_sales','5','6','7','8'))
    ax.set_ylabel("NRMSE Ratio")
    ax.set_xlabel("Dataset ID")
    # ax.set_yscale('log')
    formatter = FuncFormatter(to_percent)
    # ax.yaxis.set_major_formatter(formatter)
    plt.subplots_adjust(bottom=0.18)
    plt.subplots_adjust(left=0.18)
    plt.ylim([1,1.4])

    plt.show()
    fig.savefig(
        "/Users/qingzhima/Desktop/NRMSE/5d_all_gboost.pdf", bbox_inches='tight')

def plt_qreg_5d_all_xgboost_win_NRMSE_sample():
    plt.rcParams.update({'font.size': 22})
    width = 0.30
    x = np.arange(1,5)
    y1=[1.0659, 1.2107,  1.1790,  1.3820]
    y2=[1.0280, 1.0499,  1.0726,  1.0963]
    # X = np.arange(2)

    fig, ax = plt.subplots()

    p1 = plt.bar(x, y1, color=colors["DBEst_10k"], width=width, alpha=alpha['2'])
    p2 = plt.bar(x+width, y2, color=colors["BlinkDB_10k"], width=width, alpha=alpha['5'])
    # p2 = plt.bar(X + width, data[1], color=colors["BlinkDB_10k"], width=width)
    # p3 = plt.bar(X + 0.30, data[2], color=colors["BlinkDB_10k"], width=width)

    # plt.legend((p1[0]),
    #     ('DBEst', 'BlinkDB','BlinkDB Sampling','BlinkDB_100k'), loc='center', prop={'size': 18})

    # p1[0].set_color('r')
    # p1[1].set_color(colors["BlinkDB_10k"])
    plt.legend((p1[0], p2[0]),
               ('GBoost', 'QReg',), loc='upper left', prop={'size': 15})

    plt.xticks(x+0.5*width, ("6", '7', '8', 'store_sales','5','6','7','8'))
    ax.set_ylabel("NRMSE Ratio")
    ax.set_xlabel("Dataset ID")
    # ax.set_yscale('log')
    formatter = FuncFormatter(to_percent)
    # ax.yaxis.set_major_formatter(formatter)
    plt.subplots_adjust(bottom=0.18)
    plt.subplots_adjust(left=0.18)
    plt.ylim([1,1.5])

    plt.show()
    fig.savefig(
        "/Users/qingzhima/Desktop/NRMSE/5d_all_xgboost.pdf", bbox_inches='tight')

def plt_qreg_4d_all_gboost_win_NRMSE_sample():
    plt.rcParams.update({'font.size': 22})
    width = 0.30
    x = np.arange(1,5)
    y1=[1.0064,  1.1599,  1.1484,  1.0002]
    y2=[1.0009,  1.1051,  1.0751,  1.0001]
    # X = np.arange(2)
 
 
 
 

    fig, ax = plt.subplots()

    p1 = plt.bar(x, y1, color=colors["DBEst_10k"], width=width, alpha=alpha['2'])
    p2 = plt.bar(x+width, y2, color=colors["BlinkDB_10k"], width=width, alpha=alpha['5'])
    # p2 = plt.bar(X + width, data[1], color=colors["BlinkDB_10k"], width=width)
    # p3 = plt.bar(X + 0.30, data[2], color=colors["BlinkDB_10k"], width=width)

    # plt.legend((p1[0]),
    #     ('DBEst', 'BlinkDB','BlinkDB Sampling','BlinkDB_100k'), loc='center', prop={'size': 18})

    # p1[0].set_color('r')
    # p1[1].set_color(colors["BlinkDB_10k"])
    plt.legend((p1[0], p2[0]),
               ('XGboost', 'QReg',), loc='upper right', prop={'size': 15})

    plt.xticks(x+0.5*width, ("6", '7', '8', 'store_sales','5','6','7','8'))
    ax.set_ylabel("NRMSE Ratio")
    ax.set_xlabel("Dataset ID")
    # ax.set_yscale('log')
    formatter = FuncFormatter(to_percent)
    # ax.yaxis.set_major_formatter(formatter)
    plt.subplots_adjust(bottom=0.18)
    plt.subplots_adjust(left=0.18)
    plt.ylim([1,1.2])

    plt.show()
    fig.savefig(
        "/Users/qingzhima/Desktop/NRMSE/4d_all_gboost.pdf", bbox_inches='tight')

def plt_qreg_4d_all_xgboost_win_NRMSE_sample():
    plt.rcParams.update({'font.size': 22})
    width = 0.30
    x = np.arange(1,5)
    y1=[1.0036,  1.1397,  1.1736,  1.0002]
    y2=[1.0030,  1.0383,  1.0746,  1.0000]
    # X = np.arange(2)
 
 
 
 

    fig, ax = plt.subplots()

    p1 = plt.bar(x, y1, color=colors["DBEst_10k"], width=width, alpha=alpha['2'])
    p2 = plt.bar(x+width, y2, color=colors["BlinkDB_10k"], width=width, alpha=alpha['5'])
    # p2 = plt.bar(X + width, data[1], color=colors["BlinkDB_10k"], width=width)
    # p3 = plt.bar(X + 0.30, data[2], color=colors["BlinkDB_10k"], width=width)

    # plt.legend((p1[0]),
    #     ('DBEst', 'BlinkDB','BlinkDB Sampling','BlinkDB_100k'), loc='center', prop={'size': 18})

    # p1[0].set_color('r')
    # p1[1].set_color(colors["BlinkDB_10k"])
    plt.legend((p1[0], p2[0]),
               ('GBoost', 'QReg',), loc='upper right', prop={'size': 15})

    plt.xticks(x+0.5*width, ("6", '7', '8', 'store_sales','5','6','7','8'))
    ax.set_ylabel("NRMSE Ratio")
    ax.set_xlabel("Dataset ID")
    # ax.set_yscale('log')
    formatter = FuncFormatter(to_percent)
    # ax.yaxis.set_major_formatter(formatter)
    plt.subplots_adjust(bottom=0.18)
    plt.subplots_adjust(left=0.18)
    plt.ylim([1,1.2])

    plt.show()
    fig.savefig(
        "/Users/qingzhima/Desktop/NRMSE/4d_all_xgboost.pdf", bbox_inches='tight')

# -----------------------------------------------------------------------------------

def plt_qreg_5d_20_gboost_win_NRMSE_sample():
    plt.rcParams.update({'font.size': 22})
    width = 0.30
    x = np.arange(1,5)
    y1=[1.2862,  1.8501,  1.3434,  2.3723 ]
    y2=[1.1625,  1.3305,  1.2014,  1.9196 ]
    # X = np.arange(2)





    fig, ax = plt.subplots()

    p1 = plt.bar(x, y1, color=colors["DBEst_10k"], width=width, alpha=alpha['2'])
    p2 = plt.bar(x+width, y2, color=colors["BlinkDB_10k"], width=width, alpha=alpha['5'])
    # p2 = plt.bar(X + width, data[1], color=colors["BlinkDB_10k"], width=width)
    # p3 = plt.bar(X + 0.30, data[2], color=colors["BlinkDB_10k"], width=width)

    # plt.legend((p1[0]),
    #     ('DBEst', 'BlinkDB','BlinkDB Sampling','BlinkDB_100k'), loc='center', prop={'size': 18})

    # p1[0].set_color('r')
    # p1[1].set_color(colors["BlinkDB_10k"])
    plt.legend((p1[0], p2[0]),
               ('XGBoost', 'QReg',), loc='upper right', prop={'size': 15})

    plt.xticks(x+0.5*width, ("6", '7', '8', 'store_sales','5','6','7','8'))
    ax.set_ylabel("NRMSE Ratio")
    ax.set_xlabel("Dataset ID")
    # ax.set_yscale('log')
    formatter = FuncFormatter(to_percent)
    # ax.yaxis.set_major_formatter(formatter)
    plt.subplots_adjust(bottom=0.18)
    plt.subplots_adjust(left=0.18)
    plt.ylim([1,3])

    plt.show()
    fig.savefig(
        "/Users/qingzhima/Desktop/NRMSE/5d_20_gboost.pdf", bbox_inches='tight')

def plt_qreg_5d_20_xgboost_win_NRMSE_sample():
    plt.rcParams.update({'font.size': 22})
    width = 0.30
    x = np.arange(1,5)
    y1=[1.2910,  1.8823,  1.5265,  2.6427 ]
    y2=[1.1001,  1.2504,  1.0764,  1.1840 ]
    # X = np.arange(2)

    fig, ax = plt.subplots()

    p1 = plt.bar(x, y1, color=colors["DBEst_10k"], width=width, alpha=alpha['2'])
    p2 = plt.bar(x+width, y2, color=colors["BlinkDB_10k"], width=width, alpha=alpha['5'])
    # p2 = plt.bar(X + width, data[1], color=colors["BlinkDB_10k"], width=width)
    # p3 = plt.bar(X + 0.30, data[2], color=colors["BlinkDB_10k"], width=width)

    # plt.legend((p1[0]),
    #     ('DBEst', 'BlinkDB','BlinkDB Sampling','BlinkDB_100k'), loc='center', prop={'size': 18})

    # p1[0].set_color('r')
    # p1[1].set_color(colors["BlinkDB_10k"])
    plt.legend((p1[0], p2[0]),
               ('GBoost', 'QReg',), loc='upper left', prop={'size': 15})

    plt.xticks(x+0.5*width, ("6", '7', '8', 'store_sales','5','6','7','8'))
    ax.set_ylabel("NRMSE Ratio")
    ax.set_xlabel("Dataset ID")
    # ax.set_yscale('log')
    formatter = FuncFormatter(to_percent)
    # ax.yaxis.set_major_formatter(formatter)
    plt.subplots_adjust(bottom=0.18)
    plt.subplots_adjust(left=0.18)
    plt.ylim([1,3])

    plt.show()
    fig.savefig(
        "/Users/qingzhima/Desktop/NRMSE/5d_20_xgboost.pdf", bbox_inches='tight')

def plt_qreg_4d_20_gboost_win_NRMSE_sample():
    plt.rcParams.update({'font.size': 22})
    width = 0.30
    x = np.arange(1,5)
    y1=[1.0224,  1.7717, 1.3544,  1.0010]
    y2=[1.0014,  1.3402, 1.1840,  1.0008]
    # X = np.arange(2)




    fig, ax = plt.subplots()

    p1 = plt.bar(x, y1, color=colors["DBEst_10k"], width=width, alpha=alpha['2'])
    p2 = plt.bar(x+width, y2, color=colors["BlinkDB_10k"], width=width, alpha=alpha['5'])
    # p2 = plt.bar(X + width, data[1], color=colors["BlinkDB_10k"], width=width)
    # p3 = plt.bar(X + 0.30, data[2], color=colors["BlinkDB_10k"], width=width)

    # plt.legend((p1[0]),
    #     ('DBEst', 'BlinkDB','BlinkDB Sampling','BlinkDB_100k'), loc='center', prop={'size': 18})

    # p1[0].set_color('r')
    # p1[1].set_color(colors["BlinkDB_10k"])
    plt.legend((p1[0], p2[0]),
               ('XGBoost', 'QReg',), loc='upper right', prop={'size': 15})

    plt.xticks(x+0.5*width, ("6", '7', '8', 'store_sales','5','6','7','8'))
    ax.set_ylabel("NRMSE Ratio")
    ax.set_xlabel("Dataset ID")
    # ax.set_yscale('log')
    formatter = FuncFormatter(to_percent)
    # ax.yaxis.set_major_formatter(formatter)
    plt.subplots_adjust(bottom=0.18)
    plt.subplots_adjust(left=0.18)
    plt.ylim([1,1.8])

    plt.show()
    fig.savefig(
        "/Users/qingzhima/Desktop/NRMSE/4d_20_gboost.pdf", bbox_inches='tight')

def plt_qreg_4d_20_xgboost_win_NRMSE_sample():
    plt.rcParams.update({'font.size': 22})
    width = 0.30
    x = np.arange(1,5)
    y1=[1.0153,  1.9064, 1.4747,  1.0009]
    y2=[1.0128,  1.2266, 1.0926,  1.0001]
    # X = np.arange(2)

    fig, ax = plt.subplots()

    p1 = plt.bar(x, y1, color=colors["DBEst_10k"], width=width, alpha=alpha['2'])
    p2 = plt.bar(x+width, y2, color=colors["BlinkDB_10k"], width=width, alpha=alpha['5'])
    # p2 = plt.bar(X + width, data[1], color=colors["BlinkDB_10k"], width=width)
    # p3 = plt.bar(X + 0.30, data[2], color=colors["BlinkDB_10k"], width=width)

    # plt.legend((p1[0]),
    #     ('DBEst', 'BlinkDB','BlinkDB Sampling','BlinkDB_100k'), loc='center', prop={'size': 18})

    # p1[0].set_color('r')
    # p1[1].set_color(colors["BlinkDB_10k"])
    plt.legend((p1[0], p2[0]),
               ('GBoost', 'QReg',), loc='upper right', prop={'size': 15})

    plt.xticks(x+0.5*width, ("6", '7', '8', 'store_sales','5','6','7','8'))
    ax.set_ylabel("NRMSE Ratio")
    ax.set_xlabel("Dataset ID")
    # ax.set_yscale('log')
    formatter = FuncFormatter(to_percent)
    # ax.yaxis.set_major_formatter(formatter)
    plt.subplots_adjust(bottom=0.18)
    plt.subplots_adjust(left=0.18)
    plt.ylim([1,2])

    plt.show()
    fig.savefig(
        "/Users/qingzhima/Desktop/NRMSE/4d_20_xgboost.pdf", bbox_inches='tight')


def plt_qreg_2d_accuracy_comparison_with_base_models():
    plt.rcParams.update({'font.size': 22})
    width = 0.20
    x = np.arange(1,9)
    y1=[1.0010,  0.9999,  1.0000, 1.0005,  1.0003, 1.0000, 1.0018,  1.0000  ]
    y2=[0.9999,  1.0000,  1.0004, 1.0004,  1.0000, 1.0002, 1.0001,  1.6095  ]
    



    xx=[0.6,8.5]
    yy=[1,1]



    

    fig, ax = plt.subplots()

    p1 = plt.bar(x, y1, color=colors["DBEst_10k"], width=width, alpha=alpha['2'])
    p2 = plt.bar(x+width, y2, color=colors["BlinkDB_10k"], width=width, alpha=alpha['5'])
    plt.plot(xx,yy,alpha=0.2)
    plt.legend((p1[0], p2[0]),
               ('GBoost vs QReg','XGBoost vs QReg'), loc='upper right', prop={'size': 15})

    plt.xticks(x, ("1", '2', '3', '4','5','6','7','8'))
    ax.set_ylabel("NRMSE Ratio")
    ax.set_xlabel("Dataset ID")
    # ax.set_yscale('log')
    formatter = FuncFormatter(to_percent)
    # ax.yaxis.set_major_formatter(formatter)
    plt.subplots_adjust(bottom=0.18)
    plt.subplots_adjust(left=0.25)
    plt.ylim([0.995,1.005])

    plt.show()

def plt_qreg_3d_accuracy_comparison_with_base_models():
    plt.rcParams.update({'font.size': 22})
    width = 0.20
    x = np.arange(1,9)
    y1=[1.0006 , 1.0008 , 1.0001,  3.6798, 1.0032,  1.0002,  1.0405,  1.0133 ]
    y2=[1.0021 , 1.0005 , 1.0010,  1.0000, 0.9992,  1.0000,  1.0195,  1.0185 ]
 
 

    xx=[0.6,8.5]
    yy=[1,1]



    

    fig, ax = plt.subplots()

    p1 = plt.bar(x, y1, color=colors["DBEst_10k"], width=width, alpha=alpha['2'])
    p2 = plt.bar(x+width, y2, color=colors["BlinkDB_10k"], width=width, alpha=alpha['5'])
    plt.plot(xx,yy,alpha=0.2)
    plt.legend((p1[0], p2[0]),
               ('GBoost vs QReg','XGBoost vs QReg'), loc='upper right', prop={'size': 15})

    plt.xticks(x, ("1", '2', '3', '4','5','6','7','8'))
    ax.set_ylabel("NRMSE Ratio")
    ax.set_xlabel("Dataset ID")
    # ax.set_yscale('log')
    formatter = FuncFormatter(to_percent)
    # ax.yaxis.set_major_formatter(formatter)
    plt.subplots_adjust(bottom=0.18)
    plt.subplots_adjust(left=0.25)
    plt.ylim([0.98,1.1])

    plt.show()

def plt_qreg_4d_accuracy_comparison_with_base_models():
    plt.rcParams.update({'font.size': 22})
    width = 0.20
    x = np.arange(1,9)
    y1=[1.0010,  0.9999 , 1.0000, 1.0005 , 0.9980 ,1.0005 ,1.0846 ,1.8934  ]
    y2=[0.9999,  1.0000 , 1.0004, 1.0004 , 1.0212 ,0.9998 ,1.0497 ,1.0000  ]



    xx=[0.6,8.5]
    yy=[1,1]



    

    fig, ax = plt.subplots()

    p1 = plt.bar(x, y1, color=colors["DBEst_10k"], width=width, alpha=alpha['2'])
    p2 = plt.bar(x+width, y2, color=colors["BlinkDB_10k"], width=width, alpha=alpha['5'])
    plt.plot(xx,yy,alpha=0.2)
    plt.legend((p1[0], p2[0]),
               ('GBoost vs QReg','XGBoost vs QReg'), loc='upper right', prop={'size': 15})

    plt.xticks(x, ("1", '2', '3', '4','5','6','7','8'))
    ax.set_ylabel("NRMSE Ratio")
    ax.set_xlabel("Dataset ID")
    # ax.set_yscale('log')
    formatter = FuncFormatter(to_percent)
    # ax.yaxis.set_major_formatter(formatter)
    plt.subplots_adjust(bottom=0.18)
    plt.subplots_adjust(left=0.18)
    plt.ylim([0.95,1.15])

    plt.show()

def plt_qreg_5d_accuracy_comparison_with_base_models():
    plt.rcParams.update({'font.size': 22})
    width = 0.20
    x = np.arange(1,9)
    y1=[1.1281,  1.0193,  0.9969,  7.2361,  1.1164,  1.0013,  1.0003,  1.0291 ]
    y2=[0.9993,  1.0024,  1.0410,  0.9965,  1.0148,  1.0002,  1.0000,  1.0184 ]
    # y3=[]
    xx=[0.6,8.5]
    yy=[1,1]



    

    fig, ax = plt.subplots()

    p1 = plt.bar(x, y1, color=colors["DBEst_10k"], width=width, alpha=alpha['2'])
    p2 = plt.bar(x+width, y2, color=colors["BlinkDB_10k"], width=width, alpha=alpha['5'])
    plt.plot(xx,yy,alpha=0.2)
    plt.legend((p1[0], p2[0]),
               ('GBoost vs QReg','XGBoost vs QReg'), loc='upper right', prop={'size': 15})

    plt.xticks(x, ("1", '2', '3', '4','5','6','7','8'))
    ax.set_ylabel("NRMSE Ratio")
    ax.set_xlabel("Dataset ID")
    # ax.set_yscale('log')
    formatter = FuncFormatter(to_percent)
    # ax.yaxis.set_major_formatter(formatter)
    plt.subplots_adjust(bottom=0.18)
    plt.subplots_adjust(left=0.18)
    plt.ylim([0.95,1.25])

    plt.show()


def plt_qreg_simple_accuracy():
    plt.rcParams.update({'font.size': 16})
    width = 0.20
    x = np.arange(1,9)
    y1=[1.0611, 1.0164, 1.0385, 1.4061, 1.0238,  1.0075,  1.1715,  1.0323]
    y2=[6.0000, 1.0051, 1.0818, 1.1179, 1.0041,  0.9962,  2.0204,  1.0151]
    y3=[1.2109, 1.0078, 1.0179, 1.0383, 1.0136,  0.9978,  1.3116,  1.0305]
    xx=[0.6,8.5]
    yy=[1,1]

    fig, ax = plt.subplots()

    p1 = plt.bar(x, y1, color=colors["DBEst_10k"], width=width, alpha=alpha['2'])
    p2 = plt.bar(x+width, y2, color=colors["BlinkDB_10k"], width=width, alpha=alpha['5'])
    p3 = plt.bar(x+2*width, y3, color=colors["BlinkDB_1m"], width=width, alpha=alpha['3'])

    plt.plot(xx,yy,alpha=0.2)
    plt.legend((p1[0], p2[0], p3[0]),
               ('LR vs QReg','PR vs QReg', 'DTR vs QReg'), loc='center', prop={'size': 15})

    plt.xticks(x+width, ("1", '2', '3', '4','5','6','7','8'))
    ax.set_ylabel("NRMSE Ratio")
    ax.set_xlabel("Dataset ID")
    # ax.set_yscale('log')
    formatter = FuncFormatter(to_percent)
    # ax.yaxis.set_major_formatter(formatter)
    plt.subplots_adjust(bottom=0.13)
    plt.subplots_adjust(left=0.15)
    plt.ylim([0.95,1.5])

    plt.show()

def plt_qreg_simple_accuracy_d(d="2d"):
    plt.rcParams.update({'font.size': 22})
    width = 0.20
    x = np.arange(1,9)
    if d =="2d":
        y1=[1.0697 , 1.0032 , 0.9701 , 1.0369 , 1.0028 , 1.4859 , 1.0734 , 1.2587]
        y2=[0.9919 , 0.9976 , 0.9786 , 1.023  , 0.9937 , 0.9986 , 1.0633 , 1.0636]
        y3=[1.0512 , 0.9992 , 0.997  , 1.0361 , 1.0026 , 0.9987 , 1.067  , 1.7119]
    if d =="3d":
        y1=[1.2036 , 1.0519 , 1.0847 , 1.1140 , 1.0326 , 1.6128 , 1.1706 , 1.0858 ]
        y2=[1.1544 , 1.0630 , 0.9972 , 1.0005 , 1.0028 , 0.9984 , 1.0220 , 1.0006 ]
        y3=[1.3057 , 0.9780 , 1.0239 , 0.9927 , 0.9904 , 0.9946 , 1.2158 , 1.0130 ]
    if d =="4d":
        y1=[0.9584 , 1.1045 , 1.1416 , 1.062  , 1.0903 , 1.403  , 1.1907 , 1.1271]
        y2=[0.9171 , 1.0758 , 1.006  , 1.1024 , 1.0548 , 0.9988 , 1.2272 , 1.0382]
        y3=[1.0533 , 0.9817 , 0.9917 , 0.9554 , 0.9841 , 0.9981 , 1.1877 , 1.0344]
    if d =="5d":
        y1=[1.178  , 1.1081 , 1.7977 , 1.0445 , 0.8592 , 1.4509 , 1.2415 , 1.1211]
        y2=[1.1147 , 1.0605 , 1.0185 , 1.1942 , 0.8198 , 0.8655 , 1.2517 , 1.0316]
        y3=[1.2622 , 0.9747 , 0.9985 , 0.9357 , 0.7583 , 0.8425 , 1.1858 , 1.0218]
    xx=[0.6,8.5]
    yy=[1,1]


    fig, ax = plt.subplots()

    p1 = plt.bar(x, y1, color=colors["DBEst_10k"], width=width, alpha=alpha['2'])
    p2 = plt.bar(x+width, y2, color=colors["BlinkDB_10k"], width=width, alpha=alpha['5'])
    p3 = plt.bar(x+2*width, y3, color=colors["BlinkDB_1m"], width=width, alpha=alpha['3'])

    plt.plot(xx,yy,alpha=0.2)
    plt.legend((p1[0], p2[0], p3[0]),
               ('AdaBoost vs QReg','GBoost vs QReg', 'XGBoost vs QReg'), loc='upper left', prop={'size': 15})

    plt.xticks(x+width, ("1", '2', '3', '4','5','6','7','8'))
    ax.set_ylabel("NRMSE Ratio")
    ax.set_xlabel("Dataset ID")
    # ax.set_yscale('log')
    formatter = FuncFormatter(to_percent)
    # ax.yaxis.set_major_formatter(formatter)
    plt.subplots_adjust(bottom=0.15)
    plt.subplots_adjust(left=0.15)
    plt.ylim([0.95,1.5])

    plt.show()

def plt_qreg_classifier_selection(d="2d"):
    plt.rcParams.update({'font.size': 22})
    width = 0.20
    x = np.arange(1,6)
    if d =="2d":
        y1=[0.5082 , 0.3067, 0.3319,  0.4682, 0.4409]
        y2=[0.5082 , 0.5165, 0.6428,  0.4682, 0.5300]
        y3=[0.8005 , 0.5469, 0.6450,  0.5449, 0.5274]
    if d =="3d":
        y1=[0.3433, 0.4050 , 0.4112,  0.4487, 0.2787]
        y2=[0.3437, 0.4054 , 0.5706,  0.4201, 0.5284]
        y3=[0.8111, 0.5299 , 0.5888,  0.4782, 0.4984]
    if d =="4d":
        y1=[0.5052,  0.2706, 0.3557,  0.3258,  0.3553 ]
        y2=[0.5014,  0.4269, 0.5245,  0.4753,  0.4475 ]
        y3=[0.6885,  0.5418, 0.5220,  0.5425,  0.4249 ]
    if d =="5d":
        y1=[0.5916,  0.3303, 0.3133,  0.3139,  0.3424 ]
        y2=[0.4269,  0.4641, 0.4425,  0.5035,  0.4867 ]
        y3=[0.8402,  0.5131, 0.4524,  0.5419,  0.4722 ]

    # xx=[0.6,5.5]
    # yy=[1,1]

    fig, ax = plt.subplots()

    p1 = plt.bar(x, y1, color=colors["DBEst_10k"], width=width, alpha=alpha['2'])
    p2 = plt.bar(x+width, y2, color=colors["BlinkDB_10k"], width=width, alpha=alpha['5'])
    p3 = plt.bar(x+2*width, y3, color=colors["BlinkDB_1m"], width=width, alpha=alpha['3'])
    # plt.plot(xx,yy,alpha=0.2)
    plt.legend((p1[0], p2[0],p3[0]),
               ('SVM Linear Classifier','SVM RBF Classifier','XGBoost Classifier'), loc='upper right', prop={'size': 15})

    plt.xticks(x+1*width, ("1", '2', '3', '4','5'))
    ax.set_ylabel("Classification Accuracy")
    ax.set_xlabel("Dataset ID")
    # ax.set_yscale('log')
    formatter = FuncFormatter(to_percent)
    ax.yaxis.set_major_formatter(formatter)
    plt.subplots_adjust(bottom=0.18)
    plt.subplots_adjust(left=0.27)
    plt.ylim([0,1])

    plt.show()


def plt_qreg_model_training_time_ensemble():
    font_size=14
    x=[200,2000,20000,200000,2000000]
    X=[0.00523,0.0144,0.12209,1.09748,13.21596]
    G=[0.00834,0.01452,0.0636,0.58815,7.70868]
    C=[0.074486,0.322717,2.94475,31.227796,306.769922]
    plt.loglog(x,X,"x-",label="XGBoost")
    plt.loglog(x,G,"o-",label="GBoost")
    plt.loglog(x,C,"v-",label="QReg")
    plt.legend()
    plt.xlabel("Number of training points", fontsize=font_size)
    plt.ylabel("Training time (s)", fontsize=font_size)
    plt.tick_params(labelsize = font_size)

    plt.show()

def plt_qreg_model_training_time_base_models():
    font_size=14
    x=[100,1000,10000,100000,1000000]
    LR=[0.00056 ,    0.00061   ,  0.00073  ,   0.00221 ,    0.02457 ]
    PR=[0.00260  ,   0.00613   ,  0.02261  ,   0.57020  ,   8.13341 ]
    DTR=[0.00019,    0.00042 ,    0.00291  ,   0.02642  ,   0.26859 ]
    KNN=[0.00028  ,  0.00041  ,   0.00178  ,   0.01814  ,   0.56045 ]
    SVR=[0.00032 ,   0.01614  ,   1.21145  ,   1078.83512 ]
    Gaussian=[0.13289 ,  2.15688  ,   780.21678 ]
    plt.loglog(x,LR,"x-",label="LR")
    plt.loglog(x,PR,"o-",label="PR")
    plt.loglog(x,DTR,"v-",label="DTR")
    plt.loglog(x,KNN,"*-",label="KNN")
    plt.loglog(x[:-1],SVR,".-",label="SVR")
    plt.loglog(x[:-2],Gaussian,"h-",label="Gaussian")
    plt.legend()
    plt.xlabel("Number of training points", fontsize=font_size)
    plt.ylabel("Training time (s)", fontsize=font_size)
    plt.tick_params(labelsize = font_size)

    plt.show()

def plt_tpcds_multi_cp_relative_error_verdictdb_10k():
    plt.rcParams.update({'font.size': 12})
    width = 0.14
    # data = [
    #     [0.00829, 0.2673276,  0.03481, 0.0352, 0.04278, 0.05179, 0.07853, 0.07707],
    #     [0.09, 3.1,   0.22,  0.23, 0.22, 0.29, 0.053, 0.053],
    #     [1.13, 41.46232,  3.07, 3.08, 3.01, 4.66, 0.06, 0.06],
    #     [7.07, 200, 21.07,  21.13, 19.07, 26.44, 0.056, 0.056],
    # ]
    # data = [
    #     [0.00829, 0.12,  0.03481, 0.0352, 0.04278, 0.05179, 0.07853, 0.07707],
    #     [0.09, 1.2,   0.22,  0.23, 0.22, 0.29, 0.053, 0.053],
    #     [1.13, 24,  3.07, 3.08, 3.01, 4.66, 0.06, 0.06],
    #     [7.07, 0, 21.07,  21.13, 19.07, 26.44, 0.056, 0.056],
    # ]

    data = [
        [0.036729392, 0.147053419 ,0.01226814],
        [0.180193022, 0.19294517  ,0.016050075],
        [0.035590202, 0.085750906 ,0.010402393],
        [0.153588479, 0.10440603  ,0.021930002],
        [0.040999558, 0.090184777 ,0.014903902],
        [0.107200732, 0.139941919 ,0.017845218],
    ]



    X = np.arange(3)

    fig, ax = plt.subplots()

    p0 = plt.bar(
        X , data[0], color=colors["DBEst_10k"], width=width, alpha=alpha['2'])
    p1 = plt.bar(X + width, data[1], color=colors["BlinkDB_10k"],
                 width=width, alpha=alpha['2'])
    p2 = plt.bar(
        X + 2*width, data[2], color=colors["DBEst_100k"], width=width, alpha=alpha['3'])
    p3 = plt.bar(
        X + 3*width, data[3], color=colors["BlinkDB_100k"], width=width, alpha=alpha['4'])
    p4 = plt.bar(
        X + 4*width, data[4], color=colors["DBEst_1m"], width=width, alpha=alpha['5'])
    p5 = plt.bar(
        X + 5*width, data[5], color=colors["BlinkDB_1m"], width=width, alpha=alpha['6'])
    

    plt.legend((p0[0],p1[0], p2[0], p3[0],p4[0],p5[0]),
               ('DBEst_0.1%', 'VerdictDB_0.1%', 'DBEst_0.5%', 'VerdictDB_0.5%','DBEst_1%', 'VerdictDB_1%'), loc='1')

    plt.xticks(X + 2.5 * width, ("COUNT", 'SUM',
                                 'AVG', 'STDDEV', 'SUM', 'AVG', 'MIN', 'MAX'))
    ax.set_ylabel("Average Relative Error (%)")
    # ax.set_yscale('log')
    formatter = FuncFormatter(to_percent)
    ax.yaxis.set_major_formatter(formatter)

    # for item in ax.axes.get_xticklabels():
    #     item.set_rotation(60)
    plt.subplots_adjust(left=0.16)
    plt.subplots_adjust(bottom=0.08)

    plt.show()

def plt_tpcds_multi_cp_relative_error_verdictdb_100k():
    plt.rcParams.update({'font.size': 12})
    width = 0.14
    # data = [
    #     [0.00829, 0.2673276,  0.03481, 0.0352, 0.04278, 0.05179, 0.07853, 0.07707],
    #     [0.09, 3.1,   0.22,  0.23, 0.22, 0.29, 0.053, 0.053],
    #     [1.13, 41.46232,  3.07, 3.08, 3.01, 4.66, 0.06, 0.06],
    #     [7.07, 200, 21.07,  21.13, 19.07, 26.44, 0.056, 0.056],
    # ]
    # data = [
    #     [0.00829, 0.12,  0.03481, 0.0352, 0.04278, 0.05179, 0.07853, 0.07707],
    #     [0.09, 1.2,   0.22,  0.23, 0.22, 0.29, 0.053, 0.053],
    #     [1.13, 24,  3.07, 3.08, 3.01, 4.66, 0.06, 0.06],
    #     [7.07, 0, 21.07,  21.13, 19.07, 26.44, 0.056, 0.056],
    # ]

    data = [
        [0.013098367, 0.046292902, 0.015467639],
        [0.063509021, 0.097632026, 0.012282212],
        [0.040278354, 0.060049817, 0.01393817],
        [0.032710269, 0.044273866, 0.011985621],
        [0.044981284, 0.051119061, 0.006263069],
        [0.01956036 , 0.037487751, 0.014014555],
    ]




    X = np.arange(3)

    fig, ax = plt.subplots()

    p0 = plt.bar(
        X , data[0], color=colors["DBEst_10k"], width=width, alpha=alpha['2'])
    p1 = plt.bar(X + width, data[1], color=colors["BlinkDB_10k"],
                 width=width, alpha=alpha['2'])
    p2 = plt.bar(
        X + 2*width, data[2], color=colors["DBEst_100k"], width=width, alpha=alpha['3'])
    p3 = plt.bar(
        X + 3*width, data[3], color=colors["BlinkDB_100k"], width=width, alpha=alpha['4'])
    p4 = plt.bar(
        X + 4*width, data[4], color=colors["DBEst_1m"], width=width, alpha=alpha['5'])
    p5 = plt.bar(
        X + 5*width, data[5], color=colors["BlinkDB_1m"], width=width, alpha=alpha['6'])
    

    plt.legend((p0[0],p1[0], p2[0], p3[0],p4[0],p5[0]),
               ('DBEst_0.1%', 'VerdictDB_0.1%', 'DBEst_0.5%', 'VerdictDB_0.5%','DBEst_1%', 'VerdictDB_1%'), loc='1')

    plt.xticks(X + 2.5 * width, ("COUNT", 'SUM',
                                 'AVG', 'STDDEV', 'SUM', 'AVG', 'MIN', 'MAX'))
    ax.set_ylabel("Average Relative Error (%)")
    # ax.set_yscale('log')
    formatter = FuncFormatter(to_percent)
    ax.yaxis.set_major_formatter(formatter)

    # for item in ax.axes.get_xticklabels():
    #     item.set_rotation(60)
    plt.subplots_adjust(left=0.16)
    plt.subplots_adjust(bottom=0.08)

    plt.show()

def plt_tpcds_multi_cp_relative_error_verdictdb_0_1percent():
    plt.rcParams.update({'font.size': 12})
    width = 0.20

    data = [
        [0.036729392, 0.147053419, 0.01226814],
        [0.180193022, 0.19294517 , 0.016050075],
        [0.013098367, 0.046292902, 0.015467639],
        [0.063509021, 0.097632026, 0.012282212],
        
    ]
    X = np.arange(3)

    fig, ax = plt.subplots()

    p0 = plt.bar(
        X , data[0], color=colors["DBEst_10k"], width=width, alpha=alpha['2'])
    p1 = plt.bar(X + width, data[1], color=colors["BlinkDB_10k"],
                 width=width, alpha=alpha['2'])
    p2 = plt.bar(
        X + 2*width, data[2], color=colors["DBEst_100k"], width=width, alpha=alpha['3'])
    p3 = plt.bar(
        X + 3*width, data[3], color=colors["BlinkDB_100k"], width=width, alpha=alpha['4'])
    # p4 = plt.bar(
    #     X + 4*width, data[4], color=colors["DBEst_1m"], width=width, alpha=alpha['5'])
    # p5 = plt.bar(
    #     X + 5*width, data[5], color=colors["BlinkDB_1m"], width=width, alpha=alpha['6'])
    

    plt.legend((p0[0],p1[0], p2[0], p3[0]),
               ('DBEst_10k', 'VerdictDB_10k', 'DBEst_100k', 'VerdictDB_100k','DBEst_1%', 'VerdictDB_1%'), loc='1')

    plt.xticks(X + 1.5 * width, ("COUNT", 'SUM',
                                 'AVG', 'STDDEV', 'SUM', 'AVG', 'MIN', 'MAX'))
    ax.set_ylabel("Average Relative Error (%)")
    # ax.set_yscale('log')
    formatter = FuncFormatter(to_percent)
    ax.yaxis.set_major_formatter(formatter)

    # for item in ax.axes.get_xticklabels():
    #     item.set_rotation(60)
    plt.subplots_adjust(left=0.16)
    plt.subplots_adjust(bottom=0.08)

    plt.show()

def plt_tpcds_multi_cp_response_time_verdictdb():
    plt.rcParams.update({'font.size': 12})
    width = 0.30

    data = [
        [0.015702787, 0.114711777],
        [0.333533842, 0.420013472], 
    ]



    X = np.arange(2)

    fig, ax = plt.subplots()

    p0 = plt.bar(
        X , data[0], color=colors["DBEst_10k"], width=width, alpha=alpha['2'])
    p1 = plt.bar(X + width, data[1], color=colors["BlinkDB_10k"],
                 width=width, alpha=alpha['4'])
    # p2 = plt.bar(
    #     X + 2*width, data[2], color=colors["DBEst_100k"], width=width, alpha=alpha['3'])
    # p3 = plt.bar(
    #     X + 3*width, data[3], color=colors["BlinkDB_100k"], width=width, alpha=alpha['4'])
    # p4 = plt.bar(
    #     X + 4*width, data[4], color=colors["DBEst_1m"], width=width, alpha=alpha['5'])
    # p5 = plt.bar(
    #     X + 5*width, data[5], color=colors["BlinkDB_1m"], width=width, alpha=alpha['6'])
    

    plt.legend((p0[0],p1[0]),
               ('DBEst', 'VerdictDB', 'DBEst_100k', 'VerdictDB_100k','DBEst_1%', 'VerdictDB_1%'), loc='1')

    plt.xticks(X + 0.5 * width, ("10k", '100k',
                                 'AVG', 'STDDEV', 'SUM', 'AVG', 'MIN', 'MAX'))
    ax.set_ylabel("Qeury Response Time (s)")
    # ax.set_yscale('log')
    formatter = FuncFormatter(to_percent)
    # ax.yaxis.set_major_formatter(formatter)

    # for item in ax.axes.get_xticklabels():
    #     item.set_rotation(60)
    plt.subplots_adjust(left=0.16)
    plt.subplots_adjust(bottom=0.08)

    plt.show()

def plt_parallel_response_time_groups():
    plt.rcParams.update({'font.size': 18})
    width = 0.40
    data = [
        [1.46, 0.57, 0.82],  # , 0.0486],
        # [66.4,  102.4 ],#, 0.0335],
    ]

    X = np.arange(3)

    fig, ax = plt.subplots()

    p1 = plt.bar(X, data[0], color=colors["DBEst_10k"], width=width, alpha=alpha['4'])
    # p2 = plt.bar(X + width, data[1], color=colors["BlinkDB_10k"], width=width)
    # p3 = plt.bar(X + 0.30, data[2], color=colors["BlinkDB_10k"], width=width)

    # plt.legend((p1[0]),
    #     ('DBEst', 'BlinkDB','BlinkDB Sampling','BlinkDB_100k'), loc='center', prop={'size': 18})

    # p1[0].set_color('r')
    p1[1].set_color(colors["DBEst_100k"])
    p1[2].set_color(colors["BlinkDB_10k"])

    plt.xticks(X, ("DBEst","DBEst_parallel", 'VerdictDB', 'AVG', 'OVERALL'))
    ax.set_ylabel("Query Response Time (s)")
    # ax.set_xlabel("Sample Size")
    # ax.set_yscale('log')
    formatter = FuncFormatter(to_percent)
    # ax.yaxis.set_major_formatter(formatter)
    plt.subplots_adjust(bottom=0.10)
    plt.subplots_adjust(left=0.16)

    plt.show()

def plt_tpcds_concurrent():
    plt.rcParams.update({'font.size': 12})
    # width = 0.30
    x= [1,2,4,6,8,10,12]
    #tpcds
    data = [
        [30.72 ,  30.10 ,  30.14 , 29.54,  29.79 ,  29.37 ,  29.54],
        [32.00 ,  31.77 ,  30.56 , 30.18,  30.09 ,  30.42 ,  30.37],
        [3.76  ,  2.42  ,  1.35  , 0.96 ,  0.83  ,  0.82  ,  0.75],
        [23.45 ,  14.68 ,  7.83  , 5.83 ,  4.15  ,  3.79  ,  3.07]
    ]
    #ccpp
    data = [
        [64.93 , 61.33  , 61.46 ,  61.53 , 61.45 , 60.97 , 60.96 ],
        [62.19 , 60.36  , 60.37 ,  60.41 , 60.66 , 60.08 , 60.02 ],
        [4.60  , 2.85   , 1.60  ,  1.49  , 1.01  , 1.03  , 0.92 ],
        [35.38 , 20.99  , 11.46 ,  9.85  , 7.31  , 7.75  , 5.78 ]
    ]

    #pm2.5 beijing
    data = [
        [21.42 ,  20.74 , 20.43 , 20.05  , 20.54 ,  19.96 ,  19.24 ],
        [35.31 ,  22.39 , 20.91 , 20.75  , 20.48 ,  20.45 ,  20.40 ],
        [1.99  ,  1.22  , 0.70  , 0.61   , 0.47  ,  0.41  ,  0.36 ],
        [22.96 ,  13.88 , 8.86  , 7.41   , 6.09  ,  4.77  ,  4.63 ]
    ]


    fig, ax = plt.subplots()

    p0 = plt.plot(x, data[0], '*-',color=colors["BlinkDB_100k"], alpha=alpha['5'],linewidth=3)
    p1 = plt.plot(x, data[1], 'x-',color=colors["BlinkDB_10k"],alpha=alpha['4'],linewidth=3)
    p2 = plt.plot(x, data[2], '^-',color=colors["DBEst_100k"], alpha=alpha['3'],linewidth=3)
    p3 = plt.plot(x, data[3], '.-',color=colors["DBEst_10k"],alpha=alpha['2'],linewidth=3)
    # p2 = plt.bar(
    #     X + 2*width, data[2], color=colors["DBEst_100k"], width=width, alpha=alpha['3'])
    # p3 = plt.bar(
    #     X + 3*width, data[3], color=colors["BlinkDB_100k"], width=width, alpha=alpha['4'])
    # p4 = plt.bar(
    #     X + 4*width, data[4], color=colors["DBEst_1m"], width=width, alpha=alpha['5'])
    # p5 = plt.bar(
    #     X + 5*width, data[5], color=colors["BlinkDB_1m"], width=width, alpha=alpha['6'])
    

    plt.legend((p0[0],p1[0],p2[0],p3[0]),
               ('VerdictDB_10k', 'VerdictDB_100k', 'DBEst_10k', 'DBEst_100k','DBEst_1%', 'VerdictDB_1%'), loc='1')

    # plt.xticks(X + 0.5 * width, ("10k", '100k',
                                 # 'AVG', 'STDDEV', 'SUM', 'AVG', 'MIN', 'MAX'))
    ax.set_ylabel("Total Qeury Response Time (s)")
    ax.set_xlabel("Number of Processes")
    # ax.set_yscale('log')
    formatter = FuncFormatter(to_percent)
    # ax.yaxis.set_major_formatter(formatter)

    # for item in ax.axes.get_xticklabels():
    #     item.set_rotation(60)
    plt.subplots_adjust(left=0.13)
    plt.subplots_adjust(bottom=0.15)

    plt.show()

def plt_join_relative_error():
    plt.rcParams.update({'font.size': 12})
    width = 0.20
    data = [
        [0.060441958, 0.059393945, 0.014499711],  # , 0.0486],
        [0.040392629, 0.038002761, 0.005210391],  # , 0.0335],
        [0.033410668, 0.033225831, 0.000853844],  # , 0.0182],
        [0.024687999, 0.001692054, 0.023323738]  # , 0.0212]
    ]

    data=[
        [0.060441958, 0.059393945, 0.014499711, 0.044778538],
        [0.040392629, 0.038002761, 0.005210391, 0.027868594],
        [0.033410668, 0.033225831, 0.000853844, 0.022496781],
        [0.024687999, 0.001692054, 0.023323738, 0.01656793]
    ]





    X = np.arange(4)

    fig, ax = plt.subplots()

    p1 = plt.bar(
        X + 0.00, data[0], color=colors["DBEst_10k"], width=width, alpha=alpha['2'])
    p2 = plt.bar(
        X + 0.20, data[1], color=colors["DBEst_100k"], width=width, alpha=alpha['3'])
    p3 = plt.bar(
        X + 0.40, data[2], color=colors["DBEst_1m"], width=width, alpha=alpha['4'])
    p4 = plt.bar(
        X + 0.60, data[3], color=colors["BlinkDB_100k"], width=width, alpha=alpha['6'])

    plt.legend((p1[0], p2[0], p3[0], p4[0]),
               ('DBEst_10k', 'DBEst_100k', 'DBEst_1m', 'VerdictDB_10m'), loc='upper center')

    plt.xticks(X + 1.5 * width, ("COUNT", 'SUM', 'AVG', 'OVERALL'))
    ax.set_ylabel("Relative Error (%)")
    # ax.set_yscale('log')
    formatter = FuncFormatter(to_percent)
    ax.yaxis.set_major_formatter(formatter)
    plt.subplots_adjust(bottom=0.07)
    # plt.subplots_adjust(left=0.23)

    plt.show()

def plt_join_memory_cost_comparison():
    plt.rcParams.update({'font.size': 18})
    width = 0.40
    data = [
        [0.373182,   0.746372,    1.119562,    271.8],  # , 0.0486],
        # [66.4,  102.4 ],#, 0.0335],
    ]

    X = np.arange(4)

    fig, ax = plt.subplots()

    p1 = plt.bar(X, data[0], color=colors["DBEst_10k"], width=width)
    # p2 = plt.bar(X + width, data[1], color=colors["BlinkDB_10k"], width=width)
    # p3 = plt.bar(X + 0.30, data[2], color=colors["BlinkDB_10k"], width=width)

    # plt.legend((p1[0]),
    #     ('DBEst', 'BlinkDB','BlinkDB Sampling','BlinkDB_100k'), loc='center', prop={'size': 18})

    # p1[0].set_color('r')
    p1[1].set_color(colors["DBEst_100k"])
    p1[2].set_color(colors["DBEst_1m"])
    p1[3].set_color(colors["BlinkDB_10k"])

    plt.xticks(X, ("DBEst_10k", 'DBEst_100k', 'DBEst_1m', 'VerdictDB_10m'))
    ax.set_ylabel("Space Overhead (MB)")
    # ax.set_xlabel("Sample Size")
    ax.set_yscale('log')
    formatter = FuncFormatter(to_percent)
    # ax.yaxis.set_major_formatter(formatter)
    plt.subplots_adjust(bottom=0.40)
    plt.subplots_adjust(left=0.18)
    for item in ax.axes.get_xticklabels():
        item.set_rotation(60)

    plt.show()

def plt_join_response_time():
    plt.rcParams.update({'font.size': 18})
    width = 0.40
    data = [
        [0.028452611,    0.103724667, 0.825308944, 5.40],  # , 0.0486],
        # [66.4,  102.4 ],#, 0.0335],
    ]

    X = np.arange(4)
    

    fig, ax = plt.subplots()

    p1 = plt.bar(X, data[0], color=colors["DBEst_10k"], width=width)
    # p2 = plt.bar(X + width, data[1], color=colors["BlinkDB_10k"], width=width)
    # p3 = plt.bar(X + 0.30, data[2], color=colors["BlinkDB_10k"], width=width)

    # plt.legend((p1[0]),
    #     ('DBEst', 'BlinkDB','BlinkDB Sampling','BlinkDB_100k'), loc='center', prop={'size': 18})

    # p1[0].set_color('r')
    p1[1].set_color(colors["DBEst_100k"])
    p1[2].set_color(colors["DBEst_1m"])
    p1[3].set_color(colors["BlinkDB_10k"])

    plt.xticks(X, ("DBEst_10k", 'DBEst_100k', 'DBEst_1m', 'VerdictDB_10m'))
    ax.set_ylabel("Query Response Time (s)")
    # ax.set_xlabel("Sample Size")
    ax.set_yscale('log')
    formatter = FuncFormatter(to_percent)
    # ax.yaxis.set_major_formatter(formatter)
    plt.subplots_adjust(bottom=0.40)
    plt.subplots_adjust(left=0.18)
    for item in ax.axes.get_xticklabels():
        item.set_rotation(60)

    plt.show()

def plt_tpcds_single_cp_memory_cost_comparison_verdict():
    plt.rcParams.update({'font.size': 22})
    fig, ax = plt.subplots()
    

    y1 = [0.040,  0.192,  1.684,   18.436]
    y2 = [0.791,  1.700,  9.700,   70.300]
 
 

    
    x = [1E4, 1E5, 1E6, 5E6, 26E6]
    x = [1E3,1E4, 1E5, 1E6]
    p1 = plt.plot(x, y1, 'rx-')
    p2 = plt.plot(x, y2, 'gh-')

    plt.legend((p1[0], p2[0]),
               ('DBEst', 'VerdictDB'), loc='1')

    ax.set_xlabel("Sample Size")
    ax.set_ylabel("Space Overhead (MB)")

    plt.xticks([5E6, 26E6], ('5m', '26m'))
    ax.set_xscale('log')
    ax.set_yscale('log')

    plt.subplots_adjust(bottom=0.16)
    plt.subplots_adjust(left=0.20)

    plt.show()


def plt_pm25_relative_error():
    plt.rcParams.update({'font.size': 12})
    width = 0.14
    # data = [
    #     [0.00829, 0.2673276,  0.03481, 0.0352, 0.04278, 0.05179, 0.07853, 0.07707],
    #     [0.09, 3.1,   0.22,  0.23, 0.22, 0.29, 0.053, 0.053],
    #     [1.13, 41.46232,  3.07, 3.08, 3.01, 4.66, 0.06, 0.06],
    #     [7.07, 200, 21.07,  21.13, 19.07, 26.44, 0.056, 0.056],
    # ]
    # data = [
    #     [0.00829, 0.12,  0.03481, 0.0352, 0.04278, 0.05179, 0.07853, 0.07707],
    #     [0.09, 1.2,   0.22,  0.23, 0.22, 0.29, 0.053, 0.053],
    #     [1.13, 24,  3.07, 3.08, 3.01, 4.66, 0.06, 0.06],
    #     [7.07, 0, 21.07,  21.13, 19.07, 26.44, 0.056, 0.056],
    # ]

    data = [
        [0.013098367, 0.046292902, 0.015467639],
        [0.063509021, 0.097632026, 0.012282212],
        [0.040278354, 0.060049817, 0.01393817],
        [0.032710269, 0.044273866, 0.011985621],
        [0.044981284, 0.051119061, 0.006263069],
        [0.01956036 , 0.037487751, 0.014014555],
    ]
    data = [
        [0.0354,  0.0378,  0.0685,  0.0472],
        [0.0909,  0.0808,  0.1154,  0.0957],
        [0.0195,  0.0152,  0.0155,  0.0167],
        [0.0501,  0.0252,  0.0571,  0.0441],
        # [0.0150,  0.0052,  0.0144,  0.0115],
        # [0.0119,  0.0096,  0.0120,  0.0112],
    ]
 
    X = np.arange(4)

    fig, ax = plt.subplots()

    p0 = plt.bar(
        X , data[0], color=colors["DBEst_10k"], width=width, alpha=alpha['2'])
    p1 = plt.bar(X + width, data[1], color=colors["BlinkDB_10k"],
                 width=width, alpha=alpha['2'])
    p2 = plt.bar(
        X + 2*width, data[2], color=colors["DBEst_100k"], width=width, alpha=alpha['3'])
    p3 = plt.bar(
        X + 3*width, data[3], color=colors["BlinkDB_100k"], width=width, alpha=alpha['4'])
    # p4 = plt.bar(
    #     X + 4*width, data[4], color=colors["DBEst_1m"], width=width, alpha=alpha['5'])
    # p5 = plt.bar(
    #     X + 5*width, data[5], color=colors["BlinkDB_1m"], width=width, alpha=alpha['6'])
    

    plt.legend((p0[0],p1[0], p2[0], p3[0]),
               ('DBEst_10k', 'VerdictDB_10k', 'DBEst_100k', 'VerdictDB_100k','DBEst_1m', 'VerdictDB_1m'), loc='upper left')

    plt.xticks(X + 2.5 * width, ("COUNT", 'SUM',
                                 'AVG', 'OVERALL', 'SUM', 'AVG', 'MIN', 'MAX'))
    ax.set_ylabel("Average Relative Error (%)")
    # ax.set_yscale('log')
    formatter = FuncFormatter(to_percent)
    ax.yaxis.set_major_formatter(formatter)

    # for item in ax.axes.get_xticklabels():
    #     item.set_rotation(60)
    plt.subplots_adjust(left=0.16)
    plt.subplots_adjust(bottom=0.08)
    for item in ax.axes.get_xticklabels():
        item.set_rotation(60)

    plt.show()

def plt_pm25_response_time():
    plt.rcParams.update({'font.size': 12})
    width = 0.14
    # data = [
    #     [0.00829, 0.2673276,  0.03481, 0.0352, 0.04278, 0.05179, 0.07853, 0.07707],
    #     [0.09, 3.1,   0.22,  0.23, 0.22, 0.29, 0.053, 0.053],
    #     [1.13, 41.46232,  3.07, 3.08, 3.01, 4.66, 0.06, 0.06],
    #     [7.07, 200, 21.07,  21.13, 19.07, 26.44, 0.056, 0.056],
    # ]
    # data = [
    #     [0.00829, 0.12,  0.03481, 0.0352, 0.04278, 0.05179, 0.07853, 0.07707],
    #     [0.09, 1.2,   0.22,  0.23, 0.22, 0.29, 0.053, 0.053],
    #     [1.13, 24,  3.07, 3.08, 3.01, 4.66, 0.06, 0.06],
    #     [7.07, 0, 21.07,  21.13, 19.07, 26.44, 0.056, 0.056],
    # ]

    data = [
        [0.013098367, 0.046292902, 0.015467639],
        [0.063509021, 0.097632026, 0.012282212],
        [0.040278354, 0.060049817, 0.01393817],
        [0.032710269, 0.044273866, 0.011985621],
        # [0.044981284, 0.051119061, 0.006263069],
        # [0.01956036 , 0.037487751, 0.014014555],
    ]
    data = [
        [0.0095,  0.0141,  0.0172,  0.0136],
        [0.5851,  0.4153,  0.3815,  0.4606],
        [0.0940,  0.2231,  0.2060,  0.1744],
        [0.3167,  0.3150,  0.3269,  0.3195],
        # [1.4844 ,  2.7403,  2.6527,  2.29],
        # [0.3887,  0.4176,  0.4089,  0.4051],
    ]


 
 

 
    X = np.arange(4)

    fig, ax = plt.subplots()

    p0 = plt.bar(
        X , data[0], color=colors["DBEst_10k"], width=width, alpha=alpha['2'])
    p1 = plt.bar(X + width, data[1], color=colors["BlinkDB_10k"],
                 width=width, alpha=alpha['2'])
    p2 = plt.bar(
        X + 2*width, data[2], color=colors["DBEst_100k"], width=width, alpha=alpha['3'])
    p3 = plt.bar(
        X + 3*width, data[3], color=colors["BlinkDB_100k"], width=width, alpha=alpha['4'])
    # p4 = plt.bar(
    #     X + 4*width, data[4], color=colors["DBEst_1m"], width=width, alpha=alpha['5'])
    # p5 = plt.bar(
    #     X + 5*width, data[5], color=colors["BlinkDB_1m"], width=width, alpha=alpha['6'])
    

    plt.legend((p0[0],p1[0], p2[0], p3[0]),
               ('DBEst_10k', 'VerdictDB_10k', 'DBEst_100k', 'VerdictDB_100k','DBEst_1m', 'VerdictDB_1m'), loc='upper left')

    plt.xticks(X + 2.5 * width, ("COUNT", 'SUM',
                                 'AVG', 'OVERALL', 'SUM', 'AVG', 'MIN', 'MAX'))
    ax.set_ylabel("Average Response Time (s)")
    ax.set_yscale('log')
    formatter = FuncFormatter(to_percent)
    # ax.yaxis.set_major_formatter(formatter)

    # for item in ax.axes.get_xticklabels():
    #     item.set_rotation(60)
    plt.subplots_adjust(left=0.16)
    plt.subplots_adjust(bottom=0.08)

    for item in ax.axes.get_xticklabels():
        item.set_rotation(60)

    plt.show()

##----------------------------------------------------------------------------------------##
if __name__ == "__main__":
    plt_qreg_simple_accuracy_d(d='5d')
