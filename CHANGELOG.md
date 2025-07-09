## [v1.2.3] - 2025-07-09


- name: Update CHANGELOG.md
  run: |
    DATE=$(date +'%Y-%m-%d')
    echo -e "## [${{ env.NEW_TAG }}] - $DATE\n${{ env.CHANGELOG }}\n" | cat - CHANGELOG.md > temp && mv temp CHANGELOG.md

    git config user.name "github-actions"
    git config user.email "github-actions@github.com"
    git add CHANGELOG.md
    git commit -m "docs: update changelog for ${{ env.NEW_TAG }}"
    git push origin master
