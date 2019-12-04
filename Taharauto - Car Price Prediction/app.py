from flask import Flask,render_template,request,redirect,url_for
from datas import make,car_model,transmision_type,driven_wheel,vehicle_style,class_1_series,class_2_series,class_3_series
from prediction import prediction

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def home():
    if request.method == 'POST':
        print('trigered ')
        # Menjalankan functin predict 
        data = request.form
        data = data.to_dict()
        data['Engine HP'] = int(data['Engine HP'])
        data['Year'] = int(data['Year'])
        hasil = prediction(data)
        car_brand = data.get('Make')
        car_class = data.get('Model')
        car_style = data.get('Vehicle Style')
        car_transmission = data.get('Transmission Type')
        car_wheels = data.get('Driven_Wheels')
        car_HP = data.get('Engine HP')
        car_year = data.get('Year')
        return redirect(url_for('result',car_pam1 = car_brand, car_pam2 = car_class, car_pam3 = car_style,
        car_pam4 = car_transmission, car_pam5 = car_wheels, car_pam6 = car_HP, car_pam7 = car_year,
        display_new=data,hasil=int(hasil[0]),hasilatas=int((hasil[0]+2517.54)),
        hasilbawah=int((hasil[0]-2517.54))))
    return render_template('home.html',
    data_make= sorted(make),data_model=sorted(car_model),
    data_transmision=sorted(transmision_type), data_driven=sorted(driven_wheel), 
    data_style=sorted(vehicle_style))
    

# @app.route('/prediction',methods=['GET','POST'])

@app.route('/result')
def result():
    hasil = request.args['hasil']
    hasilbawah = request.args['hasilbawah']
    hasilatas = request.args['hasilatas']
    hasil_proper = request.args['display_new']
    hasiltable1 = request.args['car_pam1']
    hasiltable2 = request.args['car_pam2']
    hasiltable3 = request.args['car_pam3']
    hasiltable4 = request.args['car_pam4']
    hasiltable5 = request.args['car_pam5']
    hasiltable6 = request.args['car_pam6']
    hasiltable7 = request.args['car_pam7']

    return render_template('result.html',hasil_pred = hasil,
    hasil_pred_bawah=hasilbawah,hasil_pred_atas=hasilatas,
    proper_result=hasil_proper,car_table1=hasiltable1, car_table2=hasiltable2, car_table3=hasiltable3,
    car_table4=hasiltable4, car_table5=hasiltable5, car_table6=hasiltable6, car_table7=hasiltable7)


@app.route('/about')
def about():
    return render_template('about.html', data_class1=class_1_series ,data_class2=class_2_series,
    data_class3=class_3_series)

@app.route('/EDA')
def edapage():
    return render_template('eda.html')

    
if __name__ == '__main__':
    app.run(debug=True, port=4444)