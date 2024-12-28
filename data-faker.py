import numpy as np
import pandas as pd
from faker import Faker
import random
from datetime import datetime, timedelta

fake = Faker()

# Parameters
NUM_USERS = 1000
NUM_CONTENT = 200
DAYS_OF_DATA = 60  # 2 months

# 1. Generate Users
user_data = []
for user_id in range(1, NUM_USERS+1):
    # Optional: random subscription type, region, etc.
    subscription_type = random.choice(["Basic", "Premium"])
    region = random.choice(["US", "Canada", "UK", "Australia"])
    user_data.append([user_id, subscription_type, region])
    
users_df = pd.DataFrame(user_data, columns=["user_id", "subscription_type", "region"])

# 2. Generate Content
content_data = []
genres = ["Action", "Comedy", "Drama", "Sci-Fi", "Documentary"]
content_types = ["Movie", "Episode"]
for content_id in range(1, NUM_CONTENT+1):
    title = fake.catch_phrase()
    genre = random.choice(genres)
    ctype = random.choice(content_types)
    release_year = random.randint(1990, 2023)
    content_data.append([content_id, title, genre, ctype, release_year])
content_df = pd.DataFrame(content_data, columns=["content_id", "title", "genre", "content_type", "release_year"])

# 3. Generate Engagement (Watch Logs)
engagement_data = []
start_date = datetime.now() - timedelta(days=DAYS_OF_DATA)

for day_offset in range(DAYS_OF_DATA):
    current_date = start_date + timedelta(days=day_offset)
    # Let's say each day we randomly pick some users to watch random content
    daily_users = random.sample(range(1, NUM_USERS+1), k=random.randint(200, 500))
    for user in daily_users:
        # random number of content pieces watched
        num_contents_watched = random.randint(1, 5)
        for _ in range(num_contents_watched):
            content_id = random.randint(1, NUM_CONTENT)
            # random watch duration
            minutes_watched = random.randint(1, 120)  # up to 2 hours
            device_type = random.choice(["Mobile", "Smart TV", "Web", "Tablet"])
            
            # For "completion rate," let's say a watch is "completed" if minutes_watched > 80% of 120 min
            was_completed = 1 if minutes_watched >= int(0.8 * 120) else 0
            
            engagement_data.append([
                user, content_id, current_date.strftime("%Y-%m-%d"), 
                minutes_watched, device_type, was_completed
            ])

engagement_df = pd.DataFrame(engagement_data, columns=[
    "user_id", "content_id", "view_date", "minutes_watched", "device_type", "was_completed"
])

# 4. Save to CSV
users_df.to_csv("users.csv", index=False)
content_df.to_csv("content.csv", index=False)
engagement_df.to_csv("engagement.csv", index=False)

print("Synthetic data generated and saved to CSV files!")
