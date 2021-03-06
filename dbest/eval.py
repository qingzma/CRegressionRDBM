import re
import sys
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import numpy as np
import matplotlib.pyplot as plt
import matplotlib._color_data as mcd
import matplotlib.patches as mpatch

overlap = {name for name in mcd.CSS4_COLORS
           if "xkcd:" + name in mcd.XKCD_COLORS}

font_size = 14 #14
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

def to_percent(y, pos):
    return '%.1f%%' % (y * 100)

def read_results(file, b_remove_null=True, counts_group_in_sample=None,counts_group_in_original=None,func=None,split_char="\s"):
    """read the group by value and the corresponding aggregate within
    a given range, used to compare the accuracy.the

    Output: a dict contating the 

    Args:
        file (file): path to the file
    """

    key_values = {}
    with open(file) as f:
        # print("Start reading file " + file)
        index = 1
        for line in f:
            # ignore empty lines
            if  line.strip():
                key_value = line.replace(
                    "(", " ").replace(")", " ").replace(";", "").replace("\n","")#.replace(",", "")
                # self.logger.logger.info(key_value)
                key_value = re.split(split_char, key_value)
                if key_value[0] == "":
                    continue
                # remove empty strings caused by sequential blank spaces.
                key_value = list(filter(None, key_value))
                if key_value[0] !='0':
                    if counts_group_in_sample == None:
                        # print(key_value[0])
                        # print(key_value[1])
                        key_value[0]=key_value[0].replace(",","")
                        key_values[key_value[0]] = key_value[1]
                    else:
                        # print(key_value[0])
                        # print(counts_group_in_sample)
                        count_sample=float(counts_group_in_sample[key_value[0]])
                        count_original=float(counts_group_in_original[key_value[0]])
                        if func == 'avg':
                            key_values[key_value[0]] = float(key_value[1])
                        else:
                            # print(float(key_value[1]))
                            # print("-----------------")
                            key_values[key_value[0]] = float(key_value[1])*count_original/count_sample
                        # print(count)
                        # print(key_value[1])
                        # print(count*key_value[1])
                        # print("--------------------------------")
                        # return
                        
                        # print(key_values[key_value[0]])
                        # return
                else:
                    continue
    if ('NULL' in key_values) and b_remove_null:
        key_values.pop('NULL', None)
    if ('0' in key_values) and b_remove_null:
        key_values.pop('0', None)


    key_values.pop('9.0', None)
    # print(key_values)
    return key_values


def avg_relative_error(ground_truth, predictions):
    """calculate the relative error between ground truth and predictions

    Args:
        ground_truth (dict): the ground truth, with keys and values
        predictions (dict): the predictions, with keys and values

    Returns:
        float: the average relative error 
    """
    # if len(ground_truth) != len(predictions):
    #     print("Length mismatch!")
    #     print("Length of ground_truth is " + str(len(ground_truth)))
    #     print("Length of predictions is " + str(len(predictions)))
    #     print("System aborts!")
    #     sys.exit(1)

    relative_errors = []
    # ground_truth.pop('9.0', None)
    # ground_truth.pop('NULL', None)
    # print(ground_truth)
    # print(predictions)
    for key_gt, value_gt in ground_truth.items():
        if (ground_truth[key_gt] != 0):
            re = abs(float(ground_truth[key_gt]) -
                     float(predictions[key_gt])) / float(ground_truth[key_gt])
            # print(key_gt + str(re))
            relative_errors.append(re)
        else:
            print(
                "Zero is found in ground_truth, so removed to calculate relative error.")
    # print(sum(relative_errors))
    # print((relative_errors))
    # print(len(relative_errors))
    return sum(relative_errors) / len(relative_errors)

def avg_relative_errors():
    # averag_errors_blinkdb=[]
    averag_errors_DBEst=[]
    # averag_errors_mysql=[]
    averag_errors_verdict=[]
    
    # counts_group_in_sample = read_results('../data/tpcds5m/mysql/group_count_in_sample.txt')
    # counts_group_in_original = read_results('../data/tpcds5m/num_of_points.csv')

    for func in ['count','sum','avg']:
        print("---------------------"+func+"---------------------")
        # errors_blinkdb = []
        errors_DBEst = []
        # errors_mysql = []
        errors_verdict = []
        for index in range(1,11):
            file_name=func+str(int(index))
            ground_truth = read_results('../data/tpcds40g/groundtruth/'+file_name+'.txt',split_char=',')
            # predictions_blinkdb = read_results('../data/tpcds5m/blinkdb/'+file_name+'.txt') #../data/tpcds5m/blinkdb/sum1.txt
            predictions_DBEst = read_results('../data/tpcds40g/dbest/'+file_name+'.txt',split_char=',')
            # predictions_mysql = read_results('../data/tpcds5m/mysql/'+file_name+'.txt',
                # counts_group_in_sample=counts_group_in_sample,
                # counts_group_in_original=counts_group_in_original,
                # func=func)
            # save_dic(predictions_mysql, file='../data/tpcds5m/mysql/5m_predictions.txt')
            
            predictions_verdict = read_results('../data/tpcds40g/verdictdb6m/'+file_name+'.txt',split_char=",")


            # errors_blinkdb.append(avg_relative_error(ground_truth,predictions_blinkdb))
            errors_DBEst.append(avg_relative_error(ground_truth,predictions_DBEst))
            # errors_mysql.append(avg_relative_error(ground_truth,predictions_mysql))
            errors_verdict.append(avg_relative_error(ground_truth,predictions_verdict))

            # print("averge is "+str(sum(errors_DBEst)/len(errors_DBEst)))
        # averag_errors_blinkdb.append(sum(errors_blinkdb)/len(errors_blinkdb))
        averag_errors_DBEst.append(sum(errors_DBEst)/len(errors_DBEst))
        # averag_errors_mysql.append(sum(errors_mysql)/len(errors_mysql))
        averag_errors_verdict.append(sum(errors_verdict)/len(errors_verdict))
        
        
    # print(averag_errors_blinkdb)
    print(averag_errors_DBEst)
    # print(averag_errors_mysql)
    print(averag_errors_verdict)

def avg_relative_errors_per_group_value(group_num=501,function='count',size="100k"):
    res_per_group_DBEst={}
    res_per_group_blinkdb={}
    for func in ['count','sum','avg']:
        print("---------------------"+func+"---------------------")
        res_per_group_DBEst[func]=[]
        res_per_group_blinkdb[func]=[]
        
        re_per_group_DBEst={}
        re_per_group_blinkdb={}
        for index in range(1,11):
            print("Query Number: "+str(index)+"------------------")
            file_name=func+str(int(index))
            if group_num == 8:
                if size=="100k":
                    ground_truth = read_results('../data/tpcds_groupby_few_groups/groundtruth/'+file_name+'.result')
                    # predictions_blinkdb = read_results('../data/tpcds_groupby_few_groups/blinkdb_100k_new/'+file_name+'.txt') #../data/tpcds5m/blinkdb/sum1.txt
                    predictions_blinkdb = read_results('../data/tpcds_groupby_few_groups/blinkdb_100k_new/'+file_name+'.txt')
                    predictions_DBEst = read_results('../data/tpcds_groupby_few_groups/DBEst_integral_100k/'+file_name+'.txt')
                if size=="1m":
                    ground_truth = read_results('../data/tpcds_groupby_few_groups/groundtruth/'+file_name+'.result')
                    predictions_blinkdb = read_results('../data/tpcds_groupby_few_groups/blinkdb_1m_new/'+file_name+'.txt') #../data/tpcds5m/blinkdb/sum1.txt
                    predictions_DBEst = read_results('../data/tpcds_groupby_few_groups/DBEst_integral_1m/'+file_name+'.txt')
            if group_num == 501:
                # ground_truth = read_results('../data/tpcds5m/groundtruth/'+file_name+'.result')
                # predictions_blinkdb = read_results('../data/tpcds5m/blinkdb/'+file_name+'.txt') #../data/tpcds5m/blinkdb/sum1.txt
                # predictions_DBEst = read_results('../data/tpcds5m/DBEst_integral/'+file_name+'.txt')
                ground_truth = read_results('../data/tpcds40g/groundtruth/'+file_name+'.txt',split_char=',')
                # predictions_blinkdb = read_results('../data/tpcds5m/DBEst_integral/xgboost/'+file_name+'.txt') #../data/tpcds5m/blinkdb/sum1.txt
                predictions_blinkdb = read_results('../data/tpcds40g/verdictdb6m/'+file_name+'.txt',split_char=',')
                predictions_DBEst = read_results('../data/tpcds40g/dbest/'+file_name+'.txt',split_char=',')
            
            for group_id in  ground_truth:
                # print(group_id)
                if index == 1:  #initialize the error as an empty list, so as to contain further error for the same group
                    re_per_group_DBEst[group_id] = []
                    re_per_group_blinkdb[group_id] =[]

                re_per_group_DBEst[group_id].append(abs(float(predictions_DBEst[group_id])-float(ground_truth[group_id]))/float(ground_truth[group_id]))
                re_per_group_blinkdb[group_id].append(abs(float(predictions_blinkdb[group_id])-float(ground_truth[group_id]))/float(ground_truth[group_id]))

        for group_id in re_per_group_DBEst:
            avg_re_DBEst=sum(re_per_group_DBEst[group_id])/len(re_per_group_DBEst[group_id])
            avg_re_blinkdb=sum(re_per_group_blinkdb[group_id])/len(re_per_group_blinkdb[group_id])

            res_per_group_DBEst[func].append(avg_re_DBEst)
            res_per_group_blinkdb[func].append(avg_re_blinkdb)
        # averag_errors_blinkdb.append(sum(errors_blinkdb)/len(errors_blinkdb))
        # averag_errors_DBEst.append(sum(errors_DBEst)/len(errors_DBEst))
        
       
    # print(res_per_group_DBEst)
    # print(res_per_group_blinkdb)

    
    
    if group_num == 501:
        plt_histogram2(res_per_group_DBEst[function],res_per_group_blinkdb[function],title=function)
    if group_num == 8:
        plt_bar(res_per_group_DBEst[function],res_per_group_blinkdb[function],size)

    return res_per_group_DBEst, res_per_group_blinkdb
    

def plt_bar(x1,x2,size="100k"):
    plt.rcParams.update({'font.size': 12})
    width = 0.20
    

    X = np.arange(8)
  
    fig, ax = plt.subplots()

    p1 = plt.bar(X + 0.00, x1, color=colors["DBEst_10k"], width=width,alpha=alpha["2"])
    p2 = plt.bar(X + 0.20, x2, color=colors["BlinkDB_10k"], width=width,alpha=alpha["6"])
    # p3 = plt.bar(X + 0.40, data[2], color=colors["DBEst_100k"], width=width)
    # p4 = plt.bar(X + 0.60, data[3], color=colors["BlinkDB_100k"], width=width)

    if size == "100k":
        plt.legend((p1[0], p2[0]),
            ('DBEst_1o0k', 'BlinkDB_100k','DBEst_100k','BlinkDB_100k'), loc='1')
    if size =="1m":
        plt.legend((p1[0], p2[0]),
            ('DBEst_1m', 'BlinkDB_1m','DBEst_100k','BlinkDB_100k'), loc='1')
    plt.xticks(X+0.5*width, ("1", '2','3','4',"5", '6','7','8'))
    ax.set_ylabel("Relative Error (%)")
    ax.set_xlabel("Group By ID")
    # ax.set_yscale('log')
    formatter = FuncFormatter(to_percent)
    ax.yaxis.set_major_formatter(formatter)
    plt.subplots_adjust(bottom=0.10)
    plt.subplots_adjust(left=0.13)

    plt.show()


def plt_bar4(x1,x2,x3,x4,function="count"):
    plt.rcParams.update({'font.size': 12})
    width = 0.20
    

    X = np.arange(8)
  
    fig, ax = plt.subplots()

    p1 = plt.bar(X + 0.00, x1, color=colors["DBEst_10k"], width=width,alpha=alpha["2"])
    p2 = plt.bar(X + 0.20, x2, color=colors["BlinkDB_10k"], width=width,alpha=alpha["3"])
    p3 = plt.bar(X + 0.40, x3, color=colors["DBEst_100k"], width=width,alpha=alpha["4"])
    p4 = plt.bar(X + 0.60, x4, color=colors["BlinkDB_100k"], width=width,alpha=alpha["6"])

    
    plt.legend((p1[0], p2[0],p3[0], p4[0]),
        ('DBEst_100k', 'BlinkDB_100k','DBEst_1m','BlinkDB_1m'), loc='1')
    
    plt.xticks(X+0.5*width, ("1", '2','3','4',"5", '6','7','8'))
    ax.set_ylabel("Relative Error (%)")
    ax.set_xlabel("Group By ID")
    # ax.set_yscale('log')
    formatter = FuncFormatter(to_percent)
    ax.yaxis.set_major_formatter(formatter)
    plt.subplots_adjust(bottom=0.10)
    plt.subplots_adjust(left=0.13)

    plt.show()



def plt_histogram2(x1,x2,b_cumulative=False,title=None):

    plt.rcParams.update({'font.size': 12})
    x1.sort()
    x2.sort()

    fig, ax = plt.subplots()
    # p1 = plt.hist(x1,501,normed=1,cumulative=b_cumulative,color=colors["DBEst_1m"],alpha=0.3, label='DBEst')
    # p2 = plt.hist(x2,501,normed=1,cumulative=b_cumulative,color=colors["BlinkDB_1m"],alpha=0.7, label='BlinkDB')
    n_bar=57
    p1 = plt.hist(x1,n_bar,normed=1,cumulative=b_cumulative,color=colors["DBEst_1m"],alpha=0.3, label='DBEst')
    p2 = plt.hist(x2,n_bar,normed=1,cumulative=b_cumulative,color=colors["BlinkDB_1m"],alpha=0.7, label='VerdictDB')

    plt.legend( loc='1')
    # plt.legend((p1[0], p2[0]),
    #     ('DBEst_10k', 'BlinkDB_10k','DBEst_100k','BlinkDB_100k'), loc='1')

    # plt.xlim(0,0.062)
    # plt.ylim(0,1)
    formatter = FuncFormatter(to_percent)
    ax.xaxis.set_major_formatter(formatter)
    # ax.yaxis.set_major_formatter(formatter)
    plt.xlabel("Relative Error (%)")
    # plt.ylabel("Cumulative Probability")
    plt.ylabel("Number of Occurence")
    plt.subplots_adjust(bottom=0.12)
    plt.subplots_adjust(left=0.16)
    if title !=None:
        plt.title(title)


    
    plt.show()
    # fig.savefig("/home/u1796377/Desktop/figures/group_by_histgram.pdf", bbox_inches='tight')

def save_dic(dic,file):
    with open(file,mode='w+') as f:
        for key in dic:
            f.write(key+'\t'+str(dic[key])+'\n')

def process_mysql_result(file,sample_size, data_size):
    index = 0
    results=[]
    with open(file,mode='r') as f:
        for line in f:
            if "(y)" not in line:
                line=line.replace("\n","")
                results.append(float(line))
    # print(results[0:36])
    counts = [count * data_size / sample_size for count in results[0:36]]
    # print(results[36:72])
    sums = [sum_i * data_size / sample_size for sum_i in results[36:72]]
    print("-------------------------------------")
    print(file)
    print(counts)
    print(sums)
    print(results[72:108])
    print("-------------------------------------")
    print()
    return results
def process_mysql_results():
    files=[
        "../query/zipf/mysql/plain0.1_100k.dbest.result",
        "../query/zipf/mysql/plain0.1_10k.dbest.result",
        "../query/zipf/mysql/plain0.1_1m.dbest.result",
        "../query/zipf/mysql/plain1_100k.dbest.result",
        "../query/zipf/mysql/plain1_10k.dbest.result",
        "../query/zipf/mysql/plain1_1m.dbest.result",
        "../query/zipf/mysql/sharp0.1_100k.dbest.result",
        "../query/zipf/mysql/sharp0.1_10k.dbest.result",
        "../query/zipf/mysql/sharp0.1_1m.dbest.result",
        "../query/zipf/mysql/sharp1_100k.dbest.result",
        "../query/zipf/mysql/sharp1_10k.dbest.result",
        "../query/zipf/mysql/sharp1_1m.dbest.result",
    ]
    for file in files:
        sample_size=file.split("_")[1].split(".")[0]
        if sample_size =="10k":
            sample_size = 1.0E4
        if sample_size =="100k":
            sample_size = 1.0E5
        if sample_size =="1m":
            sample_size = 1.0E6

        process_mysql_result(file,sample_size, 1E8 )






if __name__ == '__main__':
    avg_relative_errors_per_group_value(function='count', group_num=501)
    # avg_relative_errors()

    # import numpy as np
    # DBEst_100k, blinkdb_100k = avg_relative_errors_per_group_value(group_num=8,function="count",size="100k")
    # DBEst_1m, blinkdb_1m = avg_relative_errors_per_group_value(group_num=8,function="count",size="1m")
    # function = "count"
    # plt_bar4(DBEst_100k[function],blinkdb_100k[function],DBEst_1m[function], blinkdb_1m[function])
    # print(np.var(DBEst_100k[function]))
    # print(np.var(DBEst_1m[function]))
    # print(np.var(blinkdb_100k[function]))
    # print(np.var(blinkdb_1m[function]))
    # process_mysql_result('../query/zipf/mysql/plain0.1_1m.dbest.result',1E4,1E8)
    # process_mysql_results()

