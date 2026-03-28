# Common Issues

## Python environment is not working

- Check that `python --version` returns the expected interpreter.
- Create a virtual environment for each repository.
- Install dependencies from the local `requirements.txt` file when present.

## The script cannot find a file

- Confirm your current working directory.
- Prefer absolute or `pathlib`-based paths in your code.
- Check file names carefully on case-sensitive systems.

## The data analysis chart does not render

- Make sure `matplotlib` is installed.
- Run the script locally instead of inside a restricted terminal environment if needed.

## The AI demo feels too simple

- That is intentional for teaching.
- Start with a deterministic local provider.
- Replace it with a live model provider only after the workflow is clear.
