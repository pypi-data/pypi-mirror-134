"""Metadata wrapper functions for cleaning notebook metadata."""
from pathlib import Path
from typing import Any, Callable, List, Optional, Sequence

from databooks import JupyterNotebook
from databooks.common import get_logger, set_verbose, write_notebook

logger = get_logger(__file__)


def clear(
    read_path: Path,
    write_path: Optional[Path] = None,
    notebook_metadata_keep: Sequence[str] = (),
    cell_metadata_keep: Sequence[str] = (),
    check: bool = False,
    verbose: bool = False,
    **kwargs: Any,
) -> bool:
    """
    Clear Jupyter Notebook metadata.

    Clear metadata (at notebook and cell level) and write clean
     notebook. By default remove all metadata.
    :param read_path: Path of notebook file with metadata to be cleaned
    :param write_path: Path of notebook file with metadata to be cleaned
    :param notebook_metadata_keep: Notebook metadata fields to keep
    :param cell_metadata_keep: Cell metadata fields to keep
    :param check: Don't write any files, check whether there is unwanted metadata
    :param verbose: Log written files
    :param kwargs: Additional keyword arguments to pass to
     `databooks.data_models.JupyterNotebook.clear_metadata`
    :return: Whether notebooks are equal
    """
    if verbose:
        set_verbose(logger)

    if write_path is None:
        write_path = read_path
    notebook = JupyterNotebook.parse_file(read_path)

    notebook.clear_metadata(
        notebook_metadata_keep=notebook_metadata_keep,
        cell_metadata_keep=cell_metadata_keep,
        **kwargs,
    )
    nb_equals = notebook == JupyterNotebook.parse_file(read_path)

    if nb_equals or check:
        msg = (
            "only check (unwanted metadata found)."
            if not nb_equals
            else "no metadata to remove."
        )
        logger.debug(f"No action taken for {read_path} - " + msg)
    else:
        write_notebook(nb=notebook, path=write_path)
        logger.debug(f"Removed metadata from {read_path}, saved as {write_path}")

    return nb_equals


def clear_all(
    read_paths: List[Path],
    write_paths: List[Path],
    *,
    progress_callback: Callable[[], None] = lambda: None,
    **clear_kwargs: Any,
) -> List[bool]:
    """
    Clear metadata for multiple notebooks at notebooks and cell level.

    :param read_paths: Paths of notebook to remove metadata
    :param write_paths: Paths of where to write cleaned notebooks
    :param progress_callback: Callback function to report progress
    :param clear_kwargs: Keyword arguments to be passed to `databooks.metadata.clear`
    :return: Whether the notebooks contained or not unwanted metadata
    """
    if len(read_paths) != len(write_paths):
        raise ValueError(
            "Read and write paths must have same length."
            f" Got {len(read_paths)} and {len(write_paths)}"
        )
    checks = []
    for nb_path, write_path in zip(read_paths, write_paths):
        checks.append(clear(read_path=nb_path, write_path=write_path, **clear_kwargs))
        progress_callback()
    return checks
