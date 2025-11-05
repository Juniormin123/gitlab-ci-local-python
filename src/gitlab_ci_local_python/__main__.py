import argparse
import sys

from gitlab_ci_local_python._op import get_node_npm_version, run_gitlab_ci_local


def gitlab_ci_local_python_main(args: argparse.Namespace) -> None:
    match args.cmd:
        case "show-meta-info":
            node_ver, npm_ver = get_node_npm_version()
            print(f"using node version: {node_ver}, npm version: {npm_ver}")
        case _:
            # pass all args to gitlab-ci-local
            npm_args = list(args.cmd_args if hasattr(args, "cmd_args") else [])
            run_gitlab_ci_local(npm_args)


def cli_main():
    # Check if the first argument is 'show-meta-info'
    if len(sys.argv) > 1 and sys.argv[1] == "show-meta-info":
        args = argparse.Namespace(cmd="show-meta-info")
    else:
        # All arguments go to npm run
        args = argparse.Namespace(cmd=None, cmd_args=sys.argv[1:])

    gitlab_ci_local_python_main(args)


if __name__ == "__main__":
    cli_main()
