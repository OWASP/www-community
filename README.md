# OWASP Community Pages

![GitHub repo size](https://img.shields.io/github/repo-size/OWASP/www-community)

OWASP Community Pages is a repository for community contributions for security-related content. The documents here create the website at https://owasp.org/www-community/.

## Contributing

We welcome contributions for new content and updates to current pages. This repository uses a [fork and pull model](https://docs.github.com/en/github/collaborating-with-pull-requests/getting-started/about-collaborative-development-models#fork-and-pull-model). Here are the steps for becoming a contributor:

1. [Fork](https://docs.github.com/en/github/getting-started-with-github/fork-a-repo) this repository and [clone](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository-from-github/cloning-a-repository) your fork.
2. In the `pages/` directory, make your changes or additions. For creating new content, please see below.
3. Push your changes to your fork, then open a pull request against this repository.

If you are making changes that address an [existing issue](https://github.com/OWASP/www-community/issues), please make a comment in the issue so we can assign it to you. This helps to prevent accidentally doubling up on work.

### Creating New Content

Go into the `pages` folder and create a new file.

Place the following front matter and `include` tag at the beginning of your file. Feel free to copy and edit this example:

```md
---

layout: col-sidebar
title: "My Page"
author: "My Name"
contributors: ["Additional Contributor Names", "If Any"]
permalink: /MyPageTitle
tags: ["attack", "XSS"]

---

{% include writers.html %}

Write your content here!

```

The fields `contributors`, `permalink`, and `tags` are optional. When in doubt, it's okay to leave them blank.

### Rules for Contributors

1. Your contribution must be your own original work. You may not submit copyrighted content you do not own. Please do not plagiarize.
2. Please ensure that contributions are vendor and product neutral.

### Note for Returning Contributors

In July of 2020, the repository's git history was rewritten to reduce its size (over 5GB!). If you forked before this date, please [delete your fork](https://docs.github.com/en/github/administering-a-repository/deleting-a-repository) and local clones, then [re-fork](https://docs.github.com/en/github/getting-started-with-github/fork-a-repo) or [re-clone](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository) this repository.