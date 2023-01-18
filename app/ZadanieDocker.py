from flask import Flask, render_template
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import io
import urllib

app = Flask(__name__)

@app.route('/graph/<float:a>/<float:b>/<float:c>/<float:xmin>/<float:xmax>/<float:ymin>/<float:ymax>')
def graph(a, b, c, xmin, xmax, ymin, ymax):
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)

    x = range(int(xmin), int(xmax))
    y = [a*i*i + b*i + c for i in x]

    axis.plot(x, y)
    axis.set_xlim(xmin, xmax)
    axis.set_ylim(ymin, ymax)

    canvas = FigureCanvas(fig)
    output = io.BytesIO()
    canvas.print_png(output)
    response = make_response(output.getvalue())
    response.mimetype = 'image/png'
    return response

if __name__ == '__main__':
    app.run(debug=True)
