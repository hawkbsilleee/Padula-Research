from flask import Flask, render_template
import random
import time 

app = Flask(__name__,template_folder="templates")

# @app.context_processor
# def inject_load():
#     return {'load1': random.randint(0,9)}

@app.route('/')
def animation():
    return render_template('anim1.html')

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
        # time.sleep(5)


if __name__ == "__main__":
    app.run(debug=True)