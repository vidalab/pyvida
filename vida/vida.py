from IPython.core.display import HTML
import json

class vida:
    def __init__(self):
        self.name = 'vida'

    def show(id, data):
        HTML('<script type="text/javascript" src="https://rawgit.com/vidalab/isender/master/isender.js"></script>' +
        '<iframe src="https://vida.io/embed/' + id + '?ext_data=true" width="800" height="500" seamless frameBorder="0" scrolling="no" id="vida-embed"></iframe>' +
        '<script type="text/javascript">' +
        'document.getElementById("vida-embed").onload = function() {' +
        'var dataObj = ' +
        json.dumps(data) + ';' +
        'var sender = new Vida.ISender("vida-embed");' +
        'sender.postRender(dataObj);' +
        '}' +
        '</script>')
