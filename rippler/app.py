from flask import Flask, render_template
import random
import time 

app = Flask(__name__,template_folder="templates")

# @app.route('/')
# def index():
#     return render_template('index.html')

@app.route('/')
def animation():
    start = time.time()
    return render_template('anim1.html')
    end = time.time()
    print(end-start)

# @app.route('/')
# def animation():
#     for _ in range(4):
#         quadrant = random.randint(1,4)
#         if quadrant == 1:
#             return render_template('anim1.html')
#         elif quadrant == 2:
#             return render_template('anim2.html')
#         elif quadrant == 3:
#             return render_template('anim3.html')
#         elif quadrant == 4:
#             return render_template('anim4.html')
#         # time.sleep(5)

if __name__ == "__main__":
    app.run(debug=True)