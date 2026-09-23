#! /usr/bin/env python3
import sys


class MazeConfig:
    """Store validated maze configuration values."""
    def __init__(
        self,
        width: int,
        height: int,
        entry: tuple[int, int],
        exit: tuple[int, int],
        output_file: str,
        perfect: bool,
        seed: int | None = None,
    ) -> None:
        self.width = width
        self.height = height
        self.entry = entry
        self.exit = exit
        self.output_file = output_file
        self.perfect = perfect
        self.seed = seed


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


def validate_config(config: dict[str, str]) -> MazeConfig:
    """Validate and convert raw configuration values to MazeConfig.

    Args:
        config: A dictionary containing raw configuration values.

    Returns:
        A validated MazeConfig instance.

    Raises:
        ValueError: If any configuration value is invalid.
    """

    mandatory_keys = [
        "WIDTH",
        "HEIGHT",
        "ENTRY",
        "EXIT",
        "OUTPUT_FILE",
        "PERFECT"
    ]

    optional_keys = [
        "SEED"
    ]

    allowed_keys = mandatory_keys + optional_keys

    # Check for missing mandatory keys
    missing_keys = [key for key in mandatory_keys if key not in config]
    if missing_keys:
        raise ValueError(
            f"Missing mandatory configuration keys: "
            f"{', '.join(missing_keys)}"
        )

    # Check for unknown keys
    unknown_keys = [key for key in config if key not in allowed_keys]
    if unknown_keys:
        raise ValueError(
            f"Unknown configuration keys: {', '.join(unknown_keys)}"
        )

    # Validate width and height
    try:
        width = int(config["WIDTH"])
        height = int(config["HEIGHT"])
    except ValueError:
        raise ValueError("Width and height must be integers")

    if width <= 0 or height <= 0:
        raise ValueError("Width and height must be positive integers")

    # Validate entry and exit points
    try:
        entry_list = [int(value) for value in config["ENTRY"].split(",")]
        exit_list = [int(value) for value in config["EXIT"].split(",")]
    except ValueError:
        raise ValueError("Entry and exit must be integers")
    if len(entry_list) != 2 or len(exit_list) != 2:
        raise ValueError("Entry and exit must be in the format 'x,y'")
    entry_tuple = (entry_list[0], entry_list[1])
    exit_tuple = (exit_list[0], exit_list[1])
    if not (0 <= entry_tuple[0] < width and 0 <= entry_tuple[1] < height):
        raise ValueError("Entry point must be within maze bounds")
    if not (0 <= exit_tuple[0] < width and 0 <= exit_tuple[1] < height):
        raise ValueError("Exit point must be within maze bounds")
    if entry_tuple == exit_tuple:
        raise ValueError("Entry and exit points must be different")

    # Validate output file
    output_file = config["OUTPUT_FILE"]
    if not output_file:
        raise ValueError("Output file must be specified")

    # Validate perfect flag
    if config["PERFECT"].lower() == "true":
        perfect = True
    elif config["PERFECT"].lower() in ("false", ""):
        perfect = False
    else:
        raise ValueError("PERFECT must be 'True', 'False', or empty")

    # Validate seed
    if "SEED" in config:
        try:
            seed = int(config["SEED"])
        except ValueError:
            raise ValueError("SEED must be an integer")
    else:
        seed = None

    return MazeConfig(
        width=width,
        height=height,
        entry=entry_tuple,
        exit=exit_tuple,
        output_file=output_file,
        perfect=perfect,
        seed=seed
    )


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
