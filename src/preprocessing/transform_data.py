import pandas as pd
import argparse
from abc import ABC
from dataclasses import dataclass, field


def read_text(file_path):
    with open(file_path) as f:
        texts = f.readlines()
    return texts[3:]


def output_csv(talk_list, columns, output_file_path):
    df_talk = pd.DataFrame(talk_list)
    df_talk.columns = columns
    df_talk.to_csv(output_file_path, index = False)


@dataclass
class DataContainer(ABC):
    date : str = ''
    time : str = ''
    who : str = ''
    text : list = field(default_factory=list)

    def make_log_tolist(self):
        joined_text = ''.join(self.text)
        return [self.date, self.time, self.who, joined_text]

def main(input_file_path, output_file_path):
    all_talks = []
    logs = read_text(input_file_path)

    for log in logs:
        date_finder = len(log.split('/'))
        start_finder = len(log.split('\t'))

        if date_finder == 3:
            date = log[:-4]

        elif start_finder == 3:
            text_info = log.split('\t')

            try:
                all_talks.append(data_holder.make_log_tolist())
            except:
                pass

            data_holder = DataContainer()
            data_holder.date = date
            data_holder.time, data_holder.who, text = text_info
            data_holder.text.append(text)

        elif log == '\n':
            continue

        else:
            data_holder.text.append(log)

    columns=[['date', 'time', 'who', 'text']]
    output_csv(all_talks, columns, output_file_path)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input-file")
    args = parser.parse_args()
    input_file_path=args.input_file
    
    main(input_file_path, 'data/processed/text_df.csv')