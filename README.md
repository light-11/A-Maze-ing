*This project has been created as part of the 42 curriculum by ayanaga, tmaeda.*

# A-Maze-ing

## Description

A-Maze-ingは、設定ファイルに基づいて迷路を生成し、16進数形式での出力とターミナル表示を行うPythonプロジェクトです。

深さ優先探索（DFS）による迷路生成と、幅優先探索（BFS）による最短経路探索を実装しています。

## Instructions

Python 3.10以降が必要です。

```bash
make install                          # 依存関係のインストール
python3 a_maze_ing.py config.txt      # 実行
make run                              # デフォルト設定で実行
make debug                            # デバッグ実行
make lint                             # flake8 / mypy
make clean                            # キャッシュ等の削除
```

## Configuration

設定ファイルは1行につき1つの`KEY=VALUE`形式で記述します。
`#`で始まる行はコメントとして無視されます。

| Key | Description | Example |
|---|---|---|
| WIDTH | 迷路の幅 | `WIDTH=20` |
| HEIGHT | 迷路の高さ | `HEIGHT=15` |
| ENTRY | 入口座標 (x,y) | `ENTRY=0,0` |
| EXIT | 出口座標 (x,y) | `EXIT=19,14` |
| OUTPUT_FILE | 出力ファイル | `OUTPUT_FILE=maze.txt` |
| PERFECT | 完全迷路の生成 | `PERFECT=True` |
| SEED | 乱数シード（任意） | `SEED=42` |

【要確認：追加キーのデフォルト値・不正入力の扱い】

## Maze Generation

### Algorithm

深さ優先探索（DFS）によるRecursive Backtrackingを採用しています。

未訪問の隣接セルをランダムに選び、壁を開放して探索します。
行き止まりではスタックを使って戻ります。

単純な構造で、ループのない完全迷路を生成できることが採用理由です。

- **PERFECT=True**：42ロゴを除くセルをDFSで接続し、ループのない完全迷路を生成
- **PERFECT=False**：【NON-PERFECT実装後に記載】

### 42 Pattern

7×5セルの42パターンを使用しています。

```text
#...###
#.....#
###.###
..#.#..
..#.###
```

パターンを構成するセルは4方向を閉鎖し、迷路中央に配置します。

配置できないサイズではメッセージを表示してロゴを省略します。
ENTRY / EXITとロゴの重複時はエラー終了します。

### Shortest Path

幅優先探索（BFS）で最短経路を探索します。

探索時に親セルと移動方向を記録し、EXITからENTRYへ逆順にたどって経路を復元します。

## Output Format

各セルの壁を1桁の16進数で表現します。

| Direction | Bit | Value |
|---|---|---|
| North | 0 | 1 |
| East | 1 | 2 |
| South | 2 | 4 |
| West | 3 | 8 |

壁が閉じている場合は対応するビットを1にします。

迷路データを行単位で出力し、空行の後にENTRY、EXIT、最短経路（N/E/S/W）を記録します。

### 出力例
```text
B95551553953
AE9396B96C7A
A96AA96C5552
C6FC6AFFF93A
97FD5057FAEA
C3FFFAFFFA96
9453FAFD506B
A93EFAFFFA96
86C394395683
C396ABC6D3AA
96A968553C6A
C7C456D54556

0,0
11,11
SSSENENESSENNENEEESWSEEEESSSWSWSSWWSWNWWSSWSEENEEESEEE

```

## Visual Representation

ターミナル上で迷路、入口、出口、最短経路を表示します。

操作：
- 迷路の再生成
- 最短経路の表示／非表示
- 壁の色変更
- 終了

## Reusable Module

【要記載：mazegenの公開API、インストール方法、使用例】

## Team and Project Management

### Team Members

| Login | Main Responsibilities |
|---|---|
| `ayanaga` | 迷路生成、seed対応、NON-PERFECT生成 |
| `tmaeda` | アプリケーション構成、Solver、Writer、Visualizer、42ロゴ |

### Planning and Evolution

当初は機能単位で分担し、並行して開発しました。

開発途中で、Config等の論理座標(x, y)と内部グリッドの配列順序が異なることによる混乱が生じたため、`grid[x][y]`に統一しました。

また、GeneratorのConfig等への依存を解消し、再利用可能な構造とするため、関連モジュールを`mazegen/`に集約しました。

### Retrospective

**What worked well**

【要記載】

**What could be improved**

【要記載】

**Tools used**

【要記載】

## Resources and AI Usage

### Resources

【要記載：実際に参照した資料・ドキュメント】

### AI Usage

【要記載：AIを利用した作業、対象コード、検証方法】

## License

迷路生成器はMIT Licenseの下で再利用・再配布できます。
詳細は`LICENSE.md`を参照してください。
