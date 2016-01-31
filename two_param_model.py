import plotly.plotly as py
import plotly.graph_objs as go

import numpy as np

class Model:
	def __init__(self):
		s = np.linspace(0, 100, 200)
		t = np.linspace(0, 100, 200)
		tGrid, sGrid = np.meshgrid(s, t)
		self.x = tGrid
		self.y = sGrid
		self.z = self.calculate(self.x,self.y)
		pass

	def calculate(self,param1,param2):
		return param1+param2
	
	def show(self):
		data = [go.Surface(x=self.x, y=self.y, z=self.z)]
		layout = go.Layout(
			title='Calculate',
			scene=dict(
				xaxis=dict(
					gridcolor='rgb(255, 255, 255)',
					zerolinecolor='rgb(255, 255, 255)',
					showbackground=True,
					backgroundcolor='rgb(230, 230,230)'
				),
				yaxis=dict(
					gridcolor='rgb(255, 255, 255)',
					zerolinecolor='rgb(255, 255, 255)',
					showbackground=True,
					backgroundcolor='rgb(230, 230,230)'
				),
				zaxis=dict(
					gridcolor='rgb(255, 255, 255)',
					zerolinecolor='rgb(255, 255, 255)',
					showbackground=True,
					backgroundcolor='rgb(230, 230,230)'
				)
			),
		)
		fig = go.Figure(data=data, layout=layout)
		plot_url = py.plot(fig, filename='test')

if __name__ == '__main__':
	m = Model()
	m.show()
