*This project has been created as part of the 42 curriculum by ayanaga, tmaeda.*

# A-Maze-ing

## Description

A-Maze-ingは、設定ファイルに基づいて迷路を生成し、16進数形式での出力とターミナル表示を行うPythonプロジェクト

深さ優先探索（DFS）による迷路生成と、幅優先探索（BFS）による最短経路探索を実装

## Instructions

Python 3.10以降が必要

### Setup and Run

```
make install                          # 開発ツールのインストール
python3 a_maze_ing.py config.txt      # 実行
make run                              # デフォルト設定で実行
```

### Development

```
make debug                            # デバッグ実行
make lint                             # flake8 / mypy
make clean                            # キャッシュ等の削除
```

## Configuration

設定ファイルは1行につき1つの`KEY=VALUE`形式で記述
`#`で始まる行はコメントとして無視

| Key | Description | Example |
|---|---|---|
| WIDTH | 迷路の幅 | `WIDTH=20` |
| HEIGHT | 迷路の高さ | `HEIGHT=15` |
| ENTRY | 入口座標 (x,y) | `ENTRY=0,0` |
| EXIT | 出口座標 (x,y) | `EXIT=19,14` |
| OUTPUT_FILE | 出力ファイル | `OUTPUT_FILE=maze.txt` |
| PERFECT | 完全迷路の生成 | `PERFECT=True` |
| SEED | 乱数シード（任意） | `SEED=42` |

SEED省略時はランダム生成

## Maze Generation

### Algorithm

深さ優先探索（DFS）によるRecursive Backtrackingを採用

未訪問の隣接セルをランダムに選び、壁を開放して探索
行き止まりではスタックにより戻り探索を再開

単純な構造で、ループのない完全迷路を生成できることが採用理由

- **PERFECT=True**：42ロゴを除くセルをDFSで接続し、ループのない完全迷路を生成
- **PERFECT=False**：PERFECT迷路を基に、行き止まりに隣接する壁を開放してループを追加

### 42 Pattern

7×5セルの42パターンを使用

```text
#...###
#.....#
###.###
..#.#..
..#.###
```

パターンを構成するセルは4方向を閉鎖し、迷路中央に配置

配置できないサイズではメッセージを表示してロゴを省略
ENTRY / EXITとロゴの重複時はエラー終了

### Shortest Path

幅優先探索（BFS）で最短経路を探索

探索時に親セルと移動方向を記録し、EXITからENTRYへ逆順にたどって経路を復元

## Output Format

各セルの壁を1桁の16進数で表現

| Direction | Bit | Value |
|---|---|---|
| North | 0 | 1 |
| East | 1 | 2 |
| South | 2 | 4 |
| West | 3 | 8 |

壁が閉じている場合は対応するビットを1に指定

迷路データを行単位で出力し、空行の後にENTRY、EXIT、最短経路（N/E/S/W）を記録

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

ターミナル上で迷路、入口、出口、最短経路を表示

操作：
- 迷路の再生成
- 最短経路の表示／非表示
- 壁の色変更
- 終了

## Reusable Module

迷路生成機能を独立したPythonパッケージ`mazegen`として提供

### Installation

リポジトリ直下のwheelファイルからインストール可能

```bash
python3 -m pip install mazegen-1.0.0-py3-none-any.whl
```

### Usage

```python
from mazegen.generator import MazeGenerator

generator = MazeGenerator(
    width=10,
    height=10,
    entry=(0, 0),
    exit=(9, 9),
    perfect=True,
    seed=42,
)

maze = generator.generate()

print(maze.grid)
print(maze.solution)
```

`generate()`は`Maze`オブジェクトを返し、`grid`から迷路の構造、`solution`から最短経路を取得可能

## Team and Project Management

### Team Members

| Login | Main Responsibilities |
|---|---|
| `ayanaga` | 迷路生成、seed対応、NON-PERFECT生成 |
| `tmaeda` | アプリケーション構成、Solver、Writer、Visualizer、42ロゴ |

### Planning and Evolution

機能単位で分担し、GitHubのPull Requestを通じて段階的に統合

当初、内部迷路データを`grid[y][x]`で開発していたが、論理座標系との不統一が開発の阻害要因となったため、`grid[x][y]`に統一

また、再利用性を確保するために関連モジュールを`mazegen/`へ集約する過程で、Generatorの外部モジュールへの依存が課題となり、依存関係を整理するリファクタリングを実施

単純な構成から段階的に実装した点は有効だったが、Generatorの再利用性を考慮した依存関係の整理は初期設計で行うのが望ましかった。

開発にはPython、Git、GitHub、flake8、mypy等を使用

## Resources and AI Usage

### Resources

- [Algorithmic Mazes in Python: From Generation to Optimal Pathfinding](https://jp.linkedin.com/pulse/algorithmic-mazes-python-from-generation-optimal-dion-mariyanayagam-mjrze?tl=ja)
  - DFSによるRecursive Backtrackingの迷路生成アルゴリズムを参考

- [Turidus / Python-Maze](https://github.com/Turidus/Python-Maze)
  - NON-PERFECT迷路の生成に向けて、行き止まりを減らすBraid Mazeの生成手法を参考

### AI Usage

- Subjectの理解：英語原文の翻訳、要件の確認・解釈
- デバッグ支援：エラーメッセージの分析、原因調査、修正方法の検討
- テスト支援：境界条件、異常入力、迷路の制約に関する検証方法の検討
- ドキュメント作成：READMEの構成整理、記載内容の検討

## License

迷路生成器はMIT Licenseの下で再利用・再配布可能
詳細は`LICENSE.md`を参照
