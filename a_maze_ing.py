def load_config(filename: str) -> dict[str, str]:
    """Load maze configuration from a file.

    The configuration file uses one KEY=VALUE pair per line.
    Lines beginning with '#' are ignored.

    Args:
        filename: Path to the configuration file.

    Returns:
        A dictionary containing raw configuration values.

    Raises:
        OSError: If the configuration file cannot be opened.
        ValueError: If the configuration syntax is invalid.
    """
    pass  # TODO: configファイルを読み込み、KEY=VALUEを解析してdictで返す


def main() -> int:
    """Run the A-Maze-ing program."""
    # コマンドライン引数がconfigファイル名１つであるかを確認

    # configファイルを読み込んでパースする
    config = load_config("config.txt")  # TODO: 実際にはコマンドライン引数から取得する

    # configの内容を検証し、エラーチェック、下準備

    # maze を生成する

    # 最短経路を求める

    # outputファイルを作成する

    # maze を表示する

    # ボーナスで追加操作を入れるならこの辺？
  
    return 0


if __name__ == "__main__":
    main()
