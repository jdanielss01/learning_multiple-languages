class Bar(object):
    def __init__(self):
        self.newText = self.text

class Foo(Bar):
    def __init__(self):
        self.txt = 'Hello World'
        Bar.__init__(self)

foo = Foo()
print(foo.newText)
