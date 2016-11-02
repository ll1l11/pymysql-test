#!/usr/bin/env bash
sync_tags() {
    git tag | xargs git tag -d
    git fetch $1 -p
}

# git只保留最新的N个tag
N=15
git push --tags
sync_tags origin
tags_count=$(git tag | wc -l | awk '{print $1}')
# tags按照时间排序： http://stackoverflow.com/questions/6269927/how-can-i-list-all-tags-in-my-git-repository-by-the-date-they-were-created
if [ $tags_count -gt $N ]; then
    git for-each-ref --sort=taggerdate --format '%(refname:short)' refs/tags | awk -v n=$N '{l[NR]=$0} END {for (i=1; i<=NR-n; i++) print l[i]}' | xargs -n 1 git push origin --delete
    sync_tags origin
else
    echo "only $tags_count tags"
fi
