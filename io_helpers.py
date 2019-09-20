import pandas as pd
import glob
import os
import collections

def csvs_to_excel(csv_path: str, excel_filename: str, sep: str = ","):
    # create a namedtuple for the filename and dataframe
    Filename_DF = collections.namedtuple("Filename_DF", "filename df")

    # set the path to read in and get all the files as a sorted list
    files = sorted(glob.glob(os.path.join(csv_path, "*.csv")))

    # generator that returns a namedtuple containing the file name sans extension and a df of the data per csv
    file_df_tuples = (Filename_DF(os.path.basename(f).replace(".csv", ""), pd.read_csv(f, header = 0, sep = sep)) for f in files)

    # instantiate the writer
    excel_filename_with_ext = excel_filename + ".xlsx"
    excel_filepath = os.path.join(csv_path, excel_filename_with_ext)
    writer = pd.ExcelWriter(excel_filepath)

    # create a sheet per csv
    for file_df_tuple in file_df_tuples:
        file_df_tuple.df.to_excel(writer, file_df_tuple.filename[0:31], index= False)

    # save to disk
    writer.save()
    
    print("Excel file save to: {}.".format(excel_filepath))