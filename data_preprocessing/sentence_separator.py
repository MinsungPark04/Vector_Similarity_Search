import kss
import csv
import pandas as pd

def sentence_split(input_csv_path, output_csv_path):
    dataframe = pd.read_csv(input_csv_path)


    with open(output_csv_path, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)

            header = list(dataframe.columns) + ['kss_content']
            
            writer.writerow(header)

            for index, row in dataframe.iterrows():

                split_sentence = kss.split_sentences(row['content'])
                
                writer.writerow(list(row) + [str(split_sentence)])

if __name__ == '__main__':
    sentence_split(input_csv_path='', output_csv_path='')