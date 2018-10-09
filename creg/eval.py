import re
import sys


def read_results(file, b_remove_null=True):
    """read the group by value and the corresponding aggregate within
    a given range, used to compare the accuracy.the

    Output: a dict contating the 

    Args:
        file (file): path to the file
    """

    key_values = {}
    with open(file) as f:
        print("Start reading file " + file)
        index = 1
        for line in f:
            # ignore empty lines
            if  line.strip():
                key_value = line.replace(
                    "(", " ").replace(")", " ").replace(";", "").replace(",", "")
                # self.logger.logger.info(key_value)
                key_value = re.split('\s+', key_value)
                # remove empty strings caused by sequential blank spaces.
                key_value = list(filter(None, key_value))
                key_values[key_value[0]] = key_value[1]
    if ('NULL' in key_values) and b_remove_null:
        key_values.pop('NULL', None)
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
    if len(ground_truth) != len(predictions):
        print("Length mismatch!")
        print("Length of ground_truth is " + str(len(ground_truth)))
        print("Length of predictions is " + str(len(predictions)))
        print("System aborts!")
        sys.exit(1)

    relative_errors = []
    for key_gt, value_gt in ground_truth.items():
        if (ground_truth[key_gt] != 0):
            re = abs(float(ground_truth[key_gt]) -
                     float(predictions[key_gt])) / float(ground_truth[key_gt])
            relative_errors.append(re)
        else:
            print(
                "Zero is found in ground_truth, so removed to calculate relative error.")
    return sum(relative_errors) / len(relative_errors)


if __name__ == '__main__':
    averag_errors_blinkdb=[]
    averag_errors_DBEst=[]
    for func in ['count','sum','avg']:
        errors_blinkdb = []
        errors_DBEst = []
        for index in range(1,11):
            file_name=func+str(int(index))
            ground_truth = read_results('../data/tpcds5m/groundtruth/'+file_name+'.result')
            predictions_blinkdb = read_results('../data/tpcds5m/blinkdb/'+file_name+'.txt') #../data/tpcds5m/blinkdb/sum1.txt
            predictions_DBEst = read_results('../data/tpcds5m/DBEst_integral/'+file_name+'.txt')
            errors_blinkdb.append(avg_relative_error(ground_truth,predictions_blinkdb))
            errors_DBEst.append(avg_relative_error(ground_truth,predictions_DBEst))
        averag_errors_blinkdb.append(sum(errors_blinkdb)/len(errors_blinkdb))
        averag_errors_DBEst.append(sum(errors_DBEst)/len(errors_DBEst))
    print(averag_errors_blinkdb)
    print(averag_errors_DBEst)

