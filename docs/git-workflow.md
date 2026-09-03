# Git Workflow

この文書は、A-Maze-ing における Git の基本運用を定める内部文書です。  
42 の Git Workflow Guidelines を基準とし、共同開発時の履歴を分かりやすく保つことを目的とします。

## 1. 基本方針

- `main` は常に安定した状態を維持する
- 新機能、修正、大きな変更は `main` 上で直接作業しない
- 作業単位ごとに専用ブランチを作成する
- コミットメッセージは Conventional Commits に従う
- 1コミットには1つの機能、修正、または論理的変更だけを含める
- 関係のない変更を同じブランチやコミットに混在させない
- `main` への統合は Pull Request を経由する
- コミットの squash は行わない
- 作業ブランチから `main` への統合は merge commit を使用する
- `main` の変更を作業ブランチへ取り込む場合は rebase または fast-forward を使用する

## 2. ブランチ

### 2.1 ブランチの作成

作業開始前に `main` を最新化し、そこから作業ブランチを作成します。

```bash
git switch main
git pull --ff-only
git switch -c <type>/<name>
```

### 2.2 ブランチ名

ブランチ名は変更内容が分かる英語名とします。

例：

```text
feat/maze-generation
feat/config-parser
fix/config-validation
docs/design
refactor/maze-generator
```

主な接頭辞：

| 種別 | 用途 |
|---|---|
| `feat/` | 新機能 |
| `fix/` | 不具合修正 |
| `docs/` | 文書変更 |
| `refactor/` | 動作を変えないコード整理 |
| `test/` | テスト追加・修正 |
| `chore/` | その他の保守作業 |

## 3. コミット

### 3.1 基本形式

コミットメッセージは Conventional Commits の形式を使用します。

```text
<type>(<scope>): <description>
```

`scope` は変更対象が明確になる場合に使用します。

例：

```text
feat(maze): add maze generation
fix(config): reject invalid dimensions
docs(design): update maze design notes
refactor(maze): simplify generation logic
test(maze): add generation tests
```

### 3.2 コミットの単位

1コミットには、1つの機能、修正、または論理的変更だけを含めます。

良い例：

```text
docs(design): move design notes to docs directory
docs(workflow): add Git workflow guidelines
```

避ける例：

```text
feat: add parser, fix maze generation, update README
```

複数の目的が含まれる場合は、コミットを分けます。

### 3.3 description の書き方

description は短い英語で、変更内容を直接表します。

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
refactor
```

例：

```text
feat(config): add config parser
fix(config): handle invalid width
docs(design): move design notes
```

### 3.4 コミットテンプレート

基本形：

```text
<type>(<scope>): <verb> <target>
```

例：

```text
feat(maze): add maze generator
fix(config): handle missing value
docs(workflow): update branch rules
```

`scope` が不要な場合：

```text
<type>: <verb> <target>
```

例：

```text
chore: update build configuration
```

## 4. 基本的な作業手順

### 4.1 作業開始

```bash
git switch main
git pull --ff-only
git switch -c feat/example
```

### 4.2 変更確認

```bash
git status
git diff
```

### 4.3 コミット

```bash
git add <file>
git commit -m "feat(example): add example feature"
```

複数の変更がある場合は、論理単位ごとに `git add` と `git commit` を繰り返します。

### 4.4 Push

```bash
git push -u origin feat/example
```

### 4.5 Pull Request

GitHub 上で Pull Request を作成し、変更内容を確認します。

GitHub CLI を使用する場合：

```bash
gh pr create
```

### 4.6 `main` への統合

作業ブランチから `main` への統合では merge commit を使用します。

squash merge は使用しません。

## 5. 作業中に `main` が更新された場合

作業ブランチへ `main` の変更を取り込む場合は、merge commit を作成せず rebase を使用します。

```bash
git switch main
git pull --ff-only

git switch <branch>
git rebase main
```

競合が発生した場合は、競合を解消してから次を実行します。

```bash
git add <resolved-file>
git rebase --continue
```

## 6. コミット履歴の確認

```bash
git log --graph --decorate --oneline --all
```

コミット内容を確認する場合：

```bash
git show <commit>
```

コミット前には、少なくとも次を確認します。

```bash
git status
git diff --staged
```

## 7. 運用上の注意

- `main` に直接機能追加を行わない
- unrelated な変更を同一コミットへ含めない
- 作業途中のコミットを理由なく squash しない
- 作業ブランチへ `main` を merge しない
- force push は、履歴修正が必要な場合を除き原則使用しない
- 不明な場合は、変更を小さく分ける
