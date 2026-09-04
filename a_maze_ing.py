#! /usr/bin/env python3
import sys


def load_config(filename: str) -> dict[str, str]:
    """Load maze configuration from a file.

    The configuration file uses one KEY=VALUE pair per line.
    Blank lines and lines whose first non-whitespace character is '#'
    are ignored.

    Args:
        filename: Path to the configuration file.

    Returns:
        A dictionary containing raw configuration values.

    Raises:
        OSError: If the configuration file cannot be opened.
        ValueError: If the configuration syntax is invalid.
    """
    if not filename:
        raise ValueError("Filename must be provided")
    config: dict[str, str] = {}
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            if "=" not in line:
                raise ValueError(f"Invalid configuration syntax: {line}")

            key, value = line.split("=", 1)
            config[key.strip()] = value.strip()
    return config


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

    # maze を生成する

    # 最短経路を求める

    # outputファイルを作成する

    # maze を表示する

    # ボーナスで追加操作を入れるならこの辺？
  
    return 0


if __name__ == "__main__":
    main(sys.argv)
