from flask import render_template as render, request, jsonify, redirect
from core import Rates, db



class Page:

    # Home controller
    def Home():

        Rate_len = len(Rates.query.all())

        Data = []
        Library = {}
        for item in range(1, Rate_len + 1):
            data = Rates.query.get(item)

            # Data.append(data.rate)
            # Data.append(data.count_rate)

            Library = {
                'rate': data.rate,
                'count': data.count_rate
            }


            Data.append(Library)


        return render(
            'home.html',
            title='Тест',
            Data=Data
        )

    def New_Rate():
        if request.method == "POST":
            data = {
                'rate': int(request.form['rate']),
                'count_rate': int(request.form['count_rate'])
            }

            # Insert data into table
            Insert_Rate = Rates(data['rate'], data['count_rate'])
            db.session.add(Insert_Rate);
            db.session.commit()

            return redirect('/')

        else:
            return render(
                'new_rate.html',
                title='Новая ставка',
            )


class Error:

    def NO_400(error):
        number = 400
        title = 'Error 400'
        description = "Bad Request "
        return render('error.html',
                      number=number,
                      title=title,
                      description=description
                      ), 400
    def NO_404(error):
        number = 404
        title = 'Error 404'
        description = "SORRY BUT WE COULDN’T FIND THIS PAGE"
        return render('error.html',
                      number=number,
                      title=title,
                      description=description
                      ), 404

    def NO_405(error):
        number = 405
        title = 'Error 405'
        description = "Method Not Allowed"
        return render('error.html',
                      number=number,
                      title=title,
                      description=description
                      ), 405

    def NO_500(error):
        number = 500
        title = 'Error 500'
        description = "Server Internal Error"
        return render('error.html',
                      number=number,
                      title=title,
                      description=description
                      ), 500

    def NO_547(error):
        number = 547
        title = 'Error 547'
        description = "Database Insert Error"
        return render('error.html',
                      number=number,
                      title=title,
                      description=description
                      ), 547
