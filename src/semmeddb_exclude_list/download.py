from pathlib import Path
import pystow


def download_file(target_directory_name: str, url: str) -> Path:
    """
    Downloads a file from the given URL.

    :param target_directory_name: The name of the directory to download the file to.
    :param config_key: The key in the config file that contains the URL to download the file from.
    :return: None

    """
    file_path = pystow.ensure(target_directory_name,
                              # SEMMEDDB semantic type exclusion
                              url=url,
                              force=True)

    return file_path