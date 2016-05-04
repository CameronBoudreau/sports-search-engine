import psycopg2
import pandas as pd
import argparse


def main(add):

    if add:
        print(add)
        conn = psycopg2.connect("dbname=Cameron user=Cameron host=/tmp/")
        cur = conn.cursor()

        columns = ['Rank', 'Player', 'Rushing_Att', 'Rushing_Yds', 'Rushing_Avg', 'Rushing_TD', 'Receiving_Rec', 'Receiving_Yds', 'Receiving_Avg', 'Receiving_TD', 'Scrimmage_Plays', 'Scrimmage_Yds', 'Scrimmage_Avg', 'Scrimmage_TD']

        cur.execute("SELECT * from player_data;")
        rows = len(cur.fetchall())

        data = pd.read_csv(add)
        data.columns = columns
        data.fillna(0, inplace=True)

        for row in data.itertuples():
            cur.execute("""INSERT INTO player_data VALUES ({}, {}, '{}', {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {});""".format(rows + row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14]))

        conn.commit()
        cur.close()
        conn.close()

    else:
        print('You did not pass in a file.')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--add', type=str, nargs='?', help='pass in a csv file with exactly 14 columns and a header (will be changed) in the correct order')
    args = parser.parse_args()
    main(args.add)
