import requests


def generate_readme():
    """
    Generates the README.md file by setting up parameters
    in "readme_template.md".
    """

    # Data getting.
    url_origin = "http://aaburlakov.ru"  # protocol + host
    api_recent_articles = "/api/v1/recentarticles"
    response = requests.get(f"{url_origin}{api_recent_articles}")

    if response.status_code != 200:
        return

    # Data handling.
    recent_posts_data = response.json()
    md_lines = []

    # Generating markdown lines for each post that looks like this:
    # * [My post number one](http://aaburlakov.ru/blog/my-post-number-one/)
    #   <br> _This is my post number one_
    for post in recent_posts_data:
        line_template = "* {} <br>  _{}_"

        line_title = f"[{ post['title'] }]({ url_origin + post['path'] })"
        line_subtitle = post["sub_title"]
        md_line = line_template.format(line_title, line_subtitle)

        md_lines.append(md_line)

    recent_posts_md_text = "\n".join(md_lines)
    # :




    # Generating README.md based on the template.
    with open("readme_template.md", "r", encoding="utf-8") as readme_template:
        md_template = readme_template.read()
    with open("README.md", "w", encoding="utf-8") as readme:
        readme_md_text = md_template.format(
            RECENT_POSTS=recent_posts_md_text, URL_ORIGIN=url_origin
        )
        readme.write(readme_md_text)


if __name__ == "__main__":
    generate_readme()
