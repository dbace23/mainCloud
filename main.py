import logging

import functions_framework

from deprecated import deprecated

logging.getLogger().setLevel(logging.INFO)


from astro.utils.scraper import scraping_tennis

def cloud_run(function_name: str, *args):
    """
    Request Handler for Cloud Run Job Request
    Args:
        function_name: Name of function
        *args: Arguments needed for function
    Returns:
        response: String responses
    """

    try:
        if function_name == 'scraping-tennis':
            response = scraping_tennis()
        else:
            raise ModuleNotFoundError(f'No {function_name} module in Cloud Run!')

        return response
    except Exception as exc:
        raise RuntimeError(exc)


if __name__ == '__main__':
    import sys

    function_name = sys.argv[1]
    args = sys.argv[2:] or []

    cloud_run(function_name, args)
