``` shell
# 删除本地tag
git tag -d V01.00.00
# 删除remote tag
git push origin --delete V01.00.00
# 重新打标签
git tag V01.00.00
# 将本地标签推送到remote
git push origin --tags

```