*This project has been created as part of the 42 curriculum by ayanaga, tmaeda.*

# A-Maze-ing

## Description（概要）

A-Maze-ing は、設定ファイルに基づいて迷路を生成し、指定形式で出力・表示する Python プロジェクトです。

【要記載：完成した実装の概要】

## Instructions（実行方法）

### Requirements

【要記載：実行に必要な環境・依存関係】

### Install

```bash
make install
```

### Run

```bash
python3 a_maze_ing.py config.txt
```

または、

```bash
make run
```

### Debug

```bash
make debug
```

### Lint

```bash
make lint
```

### Clean

```bash
make clean
```

## Configuration（設定ファイル）

設定ファイルは、1行につき1つの `KEY=VALUE` 形式で記述します。

`#` で始まる行はコメントとして無視します。

### Required keys

- `WIDTH`
- `HEIGHT`
- `ENTRY`
- `EXIT`
- `OUTPUT_FILE`
- `PERFECT`

【要記載：各キーの意味、形式、入力例】

### Optional keys

【要記載：実装した追加キー、default value、設定例】

## Maze Generation（迷路生成）

【要記載：採用した maze generation algorithm、その概要、選定理由】

### PERFECT=True

【要記載：perfect maze をどのように生成・保証したか】

### PERFECT=False

【要記載：Pac-Man-like board の要件をどのように生成・保証したか】

## The `42` Pattern（42パターン）

【要記載：採用した `42` パターン、配置方法、配置できない場合の扱い】

## Shortest Path（最短経路）

【要記載：ENTRY から EXIT までの shortest valid path の算出方法】

## Output Format（出力形式）

【要記載：hexadecimal wall representation、ENTRY、EXIT、shortest path の出力例】

## Visual Representation（表示）

【要記載：採用した表示方式、操作方法、path 表示切替、再生成、wall colour 変更】

## Reusable Module（再利用可能部分）

【要記載：再利用可能な maze generator の class、public API、package 名、利用例】

## Team and Project Management（チーム・プロジェクト管理）

### Team members

| Login | 主な担当 |
| --- | --- |
| `ayanaga` | 【要記載】 |
| `tmaeda` | 【要記載】 |

### Planning and evolution

【要記載：当初計画と、実際の進行に伴う変更】

### What worked well

【要記載：振り返り】

### What could be improved

【要記載：振り返り】

### Tools used

【要記載：実際に使用したツール】

## Resources（参考資料）

【要記載：実際に参照した documentation、article、tutorial 等】

## Use of AI（AIの利用）

【要記載：AIを使用したタスク、対象箇所、確認方法】

## Bonus Features（ボーナス）

【実装した場合のみ記載。未実装の場合は削除】

## License（ライセンス）

maze generator は MIT License の下で再利用・再配布できます。

詳細は `LICENSE.md` を参照してください。
