import os
import re
import random
from datetime import datetime

def sanitize_title(title):
    # Remove unsafe characters for filenames
    return re.sub(r'[^a-zA-Z0-9_-]', '', title.replace(' ', '-').lower())

def create_new_post_template(destination_folders):
    title = input("Enter the title of the post: ")
    category = input("Enter the category of the post: ")

    sanitized_title = sanitize_title(title)
    img_number = random.randint(1, 10)  # Random image selection
    img_filename = f":post_pic{img_number}.jpg"

    # Current date for the filename and template
    current_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    file_date = datetime.now().strftime('%Y-%m-%d')

    # Define the template with user inputs
    template = f"""---
lng_pair: id_placeholder
title: {title}
author: Your Name Here
category: {category}
tags: [tag1, tag2]
img: "{img_filename}"
date: {current_date}
---

# Your text block goes here
"""

    filename = f"{file_date}-{sanitized_title}.markdown"

    for folder in destination_folders:
        if not os.path.exists(folder):
            os.makedirs(folder)

        file_path = os.path.join(folder, filename)

        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(template)

        print(f"File created: {file_path}")

# Usage
destination_folders = ['_posts/', 'en/_posts/', 'es/_posts/', 'pl/_posts/', 'uk/_posts/']
create_new_post_template(destination_folders)
