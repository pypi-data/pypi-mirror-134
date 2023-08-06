import argparse


def dblpct(target: str) -> str:
    ret = target.replace("%", "%%")
    return ret


def dblpct_r(target: str) -> str:
    ret = target.replace("%%", "%")
    return ret


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("arg1", help="The string you want to increase %%")
    parser.add_argument(
        "-r", help="Reverse operation: decrease %% mode", action="store_true"
    )
    args = parser.parse_args()

    if args.r:
        print(dblpct_r(args.arg1))
    else:
        print(dblpct(args.arg1))

    exit(0)


if __name__ == "__main__":
    main()
