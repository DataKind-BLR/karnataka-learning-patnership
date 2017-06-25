import pandas as pd
import argparse
import sqlalchemy

COMMUNITY_QUESTION_MAP = {"1. Have you visited your child's school in the last  month?\n (Y-1, N-0, Unaware-88, Not Answered-99)": "visit_school",
                          "2.Does the school has separate functional toilet for girls?  (Y-1, N-0, Unaware-88, Not Answered-99)": "girl_toilet",
                          "3. Are you satisfied with the MDM served in your child's\nschool? (Y-1, N-0, Unaware-88, Not Answered-99)": "mid_day_meal",
                          "4. Is there a teacher shortage in the school?  (Y-1, N-0, Unaware-88, Not Answered-99)": "teacher_shortage",
                          "5. Is the SDMC gathering meeting every month? (Y-1, N-0, Unaware-88, Not Answered-99)": "sdmc_meeting",
                          "6. Do you think your child can read Kannada? (Y-1, N-0, Unaware-88, Not Answered-99)": "kannada_reading",
                          "7. Do you think your child can read English? (Y-1, N-0, Unaware-88, Not Answered-99)": "english_reading",
                          "9. Do you think your child can do subtraction Problems? (Y-1, N-0, Unaware-88, Not Answered-99)": "subtraction",
                          "8. Do you think your child can do addition Problems? (Y-1, N-0, Unaware-88, Not Answered-99)": "addition",
                          "10. Have you attended the Community last time ? (Y-1, N-0, Unaware-88, Not Answered-99)": "community"
                          }


def process_community_feedback(community_feedback):
    '''
    Process the community feedback data to generate performance and make columns
    more readable.

    Args:
        community_feedback (str): path to the community feedback file.

    Return:
        A processed pandas dataframe.
    '''
    feedback_data = pd.read_csv(community_feedback)
    community_feedback_easier_cols = feedback_data.rename(columns=COMMUNITY_QUESTION_MAP)
    for col in community_feedback_easier_cols.columns[10:]:
        community_feedback_easier_cols[col + '_yes'] = community_feedback_easier_cols[col].apply(lambda x: 1 if x == 1 else 0)
        community_feedback_easier_cols[col + '_no'] = community_feedback_easier_cols[col].apply(lambda x: 1 if x == 0 else 0)
        community_feedback_easier_cols[col + '_unaware'] = community_feedback_easier_cols[col].apply(lambda x: 1 if x == 88 else 0)
        community_feedback_easier_cols[col + '_not_answered'] = community_feedback_easier_cols[col].apply(lambda x: 1 if x == 99 else 0)
    return community_feedback_easier_cols


def process_classes_data(class4, class5, class6):
    '''
    Combine all classes together into a single dataframe.

    Args:
        class4 (str): path to the class 4 contest data.
        class5 (str): path to the class 5 contest data.
        class6 (str): path to the class 6 contest data.

    Return:
        A dataframe with all classes contest data combined.
    '''
    class_4 = pd.read_csv(class4)
    class_5 = pd.read_csv(class5)
    class_6 = pd.read_csv(class6)
    class_4['class'] = 4
    class_5['class'] = 5
    class_6['class'] = 6
    class_data = pd.concat([class_4, class_5, class_6])
    class_data['child_count'] = 1
    return class_data


def save_to_sqlite(o, combined_data):
    '''
    Save the combined data to sqlite file.

    Args:
        o (str): output file name.

    Return:
        True if sqlite file saved else raise error.
    '''
    engine = sqlalchemy.create_engine('sqlite:///{}'.format(o))
    combined_data.to_sql(name='classes', if_exists='append', con=engine, chunksize=10000)
    return True


def run(class4, class5, class6, community_feedback, o):
    print('Processing Classes.')
    class_data = process_classes_data(class4, class5, class6)
    print('Processing Community Feedback Data.')
    feedback_data = process_community_feedback(community_feedback)
    print('Joining Data.')
    combined_data = pd.merge(class_data, feedback_data, on=['District', 'Block', 'KLP ID'])
    print('Calculating Performance')
    combined_data['performance'] = combined_data['Total'] / (combined_data['child_count'] * 20)
    print('Storing To Sqlite')
    save_to_sqlite(o, combined_data)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process Class files to generate Sqlite file.')
    parser.add_argument('class4', type=str,
                        help='Path to the class 4 csv file.')
    parser.add_argument('class5', type=str,
                        help='Path to the class 5 csv file.')
    parser.add_argument('class6', type=str,
                        help='Path to the class 6 csv file.')
    parser.add_argument('community_feedback', type=str,
                        help='community feedback data.')
    parser.add_argument('-o', type=str,
                        help='Name of the output file.', default='combined_data.sqlite')

    args = parser.parse_args()
    run(getattr(args, 'class4'), getattr(args, 'class5'), getattr(args, 'class6'),
        getattr(args, 'community_feedback'), getattr(args, 'o'))
