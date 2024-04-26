class NotFlask():
    def __init__(self):
        # Store the routes for later access
        self.routes = {}

    def route(self, route_str):
        # Store an association between the route string and the function
        def decorator(f):
            self.routes[route_str] = f
            return f

        return decorator

app = NotFlask()

@app.route("/")
def hello():
    return "Hello World!"

result = app.routes["/"]()
print(result)
