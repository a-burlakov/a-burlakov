import requests


def generate_readme():
    """
    Generates the README.md file by setting up parameters (looks like "$TEST")
    in "readme_template.md".
    """
    site_url = "http://aaburlakov.ru"
    api_recent_posts = "/api/v1/recentarticles"
    response = requests.get(f"{site_url}{api_recent_posts}")
    if response.status_code != 200:
        return

    recent_posts = response.json()
    print(recent_posts)
    recent_posts_md_texts = []
    for post in recent_posts:
        recent_posts_md_texts.append(f"* [{post['title']}]({site_url + post['get_absolute_url']})")
    recent_posts_text = "\n".join(recent_posts_md_texts)
    with open('readme_template.md', 'r', encoding="utf-8") as f:
        readme_template = f.read()
    with open('README.md', 'w') as f:
        f.write(readme_template.format(RECENT_POSTS=recent_posts_text))


if __name__ == '__main__':
    generate_readme()
