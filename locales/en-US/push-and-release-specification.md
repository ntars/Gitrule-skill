# Push and Release Specification

> What this file solves: Defines the action checklist before, during, and after push, tag and release rules, incident handling procedures, as well as the complete GitHub push guide and failure handling matrix.

## 1. Before Push

1. `git status` is clean, with no untracked sensitive files.
2. `git log` contains no WIP, no `fix bug`, and no personal information leaks.
3. Confirm that `.gitignore` is effective and that artifacts and dependencies are not tracked.
4. Run build + test + lint successfully locally.
5. Run a key scan once (including history).
6. The document matrix is complete (see [Document Matrix](./document-matrix.md)).

## 2. Push Actions

7. Push a personal branch: `git push -u origin feat/xxx`.
8. The main branch goes through PR only; do not push directly.
9. `push --force` is prohibited; use `--force-with-lease` to rewrite your own branch.
10. Rebase/amend on already-pushed public branches is prohibited.
11. For a single file >50MB, use LFS before pushing.
12. Before the first push, confirm repository visibility: private by default; switch to public only if truly needed.

## 3. Tag and Release

13. Tag format `vMAJOR.MINOR.PATCH`, must be annotated: `git tag -a v1.0.0 -m "release: 1.0.0"`.
14. Tag only after CI is green and Release Notes are ready.
15. Breaking changes must use `feat!:` or `BREAKING CHANGE:`, and a migration method must be given in the CHANGELOG.

## 4. Phase 6 · Post-Push

- Create an annotated tag;
- Write Release Notes;
- Verify badges and links work;
- Confirm CI is green;
- Confirm the About section is correct (description / topics / links / social preview).

## 5. Incident Handling

16. **Key already pushed**: Immediately rotate → clean with `git filter-repo` → force-pushing a protected branch requires the administrator process → announce.
17. **Large file pushed by mistake**: Migrate to LFS or rewrite history; deleting the file only is not sufficient.

## 6. GitHub Push Guide Specification

The guide must contain the following seven parts, with commands given in complete executable form.

### 6.1 Pre-push Security

1. Before pushing, fully back up the local repository and the remote repository; `git clone --mirror` is recommended for a mirror backup.
2. Confirm the remote repository has no collaborators, or that collaborators have been notified to pause pushing.
3. Confirm that force-push protection is not enabled on the target branch.

### 6.2 Local Cleanup

```bash
git status
git diff --name-status HEAD
git ls-files
```

Check the three outputs, confirm that pending changes are consistent with the local directory, and that there are no temporary files, build artifacts, or leftover old documents. `.gitignore` must cover build artifacts and local configuration files.

### 6.3 Consistency Check

```bash
git fetch origin
git diff --name-status HEAD origin/{{分支名}}
```

This command lists the file differences between remote and local. For files that exist on the remote but have been deleted locally, execute `git rm` locally and commit so that the deletion enters version history.

### 6.4 Commit and Push

```bash
git add -A
git commit -m "docs: 重建项目文档（README、README_EN、NOTICE）"
git push --force-with-lease origin {{分支名}}
```

Use `--force-with-lease` instead of `--force`; it rejects the push when others have new commits on the remote, avoiding overwriting others' work. Deleting the remote repository and recreating it is a high-risk operation, used only for personal repositories with a completed mirror backup; the guide must explicitly mark the data loss risk.

### 6.5 Post-push Verification

```bash
git ls-remote --heads origin
gh repo view --web
```

On the web page, confirm item by item that the file list, README rendering, language switch links, and NOTICE link are valid.

### 6.6 Failure Handling Matrix

| Error Type | Typical Symptom | Handling Plan | Risk Warning |
| --- | --- | --- | --- |
| Authentication failure | `Authentication failed`, `Permission denied (publickey)` | Switch from HTTPS to SSH and configure the key, or push after `gh auth login` | None |
| Network interruption | `Failed to connect`, `RPC failed` | Change network, configure proxy, run `git config --global http.postBuffer 524288000` | None |
| File size limit | `remote: error: File exceeds 100 MB` | Remove the large file from commit history or enable Git LFS | After rewriting history, collaborators must be notified to re-clone |
| Case conflict | Duplicate entries caused by inconsistent filename case | Fix with `git mv` and commit | None |
| History conflict | `non-fast-forward`, `fetch first` | Prefer `git pull --rebase`; use `--force-with-lease` if overwrite is truly needed | Overwriting others' commits is unrecoverable |
| Branch protection | `protected branch hook declined` | Merge through the PR process, or have an administrator temporarily adjust the rules | Rule adjustments must be recorded |
| Repository corruption | `fatal: not a git repository`, missing objects | Re-clone and copy the workspace changes | The workspace must be backed up first |

### 6.7 Rollback

After push is complete, if problems are found, use `git revert` to generate a reverse commit; do not force-push again to overwrite published history.

## Related Files

- Before pushing, must pass the three gates of [Quality Gates](./quality-gate.md)
- Key and large file red lines are H3/H5/H12 in [Hard Rules](./hard-rules.md)
- The commit message specification belongs to dimension D7, see [Audit Dimension Matrix](./review-dimension-matrix.md)
- The release document `docs/release.md` responsibilities are in [Document Matrix](./document-matrix.md)
