import click
import yfinance as yf
import pandas as pd
import csv
import info
import matplotlib.pyplot as plt
from csvwriter import csvwriter
import subprocess


def checkNoneType(x,r):
    if x == None:
        return r
    else:
        return x

@click.group()
def cli():
    pass

@cli.command()
def license():
    license = info.LICENSE
    click.echo(license)

@cli.command()
@click.argument("ticker")
@click.option("--output",help="Output Data to CSV",default=None)
@click.option("--plot",help="Output Plot. Enter file name. Can use .jpg or .png",default=None)
def currentratio(ticker,output,plot):
    """
    ARGS [TICKER] : Enter Stock Ticker

    """
    data = yf.Ticker(ticker)
    ta = data.balancesheet.loc['Total Current Assets']
    tl = data.balancesheet.loc['Total Current Liabilities']
    cr = ta/tl
    cr = cr.reset_index()
    cr.columns = ["Date","Current Ratio"]
    recentCR = checkNoneType(data.info.get('currentRatio',0),0)
    avgCR = cr['Current Ratio'].mean()
    threshold = True if recentCR > 0.80 else False
    click.echo(f"\n{cr}\n")
    click.echo(f"Recent Current Ratio: {recentCR}\n")
    click.echo(f"Average Current Ratio: {avgCR}\n")
    click.echo(f"Current Ratio Differential to Average: {recentCR - avgCR}\n")
    if threshold:
        click.secho(f"Current Ratio indicates good liquidity",bg="green",fg="bright_white",bold=True)
        click.echo("\n")
    else:
        click.secho(f"Current Ratio indicates low liquidity",bg="red",fg="bright_white")
        click.echo("\n")
    if output != None:
        l1 = f"Average Current Ratio:{avgCR}"
        l2 = f"Recent Current Ratio: {recentCR}"
        csvwriter(output,cr,l1,l2)
        click.echo("File Write Successful")
    if plot != None:
        plt.style.use("ggplot")
        fig = plt.figure(figsize=(14,8))
        plt.plot(cr['Date'],cr['Current Ratio'])
        plt.title(f"Current Ratio Over Time for {ticker.upper()} \nCR as of most recent balance sheet: {recentCR}")
        plt.xlabel("Date")
        plt.ylabel("Current Ratio")
        fig.savefig(plot)

@cli.command()
@click.argument("ticker")
@click.option("--output",help="Output Data to CSV",default=None)
@click.option("--plot",help="Output Plot. Enter file name. Can use .jpg or .png",default=None)
def acidtest(ticker,output,plot):
    """
    ARGS [TICKER] : Enter Stock Ticker

    """
    data = yf.Ticker(ticker)
    assets = data.balancesheet.loc['Total Assets']
    inv = data.balancesheet.loc['Inventory']
    liab = data.balancesheet.loc['Total Liab']
    acid_test = (assets-inv)/liab
    recentQR = data.info['quickRatio']
    acid_test = acid_test.reset_index()
    acid_test.columns = ["Date","Quick Ratio"]
    avgQR = acid_test['Quick Ratio'].mean()
    threshold = True if recentQR > 1 else False
    click.echo(f"\n{acid_test}\n")
    click.echo(f"Recent Quick Ratio: {recentQR}\n")
    click.echo(f"Average Quick Ratio: {avgQR}\n")
    click.echo(f"Quick Ratio Differential to Average: {recentQR - avgQR}\n")
    if output != None:
        l1 = f"Average Current Ratio:{avgQR}"
        l2 = f"Recent Current Ratio: {recentQR}"
        csvwriter(output,acid_test,l1,l2)
        click.echo("File Write Successful")
    if plot != None:
        plt.style.use("ggplot")
        fig = plt.figure(figsize=(14,8))
        plt.plot(acid_test['Date'],acid_test['Quick Ratio'])
        plt.title(f"Quick Ratio Over Time for {ticker.upper()} \nQR as of most recent balance sheet: {recentQR}")
        plt.xlabel("Date")
        plt.ylabel("Quick Ratio")
        fig.savefig(plot)

@cli.command()
@click.argument("ticker")
@click.option("--to",help="Comparison of Debt to Assets or to Equity. Can be either assets or equity. ",type=click.Choice(['assets','equity']),default='assets')
@click.option("--output",help="Output Data to CSV",default=None)
@click.option("--plot",help="Output Plot. Enter file name. Can use .jpg or .png",default=None)
def leverage(ticker,to,output,plot):
    """
    ARGS [TICKER] : Enter Stock Ticker

    """
    data = yf.Ticker(ticker)
    if to == 'assets':
        ta = data.balancesheet.loc['Total Current Assets']
        tl = data.balancesheet.loc['Total Current Liabilities']
        dr = tl/ta
        dr = dr.reset_index()
        dr.columns = ["Date","Debt Ratio"]
        avgDR = dr['Debt Ratio'].mean()
        click.echo(f"\n{dr}\n")
        click.echo(f"Average Debt Ratio: {avgDR}\n")
        if output != None:
            csvwriter(output,dr)
    else:
        ta = data.balancesheet.loc['Total Stockholder Equity']
        tl = data.balancesheet.loc['Total Current Liabilities']
        dr = tl/ta
        dr = dr.reset_index()
        dr.columns = ["Date","Debt Ratio"]
        avgDR = dr['Debt Ratio'].mean()
        click.echo(f"\n{dr}\n")
        click.echo(f"Average Debt Ratio: {avgDR}\n")
        if output != None:
            csvwriter(output,dr)

@cli.command()
@click.argument("ticker")
def dashboard(ticker):
    """
    ARGS [TICKER] : Enter Stock Ticker
    Runs Dashboard for TICKER

    """
    click.echo("Starting Dashboard")
    subprocess.run(["streamlit", "run","dash.py",ticker])





if __name__ == "__main__":
    cli()
