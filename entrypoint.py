import os


os.system("cp -r . /data")
os.chdir("/data")


def replace_special_chararacters(content):
    content = content.replace("%", "%25")
    content = content.replace("\n", "%0A")
    content = content.replace("\r", "%0D")
    return content


if os.environ.get("INPUT_UPLOAD_METHOD") == "sarif":
    print("printing in Sarif")
    toml = open("./.ezerc.toml", "a")
    toml.write(
        """
    [sarif.github]
    REPORT_FILE = \"reports/eze.sarif\"

    [scan.github]
    reporters = [\"sarif:github\"]
    """
    )
    toml.close()
    os.system("eze test -s github")
    markdown = file_object = open("reports/eze.sarif", "r")
    content = replace_special_chararacters("".join(markdown.readlines()))
    markdown.close()
    print(f"::set-output name=sarif_file::{content}")
else:
    print("printing in MARKDOWN")
    toml = open("./.ezerc.toml", "a")
    toml.write(
        """
    [markdown.github]
    REPORT_FILE = \"reports/eze.md\"

    [scan.github]
    reporters = [\"markdown:github\"]
    """
    )
    toml.close()
    os.system("eze test -s github")
    markdown = file_object = open("reports/eze.md", "r")
    content = replace_special_chararacters("".join(markdown.readlines()))
    print(f"::set-output name=markdown_file::{content}")
