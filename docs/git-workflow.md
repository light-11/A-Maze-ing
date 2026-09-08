# Git Workflow

A-Maze-ing の共同開発で使う Git の基本ルールです。

42 の Git Workflow Guidelines を基準にしています。

## 1. 今回やってみること

- `main` で直接開発しない
- 作業ごとにブランチを作る
- 1コミットには1つの目的・論理的変更だけを入れる
- コミットメッセージは Conventional Commits を使う
- `main` への統合は Pull Request 経由
- squash merge は使わない
- 作業ブランチ → `main` は merge commit
- `main` → 作業ブランチは rebase

## 2. 新しく作業を始めるときの一連の流れ

### ① `main` を最新にする

```bash
git switch main
git pull --ff-only
```

### ② 作業ブランチを作る

例：新機能を作る場合

```bash
git switch -c feat/maze-generation
```

### ③ 作業する

変更内容を確認します。

```bash
git status
git diff
```

### ④ コミットする

```bash
git add <file>
git commit -m "feat(maze): add maze generator"
```

### ⑤ push する

初回：

```bash
git push -u origin feat/maze-generation
```

### ⑥ Pull Request を作る

```bash
gh pr create
```

内容を相互確認した後、merge commit で `main` に統合します。

---

## 3. ブランチ名の決め方

基本形：

```text
<type>/<name>
```

例：

```text
feat/maze-generation
fix/config-validation
docs/design
```

主な `type`：

| type | 用途 |
|---|---|
| `feat` | 新機能 |
| `fix` | 不具合修正 |
| `docs` | 文書変更 |
| `refactor` | 動作を変えない整理 |
| `test` | テスト |
| `chore` | その他の保守作業 |

---

## 4. コミットメッセージの書き方

基本形：

```text
<type>(<scope>): <description>
```

例：

```text
feat(maze): add maze generator
fix(config): handle invalid width
docs(design): update maze notes
```

`scope` が不要なら省略できます。

```text
chore: update build configuration
```

### 書き方の参考

description は短い英語にします。

よく使う動詞：

```text
add
update
remove
move
rename
implement
fix
handle
simplify
```

テンプレート：

```text
<type>(<scope>): <verb> <target>
```

---

## 5. コミットの分け方

1コミットには1つの目的・論理的変更だけを入れます。

良い例：

```text
docs(design): move design notes to docs directory
docs(workflow): add Git workflow guidelines
```

避ける例：

```text
feat: add parser, fix maze generation, update README
```

迷った場合は、小さく分けます。

---

## 6. 作業中に `main` が更新された場合に取り込む方法

```bash
git switch main
git pull --ff-only

git switch <branch>
git rebase main
```

競合を解消した後：

```bash
git add <resolved-file>
git rebase --continue
```

`main` を作業ブランチへ merge する方法は使いません。

---

## 7. その他の確認コマンド

現在の状態：

```bash
git status
```

変更内容：

```bash
git diff
```

コミット予定の内容：

```bash
git diff --staged
```

履歴：

```bash
git log --graph --decorate --oneline --all
```
