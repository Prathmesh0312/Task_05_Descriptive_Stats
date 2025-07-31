"""import pandas as pd
import os

file_path = 'data/2024_fb_ads_president_scored_anon.csv'
df = pd.read_csv(file_path)

numeric_cols = ['estimated_audience_size', 'estimated_impressions', 'estimated_spend']

print("\nMissing Value Count Per Column for Numerical cols:")
print(df[numeric_cols].isnull().sum())

print("\nDescriptive Statistics for Numeric Columns")
print(df[numeric_cols].describe())
    #Descriptive Stats for categorical columns
print("\nUnique Value Counts (Categorical Columns)")
for col in df.columns:
    if df[col].dtype == 'object' or df[col].dtype.name == 'category':
        print(f"\nColumn: {col}")
        print(df[col].value_counts(dropna=False).head(10))

#Grouped by page_id
output_file_for_pageid = "grouped_by_page.csv"
print("\nGrouped Statistics by 'page_id'")
grouped_by_page = df.groupby('page_id')[numeric_cols].describe().head(3)
print(grouped_by_page)
    # Save to CSV as I am not able to see the whole output for evaluation lateer
grouped_by_page.to_csv(output_file_for_pageid)
print(f"\nGrouped statistics saved to: {os.path.abspath(output_file_for_pageid)}")

    #Grouped by ad_id
top3_df = df.head(3)
output_file_for_adid = "grouped_by_ad.csv"
print("\nGrouped Statistics by 'ad_id'")
grouped_by_ad = top3_df.groupby('ad_id')[numeric_cols].describe()
print(grouped_by_ad)
    # Save to CSV as I am not able to see the whole output for evaluation lateer
grouped_by_ad.to_csv(output_file_for_adid)
print(f"\nGrouped statistics saved to: {os.path.abspath(output_file_for_adid)}")

    # Grouped Statistics by 'page_id' and 'ad_id'
if 'ad_id' in df.columns:
    first3_df = df.head(3)
    output_file_for_pagead = "grouped_by_pagead.csv"
    print("\nGrouped Statistics by 'page_id' and 'ad_id'")
    grouped_by_page_ad = first3_df.groupby(['page_id', 'ad_id']).describe()
    print(grouped_by_page_ad)

    grouped_by_page_ad.to_csv(output_file_for_pagead)
    print(f"\nGrouped statistics saved to: {os.path.abspath(output_file_for_pagead)}")


##2nd dataset
##Doing same for fb_posts dataset
file_path = 'data/2024_fb_posts_president_scored_anon.csv'
df = pd.read_csv(file_path)
numeric_cols = ['Total Interactions', 'Likes', 'Comments', 'Shares', 'Love', 'Wow', 'Haha', 'Sad', 'Angry', 'Care', 'Post Views', 'Total Views', 'Total Views', 'Total Views For All Crossposts']

print("\nDescriptive Statistics for Numeric Columns")
print(df[numeric_cols].describe())
    #Descriptive Stats for categorical columns
print("\nUnique Value Counts (Categorical Columns)")
for col in df.columns:
    if df[col].dtype == 'object' or df[col].dtype.name == 'category':
        print(f"\nColumn: {col}")
        print(df[col].value_counts(dropna=False).head(5))


    #Grouped by Facebook_Id
output_file_for_fbid = "grouped_by_fbid.csv"
print("\nGrouped Statistics by 'Facebook_Id'")
grouped_by_fbid = df.groupby('Facebook_Id')[numeric_cols].describe().head(3)
print(grouped_by_fbid)

grouped_by_fbid.to_csv(output_file_for_fbid)
print(f"\nGrouped statistics saved to: {os.path.abspath(output_file_for_fbid)}")


    #Grouped by post_id
top3_df = df.head(3)
output_file_for_postid = "grouped_by_post.csv"
print("\nGrouped Statistics by 'post_id'")
grouped_by_post = top3_df.groupby('post_id')[numeric_cols].describe()
print(grouped_by_post)

grouped_by_post.to_csv(output_file_for_postid)
print(f"\nGrouped statistics saved to: {os.path.abspath(output_file_for_postid)}")


    # Grouped Statistics by # FB and Post
if 'post_id' in df.columns:
    first3_df = df.head(3)
    output_file_for_fbpost = "grouped_by_fbpost.csv"
    print("\nGrouped Statistics by 'Facebook_Id' and 'post_id'")
    grouped_by_fbpost = first3_df.groupby(['Facebook_Id', 'post_id']).describe()
    print(grouped_by_fbpost)

    grouped_by_fbpost.to_csv(output_file_for_fbpost)
    print(f"\nGrouped statistics saved to: {os.path.abspath(output_file_for_fbpost)}")


##3rd dataset
##Doing same for tw_posts dataset
file_path = 'data/2024_tw_posts_president_scored_anon.csv'
df = pd.read_csv(file_path)
numeric_cols = ['retweetCount', 'replyCount', 'likeCount', 'quoteCount', 'viewCount', 'bookmarkCount']

print("\nDescriptive Statistics for Numeric Columns")
print(df[numeric_cols].describe())
    #Descriptive Stats for categorical columns
print("\nUnique Value Counts (Categorical Columns)")
for col in df.columns:
    if df[col].dtype == 'object' or df[col].dtype.name == 'category':
        print(f"\nColumn: {col}")
        print(df[col].value_counts(dropna=False).head(5))


    #Grouped by twitter Id
top3_df = df.head(3)
output_file_for_id = "grouped_by_id.csv"
print("\nGrouped Statistics by 'id'")
grouped_by_id = df.groupby('id')[numeric_cols].describe()
print(grouped_by_id)

grouped_by_id.to_csv(output_file_for_id)
print(f"\nGrouped statistics saved to: {os.path.abspath(output_file_for_id)}")


    #Grouped by url
top3_df = df.head(3)
output_file_for_url = "grouped_by_url.csv"
print("\nGrouped Statistics by 'url'")
grouped_by_url = top3_df.groupby('url')[numeric_cols].describe()
print(grouped_by_url)

grouped_by_url.to_csv(output_file_for_url)
print(f"\nGrouped statistics saved to: {os.path.abspath(output_file_for_url)}")


    # Grouped Statistics by # id and url
if 'url' in df.columns:
    first3_df = df.head(3)
    output_file_for_idurl = "grouped_by_idurl.csv"
    print("\nGrouped Statistics by 'id' and 'url'")
    grouped_by_idurl = first3_df.groupby(['id', 'url']).describe()
    print(grouped_by_idurl)

    grouped_by_idurl.to_csv(output_file_for_idurl)
    print(f"\nGrouped statistics saved to: {os.path.abspath(output_file_for_idurl)}")"""

##Building a function for pandas
import pandas as pd
import os

def generate_pandas_stats(file_path, numeric_columns, group_by=None, output_prefix="grouped_output"):
    """
    Generate descriptive statistics from a CSV using pandas, with optional grouping.
    
    Parameters:
        file_path (str): Path to the CSV file.
        numeric_columns (list): List of numeric column names.
        group_by (str or list, optional): Column(s) to group by. Defaults to None.
        output_prefix (str): Prefix for output CSV filenames. Defaults to "grouped_output".
    """
    df = pd.read_csv(file_path)

    print("\nMissing Value Count Per Column for Numeric Columns:")
    print(df[numeric_columns].isnull().sum())

    print("\nDescriptive Statistics for Numeric Columns:")
    print(df[numeric_columns].describe())

    print("\nUnique Value Counts (Top 10 per Categorical Column):")
    for col in df.columns:
        if df[col].dtype == 'object' or df[col].dtype.name == 'category':
            print(f"\nColumn: {col}")
            print(df[col].value_counts(dropna=False).head(10))

    # Grouped Statistics
    if group_by:
        if isinstance(group_by, str):
            group_by = [group_by]

        key_name = "_".join(group_by)
        output_file = f"{output_prefix}_by_{key_name}.csv"

        print(f"\nGrouped Statistics by {', '.join(group_by)}")
        grouped = df.groupby(group_by)[numeric_columns].describe()

        print(grouped.head(3))  # Preview first 3 groups
        grouped.to_csv(output_file)
        print(f"\nGrouped statistics saved to: {os.path.abspath(output_file)}")


"""#Giving dataset specific inputs
if __name__ == "__main__":
    file_path = 'data/IPEDS_data.csv'
    numeric_cols = ['Applicants total', 'Admissions total', 'Enrolled total','Estimated enrollment, total', 'Estimated enrollment, full time', 
                       'Estimated enrollment, part time', 'Estimated undergraduate enrollment, full time', 
                       'Estimated undergraduate enrollment, part time', 'Estimated freshman undergraduate enrollment, total', 
                       'Estimated freshman enrollment, full time', 'Estimated freshman enrollment, part time', 
                       'Estimated graduate enrollment, total',
                       'Estimated graduate enrollment, full time', 'Estimated graduate enrollment, part time']

    #  Overall stats 
    generate_pandas_stats(file_path, numeric_cols)

    #  Grouped by one column
    generate_pandas_stats(file_path, numeric_cols, group_by='Highest degree offered', output_prefix="by_degree")

    #  Grouped by 2 columns
    generate_pandas_stats(file_path, numeric_cols, group_by=['Highest degree offered', 'County name'], output_prefix="county_degree")"""


## Verifying the most overs bowled across winning matches
import pandas as pd
df = pd.read_csv("llm_ready_bowling_summary.csv")

# Find player with most overs
most_overs = df.loc[df['Total_Overs'].idxmax()]
print(f"Most Overs: {most_overs['Player']} with {most_overs['Total_Overs']} overs")


## team with most economical bowling performance
df = pd.read_csv("llm_ready_bowling_with_match_context.csv")

# Group by team and calculate mean economy rate
team_economy = df.groupby('Winner')['Economy'].mean().sort_values()
print(team_economy.head(3))

##MNumber of bowlers who bowled more than 7 overs
df = pd.read_csv("llm_ready_bowling_summary.csv")

count = df[df['Total_Overs'] > 7].shape[0]
print(f"✅ Number of bowlers with >7 overs: {count}")
