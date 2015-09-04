from IPython.core.display import HTML
import json

def show(id, data, options={}):
    opts = {'width': 800, 'height': 500, 'scrolling': 'no'}.copy()
    opts.update(options)
    return HTML('<script type="text/javascript" src="https://rawgit.com/vidalab/isender/master/isender.js"></script>' +
    '<iframe src="https://vida.io/embed/' + id + '?ext_data=true" width="' + str(opts['width']) + '" height="' + str(opts['height']) + '" seamless frameBorder="0" scrolling="' + opts['scrolling'] + '" id="vida-embed"></iframe>' +
    '<script type="text/javascript">' +
    'document.getElementById("vida-embed").onload = function() {' +
    'var dataObj = ' +
    json.dumps(data) + ';' +
    'var sender = new Vida.ISender("vida-embed");' +
    'sender.postRender(dataObj);' +
    '}' +
    '</script>')
