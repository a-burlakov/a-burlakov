import requests


def generate_readme():
    """
    Generates the README.md file by setting up parameters (looks like "$TEST")
    in "readme_template.md".
    """

    # Data getting.
    url_origin = "http://aaburlakov.ru"  # protocol + host
    api_recent_posts = "/api/v1/recentarticles"
    response = requests.get(f"{url_origin}{api_recent_posts}")
    if response.status_code != 200:
        return

    # Data handling.
    recent_posts = response.json()
    print(recent_posts)
    recent_posts_md_texts = []
    for post in recent_posts:
        recent_posts_md_texts.append(
            f"* [{post['title']}]({url_origin + post['get_absolute_url']})")
    recent_posts_text = "\n".join(recent_posts_md_texts)

    # Generating README.md based on the template.
    with open("readme_template.md", "r", encoding="utf-8") as readme_template:
        md_template = readme_template.read()
    with open("README.md", "w") as readme:
        readme_md_text = md_template.format(RECENT_POSTS=recent_posts_text,
                                            URL_ORIGIN=url_origin)
        readme.write(readme_md_text)


if __name__ == "__main__":
    generate_readme()
