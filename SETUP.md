# Publish your GitHub profile README

1. Create a **public** repository named **midra001** under your account: `midra001/midra001`. If it already exists, open it.
2. Upload `README.md` and the entire `assets/` folder from this package to the repository root. If GitHub creates a README for you, replace it with this one.
3. Commit the files to the repository's default branch. The README uses relative paths, so it works whether the branch is called `main` or `master`.
4. Open <https://github.com/midra001>. Your profile README appears on the overview page. Switch GitHub between light and dark themes to see both versions.

## Repository layout

```text
midra001/
├── README.md
└── assets/
    ├── profile-dark.svg
    └── profile-light.svg
```

The `preview-*.png` files, `ascii.txt`, and this guide are included for convenience; you do not need to upload them.

## Design and editing

- The artwork is your supplied text, preserving every character and its spacing. It is rendered in SVG because GitHub Markdown code blocks do not support arbitrary text colors.
- ASCII color in both themes: **#FC9A1F**, equivalent to **RGB(252, 154, 31)**. Supporting text has a darker orange accent in light mode for readability.
- Both images are self-contained SVGs with no scripts, remote fonts, trackers, or external image services. No tokens or automated update tasks are required.
- The name and bio are based on your public profile. Technologies and areas of interest are supplied by you; no proficiency levels are assigned.
- To change profile text, edit the corresponding `<text>` elements in **both** SVGs. Keep lines short enough to fit the right-hand column.
- The entire design scales down with GitHub's content width. The art and profile are intentionally side by side like the reference, so phone users may need to zoom to read small text.
- Layout inspiration: <https://github.com/Andrew6rant/Andrew6rant>. Your supplied README points to that profile. This package uses new SVGs rather than linking to Andrew's images or name.
