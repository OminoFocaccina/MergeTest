# MergeTest
Hi, here you fill a small test to understand how merge and rebase work.

You will find 9 branches:
- `main`
- `main_easymerge`
- `feature_easymerge`
- `main_noreabasemerge`
- `feature_norebasemerge`
- `main_reabasemerge`
- `feature_rebasemerge`
- `main_conflictmerge`
- `feature_conflictmerge`
You can:
## easymerge
Merge `main_easymerge` and `feature_easymerge`, to see how a merge without rebase and without any new commit in the main (in this case `main_easymerge`) is.
```bash
git checkout main_easymerge
git merge feature_easymerge
```

## noreabasemerge
Merge `main_noreabasemerge` and `feature_norebasemerge`, to see how a merge without rebase and with a new commit in the main (in this case `main_noreabasemerge`) is.

```bash
git checkout main_noreabasemerge
git merge feature_norebasemerge
```

## reabasemerge
From `main_reabasemerge`:
```bash
git checkout feature_rebasemerge
git rebase main_reabasemerge
git checkout main_reabasemerge
git merge feature_rebasemerge
```
## conflictmerge
```bash
git checkout feature_conflictmerge
git rebase main_conflictmerge
git checkout --ours .
git add game.py
git rebase --continue
git checkout main_conflictmerge
git merge feature_conflictmerge
```

With `--ours` you go in target branch (`main_conflictmerge`), with `--theirs` the other (`feature_conflictmerge`).


