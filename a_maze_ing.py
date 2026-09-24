#! /usr/bin/env python3
import sys
from config import load_config, validate_config


def main(args: list[str]) -> int:
    """Run the A-Maze-ing program."""
    # コマンドライン引数がconfigファイル名１つであるかを確認
    if len(args) != 2:
        print("Usage: python3 a_maze_ing.py <config_file>")
        return 1

    # configファイルを読み込んでパースする
    try:
        config = load_config(args[1])
    except (OSError, ValueError) as e:
        print(f"Error: {e}")
        return 1

    # configの内容を検証し、エラーチェック、下準備
    try:
        validate_config(config)
    except ValueError as e:
        print(f"Error: {e}")
        return 1

    # maze を生成する

    # 最短経路を求める

    # outputファイルを作成する

    # maze を表示する

    # ボーナスで追加操作を入れるならこの辺？

    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
