import argparse
import json
from matplotlib import pyplot as plt
import pandas as pd
from pandas.plotting import table
from pathlib import Path
import yaml
from typing import Text


def pixels_in_inches(pixels: int = 1) -> float:
    """Converts pixels to inches bases on
    Args:
        pixels {int}: pixels number
    Returns:
        float: value in inches
    """
    return pixels / plt.rcParams['figure.dpi']


def dataframe_to_image(
        df: pd.DataFrame, filename: Text, decimals: int = 3,
        width: int = 600, height: int = 400, fontsize: float = 15
) -> None:
    """Plots train metrics.
    Args:
        df {pd.DataFrame}: dataframe
        filename {List}: image filename
        decimals {int}: number of decimal places to round data
        width {int}: image width in pixels
        height {int}: image height in pixels
        fontsize {float}: text font size
    """

    if df.shape[0] == 0:
        df.loc[0] = [''] * df.shape[1]

    # Round data
    df = df.round(decimals)

    # Calc figure sizes
    px = pixels_in_inches()
    fig_width = width * px
    fig_height = height * px

    # Create subplot
    fig, ax = plt.subplots(figsize=(fig_width, fig_height))
    # Hide axes
    ax.xaxis.set_visible(False)
    ax.yaxis.set_visible(False)
    # Hide frame
    ax.set_frame_on(False)
    # Build table
    tbl = table(
        ax,
        df,
        loc='center',
        cellLoc='center'
    )
    # Set font size
    tbl.auto_set_font_size(False)
    tbl.set_fontsize(fontsize)
    # Scale vertically to avoid rows overlapping
    tbl.scale(1, fig_height)

    # Save table to image
    fig.savefig(filename, transparent=True)


if __name__ == '__main__':

    args_parser = argparse.ArgumentParser()
    args_parser.add_argument('--config', dest='config', required=True)
    args = args_parser.parse_args()

    print("Stage: CHECK_METRICS")

    # Load main config (params.yaml)
    with open(args.config) as fd:
        params = yaml.safe_load(fd)

    reports_dir = Path(params['reports_dir'])

    metrics_path = reports_dir / params['collect_metrics']['metrics']

    with open(metrics_path) as metrics_file:
        metrics = json.load(metrics_file)

    rules = params['check_metrics']['rules']

    alerts = {
        'dataset': [],
        'metric_name': [],
        'value': [],
        'status': [],
        'expected_range': []
    }

    for ds, ds_metrics in metrics.items():
        for metric_name, value in ds_metrics.items():

            metric_rules = rules[metric_name]
            low, high = metric_rules.get('low'), metric_rules.get('high')

            alert_status = None

            if low and value < low:
                alert_status = 'low'

            if high and value > high:
                alert_status = 'high'

            if alert_status:

                alerts['dataset'].append(ds)
                alerts['metric_name'].append(metric_name)
                alerts['value'].append(value)
                alerts['status'].append(alert_status)
                alerts['expected_range'].append([low, high])

    alerts_df = pd.DataFrame(alerts)
    report_path = reports_dir / params['check_metrics']['report']
    dataframe_to_image(
        alerts_df,
        report_path,
        width=2048
    )
