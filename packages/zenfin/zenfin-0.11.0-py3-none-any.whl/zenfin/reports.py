import pandas as pd
from . import utils
from . import stats
from . import plots
from tabulate import tabulate
import io
import re as regex
from base64 import b64encode
from datetime import date

def _download_html(html, filename="tearsheet.html"):
    jscode = regex.sub(' +', ' ', """<script>
    var bl=new Blob(['{{html}}'],{type:"text/html"});
    var a=document.createElement("a");
    a.href=URL.createObjectURL(bl);
    a.download="{{filename}}";
    a.hidden=true;document.body.appendChild(a);
    a.innerHTML="download report";
    a.click();</script>""".replace('\n', ''))
    jscode = jscode.replace('{{html}}', _regex.sub(
        ' +', ' ', html.replace('\n', '')))

def _file_stream():
    """Returns a file stream"""
    return io.BytesIO()
  
def _html_table(obj, showindex=True, headers="keys"):
    obj = tabulate(obj.T, headers=headers, tablefmt='html',
                    floatfmt=".2f", showindex=showindex)
    obj = obj.replace(' style="text-align: right;"', '')
    obj = obj.replace(' style="text-align: left;"', '')
    obj = obj.replace(' style="text-align: center;"', '')
    obj = regex.sub('<td> +', '<td>', obj)
    obj = regex.sub(' +</td>', '</td>', obj)
    obj = regex.sub('<th> +', '<th>', obj)
    obj = regex.sub(' +</th>', '</th>', obj)
    return obj

def _embed_figure(figfile, figfmt):
    figbytes = figfile.getvalue()
    if figfmt == 'svg':
        return figbytes.decode()
    data_uri = b64encode(figbytes).decode()
    return '<img src="data:image/{};base64,{}" />'.format(figfmt, data_uri)

def report(returns, benchmark, rf,
         grayscale=False,
         title='Strategy Tearsheet',
         output=None,
         periods=252,
         download_filename='tearsheet.html',
         firm='Tera Capital',
         version='0',
         figfmt='svg',
         template_path=None):

    tpl = ""
    with open(template_path or __file__[:-4] + '.html') as f:
        tpl = f.read()
        f.close()

    date_now = date.today().strftime('%e %b, %Y')
    tpl = tpl.replace('{{date}}', date_now)
    tpl = tpl.replace('{{title}}', title)
    tpl = tpl.replace('{{firm}}', firm)
    tpl = tpl.replace('{{v}}', version)

    mtrx = report_metrics(returns, benchmark, rf,
                          display=False,
                          periods=periods)

    tpl = tpl.replace('{{info}}', _html_table(mtrx[0],headers=['Analysis info']))
    tpl = tpl.replace('{{returns}}', _html_table(mtrx[1]))
    tpl = tpl.replace('{{performance}}', _html_table(mtrx[2]))
    tpl = tpl.replace('{{risk}}', _html_table(mtrx[3]))
    tpl = tpl.replace('{{pnl}}', _html_table(mtrx[4]))

    tpl = tpl.replace('<tr><td></td><td></td><td></td></tr>',
                      '<tr><td colspan="3"><hr></td></tr>')
    tpl = tpl.replace('<tr><td></td><td></td></tr>',
                      '<tr><td colspan="2"><hr></td></tr>')

           
    dd_info = mtrx[5][mtrx[5].columns.get_level_values(0).unique()[0]]
    dd_info = dd_info.sort_values(
        by='max drawdown', ascending=True)[:10]
    dd_info = dd_info[['start', 'valley', 'end', 'max drawdown', 'days']]
    dd_info.columns = ['Started', 'Valley','Recovered', 'Drawdown', 'Days']
    tpl = tpl.replace('{{dd_info}}', _html_table(dd_info.T, showindex=False))

    figs = report_plots(returns.iloc[:,0], benchmark.iloc[:,0], rf, grayscale=grayscale, periods=periods, display=False, save=True)

    tpl = tpl.replace('{{cum_returns}}', figs[0])
    tpl = tpl.replace('{{log_returns}}', figs[1])
    tpl = tpl.replace('{{vol_returns}}', figs[2])
    tpl = tpl.replace('{{eoy_returns}}', figs[3])
    tpl = tpl.replace('{{monthly_dist}}', figs[4])
    tpl = tpl.replace('{{daily_returns}}', figs[5])
    tpl = tpl.replace('{{rolling_beta}}', figs[6])
    tpl = tpl.replace('{{rolling_vol}}', figs[7])
    tpl = tpl.replace('{{rolling_sharpe}}', figs[8])
    tpl = tpl.replace('{{rolling_sortino}}', figs[9])
    tpl = tpl.replace('{{dd_periods}}', figs[10])
    tpl = tpl.replace('{{dd_plot}}', figs[11])
    tpl = tpl.replace('{{monthly_heatmap}}', figs[12])
    tpl = tpl.replace('{{returns_dist}}', figs[13])

    tpl = regex.sub(r'\{\{(.*?)\}\}', '', tpl)
    tpl = tpl.replace('white-space:pre;', '')

    if output is None:
        _download_html(tpl, download_filename)
        return

    with open(output, 'w', encoding='utf-8') as f:
        f.write(tpl)
      
def report_metrics(dr, bench, rf, periods=252, display=True):

  rfd = rf['dR'].rename('DI')
  rfy = rf['yR'].rename('DI')
  frames = [dr, bench]
  df = pd.concat(frames, axis=1)

  dd = utils.to_drawdown_series(df)
  dd_details = utils.drawdown_details(dd)

  dsp_info = pd.DataFrame()
  date_start = dr.index.strftime('%Y-%m-%d')[0]
  date_end = dr.index.strftime('%Y-%m-%d')[-1]
  dsp_info['Strategy'] = pd.Series(dr.columns[0])
  dsp_info['Benchmark'] = pd.Series(bench.columns[0])
  dsp_info['Start Period'] = pd.Series(date_start)
  dsp_info['End Period'] = pd.Series(date_end)
  dsp_info['Working days'] = pd.Series(len(dr.index)) 
  dsp_info['Years'] = pd.Series("{:.1f}".format(len(dr.index)/ periods))

  dsp_returns = pd.DataFrame()
  frames = [dr, bench, rfd ]
  df = pd.concat(frames, axis=1)
  total_return = utils.to_pct(stats.total_return(df),2)
  dsp_returns['Total return'] = pd.Series(total_return)
  cagr = utils.to_pct(stats.cagr(df),2)
  dsp_returns['CAGR'] = pd.Series(cagr)
  d_r = utils.to_pct(stats.expected_return(df),2)
  dsp_returns['E[Daily Returns]'] = pd.Series(d_r)
  m_r = utils.to_pct(stats.expected_return(df, aggregate='M'),2)
  dsp_returns['E[Monthly Returns]'] = pd.Series(m_r)
  y_r = utils.to_pct(stats.expected_return(df, aggregate='Y'),2)
  dsp_returns['E[Yearly Returns]'] = pd.Series(y_r)
  r_mtd = utils.to_pct(stats.total_return(utils.mtd(df, df.index[-1])),2)
  dsp_returns['MTD'] = pd.Series(r_mtd)
  r_l3m = utils.to_pct(stats.total_return(utils.l3m(df, df.index[-1])),2)
  dsp_returns['3M'] = pd.Series(r_l3m)
  r_l6m = utils.to_pct(stats.total_return(utils.l6m(df, df.index[-1])),2)
  dsp_returns['6M'] = pd.Series(r_l6m)
  r_ytd = utils.to_pct(stats.total_return(utils.ytd(df, df.index[-1])),2)
  dsp_returns['YTD'] = pd.Series(r_ytd)
  r_l1y = utils.to_pct(stats.total_return(utils.l1y(df, df.index[-1])),2)
  dsp_returns['1Y'] = pd.Series(r_l1y)
  cagr_3y = utils.to_pct(stats.cagr(utils.l3y(df, df.index[-3])),2)
  dsp_returns['3Y (aa)'] = pd.Series(cagr_3y)
  cagr_5y = utils.to_pct(stats.cagr(utils.l5y(df, df.index[-1])),2)
  dsp_returns['5Y (aa)'] = pd.Series(cagr_5y)
  cagr_10y = utils.to_pct(stats.cagr(utils.l10y(df, df.index[-1])),2)
  dsp_returns['10Y (aa)'] = pd.Series(cagr_10y)
  dsp_returns['Inception (aa)'] = pd.Series(cagr)
  
  dsp_performance = pd.DataFrame()
  frames = [dr, bench]
  df = pd.concat(frames, axis=1)
  sharpe = utils.to_num(stats.sharpe(df, rfy, smart=False),2)
  dsp_performance['Sharpe'] = pd.Series(sharpe)
  smart_sharpe = utils.to_num(stats.sharpe(df, rfy, smart=True),2)
  dsp_performance['Smart Sharpe'] = pd.Series(smart_sharpe)
  sortino = utils.to_num(stats.sortino(df, rfy, smart=False),2)
  dsp_performance['Sortino'] = pd.Series(sortino)
  smart_sortino = utils.to_num(stats.sortino(df, rfy, smart=True),2)
  dsp_performance['Smart Sortino'] = pd.Series(smart_sortino)
  adj_sortino = utils.to_num(stats.adjusted_sortino(df, rfy, smart=False),2)
  dsp_performance['Sortino/√2'] = pd.Series(adj_sortino)
  adj_smart_sortino = utils.to_num(stats.adjusted_sortino(df, rfy, smart=True),2)
  dsp_performance['Smart Sortino/√2'] = pd.Series(adj_smart_sortino)
  omega = utils.to_num(stats.omega(df, rfy),2)
  dsp_performance['Omega'] = pd.Series(omega)
  beta = utils.to_num(stats.beta(dr, bench),2)
  dsp_performance['Beta'] = pd.Series(beta)
  alpha = utils.to_num(stats.alpha(dr, bench),2)
  dsp_performance['Alpha'] = pd.Series(alpha)
  
  dsp_risk = pd.DataFrame()
  frames = [dr, bench]
  df = pd.concat(frames, axis=1)
  max_drawdown = utils.to_pct(stats.max_drawdown(df),2)
  dsp_risk['Max Drawdown'] = pd.Series(max_drawdown)
  longest_drawdown_days = utils.to_num(stats.longest_drawdown_days(df),0)
  dsp_risk['Longest DD Days'] = pd.Series(longest_drawdown_days)
  avg_drawdown = utils.to_pct(stats.avg_drawdown(dd_details),2)
  dsp_risk['Avg. Drawdown'] = pd.Series(avg_drawdown)
  avg_drawdown_days = utils.to_num(stats.avg_drawdown_days(df),0)
  dsp_risk['Avg. Drawdown Days'] = pd.Series(avg_drawdown_days)
  volatility = utils.to_pct(stats.volatility(df, periods),2)
  dsp_risk['Volatility (aa)'] = pd.Series(volatility)
  r_squared = utils.to_num(stats.r_squared(dr, bench),2)
  dsp_risk['R^2'] = pd.Series(r_squared)
  calmar = utils.to_num(stats.calmar(df),2)
  dsp_risk['Calmar'] = pd.Series(calmar)
  skew = utils.to_num(stats.skew(df),2)
  dsp_risk['Skew'] = pd.Series(skew)
  kurtosis = utils.to_num(stats.kurtosis(df),2)
  dsp_risk['Kurtosis'] = pd.Series(kurtosis)
  kelly_criterion = utils.to_pct(stats.kelly_criterion(df),2)
  dsp_risk['Kelly Criterion'] = pd.Series(kelly_criterion)
  risk_of_ruin = utils.to_pct(stats.risk_of_ruin(df),2)
  dsp_risk['Risk of Ruin'] = pd.Series(risk_of_ruin)
  value_at_risk = utils.to_pct(stats.value_at_risk(df),2)
  dsp_risk['Daily VaR'] = pd.Series(value_at_risk)
  conditional_value_at_risk = utils.to_pct(stats.conditional_value_at_risk(df),2)
  dsp_risk['Expected Shortfall (cVaR)'] = pd.Series(conditional_value_at_risk)
  recovery_factor = utils.to_num(stats.recovery_factor(df),2)
  dsp_risk['Recovery Factor'] = pd.Series(recovery_factor)
  ulcer_index = utils.to_num(stats.ulcer_index(df),2)
  dsp_risk['Ulcer Index'] = pd.Series(ulcer_index)
  serenity_index = utils.to_num(stats.serenity_index(df, rfy),2)
  dsp_risk['Serenity Index'] = pd.Series(serenity_index)
  
  dsp_pnl = pd.DataFrame()
  frames = [dr, bench]
  df = pd.concat(frames, axis=1)
  er = utils.to_excess_returns(df, rfy)
  gtp = utils.to_num(stats.gain_to_pain_ratio(er),2)
  dsp_pnl['Gain/Pain Ratio'] = pd.Series(gtp)
  gtp_1m = utils.to_num(stats.gain_to_pain_ratio(er, 'M'),2)
  dsp_pnl['Gain/Pain (1M)'] = pd.Series(gtp_1m)
  gtp_3m = utils.to_num(stats.gain_to_pain_ratio(er, 'Q'),2)
  dsp_pnl['Gain/Pain (3M)'] = pd.Series(gtp_3m)
  gtp_6m = utils.to_num(stats.gain_to_pain_ratio(er, 'BQ'),2)
  dsp_pnl['Gain/Pain (6M)'] = pd.Series(gtp_6m)
  gtp_1y = utils.to_num(stats.gain_to_pain_ratio(er, 'A'),2)
  dsp_pnl['Gain/Pain (1Y)'] = pd.Series(gtp_1y)
  payoff_ratio = utils.to_num(stats.payoff_ratio(df),2)
  dsp_pnl['Payoff Ratio'] = pd.Series(payoff_ratio)
  profit_factor = utils.to_num(stats.profit_factor(df),2)
  dsp_pnl['Profit Factor'] = pd.Series(profit_factor)
  common_sense_ratio = utils.to_num(stats.common_sense_ratio(df),2)
  dsp_pnl['Common Sense Ratio'] = pd.Series(common_sense_ratio)
  cpc_index = utils.to_num(stats.cpc_index(df),2)
  dsp_pnl['CPC Index'] = pd.Series(cpc_index)
  tail_ratio = utils.to_num(stats.tail_ratio(df),2)
  dsp_pnl['Tail Ratio'] = pd.Series(tail_ratio)
  outlier_win_ratio = utils.to_num(stats.outlier_win_ratio(df),2)
  dsp_pnl['Outlier Win Ratio'] = pd.Series(outlier_win_ratio)
  outlier_loss_ratio = utils.to_num(stats.outlier_loss_ratio(df),2)
  dsp_pnl['Outlier Loss Ratio'] = pd.Series(outlier_loss_ratio)
  avg_win = utils.to_pct(stats.avg_win(df, aggregate='M'),2)
  dsp_pnl['Avg. Up Month'] = pd.Series(avg_win)
  avg_loss = utils.to_pct(stats.avg_loss(df, aggregate='M'),2)
  dsp_pnl['Avg. Down Month'] = pd.Series(avg_loss)
  win_rate = utils.to_pct(stats.win_rate(df),2)
  dsp_pnl['Win Days %'] = pd.Series(win_rate)
  win_rate_m = utils.to_pct(stats.win_rate(df, aggregate='M'),2)
  dsp_pnl['Win Month %'] = pd.Series(win_rate_m)
  win_rate_q = utils.to_pct(stats.win_rate(df, aggregate='Q'),2)
  dsp_pnl['Win Quarter %'] = pd.Series(win_rate_q)
  win_rate_y = utils.to_pct(stats.win_rate(df, aggregate='Y'),2)
  dsp_pnl['Win Year %'] = pd.Series(win_rate_y)
  best = utils.to_pct(stats.best(df),2)
  dsp_pnl['Best Day'] = pd.Series(best)
  worst = utils.to_pct(stats.worst(df),2)
  dsp_pnl['Worst Day'] = pd.Series(worst)
  best_m = utils.to_pct(stats.best(df, aggregate='M'),2)
  dsp_pnl['Best Month'] = pd.Series(best_m)
  worst_m = utils.to_pct(stats.worst(df, aggregate='M'),2)
  dsp_pnl['Worst Month'] = pd.Series(worst_m)
  best_y = utils.to_pct(stats.best(df, aggregate='Y'),2)
  dsp_pnl['Best Year'] = pd.Series(best_y)
  worst_y = utils.to_pct(stats.worst(df, aggregate='Y'),2)
  dsp_pnl['Worst Year'] = pd.Series(worst_y)

  if display:
    print('[Analysis info]')
    print(tabulate(dsp_info.T, tablefmt='simple'))
    print('\n')
    print('[Performance Metrics]')
    print('Return Info')
    print(tabulate(dsp_returns.T, headers="keys", tablefmt='simple'))
    print('\n')
    print('Performance Info')
    print(tabulate(dsp_performance.T, headers="keys", tablefmt='simple'))
    print('\n')
    print('Risk Info')
    print(tabulate(dsp_risk.T, headers="keys", tablefmt='simple'))
    print('\n')
    print('P&L Info')
    print(tabulate(dsp_pnl.T, headers="keys", tablefmt='simple'))
    print('\n')
    for c in dd_details.columns.get_level_values(0).unique():
      print('%s : 5 Worst Drawdowns' % c)
      print(tabulate(dd_details[c].sort_values(by='max drawdown', ascending=True)[:5], headers="keys", tablefmt='simple', showindex=False))
      print('\n')
    return None

  return dsp_info, dsp_returns, dsp_performance, dsp_risk, dsp_pnl, dd_details

def report_plots(returns, benchmark, rf, grayscale=False, figsize=(8, 5), periods=252, display=True, figfmt='svg', save=False):
  rfd=rf['dR']
  rfy=rf['yR']
  
  figs = []
  savefig = {'fname': _file_stream(), 'format': figfmt} if save else None
  plots.plt_returns(returns, benchmark, rfd,
              grayscale=grayscale,
              figsize=(figsize[0], figsize[0]*.6),
              show=display,
              savefig=savefig,
              ylabel=False)
  figs.append(_embed_figure(savefig['fname'], savefig['format'])) if save else None

  savefig = {'fname': _file_stream(), 'format': figfmt} if save else None
  plots.plt_log_returns(returns, benchmark, rfd,
              grayscale=grayscale,
              figsize=(figsize[0], figsize[0]*.5),
              show=display,
              savefig=savefig,
              ylabel=False)
  figs.append(_embed_figure(savefig['fname'], savefig['format'])) if save else None

  savefig = {'fname': _file_stream(), 'format': figfmt} if save else None
  plots.plt_volmatch_returns(returns, benchmark, rfd,
              grayscale=grayscale,
              figsize=(figsize[0], figsize[0]*.5),
              show=display,
              savefig=savefig,
              ylabel=False)
  figs.append(_embed_figure(savefig['fname'], savefig['format'])) if save else None
  
  savefig = {'fname': _file_stream(), 'format': figfmt} if save else None
  plots.plt_yearly_returns(returns, benchmark, rfd,
              grayscale=grayscale,
              figsize=(figsize[0], figsize[0]*.5),
              show=display,
              savefig=savefig,
              ylabel=False)
  figs.append(_embed_figure(savefig['fname'], savefig['format'])) if save else None

  savefig = {'fname': _file_stream(), 'format': figfmt} if save else None
  plots.plt_histogram(returns,
                grayscale=grayscale,
                figsize=(figsize[0], figsize[0]*.5),
                show=display,
                savefig=savefig,
                ylabel=False)
  figs.append(_embed_figure(savefig['fname'], savefig['format'])) if save else None

  savefig = {'fname': _file_stream(), 'format': figfmt} if save else None
  plots.plt_daily_returns(returns,
                    grayscale=grayscale,
                    figsize=(figsize[0], figsize[0]*.3),
                    show=display,
                    savefig=savefig,
                    ylabel=False)
  figs.append(_embed_figure(savefig['fname'], savefig['format'])) if save else None

  savefig = {'fname': _file_stream(), 'format': figfmt} if save else None
  plots.plt_rolling_beta(returns, benchmark,
                   grayscale=grayscale,
                   window1=int(periods/2),
                   window2=periods,
                   figsize=(figsize[0], figsize[0]*.3),
                   show=display,
                   savefig=savefig,
                   ylabel=False)
  figs.append(_embed_figure(savefig['fname'], savefig['format'])) if save else None
  
  savefig = {'fname': _file_stream(), 'format': figfmt} if save else None
  plots.plt_rolling_volatility(returns, benchmark,
                         grayscale=grayscale,
                         figsize=(figsize[0], figsize[0]*.3),
                         show=display,
                         savefig=savefig,
                         ylabel=False,
                         period=int(periods/2))
  figs.append(_embed_figure(savefig['fname'], savefig['format'])) if save else None

  savefig = {'fname': _file_stream(), 'format': figfmt} if save else None
  plots.plt_rolling_sharpe(returns, benchmark, rfy,
                     grayscale=grayscale,
                     figsize=(figsize[0], figsize[0]*.3),
                     show=display,
                     savefig=savefig,
                     ylabel=False,
                     period=int(periods/2))
  figs.append(_embed_figure(savefig['fname'], savefig['format'])) if save else None
  
  savefig = {'fname': _file_stream(), 'format': figfmt} if save else None
  plots.plt_rolling_sortino(returns, benchmark, rfy,
                      grayscale=grayscale,
                      figsize=(figsize[0], figsize[0]*.3),
                      show=display,
                      savefig=savefig,
                      ylabel=False,
                      period=int(periods/2))
  figs.append(_embed_figure(savefig['fname'], savefig['format'])) if save else None

  savefig = {'fname': _file_stream(), 'format': figfmt} if save else None
  plots.plt_drawdowns_periods(returns, periods=5,
                        grayscale=grayscale,
                        figsize=(figsize[0], figsize[0]*.5),
                        show=display,
                        savefig=savefig,
                        ylabel=False)
  figs.append(_embed_figure(savefig['fname'], savefig['format'])) if save else None

  savefig = {'fname': _file_stream(), 'format': figfmt} if save else None
  plots.plt_drawdown(returns,
               grayscale=grayscale,
               figsize=(figsize[0], figsize[0]*.4),
               show=display,
               savefig=savefig,
               ylabel=False)
  figs.append(_embed_figure(savefig['fname'], savefig['format'])) if save else None

  savefig = {'fname': _file_stream(), 'format': figfmt} if save else None
  plots.plt_monthly_heatmap(returns,
                      grayscale=grayscale,
                      figsize=(figsize[0], figsize[0]*.5),
                      show=display,
                      savefig=savefig,
                      ylabel=False)
  figs.append(_embed_figure(savefig['fname'], savefig['format'])) if save else None

  savefig = {'fname': _file_stream(), 'format': figfmt} if save else None
  plots.plt_distribution(returns,
                   grayscale=grayscale,
                   figsize=(figsize[0], figsize[0]*.5),
                   show=display,
                   savefig=savefig,
                   ylabel=False)
  figs.append(_embed_figure(savefig['fname'], savefig['format'])) if save else None

  if save:
    return figs
