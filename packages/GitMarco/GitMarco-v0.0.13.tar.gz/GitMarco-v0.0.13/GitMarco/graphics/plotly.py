import plotly.graph_objects as go
import numpy as np


class Scatter3D(object):
    def __init__(self,
                 x: np.ndarray,
                 y: np.ndarray,
                 z: np.ndarray, ):
        """
        :param x: np.ndarray - data are reshaped with (-1, 1)
        :param y: np.ndarray - data are reshaped with (-1, 1)
        :param z: np.ndarray - data are reshaped with (-1, 1)

        Create a 3D scatter plot with plotly
        """
        self.x = x
        self.y = y
        self.z = z
        self.grid = np.hstack((self.x.reshape(-1, 1),
                               self.y.reshape(-1, 1),
                               self.z.reshape(-1, 1)))

    def plot(self,
             color: np.ndarray = None,
             title: str = '',
             xlabel: str = '',
             ylabel: str = '',
             legend_title: str = '',
             size: tuple = (800, 600),
             marker_size: int = 5,
             x_range=None,
             y_range=None,
             z_range=None,
             n_ticks: int = 10,
             margin=None,
             alpha: float = 0.8,
             show: bool = False,
             cmin: float = 0.,
             cmax: float = 1.):
        """
        :param cmax: maximum value of the colorbar
        :param cmin: minimum value of the colorbar
        :param alpha: alpha
        :param margin: scene margins
        :param n_ticks: number of ticks on every axis
        :param x_range: x range
        :param z_range: z range
        :param y_range: y range
        :param marker_size: marker size
        :param color: nodal values for the color scale
        :param title: figure title
        :param xlabel: xlabel
        :param ylabel: ylabel
        :param legend_title: legend_title
        :param size: size of the figure
        :param show: show (or not) the figure
        :return:

        Create the 3d scatter plot
        """
        # color = color.reshape(-1, 1) if color is not None else color
        if margin is None:
            margin = dict(r=10, l=10, b=10, t=10)
        if z_range is None:
            z_range = [-1, 1]
        if y_range is None:
            y_range = [-1, 1]
        if x_range is None:
            x_range = [-1, 1]
        fig = go.Figure(data=[go.Scatter3d(x=self.x, y=self.y, z=self.z,
                                           mode='markers',
                                           marker=dict(size=marker_size,
                                                       color=color,
                                                       colorscale='Turbo',
                                                       opacity=alpha,
                                                       colorbar=dict(thickness=20),
                                                       cmin=cmin,
                                                       cmax=cmax,
                                                       # line=dict(width=0.5,
                                                       #          color='black')
                                                       ))],
                        layout=go.Layout(
                            width=size[0],
                            height=size[1],
                        ))

        fig.update_layout(
            title=title,
            xaxis_title=xlabel,
            yaxis_title=ylabel,
            legend_title=legend_title,
            scene=dict(
                xaxis=dict(nticks=n_ticks, range=x_range, ),
                yaxis=dict(nticks=n_ticks, range=y_range, ),
                zaxis=dict(nticks=n_ticks, range=z_range, ), ),

            margin=margin
        )

        fig.show() if show else None
        return fig
