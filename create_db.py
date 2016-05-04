import psycopg2
import pandas as pd


def main():

    def create_db():
        conn = psycopg2.connect("dbname=Cameron user=Cameron host=/tmp/")
        cur = conn.cursor()

        cur.execute("CREATE TABLE player_data(id serial PRIMARY KEY, Rank varchar, Player varchar, Rushing_Att integer, Rushing_Yds integer, Rushing_Avg integer, Rushing_TD integer, Receiving_Rec integer, Receiving_Yds integer, Receiving_Avg integer, Receiving_TD integer, Scrimmage_Plays integer, Scrimmage_Yds integer, Scrimmage_Avg integer, Scrimmage_TD integer); ")

        columns = ['Rank', 'Player', 'Rushing_Att', 'Rushing_Yds', 'Rushing_Avg', 'Rushing_TD', 'Receiving_Rec', 'Receiving_Yds', 'Receiving_Avg', 'Receiving_TD', 'Scrimmage_Plays', 'Scrimmage_Yds', 'Scrimmage_Avg', 'Scrimmage_TD']

        data = pd.read_csv('stats.csv', header=1)
        data.columns = columns
        data.fillna(0, inplace=True)

        for row in data.itertuples():
            cur.execute("""INSERT INTO player_data VALUES ({}, {}, '{}', {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {});""".format(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14]))

        conn.commit()
        cur.close()
        conn.close()

    create_db()

if __name__ == '__main__':
    main()
