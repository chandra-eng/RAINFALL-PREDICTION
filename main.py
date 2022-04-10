from flask import *
import pickle
import os
app=Flask(__name__,template_folder="templates")

PEOPLE_FOLDER = os.path.join('static', 'image')
app.config['UPLOAD_FOLDER'] = PEOPLE_FOLDER

file=open("model.pkl","rb")
random_Forest=pickle.load(file)
file.close()

@app.route("/", methods=["GET","POST"])
def home():
    if request.method=="POST":
        myDict = request.form
        Month = int(myDict["Month"])
        Year = int(myDict["Year"])
        pred = [Year,Month]
        res=random_Forest.predict([pred])[0]
        res=round(res,2)
        full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'rainfall.jpg')
        print(full_filename)
        return render_template('result.html',Month=Month,Year=Year,res=res,user_image='rainfall.jpg')
    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'rainfall.jpg')
    return render_template('Index.html',user_image=full_filename)

if __name__ == "__main__":
    app.run(debug=True)