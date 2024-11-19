import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import warnings
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots


class Plots:
    @staticmethod
    def periodic_month(
        xcol,
        ycol,
        xlabel,
        ylabel,
        tlabel,
        style="plotly",
        nbins=18,
        df=None,
        line_col=None,
        line_selc=None,
    ):

        if line_selc is None:
            print("line_selc in None")
            return None

        elif len(line_selc) == 1:
            warnings.filterwarnings(action="ignore")
            df_selected = df[df[line_col] == line_selc].copy()
            df_selected.sort_values(xcol, inplace=True)

            if style == "seaborn":
                plt.figure(figsize=(8, 4))
                sns.lineplot(x=xcol, y=ycol, data=df_selected)
                plt.xticks(rotation=45)
                plt.gca().xaxis.set_major_locator(plt.MaxNLocator(nbins=nbins))
                plt.title(label=tlabel)
                plt.xlabel(xlabel=xlabel)
                plt.ylabel(ylabel=ylabel)
                plt.tight_layout()
                plt.show()

            if style == "plotly":
                fig = px.line(
                    data_frame=df_selected,
                    x=xcol,
                    y=ycol,
                    title=tlabel,
                    labels={xcol: xlabel, ycol: ycol},
                )
                fig.update_xaxes(tickangle=45)
                fig.show()
        else:

            warnings.filterwarnings(action="ignore")
            df_selected = df[df[line_col].isin(line_selc)].copy()
            df_selected.sort_values([line_col, xcol], inplace=True)

            if style == "seaborn":
                plt.figure(figsize=(10, 6))
                sns.lineplot(x=xcol, y=ycol, hue=line_col, data=df_selected)
                plt.xticks(rotation=45)
                plt.gca().xaxis.set_major_locator(plt.MaxNLocator(nbins=nbins))
                plt.title(label=tlabel)
                plt.xlabel(xlabel=xlabel)
                plt.ylabel(ylabel=ylabel)
                plt.tight_layout()
                plt.show()

            if style == "plotly":
                fig = px.line(
                    data_frame=df_selected,
                    x=xcol,
                    y=ycol,
                    color=line_col,
                    title=tlabel,
                    labels={xcol: xlabel, ycol: ylabel},
                )
                fig.update_xaxes(tickangle=45)
                fig.show()

    @staticmethod
    def lines_inplot(
        xcol,
        xlabel,
        ycol1,
        ylabel1,
        ycol2,
        ylabel2,
        style="plotly",
        nbins=18,
        df=None,
        line_col=None,
        line_selc=None,
        split=False,
    ):

        if line_selc is None:
            print("location select in None")
            return None

        elif len(line_selc) >= 1:
            warnings.filterwarnings(action="ignore")
            df = df[df[line_col].isin(line_selc)]
            tags = df[line_col].unique()

            for tag in line_selc:
                if tag in tags:
                    df_country = df[df[line_col] == tag].copy()
                    df_country.sort_values(xcol, inplace=True)

                    if style == "seaborn":
                        plt.figure(figsize=(8, 4))

                        sns.lineplot(
                            x=xcol,
                            y=ycol1,
                            data=df_country,
                            label=ylabel1,
                            color="blue",
                        )

                        sns.lineplot(
                            x=xcol, y=ycol2, data=df_country, label=ylabel2, color="red"
                        )

                        plt.xticks(rotation=45)
                        plt.gca().xaxis.set_major_locator(plt.MaxNLocator(nbins=nbins))
                        plt.title(f"{tag} - {ylabel1} vs {ylabel2}", fontsize=14)
                        plt.xlabel(xlabel)
                        plt.ylabel(f"{ycol1} & {ycol2}")
                        plt.legend()
                        plt.tight_layout()
                        plt.show()

                        if split:
                            fig, axs = plt.subplots(2, 1, figsize=(10, 8))

                            sns.lineplot(
                                x=xcol,
                                y=ycol1,
                                data=df_country,
                                ax=axs[0],
                                label=f"{ylabel1} - {tag}",
                                color="blue",
                            )
                            axs[0].set_title(f"{ylabel1}")
                            axs[0].set_ylabel(ylabel1)
                            axs[0].legend()

                            sns.lineplot(
                                x=xcol,
                                y=ycol2,
                                data=df_country,
                                ax=axs[1],
                                label=f"{ylabel2} - {tag}",
                                color="red",
                            )
                            axs[1].set_title(f"{ylabel2}")
                            axs[1].set_xlabel(xlabel)
                            axs[1].set_ylabel(ylabel2)
                            axs[1].legend()

                            for ax in axs:
                                ax.tick_params(axis="x", rotation=45)
                                ax.xaxis.set_major_locator(plt.MaxNLocator(nbins=nbins))

                            fig.suptitle(f"{tag} - {ylabel1} vs {ylabel2}", fontsize=16)

                            plt.tight_layout(rect=[0, 0, 1, 0.96])
                            plt.show()

                    elif style == "plotly":
                        fig = px.line(
                            data_frame=df_country,
                            x=xcol,
                            y=[ycol1, ycol2],
                            title=f"{tag} - {ylabel1} vs {ylabel2}",
                            labels={
                                xcol: xlabel,
                                ylabel1: ylabel1,
                                ylabel2: ylabel2,
                            },
                        )
                        fig.update_xaxes(tickangle=45)
                        fig.update_layout(yaxis_title=None)
                        fig.show()

                        if split:
                            fig = make_subplots(
                                rows=2,
                                cols=1,
                                shared_xaxes=True,
                                vertical_spacing=0.1,
                                subplot_titles=[
                                    f"{ylabel1}",
                                    f"{ylabel2}",
                                ],
                            )

                            # Add line to top subplot (row 1)
                            fig.add_trace(
                                go.Scatter(
                                    x=df_country[xcol],
                                    y=df_country[ycol1],
                                    mode="lines",
                                    name=ylabel1,
                                ),
                                row=1,
                                col=1,
                            )

                            # Add line to bottom subplot (row 2)
                            fig.add_trace(
                                go.Scatter(
                                    x=df_country[xcol],
                                    y=df_country[ycol2],
                                    mode="lines",
                                    name=ylabel2,
                                ),
                                row=2,
                                col=1,
                            )

                            # Update layout and labels
                            fig.update_layout(
                                title=f"{tag} - {ylabel1} vs {ylabel2}",
                                showlegend=True,
                                xaxis=dict(tickangle=45),
                                height=600,
                                template="plotly_white",
                            )
                            fig.update_xaxes(title_text=xlabel, row=2, col=1)

                            fig.show()
