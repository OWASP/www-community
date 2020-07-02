# 2020-July-02: Please Re-fork and Re-clone

In order to greatly reduce the repository's size (from >5GB to ~211MB) we have had to re-write the repo's history. Please [delete your fork](https://docs.github.com/en/github/administering-a-repository/deleting-a-repository) and local clones. [Re-fork](https://docs.github.com/en/github/getting-started-with-github/fork-a-repo) and [re-clone](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository).

This was done to make the repository more manageable for those not on high speed connections:

Before:
`Receiving objects: 100% (8604/8604), 5.27 GiB | 16.23 MiB/s, done.`

After:
`Receiving objects: 100% (4672/4672), 211.77 MiB | 17.10 MiB/s, done.`

# General

[OWASP Community Pages](https://owasp.org/www-community/) are a place where OWASP can accept community contributions for security-related content. To contribute, go to the repository for this site. Go into the pages folder and create a new file. Save and commit the file.

Include the following front matter in your file (for examples, see pages/password-special-characters.md in this repository):

    ---

    layout: col-sidebar
    title: [title of page]
    author: [author name]
    contributors: [contributors]
    permalink: [direct link to page, removes /pages]
    tags: [Attacks, XSS, etc]

    ---
