# GameHub.Py
Games.Py (this name mid asf ngl) is a repository of python games meant to be executable on any machine.

# Quick Start Guide
We currently don't have any official releases, so:
- Note: `main.py` is broken rn
- Download the repo: `git clone https://github.com/AxaQuilPre/Games.Py`
- Open the folder in VS Code.
- Run the setup script: `sh ./setup.sh` (This downloads the dependencies)
- Run main.py: `python3 main.py`

# Current Contributors
- [AxeQuilPre](https://github.com/AxaQuilPre)
- [OrnitOnGithub](https://github.com/OrnitOnGithub)
- [DrN1ghtW0lf](https://github.com/DrN1ghtW0lf)
- [andrei73457](https://github.com/andrei73457)

# Contribute
Want to contribute to the project?
- Check out the [Contribution guidelines](#contribution-guidelines).
- Create a pull request.
- Wait for approval.

# Contribution Guidelines
- Github guidelines:
  - Please be very descriptive in your commits about what you added. No "minor changes" or "updated main.py".
- Python guidelines:
  - Follow python conventions:
    - Name variables, functions, methods in snake_case.
    - Comment extensively. Most importantly use `""" """` to comment functions.
    - Name variables properly. NO `i` or `x` or `var1`.
  - Follow our own conventions:
    - Do not create file paths with strings: `"example_directory/example_file"`, please use `os.path.join("example_directory", "example_file")`
    - Add all your dependencies to the `setup.sh` script. You can *also* have a localised `setup.sh`script in the directory of your game.
