#!/usr/bin/env python
# coding=utf-8
from dbest import tools
import pandas as pd
import numpy as np
file1 = "../data/1online_video_dataset/1transcoding_mesurment.csv"
file2 = "../data/2CASP.csv"
file3 = "../data/3PRSA_data.csv"
file4 = "../data/4OnlineNewsPopularity1.csv"
file5 = "../data/5CCPP/5Folds5x2_pp.csv"
file6 = "../data/6YearPredictionMSD_with_header.csv"
file7 = "../data/7/7ethylene_methane_with_header.csv"
file8 = "../data/8data.txt"
file9 = "../data/1m.csv"
file10 = "../data/5m.csv"
file11 = "../data/10k.csv"
file12 = "../data/100k.csv"
file13 = "../data/1_percent.csv"

file1 =  "/home/u1796377/Workspace/DBEst/data/1online_video_dataset/1transcoding_mesurment.csv"
file2 =  "/home/u1796377/Workspace/DBEst/data/2CASP.csv"
file3 =  "/home/u1796377/Workspace/DBEst/data/3PRSA_data.csv"
file4 =  "/home/u1796377/Workspace/DBEst/data/4OnlineNewsPopularity1.csv"
file5 =  "/home/u1796377/Workspace/DBEst/data/5CCPP/5Folds5x2_pp.csv"
file6 =  "/home/u1796377/Workspace/DBEst/data/6YearPredictionMSD_with_header.csv"
file7 =  "/home/u1796377/Workspace/DBEst/data/7/7ethylene_methane_with_header.csv"
file8 =  "/home/u1796377/Workspace/DBEst/data/8data.txt"

file1_qreg_sample_10k =  "/home/u1796377/Workspace/DBEst/data/QReg_sample/10k/1.csv"
file2_qreg_sample_10k =  "/home/u1796377/Workspace/DBEst/data/QReg_sample/10k/2.csv"
file3_qreg_sample_10k =  "/home/u1796377/Workspace/DBEst/data/QReg_sample/10k/3.csv"
file4_qreg_sample_10k =  "/home/u1796377/Workspace/DBEst/data/QReg_sample/10k/4.csv"
file5_qreg_sample_10k =  "/home/u1796377/Workspace/DBEst/data/QReg_sample/10k/5.csv"
file6_qreg_sample_10k =  "/home/u1796377/Workspace/DBEst/data/QReg_sample/10k/6.csv"
file7_qreg_sample_10k =  "/home/u1796377/Workspace/DBEst/data/QReg_sample/10k/7.csv"
file8_qreg_sample_10k =  "/home/u1796377/Workspace/DBEst/data/QReg_sample/10k/8.csv"

file1_qreg_sample_100k =  "/home/u1796377/Workspace/DBEst/data/QReg_sample/100k/1.csv"
file2_qreg_sample_100k =  "/home/u1796377/Workspace/DBEst/data/QReg_sample/100k/2.csv"
file3_qreg_sample_100k =  "/home/u1796377/Workspace/DBEst/data/QReg_sample/100k/3.csv"
file4_qreg_sample_100k =  "/home/u1796377/Workspace/DBEst/data/QReg_sample/100k/4.csv"
file5_qreg_sample_100k =  "/home/u1796377/Workspace/DBEst/data/QReg_sample/100k/5.csv"
file6_qreg_sample_100k =  "/home/u1796377/Workspace/DBEst/data/QReg_sample/100k/6.csv"
file7_qreg_sample_100k =  "/home/u1796377/Workspace/DBEst/data/QReg_sample/100k/7.csv"
file8_qreg_sample_100k =  "/home/u1796377/Workspace/DBEst/data/QReg_sample/100k/8.csv"

file1_qreg_sample_1m =  "/home/u1796377/Workspace/DBEst/data/QReg_sample/1m/1.csv"
file2_qreg_sample_1m =  "/home/u1796377/Workspace/DBEst/data/QReg_sample/1m/2.csv"
file3_qreg_sample_1m =  "/home/u1796377/Workspace/DBEst/data/QReg_sample/1m/3.csv"
file4_qreg_sample_1m =  "/home/u1796377/Workspace/DBEst/data/QReg_sample/1m/4.csv"
file5_qreg_sample_1m =  "/home/u1796377/Workspace/DBEst/data/QReg_sample/1m/5.csv"
file6_qreg_sample_1m =  "/home/u1796377/Workspace/DBEst/data/QReg_sample/1m/6.csv"
file7_qreg_sample_1m =  "/home/u1796377/Workspace/DBEst/data/QReg_sample/1m/7.csv"
file8_qreg_sample_1m =  "/home/u1796377/Workspace/DBEst/data/QReg_sample/1m/8.csv"

file9 =  "/home/u1796377/Workspace/DBEst/data/1m.csv"
file10 = "/home/u1796377/Workspace/DBEst/data/5m.csv"
file11 = "/home/u1796377/Workspace/DBEst/data/10k.csv"
file12 = "/home/u1796377/Workspace/DBEst/data/100k.csv"
file13 = "/home/u1796377/Workspace/DBEst/data/1_percent.csv"

etrade_price_comm_1m = "../data/etrade_price_comm_1m.csv"
etrade_price_comm_100k = "../data/etrade_price_comm_100k.csv"
etrade_price_comm_10k = "../data/etrade_price_comm_10k.csv"
etrade_price_comm_1k = "../data/etrade_price_comm_1k.csv"

def load2d(dataID,sample_size=None):
    if dataID == 1:
        # Number 1 dataset

        fields = ['duration', 'width', 'height', 'bitrate', 'framerate', 'i', 'p', 'b', 'frames', 'i_size',
                  'p_size',
                  'b_size', 'size', 'o_bitrate', 'o_framerate', 'o_width', 'o_height', 'umem', 'utime']
        fields = ['utime', 'umem']
        fields = ['i_size', 'umem']
        # fields = ['bitrate', 'framerate']
        # fields = ['umem', 'utime']
        y_column = 1  # should be the order in the input file, not in the "fields" order.
        # fields = ['bitrate','framerate', 'utime']
        # y_column = 2  # should be the order in the input file, not in the "fields" order.
        if sample_size is None:
            data = tools.load_csv(file1, fields, y_column)
        elif sample_size== "10k":
            data = tools.load_csv(file1_qreg_sample_10k, fields, y_column)
        elif sample_size== "100k":
            data = tools.load_csv(file1_qreg_sample_100k, fields, y_column)
        elif sample_size== "1m":
            data = tools.load_csv(file1_qreg_sample_1m, fields, y_column)
        else:
            return None


    if dataID == 2:
        # Number 2 dataset
        fields = ["RMSD", "F1", "F2", "F3", "F4", "F5", "F6", "F7", "F8", "F9"]
        fields = ["RMSD", "F2"]
        y_column = 0  # should be the order in the input file, not in the "fields" order.
        if sample_size is None:
            data = tools.load_csv(file2, fields, y_column)
        elif sample_size== "10k":
            data = tools.load_csv(file2_qreg_sample_10k, fields, y_column)
        elif sample_size== "100k":
            data = tools.load_csv(file2_qreg_sample_100k, fields, y_column)
        elif sample_size== "1m":
            data = tools.load_csv(file2_qreg_sample_1m, fields, y_column)
        else:
            return None
        # data = tools.load_csv(file2, fields, y_column)
    if dataID == 3:
        # Number 3 dataset

        fields = ['year', 'month', 'day', 'hour', 'pm2.5', 'DEWP', 'TEMP', 'PRES', 'Iws', 'Is', 'Ir']
        fields = ['pm2.5', 'Iws']
        y_column = 0  # should be the order in the input file, not in the "fields" order.
        if sample_size is None:
            data = tools.load_csv(file3, fields, y_column)
        elif sample_size== "10k":
            data = tools.load_csv(file3_qreg_sample_10k, fields, y_column)
        elif sample_size== "100k":
            data = tools.load_csv(file3_qreg_sample_100k, fields, y_column)
        elif sample_size== "1m":
            data = tools.load_csv(file3_qreg_sample_1m, fields, y_column)
        else:
            return None
        # data = tools.load_csv(file3, fields, y_column)
    if dataID == 4:
        # Number 4 dataset

        # load the data
        fields = ['n_tokens_title', 'n_tokens_content', 'n_unique_tokens', 'n_non_stop_unique_tokens']
        fields = ['n_tokens_content', 'n_unique_tokens']
        y_column = 0  # should be the order in the input file, not in the "fields" order.
        # fields = ['n_unique_tokens', 'n_non_stop_unique_tokens']
        # y_column = 1  # should be the order in the input file, not in the "fields" order.
        # data = tools.load_csv(file4, fields, y_column)
        if sample_size is None:
            data = tools.load_csv(file4, fields, y_column)
        elif sample_size== "10k":
            data = tools.load_csv(file4_qreg_sample_10k, fields, y_column)
        elif sample_size== "100k":
            data = tools.load_csv(file4_qreg_sample_100k, fields, y_column)
        elif sample_size== "1m":
            data = tools.load_csv(file4_qreg_sample_1m, fields, y_column)
        else:
            return None
    if dataID == 5:
        # Number 5 dataset
        # '''
        # load the data
        fields = ['Temperature', 'Exhaust_Vacuum', 'Ambient_Pressure', 'Relative_Humidity', 'energy_output']
        fields = ['Relative_Humidity', 'energy_output']
        y_column = 1  # should be the order in the input file, not in the "fields" order.
        # data = tools.load_csv(file5, fields, y_column)
        if sample_size is None:
            data = tools.load_csv(file5, fields, y_column)
        elif sample_size== "10k":
            data = tools.load_csv(file5_qreg_sample_10k, fields, y_column)
        elif sample_size== "100k":
            data = tools.load_csv(file5_qreg_sample_100k, fields, y_column)
        elif sample_size== "1m":
            data = tools.load_csv(file5_qreg_sample_1m, fields, y_column)
        else:
            return None
    if dataID == 6:
        # Number 6 dataset

        fields = ['year', 'c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8', 'c9', 'c10', 'c11', 'c12', 'c13', 'c14',
                  'c15',
                  'c16', 'c17', 'c18', 'c19', 'c20',
                  'c21', 'c22', 'c23', 'c24', 'c25', 'c26', 'c27', 'c28', 'c29', 'c30', 'c31', 'c32', 'c33', 'c34',
                  'c35',
                  'c36', 'c37', 'c38', 'c39',
                  'c40', 'c41', 'c42', 'c43', 'c44', 'c45', 'c46', 'c47', 'c48', 'c49', 'c50', 'c51', 'c52', 'c53',
                  'c54',
                  'c55', 'c56', 'c57', 'c58',
                  'c59', 'c60', 'c61', 'c62', 'c63', 'c64', 'c65', 'c66', 'c67', 'c68', 'c69', 'c70', 'c71', 'c72',
                  'c73',
                  'c74', 'c75', 'c76', 'c77',
                  'c78', 'c79', 'c80', 'c81', 'c82', 'c83', 'c84', 'c85', 'c86', 'c87', 'c88', 'c89', 'c90']
        fields = ['year', 'c1']
        y_column = 0  # should be the order in the input file, not in the "fields" order.
        # data = tools.load_csv(file6, fields, y_column)
        if sample_size is None:
            data = tools.load_csv(file6, fields, y_column)
        elif sample_size== "10k":
            data = tools.load_csv(file6_qreg_sample_10k, fields, y_column)
        elif sample_size== "100k":
            data = tools.load_csv(file6_qreg_sample_100k, fields, y_column)
        elif sample_size== "1m":
            data = tools.load_csv(file6_qreg_sample_1m, fields, y_column)
        else:
            return None
    if dataID == 7:
        # Number 7 dataset

        # load the data
        # fields = ['duration','width','height','bitrate','framerate','i','p','b','frames','i_size','p_size','b_size','size','o_bitrate','o_framerate','o_width','o_height','umem','utime']

        fields = ['Time_(seconds)', 'Methane_conc_(ppm)', 'Ethylene_conc_(ppm)', 'c1', 'c2', 'c3', 'c4', 'c5', 'c6',
                  'c7',
                  'c8', 'c9', 'c10', 'c11', 'c12', 'c13', 'c14', 'c15', 'c16']
        fields = ['c1', 'c2']
        y_column = 1  # should be the order in the input file, not in the "fields" order.
        # data = tools.load_csv("datasets/1online_video_dataset/1transcoding_mesurment.csv",fields,y_column)
        # data = tools.load_csv(file7, fields, y_column, sep=' ')
        if sample_size is None:
            data = tools.load_csv(file7, fields, y_column, sep=' ')
        elif sample_size== "10k":
            data = tools.load_csv(file7_qreg_sample_10k, fields, y_column)
        elif sample_size== "100k":
            data = tools.load_csv(file7_qreg_sample_100k, fields, y_column)
        elif sample_size== "1m":
            data = tools.load_csv(file7_qreg_sample_1m, fields, y_column)
        else:
            return None
    if dataID == 8:
        # Number 8 dataset

        # Number 8 dataset

        # load the data

        fields = ['timestamp', 'Global_active_power', 'Global_reactive_power', 'Voltage', 'Global_intensity',
                  'Sub_metering_1', 'Sub_metering_2', 'Sub_metering_3', 'energy']
        # fields = ['Date',  'Global_active_power', 'Global_reactive_power', 'Voltage', 'Global_intensity',
        #          'Sub_metering_1', 'Sub_metering_2', 'Sub_metering_3']
        fields = ['timestamp', 'energy']
        y_column = 1  # should be the order in the input file, not in the "fields" order.
        # data = tools.load_csv(file8, fields, y_column, sep=',')
        if sample_size is None:
            data = tools.load_csv(file8, fields, y_column, sep=',')
        elif sample_size== "10k":
            fields = ['Global_intensity', 'energy']
            data = tools.load_csv(file8_qreg_sample_10k, fields, y_column)
        elif sample_size== "100k":
            fields = ['Global_intensity', 'energy']
            data = tools.load_csv(file8_qreg_sample_100k, fields, y_column)
        elif sample_size== "1m":
            fields = ['Global_intensity', 'energy']
            data = tools.load_csv(file8_qreg_sample_1m, fields, y_column)
        else:
            return None

    if dataID == "1m":
        fields = ['ss_list_price', 'ss_wholesale_cost']
        y_column = 1  # should be the order in the input file, not in the "fields" order.
        data = tools.load_csv(file9, fields, y_column, sep=',')



    if dataID == "5m":
        fields = ['ss_list_price', 'ss_wholesale_cost']
        y_column = 1  # should be the order in the input file, not in the "fields" order.
        data = tools.load_csv(file10, fields, y_column, sep=',')


    if dataID == "10k":
        fields = ['ss_list_price', 'ss_wholesale_cost']
        y_column = 1  # should be the order in the input file, not in the "fields" order.
        data = tools.load_csv(file11, fields, y_column, sep=',')

    if dataID == "100k":
        fields = ['ss_list_price', 'ss_wholesale_cost']
        y_column = 1  # should be the order in the input file, not in the "fields" order.
        data = tools.load_csv(file12, fields, y_column, sep=',')

    if dataID == "1%":
        fields = ['ss_list_price', 'ss_wholesale_cost']
        y_column = 1  # should be the order in the input file, not in the "fields" order.
        data = tools.load_csv(file13, fields, y_column, sep=',')
    
    if dataID == "etrade_price_comm_1m":
        fields = ['T_TRADE_PRICE', 'T_COMM']
        y_column = 1  # should be the order in the input file, not in the "fields" order.
        data = tools.load_csv(etrade_price_comm_1m, fields, y_column, sep=',')

    if dataID == "etrade_price_comm_100k":
        fields = ['T_TRADE_PRICE', 'T_COMM']
        y_column = 1  # should be the order in the input file, not in the "fields" order.
        data = tools.load_csv(etrade_price_comm_100k, fields, y_column, sep=',')

    if dataID == "etrade_price_comm_10k":
        fields = ['T_TRADE_PRICE', 'T_COMM']
        y_column = 1  # should be the order in the input file, not in the "fields" order.
        data = tools.load_csv(etrade_price_comm_10k, fields, y_column, sep=',')

    if dataID == "etrade_price_comm_1k":
        fields = ['T_TRADE_PRICE', 'T_COMM']
        y_column = 1  # should be the order in the input file, not in the "fields" order.
        data = tools.load_csv(etrade_price_comm_1k, fields, y_column, sep=',')

    return data


def load3d(dataID,sample_size=None):
    if dataID == 1:
        # Number 1 dataset

        fields = ['duration', 'width', 'height', 'bitrate', 'framerate', 'i', 'p', 'b', 'frames', 'i_size',
                  'p_size',
                  'b_size', 'size', 'o_bitrate', 'o_framerate', 'o_width', 'o_height', 'umem', 'utime']
        fields = ['i_size', 'umem', 'utime']
        y_column = 1  # should be the order in the input file, not in the "fields" order.
        if sample_size is None:
            data = tools.load_csv(file1, fields, y_column)
        elif sample_size== "10k":
            data = tools.load_csv(file1_qreg_sample_10k, fields, y_column)
        elif sample_size== "100k":
            data = tools.load_csv(file1_qreg_sample_100k, fields, y_column)
        elif sample_size== "1m":
            data = tools.load_csv(file1_qreg_sample_1m, fields, y_column)
        else:
            return None
        # "../data/1online_video_dataset/1transcoding_mesurment.csv"
    if dataID == 2:
        # Number 2 dataset
        fields = ["RMSD", "F1", "F2", "F3", "F4", "F5", "F6", "F7", "F8", "F9"]
        fields = ["RMSD", "F3", "F5"]

        # fields = ["RMSD", "F2", "F7"]
        fields = ["RMSD", "F4", "F5"]

        y_column = 0  # should be the order in the input file, not in the "fields" order.
        if sample_size is None:
            data = tools.load_csv(file2, fields, y_column)
        elif sample_size== "10k":
            data = tools.load_csv(file2_qreg_sample_10k, fields, y_column)
        elif sample_size== "100k":
            data = tools.load_csv(file2_qreg_sample_100k, fields, y_column)
        elif sample_size== "1m":
            data = tools.load_csv(file2_qreg_sample_1m, fields, y_column)
        else:
            return None
        # "../data/2CASP.csv"
    if dataID == 3:
        # Number 3 dataset

        fields = ['year', 'month', 'day', 'hour', 'pm2.5', 'DEWP', 'TEMP', 'PRES', 'Iws', 'Is', 'Ir']
        fields = ['pm2.5', 'PRES']
        y_column = 0  # should be the order in the input file, not in the "fields" order.
        fields = ['pm2.5', 'TEMP', 'PRES']
        fields = ['pm2.5', 'TEMP', 'Iws']  # good vision
        fields = ['pm2.5', 'PRES', 'Iws']
        y_column = 0  # should be the order in the input file, not in the "fields" order.
        if sample_size is None:
            data = tools.load_csv(file3, fields, y_column)
        elif sample_size== "10k":
            data = tools.load_csv(file3_qreg_sample_10k, fields, y_column)
        elif sample_size== "100k":
            data = tools.load_csv(file3_qreg_sample_100k, fields, y_column)
        elif sample_size== "1m":
            data = tools.load_csv(file3_qreg_sample_1m, fields, y_column)
        else:
            return None
        # "../data/3PRSA_data.csv"
    if dataID == 4:
        # Number 4 dataset

        # load the data
        fields = ['n_tokens_title', 'n_tokens_content', 'n_unique_tokens', 'n_non_stop_unique_tokens']
        fields = ['n_tokens_content', 'n_unique_tokens']
        y_column = 1  # should be the order in the input file, not in the "fields" order.
        fields = ['n_tokens_title', 'n_tokens_content', 'n_unique_tokens']
        fields = ['n_tokens_content', 'n_unique_tokens', 'n_non_stop_unique_tokens']
        # fields = [ 'n_tokens_content', 'n_unique_tokens', 'n_non_stop_unique_tokens']
        y_column = 1  # should be the order in the input file, not in the "fields" order.
        if sample_size is None:
            data = tools.load_csv(file4, fields, y_column)
        elif sample_size== "10k":
            data = tools.load_csv(file4_qreg_sample_10k, fields, y_column)
        elif sample_size== "100k":
            data = tools.load_csv(file4_qreg_sample_100k, fields, y_column)
        elif sample_size== "1m":
            data = tools.load_csv(file4_qreg_sample_1m, fields, y_column)
        else:
            return None
        # "../data/4OnlineNewsPopularity1.csv"
    if dataID == 5:
        # Number 5 dataset
        # '''
        # load the data
        fields = ['Temperature', 'Exhaust_Vacuum', 'Ambient_Pressure', 'Relative_Humidity', 'energy_output']
        fields = ['Exhaust_Vacuum', 'energy_output']
        y_column = 1  # should be the order in the input file, not in the "fields" order.
        # fields = ['Exhaust_Vacuum', 'Ambient_Pressure', 'energy_output']
        fields = ['Temperature', 'Ambient_Pressure', 'energy_output']
        fields = ['Ambient_Pressure', 'Relative_Humidity', 'energy_output']
        # fields = ['Exhaust_Vacuum', 'Ambient_Pressure', 'energy_output']
        # fields = ['Temperature', 'Exhaust_Vacuum', 'energy_output']

        y_column = 2  # should be the order in the input file, not in the "fields" order.
        if sample_size is None:
            data = tools.load_csv(file5, fields, y_column)
        elif sample_size== "10k":
            data = tools.load_csv(file5_qreg_sample_10k, fields, y_column)
        elif sample_size== "100k":
            data = tools.load_csv(file5_qreg_sample_100k, fields, y_column)
        elif sample_size== "1m":
            data = tools.load_csv(file5_qreg_sample_1m, fields, y_column)
        else:
            return None
        # "../data/5CCPP/5Folds5x2_pp.csv"
    if dataID == 6:
        # Number 6 dataset

        fields = ['year', 'c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8', 'c9', 'c10', 'c11', 'c12', 'c13', 'c14',
                  'c15',
                  'c16', 'c17', 'c18', 'c19', 'c20',
                  'c21', 'c22', 'c23', 'c24', 'c25', 'c26', 'c27', 'c28', 'c29', 'c30', 'c31', 'c32', 'c33', 'c34',
                  'c35',
                  'c36', 'c37', 'c38', 'c39',
                  'c40', 'c41', 'c42', 'c43', 'c44', 'c45', 'c46', 'c47', 'c48', 'c49', 'c50', 'c51', 'c52', 'c53',
                  'c54',
                  'c55', 'c56', 'c57', 'c58',
                  'c59', 'c60', 'c61', 'c62', 'c63', 'c64', 'c65', 'c66', 'c67', 'c68', 'c69', 'c70', 'c71', 'c72',
                  'c73',
                  'c74', 'c75', 'c76', 'c77',
                  'c78', 'c79', 'c80', 'c81', 'c82', 'c83', 'c84', 'c85', 'c86', 'c87', 'c88', 'c89', 'c90']
        fields = ['year', 'c1']
        y_column = 0  # should be the order in the input file, not in the "fields" order.
        fields = ['year', 'c1', 'c2']
        # fields = ['year', 'c2', 'c4']
        y_column = 0  # should be the order in the input file, not in the "fields" order.
        # data = tools.load_csv("datasets/1online_video_dataset/1transcoding_mesurment.csv",fields,y_column)
        if sample_size is None:
            data = tools.load_csv(file6, fields, y_column)
        elif sample_size== "10k":
            data = tools.load_csv(file6_qreg_sample_10k, fields, y_column)
        elif sample_size== "100k":
            data = tools.load_csv(file6_qreg_sample_100k, fields, y_column)
        elif sample_size== "1m":
            data = tools.load_csv(file6_qreg_sample_1m, fields, y_column)
        else:
            return None
        # "../data/6YearPredictionMSD_with_header.csv"
    if dataID == 7:
        # Number 7 dataset

        # load the data
        # fields = ['duration','width','height','bitrate','framerate','i','p','b','frames','i_size','p_size','b_size','size','o_bitrate','o_framerate','o_width','o_height','umem','utime']

        fields = ['Time_(seconds)', 'Methane_conc_(ppm)', 'Ethylene_conc_(ppm)', 'c1', 'c2', 'c3', 'c4', 'c5', 'c6',
                  'c7',
                  'c8', 'c9', 'c10', 'c11', 'c12', 'c13', 'c14', 'c15', 'c16']
        fields = ['c1', 'c2']
        y_column = 1  # should be the order in the input file, not in the "fields" order.
        fields = ['c1', 'c2', 'c4']
        fields = ['Methane_conc_(ppm)', 'c1', 'c2']
        y_column = 2  # should be the order in the input file, not in the "fields" order.
        # data = tools.load_csv("datasets/1online_video_dataset/1transcoding_mesurment.csv",fields,y_column)
        # data = tools.load_csv(file7, fields, y_column, sep=' ')
        if sample_size is None:
            data = tools.load_csv(file7, fields, y_column, sep=' ')
        elif sample_size== "10k":
            data = tools.load_csv(file7_qreg_sample_10k, fields, y_column)
        elif sample_size== "100k":
            data = tools.load_csv(file7_qreg_sample_100k, fields, y_column)
        elif sample_size== "1m":
            data = tools.load_csv(file7_qreg_sample_1m, fields, y_column)
        else:
            return None
        # "../data/6YearPredictionMSD_with_header.csv"
    if dataID == 8:
        # Number 8 dataset

        # load the data

        fields = ['timestamp', 'Global_active_power', 'Global_reactive_power', 'Voltage', 'Global_intensity',
                  'Sub_metering_1', 'Sub_metering_2', 'Sub_metering_3', 'energy']
        # fields = ['Date',  'Global_active_power', 'Global_reactive_power', 'Voltage', 'Global_intensity',
        #          'Sub_metering_1', 'Sub_metering_2', 'Sub_metering_3']
        fields = ['Global_active_power', 'Global_reactive_power', 'energy']
        y_column = 2  # should be the order in the input file, not in the "fields" order.
        if sample_size is None:
            data = tools.load_csv(file8, fields, y_column, sep=',')
        elif sample_size== "10k":
            data = tools.load_csv(file8_qreg_sample_10k, fields, y_column)
        elif sample_size== "100k":
            data = tools.load_csv(file8_qreg_sample_100k, fields, y_column)
        elif sample_size== "1m":
            data = tools.load_csv(file8_qreg_sample_1m, fields, y_column)
        else:
            return None
        # "../data/8data.txt"
    return data


def load4d(dataID,sample_size=None):
    if dataID == 1:
        # Number 1 dataset

        fields = ['duration', 'width', 'height', 'bitrate', 'framerate', 'i', 'p', 'b', 'frames', 'i_size',
                  'p_size',
                  'b_size', 'size', 'o_bitrate', 'o_framerate', 'o_width', 'o_height', 'umem', 'utime']
        fields = ['duration', 'i_size', 'umem', 'utime']
        y_column = 2  # should be the order in the input file, not in the "fields" order.
        if sample_size is None:
            data = tools.load_csv(file1, fields, y_column)
        elif sample_size== "10k":
            data = tools.load_csv(file1_qreg_sample_10k, fields, y_column)
        elif sample_size== "100k":
            data = tools.load_csv(file1_qreg_sample_100k, fields, y_column)
        elif sample_size== "1m":
            data = tools.load_csv(file1_qreg_sample_1m, fields, y_column)
        else:
            return None
        # "../data/1online_video_dataset/1transcoding_mesurment.csv"
    if dataID == 2:
        # Number 2 dataset
        fields = ["RMSD", "F1", "F2", "F3", "F4", "F5", "F6", "F7", "F8", "F9"]
        fields = ["RMSD", "F3", "F5"]

        # fields = ["RMSD", "F2", "F7"]
        fields = ["RMSD", "F4", "F5"]
        fields = ["RMSD", 'F3', "F4", "F5"]

        y_column = 0  # should be the order in the input file, not in the "fields" order.
        if sample_size is None:
            data = tools.load_csv(file2, fields, y_column)
        elif sample_size== "10k":
            data = tools.load_csv(file2_qreg_sample_10k, fields, y_column)
        elif sample_size== "100k":
            data = tools.load_csv(file2_qreg_sample_100k, fields, y_column)
        elif sample_size== "1m":
            data = tools.load_csv(file2_qreg_sample_1m, fields, y_column)
        else:
            return None
        # "../data/2CASP.csv"
    if dataID == 3:
        # Number 3 dataset

        fields = ['year', 'month', 'day', 'hour', 'pm2.5', 'DEWP', 'TEMP', 'PRES', 'Iws', 'Is', 'Ir']
        fields = ['pm2.5', 'PRES']
        y_column = 0  # should be the order in the input file, not in the "fields" order.
        fields = ['pm2.5', 'TEMP', 'PRES']
        fields = ['pm2.5', 'TEMP', 'Iws']  # good vision
        fields = ['pm2.5', 'TEMP', 'PRES', 'Iws']
        y_column = 0  # should be the order in the input file, not in the "fields" order.
        if sample_size is None:
            data = tools.load_csv(file3, fields, y_column)
        elif sample_size== "10k":
            data = tools.load_csv(file3_qreg_sample_10k, fields, y_column)
        elif sample_size== "100k":
            data = tools.load_csv(file3_qreg_sample_100k, fields, y_column)
        elif sample_size== "1m":
            data = tools.load_csv(file3_qreg_sample_1m, fields, y_column)
        else:
            return None
        # "../data/3PRSA_data.csv"
    if dataID == 4:
        # Number 4 dataset

        # load the data
        fields = ['n_tokens_title', 'n_tokens_content', 'n_unique_tokens', 'n_non_stop_unique_tokens']

        # fields = [ 'n_tokens_content', 'n_unique_tokens', 'n_non_stop_unique_tokens']
        y_column = 2  # should be the order in the input file, not in the "fields" order.
        if sample_size is None:
            data = tools.load_csv(file4, fields, y_column)
        elif sample_size== "10k":
            data = tools.load_csv(file4_qreg_sample_10k, fields, y_column)
        elif sample_size== "100k":
            data = tools.load_csv(file4_qreg_sample_100k, fields, y_column)
        elif sample_size== "1m":
            data = tools.load_csv(file4_qreg_sample_1m, fields, y_column)
        else:
            return None
        # "../data/4OnlineNewsPopularity1.csv"
    if dataID == 5:
        # Number 5 dataset
        # '''
        # load the data
        fields = ['Temperature', 'Exhaust_Vacuum', 'Ambient_Pressure', 'Relative_Humidity', 'energy_output']
        fields = ['Exhaust_Vacuum', 'energy_output']
        y_column = 1  # should be the order in the input file, not in the "fields" order.
        # fields = ['Exhaust_Vacuum', 'Ambient_Pressure', 'energy_output']
        fields = ['Temperature', 'Ambient_Pressure', 'energy_output']
        fields = ['Temperature', 'Ambient_Pressure', 'Relative_Humidity', 'energy_output']
        # fields = ['Exhaust_Vacuum', 'Ambient_Pressure', 'energy_output']
        # fields = ['Temperature', 'Exhaust_Vacuum', 'energy_output']

        y_column = 3  # should be the order in the input file, not in the "fields" order.
        if sample_size is None:
            data = tools.load_csv(file5, fields, y_column)
        elif sample_size== "10k":
            data = tools.load_csv(file5_qreg_sample_10k, fields, y_column)
        elif sample_size== "100k":
            data = tools.load_csv(file5_qreg_sample_100k, fields, y_column)
        elif sample_size== "1m":
            data = tools.load_csv(file5_qreg_sample_1m, fields, y_column)
        else:
            return None
        # "../data/5CCPP/5Folds5x2_pp.csv"
    if dataID == 6:
        # Number 6 dataset

        fields = ['year', 'c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8', 'c9', 'c10', 'c11', 'c12', 'c13', 'c14',
                  'c15',
                  'c16', 'c17', 'c18', 'c19', 'c20',
                  'c21', 'c22', 'c23', 'c24', 'c25', 'c26', 'c27', 'c28', 'c29', 'c30', 'c31', 'c32', 'c33', 'c34',
                  'c35',
                  'c36', 'c37', 'c38', 'c39',
                  'c40', 'c41', 'c42', 'c43', 'c44', 'c45', 'c46', 'c47', 'c48', 'c49', 'c50', 'c51', 'c52', 'c53',
                  'c54',
                  'c55', 'c56', 'c57', 'c58',
                  'c59', 'c60', 'c61', 'c62', 'c63', 'c64', 'c65', 'c66', 'c67', 'c68', 'c69', 'c70', 'c71', 'c72',
                  'c73',
                  'c74', 'c75', 'c76', 'c77',
                  'c78', 'c79', 'c80', 'c81', 'c82', 'c83', 'c84', 'c85', 'c86', 'c87', 'c88', 'c89', 'c90']
        fields = ['year', 'c1']
        y_column = 0  # should be the order in the input file, not in the "fields" order.
        fields = ['year', 'c1', 'c2']
        fields = ['year', 'c2', 'c2', 'c3']
        y_column = 0  # should be the order in the input file, not in the "fields" order.
        # data = tools.load_csv("datasets/1online_video_dataset/1transcoding_mesurment.csv",fields,y_column)
        if sample_size is None:
            data = tools.load_csv(file6, fields, y_column)
        elif sample_size== "10k":
            data = tools.load_csv(file6_qreg_sample_10k, fields, y_column)
        elif sample_size== "100k":
            data = tools.load_csv(file6_qreg_sample_100k, fields, y_column)
        elif sample_size== "1m":
            data = tools.load_csv(file6_qreg_sample_1m, fields, y_column)
        else:
            return None
        # "../data/6YearPredictionMSD_with_header.csv"
    if dataID == 7:
        # Number 7 dataset

        # load the data
        # fields = ['duration','width','height','bitrate','framerate','i','p','b','frames','i_size','p_size','b_size','size','o_bitrate','o_framerate','o_width','o_height','umem','utime']

        fields = ['Time_(seconds)', 'Methane_conc_(ppm)', 'Ethylene_conc_(ppm)', 'c1', 'c2', 'c3', 'c4', 'c5', 'c6',
                  'c7',
                  'c8', 'c9', 'c10', 'c11', 'c12', 'c13', 'c14', 'c15', 'c16']
        fields = ['c1', 'c2']
        y_column = 1  # should be the order in the input file, not in the "fields" order.
        fields = ['c1', 'c2', 'c4']
        fields = ['Methane_conc_(ppm)', 'c1', 'c2']
        fields = ['Methane_conc_(ppm)', 'c1', 'c2', 'c3']
        y_column = 2  # should be the order in the input file, not in the "fields" order.
        # data = tools.load_csv("datasets/1online_video_dataset/1transcoding_mesurment.csv",fields,y_column)
        if sample_size is None:
            data = tools.load_csv(file7, fields, y_column, sep=' ')
        elif sample_size== "10k":
            data = tools.load_csv(file7_qreg_sample_10k, fields, y_column)
        elif sample_size== "100k":
            data = tools.load_csv(file7_qreg_sample_100k, fields, y_column)
        elif sample_size== "1m":
            data = tools.load_csv(file7_qreg_sample_1m, fields, y_column)
        else:
            return None
        # "../data/7/7ethylene_methane_with_header.csv"
    if dataID == 8:
        # Number 8 dataset

        # load the data

        fields = ['timestamp', 'Global_active_power', 'Global_reactive_power', 'Voltage', 'Global_intensity',
                  'Sub_metering_1', 'Sub_metering_2', 'Sub_metering_3', 'energy']
        # fields = ['Date',  'Global_active_power', 'Global_reactive_power', 'Voltage', 'Global_intensity',
        #          'Sub_metering_1', 'Sub_metering_2', 'Sub_metering_3']
        fields = ['Global_active_power', 'Global_reactive_power', 'Voltage', 'energy']
        y_column = 3  # should be the order in the input file, not in the "fields" order.
        if sample_size is None:
            data = tools.load_csv(file8, fields, y_column, sep=',')
        elif sample_size== "10k":
            data = tools.load_csv(file8_qreg_sample_10k, fields, y_column)
        elif sample_size== "100k":
            data = tools.load_csv(file8_qreg_sample_100k, fields, y_column)
        elif sample_size== "1m":
            data = tools.load_csv(file8_qreg_sample_1m, fields, y_column)
        else:
            return None
        # "../data/8data.txt"
    return data


def load5d(dataID,sample_size=None):
    if dataID == 1:
        # Number 1 dataset

        fields = ['duration', 'width', 'height', 'bitrate', 'framerate', 'i', 'p', 'b', 'frames', 'i_size',
                  'p_size',
                  'b_size', 'size', 'o_bitrate', 'o_framerate', 'o_width', 'o_height', 'umem', 'utime']
        fields = ['duration', 'width', 'i_size', 'umem', 'utime']
        y_column = 3  # should be the order in the input file, not in the "fields" order.
        if sample_size is None:
            data = tools.load_csv(file1, fields, y_column)
        elif sample_size== "10k":
            data = tools.load_csv(file1_qreg_sample_10k, fields, y_column)
        elif sample_size== "100k":
            data = tools.load_csv(file1_qreg_sample_100k, fields, y_column)
        elif sample_size== "1m":
            data = tools.load_csv(file1_qreg_sample_1m, fields, y_column)
        else:
            return None
        # "../data/1online_video_dataset/1transcoding_mesurment.csv"
    if dataID == 2:
        # Number 2 dataset
        fields = ["RMSD", "F1", "F2", "F3", "F4", "F5", "F6", "F7", "F8", "F9"]
        fields = ["RMSD", "F3", "F5"]

        # fields = ["RMSD", "F2", "F7"]
        fields = ["RMSD", "F4", "F5"]
        fields = ["RMSD", 'F3', "F4", "F5"]
        fields = ["RMSD", 'F2', 'F3', "F4", "F5"]

        y_column = 0  # should be the order in the input file, not in the "fields" order.
        if sample_size is None:
            data = tools.load_csv(file2, fields, y_column)
        elif sample_size== "10k":
            data = tools.load_csv(file2_qreg_sample_10k, fields, y_column)
        elif sample_size== "100k":
            data = tools.load_csv(file2_qreg_sample_100k, fields, y_column)
        elif sample_size== "1m":
            data = tools.load_csv(file2_qreg_sample_1m, fields, y_column)
        else:
            return None
        # "../data/2CASP.csv"
    if dataID == 3:
        # Number 3 dataset

        fields = ['year', 'month', 'day', 'hour', 'pm2.5', 'DEWP', 'TEMP', 'PRES', 'Iws', 'Is', 'Ir']
        fields = ['pm2.5', 'PRES']
        y_column = 0  # should be the order in the input file, not in the "fields" order.
        fields = ['pm2.5', 'TEMP', 'PRES']
        fields = ['pm2.5', 'TEMP', 'Iws']  # good vision
        fields = ['pm2.5', 'DEWP', 'TEMP', 'PRES', 'Iws']
        y_column = 0  # should be the order in the input file, not in the "fields" order.
        if sample_size is None:
            data = tools.load_csv(file3, fields, y_column)
        elif sample_size== "10k":
            data = tools.load_csv(file3_qreg_sample_10k, fields, y_column)
        elif sample_size== "100k":
            data = tools.load_csv(file3_qreg_sample_100k, fields, y_column)
        elif sample_size== "1m":
            data = tools.load_csv(file3_qreg_sample_1m, fields, y_column)
        else:
            return None
        # "../data/3PRSA_data.csv"
    if dataID == 4:
        # Number 4 dataset

        # load the data
        fields = ['n_tokens_title', 'n_tokens_content', 'n_unique_tokens', 'n_non_stop_unique_tokens', 'num_hrefs']

        # fields = [ 'n_tokens_content', 'n_unique_tokens', 'n_non_stop_unique_tokens']
        y_column = 2  # should be the order in the input file, not in the "fields" order.
        if sample_size is None:
            data = tools.load_csv(file4, fields, y_column)
        elif sample_size== "10k":
            data = tools.load_csv(file4_qreg_sample_10k, fields, y_column)
        elif sample_size== "100k":
            data = tools.load_csv(file4_qreg_sample_100k, fields, y_column)
        elif sample_size== "1m":
            data = tools.load_csv(file4_qreg_sample_1m, fields, y_column)
        else:
            return None
        # "../data/4OnlineNewsPopularity1.csv"
    if dataID == 5:
        # Number 5 dataset
        # '''
        # load the data
        fields = ['Temperature', 'Exhaust_Vacuum', 'Ambient_Pressure', 'Relative_Humidity', 'energy_output']
        fields = ['Exhaust_Vacuum', 'energy_output']
        y_column = 1  # should be the order in the input file, not in the "fields" order.
        # fields = ['Exhaust_Vacuum', 'Ambient_Pressure', 'energy_output']
        fields = ['Temperature', 'Ambient_Pressure', 'energy_output']
        fields = ['Ambient_Pressure', 'Relative_Humidity', 'energy_output']
        # fields = ['Exhaust_Vacuum', 'Ambient_Pressure', 'energy_output']
        # fields = ['Temperature', 'Exhaust_Vacuum', 'energy_output']
        fields = ['Temperature', 'Exhaust_Vacuum', 'Ambient_Pressure', 'Relative_Humidity', 'energy_output']

        y_column = 4  # should be the order in the input file, not in the "fields" order.
        if sample_size is None:
            data = tools.load_csv(file5, fields, y_column)
        elif sample_size== "10k":
            data = tools.load_csv(file5_qreg_sample_10k, fields, y_column)
        elif sample_size== "100k":
            data = tools.load_csv(file5_qreg_sample_100k, fields, y_column)
        elif sample_size== "1m":
            data = tools.load_csv(file5_qreg_sample_1m, fields, y_column)
        else:
            return None
        # "../data/5CCPP/5Folds5x2_pp.csv"
    if dataID == 6:
        # Number 6 dataset

        fields = ['year', 'c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8', 'c9', 'c10', 'c11', 'c12', 'c13', 'c14',
                  'c15',
                  'c16', 'c17', 'c18', 'c19', 'c20',
                  'c21', 'c22', 'c23', 'c24', 'c25', 'c26', 'c27', 'c28', 'c29', 'c30', 'c31', 'c32', 'c33', 'c34',
                  'c35',
                  'c36', 'c37', 'c38', 'c39',
                  'c40', 'c41', 'c42', 'c43', 'c44', 'c45', 'c46', 'c47', 'c48', 'c49', 'c50', 'c51', 'c52', 'c53',
                  'c54',
                  'c55', 'c56', 'c57', 'c58',
                  'c59', 'c60', 'c61', 'c62', 'c63', 'c64', 'c65', 'c66', 'c67', 'c68', 'c69', 'c70', 'c71', 'c72',
                  'c73',
                  'c74', 'c75', 'c76', 'c77',
                  'c78', 'c79', 'c80', 'c81', 'c82', 'c83', 'c84', 'c85', 'c86', 'c87', 'c88', 'c89', 'c90']
        fields = ['year', 'c1']
        y_column = 0  # should be the order in the input file, not in the "fields" order.
        fields = ['year', 'c1', 'c2', 'c3', 'c4']
        # fields = ['year', 'c2', 'c4']
        y_column = 0  # should be the order in the input file, not in the "fields" order.
        # data = tools.load_csv("datasets/1online_video_dataset/1transcoding_mesurment.csv",fields,y_column)
        if sample_size is None:
            data = tools.load_csv(file6, fields, y_column)
        elif sample_size== "10k":
            data = tools.load_csv(file6_qreg_sample_10k, fields, y_column)
        elif sample_size== "100k":
            data = tools.load_csv(file6_qreg_sample_100k, fields, y_column)
        elif sample_size== "1m":
            data = tools.load_csv(file6_qreg_sample_1m, fields, y_column)
        else:
            return None
        # "../data/6YearPredictionMSD_with_header.csv"
    if dataID == 7:
        # Number 7 dataset

        # load the data
        # fields = ['duration','width','height','bitrate','framerate','i','p','b','frames','i_size','p_size','b_size','size','o_bitrate','o_framerate','o_width','o_height','umem','utime']

        fields = ['Time_(seconds)', 'Methane_conc_(ppm)', 'Ethylene_conc_(ppm)', 'c1', 'c2', 'c3', 'c4', 'c5', 'c6',
                  'c7',
                  'c8', 'c9', 'c10', 'c11', 'c12', 'c13', 'c14', 'c15', 'c16']
        fields = ['c1', 'c2']
        y_column = 1  # should be the order in the input file, not in the "fields" order.
        fields = ['c1', 'c2', 'c4']
        fields = ['Methane_conc_(ppm)', 'c1', 'c2']
        fields = ['Methane_conc_(ppm)', 'c1', 'c2', 'c3', 'c4']
        y_column = 2  # should be the order in the input file, not in the "fields" order.
        # data = tools.load_csv("datasets/1online_video_dataset/1transcoding_mesurment.csv",fields,y_column)
        if sample_size is None:
            data = tools.load_csv(file7, fields, y_column, sep=' ')
        elif sample_size== "10k":
            data = tools.load_csv(file7_qreg_sample_10k, fields, y_column)
        elif sample_size== "100k":
            data = tools.load_csv(file7_qreg_sample_100k, fields, y_column)
        elif sample_size== "1m":
            data = tools.load_csv(file7_qreg_sample_1m, fields, y_column)
        else:
            return None
        # "../data/7/7ethylene_methane_with_header.csv"
    if dataID == 8:
        # Number 8 dataset

        # load the data

        fields = ['timestamp', 'Global_active_power', 'Global_reactive_power', 'Voltage', 'Global_intensity',
                  'Sub_metering_1', 'Sub_metering_2', 'Sub_metering_3', 'energy']
        # fields = ['Date',  'Global_active_power', 'Global_reactive_power', 'Voltage', 'Global_intensity',
        #          'Sub_metering_1', 'Sub_metering_2', 'Sub_metering_3']
        fields = ['Global_active_power', 'Global_reactive_power', 'Voltage', 'Global_intensity', 'energy']
        y_column = 4  # should be the order in the input file, not in the "fields" order.
        if sample_size is None:
            data = tools.load_csv(file8, fields, y_column, sep=',')
        elif sample_size== "10k":
            data = tools.load_csv(file8_qreg_sample_10k, fields, y_column)
        elif sample_size== "100k":
            data = tools.load_csv(file8_qreg_sample_100k, fields, y_column)
        elif sample_size== "1m":
            data = tools.load_csv(file8_qreg_sample_1m, fields, y_column)
        else:
            return None
        # "../data/8data.txt"
    return data


def loadNd(dataID,sample_size=None):
    if dataID == 1:
        # Number 1 dataset

        fields = ['duration', 'width', 'height', 'bitrate', 'framerate', 'i', 'p', 'b', 'frames', 'i_size',
                  'p_size',
                  'b_size', 'size', 'o_bitrate', 'o_framerate', 'o_width', 'o_height', 'umem', 'utime']
        # fields = ['i_size', 'umem','utime']
        fields = ['duration', 'bitrate', 'framerate', 'size', 'umem', 'utime']
        y_column = 4  # should be the order in the input file, not in the "fields" order.
        if sample_size is None:
            data = tools.load_csv(file1, fields, y_column)
        elif sample_size== "10k":
            data = tools.load_csv(file1_qreg_sample_10k, fields, y_column)
        elif sample_size== "100k":
            data = tools.load_csv(file1_qreg_sample_100k, fields, y_column)
        elif sample_size== "1m":
            data = tools.load_csv(file1_qreg_sample_1m, fields, y_column)
        else:
            return None
        # "../data/1online_video_dataset/1transcoding_mesurment.csv"
    if dataID == 2:
        # Number 2 dataset
        fields = ["RMSD", "F1", "F2", "F3", "F4", "F5", "F6", "F7", "F8", "F9"]
        # fields = ["RMSD", "F3", "F5"]

        # fields = ["RMSD", "F2", "F7"]
        fields = ["RMSD", "F4", "F5"]

        y_column = 0  # should be the order in the input file, not in the "fields" order.
        if sample_size is None:
            data = tools.load_csv(file2, fields, y_column)
        elif sample_size== "10k":
            data = tools.load_csv(file2_qreg_sample_10k, fields, y_column)
        elif sample_size== "100k":
            data = tools.load_csv(file2_qreg_sample_100k, fields, y_column)
        elif sample_size== "1m":
            data = tools.load_csv(file2_qreg_sample_1m, fields, y_column)
        else:
            return None
        # "../data/2CASP.csv"
    if dataID == 3:
        # Number 3 dataset

        fields = ['year', 'month', 'day', 'hour', 'pm2.5', 'DEWP', 'TEMP', 'PRES', 'Iws', 'Is', 'Ir']
        y_column = 4
        # fields = ['pm2.5','PRES']
        # y_column = 0  # should be the order in the input file, not in the "fields" order.
        # fields = ['pm2.5','TEMP', 'PRES']
        # fields = ['pm2.5', 'TEMP', 'Iws'] # good vision
        # fields = ['pm2.5', 'PRES', 'Iws']
        # y_column = 0  # should be the order in the input file, not in the "fields" order.
        if sample_size is None:
            data = tools.load_csv(file3, fields, y_column)
        elif sample_size== "10k":
            data = tools.load_csv(file3_qreg_sample_10k, fields, y_column)
        elif sample_size== "100k":
            data = tools.load_csv(file3_qreg_sample_100k, fields, y_column)
        elif sample_size== "1m":
            data = tools.load_csv(file3_qreg_sample_1m, fields, y_column)
        else:
            return None
    if dataID == 4:
        # Number 4 dataset

        # load the data
        fields = ['n_tokens_title', 'n_tokens_content', 'n_unique_tokens', 'n_non_stop_unique_tokens']
        y_column = 2
        # fields = ['n_tokens_content', 'n_unique_tokens']
        # y_column = 1  # should be the order in the input file, not in the "fields" order.
        # fields = ['n_tokens_title','n_tokens_content','n_unique_tokens']
        # fields = ['n_tokens_content', 'n_unique_tokens','n_non_stop_unique_tokens']
        # #fields = [ 'n_tokens_content', 'n_unique_tokens', 'n_non_stop_unique_tokens']
        # y_column = 1  # should be the order in the input file, not in the "fields" order.
        if sample_size is None:
            data = tools.load_csv(file4, fields, y_column)
        elif sample_size== "10k":
            data = tools.load_csv(file4_qreg_sample_10k, fields, y_column)
        elif sample_size== "100k":
            data = tools.load_csv(file4_qreg_sample_100k, fields, y_column)
        elif sample_size== "1m":
            data = tools.load_csv(file4_qreg_sample_1m, fields, y_column)
        else:
            return None
    if dataID == 5:
        # Number 5 dataset
        # '''
        # load the data
        fields = ['Temperature', 'Exhaust_Vacuum', 'Ambient_Pressure', 'Relative_Humidity', 'energy_output']
        y_column = 4  # should be the order in the input file, not in the "fields" order.
        if sample_size is None:
            data = tools.load_csv(file5, fields, y_column)
        elif sample_size== "10k":
            data = tools.load_csv(file5_qreg_sample_10k, fields, y_column)
        elif sample_size== "100k":
            data = tools.load_csv(file5_qreg_sample_100k, fields, y_column)
        elif sample_size== "1m":
            data = tools.load_csv(file5_qreg_sample_1m, fields, y_column)
        else:
            return None
    if dataID == 6:
        # Number 6 dataset

        fields = ['year', 'c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8', 'c9', 'c10', 'c11', 'c12', 'c13', 'c14',
                  'c15',
                  'c16', 'c17', 'c18', 'c19', 'c20',
                  'c21', 'c22', 'c23', 'c24', 'c25', 'c26', 'c27', 'c28', 'c29', 'c30', 'c31', 'c32', 'c33', 'c34',
                  'c35',
                  'c36', 'c37', 'c38', 'c39',
                  'c40', 'c41', 'c42', 'c43', 'c44', 'c45', 'c46', 'c47', 'c48', 'c49', 'c50', 'c51', 'c52', 'c53',
                  'c54',
                  'c55', 'c56', 'c57', 'c58',
                  'c59', 'c60', 'c61', 'c62', 'c63', 'c64', 'c65', 'c66', 'c67', 'c68', 'c69', 'c70', 'c71', 'c72',
                  'c73',
                  'c74', 'c75', 'c76', 'c77',
                  'c78', 'c79', 'c80', 'c81', 'c82', 'c83', 'c84', 'c85', 'c86', 'c87', 'c88', 'c89', 'c90']
        fields = ['year', 'c1', 'c2', 'c3']
        y_column = 0  # should be the order in the input file, not in the "fields" order.
        if sample_size is None:
            data = tools.load_csv(file6, fields, y_column)
        elif sample_size== "10k":
            data = tools.load_csv(file6_qreg_sample_10k, fields, y_column)
        elif sample_size== "100k":
            data = tools.load_csv(file6_qreg_sample_100k, fields, y_column)
        elif sample_size== "1m":
            data = tools.load_csv(file6_qreg_sample_1m, fields, y_column)
        else:
            return None
    if dataID == 7:
        # Number 7 dataset

        # load the data
        # fields = ['duration','width','height','bitrate','framerate','i','p','b','frames','i_size','p_size','b_size','size','o_bitrate','o_framerate','o_width','o_height','umem','utime']

        fields = ['Time_(seconds)', 'Methane_conc_(ppm)', 'Ethylene_conc_(ppm)', 'c1', 'c2', 'c3', 'c4', 'c5', 'c6',
                  'c7',
                  'c8', 'c9', 'c10', 'c11', 'c12', 'c13', 'c14', 'c15', 'c16']
        fields = ['c1', 'c2']
        y_column = 1  # should be the order in the input file, not in the "fields" order.
        fields = ['c1', 'c2', 'c4']
        fields = ['Methane_conc_(ppm)', 'Ethylene_conc_(ppm)', 'c1', 'c2', 'c3', 'c4']
        y_column = 3  # should be the order in the input file, not in the "fields" order.
        # data = tools.load_csv("datasets/1online_video_dataset/1transcoding_mesurment.csv",fields,y_column)
        if sample_size is None:
            data = tools.load_csv(file7, fields, y_column, sep=' ')
        elif sample_size== "10k":
            data = tools.load_csv(file7_qreg_sample_10k, fields, y_column)
        elif sample_size== "100k":
            data = tools.load_csv(file7_qreg_sample_100k, fields, y_column)
        elif sample_size== "1m":
            data = tools.load_csv(file7_qreg_sample_1m, fields, y_column)
        else:
            return None
    if dataID == 8:
        # Number 8 dataset

        # load the data

        fields = ['timestamp', 'Global_active_power', 'Global_reactive_power', 'Voltage', 'Global_intensity',
                  'Sub_metering_1', 'Sub_metering_2', 'Sub_metering_3', 'energy']
        # fields = ['Date',  'Global_active_power', 'Global_reactive_power', 'Voltage', 'Global_intensity',
        #          'Sub_metering_1', 'Sub_metering_2', 'Sub_metering_3']
        # fields = ['Global_active_power', 'Global_reactive_power', 'energy']
        y_column = 8  # should be the order in the input file, not in the "fields" order.
        if sample_size is None:
            data = tools.load_csv(file8, fields, y_column, sep=',')
        elif sample_size== "10k":
            data = tools.load_csv(file8_qreg_sample_10k, fields, y_column)
        elif sample_size== "100k":
            data = tools.load_csv(file8_qreg_sample_100k, fields, y_column)
        elif sample_size== "1m":
            data = tools.load_csv(file8_qreg_sample_1m, fields, y_column)
        else:
            return None
    return data

def save_2d(dataID):
    data = load2d(dataID)
    d = {'x':np.array(data.features).reshape(1,-1)[0],'y':data.labels}
    # print(d)
    df = pd.DataFrame(data=d)
    # print(df)
    df.to_csv('file'+str(dataID)+'.csv', sep=',',index=False)

def save_2d_no_repeated_value(dataID):
    data = load2d(dataID)
    data.remove_repeated_x_1d()
    d = {'x':np.array(data.features).reshape(1,-1)[0],'y':data.labels}
    # print(d)
    df = pd.DataFrame(data=d)
    # print(df)
    df.to_csv('file'+str(dataID)+'_unique.csv', sep=',',index=False)


if __name__ == "__main__":
    data = load2d(5)
    # save_2d(1)
    # save_2d(2)
    # save_2d(3)
    # save_2d(4)
    # save_2d(5)
    # save_2d(6)
    # save_2d(7)
    # save_2d(8)
    for i in range(1,9):
        save_2d_no_repeated_value(i)

