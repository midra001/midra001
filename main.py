from datetime import datetime

import os
import json
import random
from pathlib import Path
from types import SimpleNamespace
from PIL import Image, ImageDraw, ImageFont

os.chdir(Path(__file__).resolve().parent)
os.environ.setdefault("GIFOS_GENERAL_FPS", "13")
os.environ.setdefault("GIFOS_GENERAL_LOOP_COUNT", "0")
os.environ.setdefault("GIFOS_GENERAL_COLOR_SCHEME", "everblush")
os.environ.setdefault("GIFOS_GENERAL_USER_NAME", "midra001")
import gifos
from zoneinfo import ZoneInfo

FONT_FILE_LOGO = "./fonts/DejaVuSansMono.ttf"
FONT_FILE_BITMAP = "./fonts/gohufont-uni-14.pil"


def boot_banner_frame(glitch=0.0, seed=0):
    """Render ANSI-shadow block art with a red-to-yellow row gradient."""
    lines = Path("banner.txt").read_text(encoding="utf-8").splitlines()
    frame = Image.new("RGB", (750, 500), "#141b1e")
    draw = ImageDraw.Draw(frame)
    face = ImageFont.truetype(FONT_FILE_LOGO, 18)
    size = 18
    while max(map(len, lines))*face.getlength("█") > 690 and size > 8:
        size -= 1
        face = ImageFont.truetype(FONT_FILE_LOGO, size)
    cell = face.getlength("█")
    line_height = round(size*4/3)
    x_origin = (750-max(map(len, lines))*cell)/2
    y_origin = (500-len(lines)*line_height)/2
    rng = random.Random(seed)
    for row, line in enumerate(lines):
        color = (255, round(255*row/max(1, len(lines)-1)), 0)
        shift = rng.choice([-3, 0, 3]) if glitch else 0
        for col, char in enumerate(line):
            if char == " ":
                continue
            if glitch and rng.random() < glitch:
                char = rng.choice("█▓▒░╬╳")
            draw.text((x_origin+col*cell+shift, y_origin+row*line_height), char, fill=color, font=face)
    return frame


def main():
    t = gifos.Terminal(750, 500, 15, 15, FONT_FILE_BITMAP, 15)
    t.set_prompt("\x1b[0;91mmidra001\x1b[0m@\x1b[0;93mXypherOS ~> \x1b[0m")

    t.gen_text("", 1, count=20)
    t.toggle_show_cursor(False)
    year_now = datetime.now(ZoneInfo("Asia/Kolkata")).strftime("%Y")
    t.gen_text("XypherOS Modular BIOS v1.0.11", 1)
    t.gen_text(f"Copyright (C) {year_now}, \x1b[31mmidra001\x1b[0m", 2)
    t.gen_text("\x1b[94mGitHub Profile ReadMe Terminal, Rev 1011\x1b[0m", 4)
    t.gen_text("Xypher(tm) CPU - 250Hz", 6)
    t.gen_text(
        "Press \x1b[94mDEL\x1b[0m to enter SETUP, \x1b[94mESC\x1b[0m to cancel Memory Test",
        t.num_rows,
    )
    for i in range(0, 65653, 7168): 
        t.delete_row(7)
        if i < 30000:
            t.gen_text(
                f"Memory Test: {i}", 7, count=2, contin=True
            )
        else:
            t.gen_text(f"Memory Test: {i}", 7, contin=True)
    t.delete_row(7)
    t.gen_text("Memory Test: 64KB OK", 7, count=10, contin=True)
    t.gen_text("", 11, count=10, contin=True)

    t.clear_frame()
    t.gen_text("Initiating Boot Sequence ", 1, contin=True)
    t.gen_typing_text(".....", 1, contin=True)
    t.toggle_show_cursor(False)
    for i in range(10):
        t._Terminal__frame = boot_banner_frame(glitch=0.55*(1-i/9), seed=i)
        t.clone_frame(2)
    t._Terminal__frame = boot_banner_frame()
    t.save_frame("banner-preview.png")
    t.clone_frame(24)

    t.set_font(FONT_FILE_BITMAP, 15)
    t.clear_frame()
    t.clone_frame(5)
    t.toggle_show_cursor(False)
    t.gen_text("\x1b[93mXypherOS v1.0.11 (tty1)\x1b[0m", 1, count=5)
    t.gen_text("login: ", 3, count=5)
    t.toggle_show_cursor(True)
    t.gen_typing_text("midra001", 3, contin=True)
    t.gen_text("", 4, count=5)
    t.toggle_show_cursor(False)
    t.gen_text("password: ", 4, count=5)
    t.toggle_show_cursor(True)
    t.gen_typing_text("*********", 4, contin=True)
    t.toggle_show_cursor(False)
    time_now = datetime.now(ZoneInfo("Etc/GMT-1")).strftime(
        "%a %b %d %I:%M:%S %p %Z %Y"
    )
    t.gen_text(f"Last login: {time_now} on tty1", 6)

    t.gen_prompt(7, count=5)
    prompt_col = t.curr_col
    t.toggle_show_cursor(True)
    t.gen_typing_text("\x1b[91mclea", 7, contin=True)
    t.delete_row(7, prompt_col)
    t.gen_text("\x1b[92mclear\x1b[0m", 7, count=3, contin=True)
    git_user_details = SimpleNamespace(
        languages_sorted=[], user_rank=SimpleNamespace(level="--"),
        total_stargazers="--", total_commits_last_year="--",
        total_pull_requests_made="--", pull_requests_merge_percentage="--",
        total_repo_contributions="--",
    )
    if os.environ.get("GITHUB_TOKEN") and not os.environ.get("PROFILE_OFFLINE"):
        try:
            git_user_details = gifos.utils.fetch_github_stats("midra001", [])
        except Exception as error:
            print(f"Stats unavailable; retaining --: {error}")
    personal = json.loads(Path("profile.json").read_text())
    t.clear_frame()
    top_languages = [lang[0] for lang in git_user_details.languages_sorted]
    t.gen_prompt(1)
    prompt_col = t.curr_col
    t.clone_frame(10)
    t.toggle_show_cursor(True)
    t.gen_typing_text("\x1b[91mfetch.s", 1, contin=True)
    t.delete_row(1, prompt_col)
    t.gen_text("\x1b[92mfetch.sh\x1b[0m", 1, contin=True)
    t.gen_typing_text(" -u midra001", 1, contin=True)

    t.toggle_show_cursor(False)
    lines = Path("ascii.txt").read_text().splitlines()
    art_font = ImageFont.truetype("./fonts/DejaVuSansMono.ttf", 18)
    cell, line_height = 11, 20
    art = Image.new("RGB", (max(map(len, lines))*cell, len(lines)*line_height), "#141b1e")
    draw = ImageDraw.Draw(art)
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char != " ":
                draw.text((x*cell, y*line_height), char, font=art_font, fill="#b3b9b8")
    art = art.resize((260, 335), Image.Resampling.LANCZOS)
    art.save("ascii-render.png")
    t.paste_image("ascii-render.png", 6, 1)

    t.set_font(FONT_FILE_BITMAP)
    t.toggle_show_cursor(True)
    panel = t._Terminal__frame
    draw = ImageDraw.Draw(panel)
    bitmap = ImageFont.load(FONT_FILE_BITMAP)
    x = 319
    draw.rectangle((x, 51, x+120, 65), fill="#ef7e7e")
    draw.text((x, 51), "midra001@GitHub", font=bitmap, fill="#232a2d")
    draw.text((x, 69), "--------------", font=bitmap, fill="#dadada")
    def field(y, label, value, offset=64):
        draw.text((x, y), label, font=bitmap, fill="#67cbe7")
        draw.text((x+offset, y), str(value), font=bitmap, fill="#f4d67a")
    for y, label, key in [(87,"OS:","os"), (105,"Host:","host"), (123,"Kernel:","kernel"), (141,"Uptime:","uptime"), (159,"IDE:","ide")]:
        field(y, label, personal[key])
    for y, label in [(213,"GitHub Stats:")]:
        draw.rectangle((x,y,x+len(label)*8,y+14), fill="#ef7e7e")
        draw.text((x,y), label, font=bitmap, fill="#232a2d")
        draw.text((x,y+18), "--------------", font=bitmap, fill="#dadada")
    rows = [
        ("Total Stars Earned:", git_user_details.total_stargazers),
        (f"Total Commits ({int(year_now)-1}):", git_user_details.total_commits_last_year),
        ("Total PRs:", git_user_details.total_pull_requests_made),
        ("Merged PR %:", git_user_details.pull_requests_merge_percentage),
        ("Total Contributions:", git_user_details.total_repo_contributions),
        ("Top Languages:", ', '.join(top_languages[:5]) or '--'),
    ]
    for i, (label, value) in enumerate(rows):
        field(249+i*18, label, value, (len(label)+1)*8)
    t.clone_frame(5)
    t.gen_prompt(26)
    t.gen_typing_text(
        "\x1b[92m# Session complete. Build something worth running.",
        t.curr_row,
        contin=True,
    )
    t.gen_text("", t.curr_row, count=3900, contin=True)

    t.save_frame("preview.png")
    t.gen_gif()
    readme_file_content = '<div align="justify">\n<picture>\n  <source media="(prefers-color-scheme: dark)" srcset="./output.gif">\n  <source media="(prefers-color-scheme: light)" srcset="./output.gif">\n  <img alt="XypherOS terminal profile for midra001" src="./output.gif" width="100%">\n</picture>\n</div>\n\n<hr>\n\n<h3 align="center">📊 My GitHub Activity</h3>\n<a href="https://github.com/midra001?tab=overview">\n  <img src="./profile-3d-contrib/profile-night-view.svg" alt="3D contribution calendar, activity radar, and repository language breakdown for midra001; refreshed daily by GitHub Actions" width="100%">\n</a>\n\n<sub><i>Terminal generated using [x0rzavi/github-readme-terminal](https://github.com/x0rzavi/github-readme-terminal).</i></sub>\n'
    Path("README.md").write_text(readme_file_content, encoding="utf-8")
    print("INFO: README.md file generated")


if __name__ == "__main__":
    main()
