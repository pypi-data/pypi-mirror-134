class ColorClass:
  def __init__(self):
    self.colors = {
      'gray'   : '\033[30',
      'red'    : '\033[31',
      'green'  : '\033[32',
      'yellow' : '\033[33',
      'blue'   : '\033[34',
      'purple' : '\033[35',
      'lime'   : '\033[36',
      'white'  : '\033[37',
    }

    self.backgrounds = {
        'gray'   : ';40',
        'red'    : ';41',
        'green'  : ';42',
        'yellow' : ';43',
        'blue'   : ';44',
        'purple' : ';45',
        'lime'   : ';46',
        'white'  : ';47',
    }

    self.style = {
        'bold'      : ';1',
        'em'        : ';2',
        'underline' : ';4',
        'blink'     : ';5',
        'invert'    : ';7',
        'hidden'    : ';8',
    }

    self.end    = '\033[0m'

  def set(self, text, color, background = '', style = '', end='\n'):
    colorCode = self.colors.get(color, '\033[30m')
    bgCode    = self.backgrounds.get(background, '')
    styleCode = self.style.get(style, '')
    output    = colorCode + bgCode + styleCode + 'm' + text + self.end
    print(output, end=end)

