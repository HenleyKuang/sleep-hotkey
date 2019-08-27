import argparse

from sleep_hotkey.sleep_hotkey import sleep


def _parse_args():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('--seconds',
                        action='store',
                        type=int,
                        default=10)
    return parser.parse_args()


def _main():
    options = _parse_args()
    sleep_seconds = options.seconds

    sleep(sleep_seconds)


if __name__ == "__main__":
    _main()
