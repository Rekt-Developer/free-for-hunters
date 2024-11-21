import os
import subprocess
from datetime import datetime

# Repository Info
repo_name = "free-for-hunters"
author_name = "Rekt-Developer"
telegram_channel = "https://t.me/RektDevelopers"
donation_address = "0x00fC876d03172279E04CC30E5edCE103c3d23C1A"
languages = ["English", "বাংলা (Bangla)"]

ads_scripts = [
    """<script type='text/javascript' src='//pl25013478.profitablecpmrate.com/66/17/d7/6617d7163a895c776c2db7800c9d3306.js'></script>""",
    """<script type='text/javascript' src='//pl25032294.profitablecpmrate.com/0f/9f/9c/0f9f9c5c85bb14b4da3ce62b002175ec.js'></script>""",
    """<script type='text/javascript' src='//pl25065815.profitablecpmrate.com/44/b6/6a/44b66a6e9001dbd38d6ede46d83f3a88.js'></script>"""
]

# Helper function to create a file
def create_file(file_path, content):
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

# Create folders
def create_folders():
    os.makedirs(f"{repo_name}/assets/css", exist_ok=True)
    os.makedirs(f"{repo_name}/assets/js", exist_ok=True)
    os.makedirs(f"{repo_name}/docs", exist_ok=True)

# Generate index.html
def generate_index_html():
    ads = "\n".join(ads_scripts)
    content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta property="og:title" content="Free for Hunters - Free Resources for Developers">
    <meta property="og:description" content="Discover free resources, tools, and templates for developers. Join our dev channel and support us.">
    <meta property="og:image" content="https://example.com/your-image.jpg">
    <meta property="og:url" content="https://github.com/{author_name}/{repo_name}">
    <meta name="description" content="Free resources, tools, and templates for developers and enthusiasts. Join our dev channel and contribute to our community.">
    <title>Free for Hunters</title>
    <link rel="stylesheet" href="assets/css/style.css">
    <script src="assets/js/script.js" defer></script>
</head>
<body>
    <header>
        <h1>Welcome to Free for Hunters</h1>
        <p>Discover free resources, tools, and templates for developers and enthusiasts.</p>
        <p>Languages Supported: {", ".join(languages)}</p>
        <p>Join our dev channel: <a href="{telegram_channel}" target="_blank">Rekt Developers</a></p>
        <p>Support us with donations: <code>{donation_address}</code></p>
    </header>
    <main>
        <section>
            <h2>Search for Resources</h2>
            <input type="text" id="search" placeholder="Search resources..." onkeyup="performSearch()">
            <div id="results"></div>
        </section>
        <section id="ads">
            <h2>Sponsored Ads</h2>
            {ads}
        </section>
    </main>
    <footer>
        <p>© {datetime.now().year} {author_name}. All rights reserved.</p>
    </footer>
</body>
</html>
    """
    create_file(f"{repo_name}/index.html", content)

# Generate CSS
def generate_css():
    content = """body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
    line-height: 1.6;
    background-color: #f4f4f4;
    color: #333;
}
header, footer {
    background: #333;
    color: #fff;
    text-align: center;
    padding: 20px 0;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}
h1, h2 {
    color: #fff;
}
main {
    padding: 20px;
}
input#search {
    width: 100%;
    padding: 15px;
    margin: 10px 0;
    font-size: 18px;
    border: 1px solid #ccc;
    border-radius: 5px;
}
#ads {
    margin-top: 20px;
    padding: 10px;
    background: #f9f9f9;
    border: 1px solid #ccc;
}
section {
    margin-bottom: 20px;
}
footer p {
    font-size: 14px;
}
@media screen and (max-width: 768px) {
    header, footer {
        padding: 15px 0;
    }
    input#search {
        padding: 12px;
        font-size: 16px;
    }
}
"""
    create_file(f"{repo_name}/assets/css/style.css", content)

# Generate JavaScript
def generate_js():
    content = """function performSearch() {
    const query = document.getElementById("search").value.toLowerCase();
    const results = document.getElementById("results");
    results.innerHTML = query
        ? `Searching for: <strong>${query}</strong> (feature under development)`
        : "Start typing to search for resources...";
}
"""
    create_file(f"{repo_name}/assets/js/script.js", content)

# Generate README.md
def generate_readme():
    content = f"""# {repo_name}

Free resources, tools, and templates for developers and enthusiasts.

## Features
- Multi-language support: {", ".join(languages)}
- Advanced search for resources.
- Sponsored ads integration.
- Contributions welcome!

## Dev Channel
Join our dev channel: [Rekt Developers]({telegram_channel})

## Support Us
Donate crypto: `{donation_address}`

## License
This project is licensed under the MIT License.
"""
    create_file(f"{repo_name}/README.md", content)

# Generate Docs
def generate_docs():
    content = """# Documentation

## About
This repository provides free resources for developers, including templates, tools, and tutorials.

## Structure
- `index.html`: Homepage with resource search and ads.
- `assets/css/style.css`: Styling for the website.
- `assets/js/script.js`: JavaScript functionality.

## How to Contribute
1. Fork the repository.
2. Create a new branch.
3. Submit a pull request.
"""
    create_file(f"{repo_name}/docs/documentation.md", content)

# Initialize GitHub repo and push
def initialize_repo():
    os.chdir(repo_name)
    subprocess.run(["git", "init"])
    subprocess.run(["git", "add", "."])
    subprocess.run(["git", "commit", "-m", "Initial commit"])
    subprocess.run(["git", "branch", "-M", "main"])
    subprocess.run(["git", "remote", "add", "origin", f"https://github.com/{author_name}/{repo_name}.git"])
    subprocess.run(["git", "push", "-u", "origin", "main"])

def main():
    create_folders()
    generate_index_html()
    generate_css()
    generate_js()
    generate_readme()
    generate_docs()
    initialize_repo()

if __name__ == "__main__":
    main()
