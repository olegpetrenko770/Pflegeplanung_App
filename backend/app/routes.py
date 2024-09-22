from flask import render_template, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity, create_access_token  # Import hinzugefügt
from . import app, db  # Angepasster Importpfad
from .models import User, Pflegeplan, Pflegebericht  # Angepasster Importpfad

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/example')
def example():
    return jsonify({'message': 'Example response'})

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        data = request.json  # Verwende request.json anstelle von request.form
        if not data or 'username' not in data or 'password' not in data:
            return jsonify({'message': 'Ungültige Eingabe!'}), 400

        if User.query.filter_by(username=data['username']).first():
            return jsonify({'message': 'Benutzername bereits vergeben!'}), 400

        new_user = User(username=data['username'], password=data['password'])
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'message': 'Benutzer erfolgreich registriert!'}), 201
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        data = request.json  # Verwende request.json anstelle von request.form
        user = User.query.filter_by(username=data['username'], password=data['password']).first()
        if user:
            access_token = create_access_token(identity={'username': user.username})
            return jsonify({'message': 'Anmeldung erfolgreich!', 'access_token': access_token}), 200
        return jsonify({'message': 'Anmeldung fehlgeschlagen!'}), 401
    return render_template('login.html')

@app.route('/pflegeplan', methods=['GET', 'POST'])
@jwt_required()
def create_pflegeplan():
    if request.method == 'POST':
        data = request.json  # Verwende request.json anstelle von request.form
        user = User.query.filter_by(username=get_jwt_identity()['username']).first()
        if user:
            new_pflegeplan = Pflegeplan(
                patientenname=data['patientenname'],
                informationen=data.get('informationen'),
                probleme_ressourcen=data.get('probleme_ressourcen'),
                pflegeziele=data.get('pflegeziele'),
                pflegemassnahmen=data.get('pflegemassnahmen'),
                durchfuehrung=data.get('durchfuehrung'),
                beurteilung=data.get('beurteilung'),
                user_id=user.id
            )
            db.session.add(new_pflegeplan)
            db.session.commit()
            return jsonify({'message': 'Pflegeplan erfolgreich erstellt!'})
        return jsonify({'message': 'Benutzer nicht gefunden!'})
    return render_template('pflegeplan.html')

@app.route('/pflegebericht', methods=['GET', 'POST'])
@jwt_required()
def create_pflegebericht():
    if request.method == 'POST':
        data = request.json  # Verwende request.json anstelle von request.form
        pflegeplan = Pflegeplan.query.get(data['pflegeplan_id'])
        if pflegeplan:
            new_bericht = Pflegebericht(
                datum=data['datum'],
                inhalt=data['inhalt'],
                pflegeplan_id=pflegeplan.id
            )
            db.session.add(new_bericht)
            db.session.commit()
            return jsonify({'message': 'Pflegebericht erfolgreich erstellt!'})
        return jsonify({'message': 'Pflegeplan nicht gefunden!'})
    return render_template('pflegebericht.html')

@app.route('/pflegeplaene', methods=['GET'])
@jwt_required()
def get_pflegeplaene():
    pflegeplaene = Pflegeplan.query.all()
    return jsonify([pflegeplan.to_dict() for pflegeplan in pflegeplaene])

@app.route('/pflegeberichte/<int:pflegeplan_id>', methods=['GET'])
@jwt_required()
def get_pflegeberichte(pflegeplan_id):
    pflegeberichte = Pflegebericht.query.filter_by(pflegeplan_id=pflegeplan_id).all()
    return jsonify([bericht.to_dict() for bericht in pflegeberichte])

@app.route('/pflegebericht/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_pflegebericht(id):
    pflegebericht = Pflegebericht.query.get(id)
    if pflegebericht:
        db.session.delete(pflegebericht)
        db.session.commit()
        return jsonify({'message': 'Pflegebericht erfolgreich gelöscht!'})
    return jsonify({'message': 'Pflegebericht nicht gefunden!'})
