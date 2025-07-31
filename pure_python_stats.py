"""#data extraction, statistics, counting, math
import csv
from statistics import mean, median, mode, StatisticsError
from collections import defaultdict

file_path = "data/2024_fb_ads_president_scored_anon.csv"

# Load the CSV file
with open(file_path, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    data = list(reader)

numeric_columns = ['estimated_spend', 'estimated_impressions', 'estimated_audience_size']
#check for null values in numerical cols
print("\nMissing (null/empty) value count per numeric column:")
for col in numeric_columns:
    missing = sum(1 for row in data if not row[col].strip())
    print(f"  {col}: {missing} missing values")


print("\nDescriptive Statistics (Overall - Pure Python):")
for col in numeric_columns:
    values = [float(row[col]) for row in data if row[col].replace('.', '', 1).isdigit()]
    if values:
        print(f"\nColumn: {col}")
        print(f"  Count: {len(values)}")
        print(f"  Mean: {mean(values):.2f}")
        print(f"  Median: {median(values):.2f}")
        try:
            print(f"  Mode: {mode(values)}")
        except StatisticsError:
            print("  Mode: No unique mode found")
        print(f"  Min: {min(values)}")
        print(f"  Max: {max(values)}")
    else:
        print(f"\nColumn: {col} has no valid numeric data.")

## Grouped by page_id
grouped_by_page = defaultdict(list) 
for row in data:
    grouped_by_page[row['page_id']].append(row) 

print("\nGrouped Descriptive Statistics by page_id:")
for page_id, rows in list(grouped_by_page.items())[:3]:  
    print(f"\nPage ID: {page_id}")
    for col in numeric_columns:
        values = [float(r[col]) for r in rows if r[col].replace('.', '', 1).isdigit()]
        if values:
            print(f"  {col}:")
            print(f"    Count: {len(values)}")
            print(f"    Mean: {mean(values):.2f}")
            print(f"    Median: {median(values):.2f}")
            try:
                print(f"    Mode: {mode(values)}")
            except StatisticsError:
                print("    Mode: No unique mode found")
            print(f"    Min: {min(values)}")
            print(f"    Max: {max(values)}")
        else:
            print(f"  {col}: No valid numeric data.")

# Grouped by ad_id
grouped_by_ad = defaultdict(list) 
for row in data:
    grouped_by_ad[row['ad_id']].append(row)

print("\nGrouped Descriptive Statistics by ad_id:")
for ad_id, rows in list(grouped_by_ad.items())[:3]:
    print(f"\nAd ID: {ad_id}")
    for col in numeric_columns:
        values = [float(r[col]) for r in rows if r[col].replace('.', '', 1).isdigit()] 
        if values:
            print(f"  {col}:")
            print(f"    Count: {len(values)}")
            print(f"    Mean: {mean(values):.2f}")
            print(f"    Median: {median(values):.2f}")
            try:
                print(f"    Mode: {mode(values)}")
            except StatisticsError:
                print("    Mode: No unique mode found")
            print(f"    Min: {min(values)}")
            print(f"    Max: {max(values)}")
        else:
            print(f"  {col}: No valid numeric data.")

# Grouped by (page_id, ad_id)
grouped_by_page_ad = defaultdict(list) 
for row in data:
    key = (row['page_id'], row['ad_id'])
    grouped_by_page_ad[key].append(row)

print("\nGrouped Descriptive Statistics by (page_id, ad_id):")
for (page_id, ad_id), rows in list(grouped_by_page_ad.items())[:3]: 
    print(f"\nPage ID: {page_id} | Ad ID: {ad_id}")
    for col in numeric_columns:
        values = [float(r[col]) for r in rows if r[col].replace('.', '', 1).isdigit()] 
        if values:
            print(f"  {col}:")
            print(f"    Count: {len(values)}")
            print(f"    Mean: {mean(values):.2f}")
            print(f"    Median: {median(values):.2f}")
            try:
                print(f"    Mode: {mode(values)}")
            except StatisticsError:
                print("    Mode: No unique mode found")
            print(f"    Min: {min(values)}")
            print(f"    Max: {max(values)}")
        else:
            print(f"  {col}: No valid numeric data.")


##Doing same for fb-posts dataset
#data extraction, statistics, counting, math
from statistics import mean, median, mode, StatisticsError
from collections import defaultdict

file_path = "data/2024_fb_posts_president_scored_anon.csv"


with open(file_path, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    data = list(reader)

numeric_columns = ['Total Interactions', 'Likes', 'Comments', 'Shares', 'Love', 'Wow', 'Haha', 'Sad', 'Angry', 'Care', 'Post Views', 'Total Views', 'Total Views', 'Total Views For All Crossposts']

print("\nDescriptive Statistics (Overall - Pure Python):")
for col in numeric_columns:
    values = [float(row[col]) for row in data if row[col].replace('.', '', 1).isdigit()]
    if values:
        print(f"\nColumn: {col}")
        print(f"  Count: {len(values)}")
        print(f"  Mean: {mean(values):.2f}")
        print(f"  Median: {median(values):.2f}")
        try:
            print(f"  Mode: {mode(values)}")
        except StatisticsError:
            print("  Mode: No unique mode found")
        print(f"  Min: {min(values)}")
        print(f"  Max: {max(values)}")
    else:
        print(f"\nColumn: {col} has no valid numeric data.")

# Facebook_Id Group By
grouped_by_FBID = defaultdict(list)  
for row in data:
    grouped_by_FBID[row['Facebook_Id']].append(row)  
print("\nGrouped Descriptive Statistics by Facebook_Id:")
for Facebook_Id, rows in list(grouped_by_FBID.items())[:3]:    
    print(f"\nFacebook_Id: {Facebook_Id}")
    for col in numeric_columns:
        values = [float(r[col]) for r in rows if r[col].replace('.', '', 1).isdigit()]  
        if values:
            print(f"  {col}:")
            print(f"    Count: {len(values)}")
            print(f"    Mean: {mean(values):.2f}")
            print(f"    Median: {median(values):.2f}")
            try:
                print(f"    Mode: {mode(values)}")
            except StatisticsError:
                print("    Mode: No unique mode found")
            print(f"    Min: {min(values)}")
            print(f"    Max: {max(values)}")
        else:
            print(f"  {col}: No valid numeric data.")

# Grouped by post_id
grouped_by_post = defaultdict(list)  
for row in data:
    grouped_by_post[row['post_id']].append(row)  
print("\nGrouped Descriptive Statistics by post:")
for post_id, rows in list(grouped_by_post.items())[:3]: 
    print(f"\npost_id: {post_id}")
    for col in numeric_columns:
        values = [float(r[col]) for r in rows if r[col].replace('.', '', 1).isdigit()]
        if values:
            print(f"  {col}:")
            print(f"    Count: {len(values)}")
            print(f"    Mean: {mean(values):.2f}")
            print(f"    Median: {median(values):.2f}")
            try:
                print(f"    Mode: {mode(values)}")
            except StatisticsError:
                print("    Mode: No unique mode found")
            print(f"    Min: {min(values)}")
            print(f"    Max: {max(values)}")
        else:
            print(f"  {col}: No valid numeric data.")

# Grouped by 
# FB and Post
grouped_by_FB_Post = defaultdict(list)
for row in data:
    key = (row['Facebook_Id'], row['post_id'])
    grouped_by_FB_Post[key].append(row) 

print("\nGrouped Descriptive Statistics by (FB_Id,Post_id):")
for (Facebook_Id, post_id), rows in list(grouped_by_FB_Post.items())[:3]: 
    print(f"\nFB ID: {Facebook_Id} | Post ID: {post_id}")
    for col in numeric_columns:
        values = [float(r[col]) for r in rows if r[col].replace('.', '', 1).isdigit()]
        if values:
            print(f"  {col}:")
            print(f"    Count: {len(values)}")
            print(f"    Mean: {mean(values):.2f}")
            print(f"    Median: {median(values):.2f}")
            try:
                print(f"    Mode: {mode(values)}")
            except StatisticsError:
                print("    Mode: No unique mode found")
            print(f"    Min: {min(values)}")
            print(f"    Max: {max(values)}")
        else:
            print(f"  {col}: No valid numeric data.")

##doing same for tw dataset
from statistics import mean, median, mode, StatisticsError
from collections import defaultdict

file_path = "data/2024_tw_posts_president_scored_anon.csv"

with open(file_path, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    data = list(reader)

numeric_columns = ['retweetCount', 'replyCount', 'likeCount', 'quoteCount', 'viewCount', 'bookmarkCount']

print("\nDescriptive Statistics (Overall - Pure Python):")
for col in numeric_columns:
    values = [float(row[col]) for row in data if row[col].replace('.', '', 1).isdigit()]
    
    if values:
        print(f"\nColumn: {col}")
        print(f"  Count: {len(values)}")
        print(f"  Mean: {mean(values):.2f}")
        print(f"  Median: {median(values):.2f}")
        try:
            print(f"  Mode: {mode(values)}")
        except StatisticsError:
            print("  Mode: No unique mode found")
        print(f"  Min: {min(values)}")
        print(f"  Max: {max(values)}")
    else:
        print(f"\nColumn: {col} has no valid numeric data.")

# Tw id Group By
grouped_by_TWID = defaultdict(list)  
for row in data:
    grouped_by_TWID[row['id']].append(row)   
print("\nGrouped Descriptive Statistics by TWID:")
for id, rows in list(grouped_by_TWID.items())[:3]:   
    print(f"\nTW_Id: {id}")
    for col in numeric_columns:
        values = [float(r[col]) for r in rows if r[col].replace('.', '', 1).isdigit()] 
        if values:
            print(f"  {col}:")
            print(f"    Count: {len(values)}")
            print(f"    Mean: {mean(values):.2f}")
            print(f"    Median: {median(values):.2f}")
            try:
                print(f"    Mode: {mode(values)}")
            except StatisticsError:
                print("    Mode: No unique mode found")
            print(f"    Min: {min(values)}")
            print(f"    Max: {max(values)}")
        else:
            print(f"  {col}: No valid numeric data.")

# Grouped by url
grouped_by_url = defaultdict(list)  
for row in data:
    grouped_by_url[row['url']].append(row)  
print("\nGrouped Descriptive Statistics by url:")
for url, rows in list(grouped_by_url.items())[:3]: 
    print(f"\nurl: {url}")
    for col in numeric_columns:
        values = [float(r[col]) for r in rows if r[col].replace('.', '', 1).isdigit()]
        if values:
            print(f"  {col}:")
            print(f"    Count: {len(values)}")
            print(f"    Mean: {mean(values):.2f}")
            print(f"    Median: {median(values):.2f}")
            try:
                print(f"    Mode: {mode(values)}")
            except StatisticsError:
                print("    Mode: No unique mode found")
            print(f"    Min: {min(values)}")
            print(f"    Max: {max(values)}")
        else:
            print(f"  {col}: No valid numeric data.")

# Grouped by 
# id and url
grouped_by_id_url = defaultdict(list)
for row in data:
    key = (row['id'], row['url'])
    grouped_by_id_url[key].append(row) 

print("\nGrouped Descriptive Statistics by (Id, url):")
for (id, url), rows in list(grouped_by_id_url.items())[:3]: 
    print(f"\nid: {id} | url: {url}")
    for col in numeric_columns:
        values = [float(r[col]) for r in rows if r[col].replace('.', '', 1).isdigit()] 
        if values:
            print(f"  {col}:")
            print(f"    Count: {len(values)}")
            print(f"    Mean: {mean(values):.2f}")
            print(f"    Median: {median(values):.2f}")
            try:
                print(f"    Mode: {mode(values)}")
            except StatisticsError:
                print("    Mode: No unique mode found")
            print(f"    Min: {min(values)}")
            print(f"    Max: {max(values)}")
        else:
            print(f"  {col}: No valid numeric data.")


            
"""


"""##Buinding a function which will analyze with any given dataset input
import csv
from statistics import mean, median, mode, StatisticsError
from collections import defaultdict

def generate_pure_python_stats(file_path, numeric_columns, group_by=None):
    # Load CSV data
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        data = list(reader)

    print("\nMissing (null/empty) value count per numeric column:")
    for col in numeric_columns:
        missing = sum(1 for row in data if not row[col].strip())
        print(f"  {col}: {missing} missing values")

    print("\nDescriptive Statistics (Overall - Pure Python):")
    for col in numeric_columns:
        values = [float(row[col]) for row in data if row[col].replace('.', '', 1).isdigit()]
        if values:
            print(f"\nColumn: {col}")
            print(f"  Count: {len(values)}")
            print(f"  Mean: {mean(values):.2f}")
            print(f"  Median: {median(values):.2f}")
            try:
                print(f"  Mode: {mode(values)}")
            except StatisticsError:
                print("  Mode: No unique mode found")
            print(f"  Min: {min(values)}")
            print(f"  Max: {max(values)}")
        else:
            print(f"\nColumn: {col} has no valid numeric data.")

    # Grouped by 
    if group_by:
        if isinstance(group_by, str):
            group_by = [group_by]

        key_name = " + ".join(group_by)
        print(f"\nGrouped Descriptive Statistics by {key_name}:")
        grouped = defaultdict(list)

        for row in data:
            key = tuple(row[g] for g in group_by)
            grouped[key].append(row)

        for group_key, rows in list(grouped.items())[:3]: 
            group_label = " | ".join(group_key)
            print(f"\nGroup: {group_label}")
            for col in numeric_columns:
                values = [float(r[col]) for r in rows if r[col].replace('.', '', 1).isdigit()]
                if values:
                    print(f"  {col}:")
                    print(f"    Count: {len(values)}")
                    print(f"    Mean: {mean(values):.2f}")
                    print(f"    Median: {median(values):.2f}")
                    try:
                        print(f"    Mode: {mode(values)}")
                    except StatisticsError:
                        print("    Mode: No unique mode found")
                    print(f"    Min: {min(values)}")
                    print(f"    Max: {max(values)}")
                else:
                    print(f"  {col}: No valid numeric data.")


##Giving input for specific dataset to try out the function
if __name__ == "__main__":
    file_path = "data/IPEDS_data.csv"
    numeric_columns = ['Applicants total', 'Admissions total', 'Enrolled total','Estimated enrollment, total', 'Estimated enrollment, full time', 
                       'Estimated enrollment, part time', 'Estimated undergraduate enrollment, full time', 
                       'Estimated undergraduate enrollment, part time', 'Estimated freshman undergraduate enrollment, total', 
                       'Estimated freshman enrollment, full time', 'Estimated freshman enrollment, part time', 
                       'Estimated graduate enrollment, total',
                       'Estimated graduate enrollment, full time', 'Estimated graduate enrollment, part time']
                   
    # Overall stats + Group by one column
    generate_pure_python_stats(file_path, numeric_columns, group_by="Highest degree offered")

    # group by 2 columns
    generate_pure_python_stats(file_path, numeric_columns, group_by=["Highest degree offered", "County name"])"""


import pandas as pd

# Load datasets
matches = pd.read_csv("match_schedule_results.csv")
bowling = pd.read_csv("bowling_summary.csv")

# Merge both on Match_no
merged = bowling.merge(
    matches[['Match_no', 'Date', 'Venue', 'Team1', 'Team2', 'Winner']],
    on='Match_no',
    how='left'
)

# Filter only bowlers from the winning team
winning_bowling = merged[merged['Bowling_Team'] == merged['Winner']]

# Select and rename final columns
final_df = winning_bowling[[
    'Match_no', 'Date', 'Venue', 'Team1', 'Team2', 'Winner',
    'Bowling_Team', 'Bowler_Name', 'Overs', 'Maidens', 'Runs', 'Wickets', 'Economy'
]].rename(columns={
    'Bowling_Team': 'Team',
    'Bowler_Name': 'Bowler'
})

# Save to CSV
output_file = "llm_ready_bowling_with_match_context.csv"
final_df.to_csv(output_file, index=False)

print(f"Final LLM-ready file saved to: {output_file}")



