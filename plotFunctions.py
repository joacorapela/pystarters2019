
def plotRegressionPanel(ax, x, y, coefsAndStatsFn=None, statsLegendFn=None,
                        title="", xlabel="|Speed|", ylabel="Spike Count",
                        pointsCol="lightgray", regLineCol="red",
                        legendLoc="upper left"):

    ax.scatter(x, y, c=pointsCol)

    if coefsAndStatsFn is not None:
        lrCoefs, stats = coefsAndStatsFn(x=x, y=y)
        if statsLegendFn is not None:
            legend = statsLegendFn(stats=stats)
            ax.plot(x, lrCoefs[0]+x*lrCoefs[1], color=regLineCol, label=legend)
            ax.legend(loc=legendLoc)
        else:
            ax.plot(x, lrCoefs[0]+x*lrCoefs[1], color=regLineCol)

    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title(title)

