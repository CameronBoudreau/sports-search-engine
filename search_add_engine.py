import psycopg2
import pandas as pd


def get_search_terms(columns):
    search_terms = list([])

    print("What would you like to search for? You will be prompted for each field value in order. If you want to skip a field, simply press Enter.")

    for i in range(14):
        term = input("{}: ".format(columns[i]))
        if term == '':
            search_terms.append('9999')
        else:
            search_terms.append(term)
    return search_terms


def check_database(search_terms, columns, cur):
    cur.execute("SELECT * from player_data WHERE Rank='{}' OR Player='{}' OR Rushing_Att='{}' OR Rushing_Yds='{}' OR Rushing_Avg='{}' OR Rushing_TD='{}' OR Receiving_Rec='{}' OR Receiving_Yds='{}' OR Receiving_Avg='{}' OR Receiving_TD='{}' OR Scrimmage_Plays='{}' OR Scrimmage_Yds='{}' OR Scrimmage_Avg='{}' OR Scrimmage_TD='{}'".format(search_terms[0], search_terms[1], search_terms[2], search_terms[3], search_terms[4], search_terms[5], search_terms[6], search_terms[7], search_terms[8], search_terms[9], search_terms[10], search_terms[11], search_terms[12], search_terms[13]))

    cur.fetchall()
    # return results

def create_df_display(results, columns):
    print(results)
    results_df = pd.DataFrame()
    results
    return results_df

def main():

    conn = psycopg2.connect("dbname=Cameron user=Cameron host=/tmp/")
    cur = conn.cursor()
    columns = ['Rank', 'Player', 'Rushing_Att', 'Rushing_Yds', 'Rushing_Avg', 'Rushing_TD', 'Receiving_Rec', 'Receiving_Yds', 'Receiving_Avg', 'Receiving_TD', 'Scrimmage_Plays', 'Scrimmage_Yds', 'Scrimmage_Avg', 'Scrimmage_TD']

    search_terms = get_search_terms(columns)

    check_database(search_terms, columns, cur)
    # results
    # results = [x for x in results]
    # del results[0]

if __name__ == '__main__':
    main()
