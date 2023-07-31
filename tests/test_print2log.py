def test_print2log_logged():
    from print2log import print2log

    print(f"print: This is a log line from module: {__name__}")


def test_print2log_nonlogged():
    print(f"print: This is a log line from module: {__name__}")


def test_context_mgr():
    from print2log.print2log import log2print

    with log2print():
        print(f"ctx: This is a log line from module: {__name__}")

    print(f"print: This is a log line from module: {__name__}")


if __name__ == "__main__":
    test_print2log_nonlogged()
    test_print2log_logged()
    test_context_mgr()
